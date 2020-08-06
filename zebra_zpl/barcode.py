import re
from .printable import Printable, InvalidAttributeError
from .barcode_types import barcode_types



class Barcode(Printable):

    def __init__(self, data, **kwargs):
        
        self.type = kwargs['type'] if 'type' in kwargs.keys() else 'C'
        self.width = 2
        self.height = 0
        self.ratio = 3.0
        # self.human_readable = 'Y'

        self._set_default_field_attributes()
        super().__init__(data, **kwargs)
        self._check_attributes()

    def _set_default_field_attributes(self):
        attrs = barcode_types[self.type]
        self.__dict__.update((k, v) for k, v in attrs.items())

    def _barcode_field(self):
        attrs = ','.join([ str(getattr(self, k)) for k in barcode_types[self.type].keys() ])
        field = f'^B{self.type}{attrs}'
        return field

    def to_zpl(self):
        zpl = f'^FW{self.orientation},{self.justification}'
        zpl += f'^FO{self.x},{self.y}'
        zpl += f'^BY{self.width},{self.ratio},{self.height}'
        zpl += self._barcode_field()
        if self.type == 'Q':
            zpl += f'^FD{self.correction_level}A,{self.data}^FS'
        else:
            zpl += f'^FD{self.data}^FS'
        
        return zpl

    def _check_attributes(self):
        super()._check_attributes()
        supported_barcode_types = barcode_types.keys()
        if str(self.type) not in supported_barcode_types:
            raise ValueError(f"invalid or unsupported barcode type '{self.type}'. \
                               Supported types: {', '.join(supported_barcode_types)}")
        supported_attributes = barcode_types[self.type].keys()
        default_attributes = ['type','width','height','ratio','data','x','y','position','orientation','justification']
        instance_attributes = {k: v for k, v in self.__dict__.items() if k not in default_attributes}
        for attr in instance_attributes:
            if attr not in supported_attributes:
                raise InvalidAttributeError(f"Invalid attribute '{attr}' for barcode type '{self.type}'")
