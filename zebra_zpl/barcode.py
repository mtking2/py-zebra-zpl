import re
from .printable import Printable

class Barcode(Printable):

    def __init__(self, data, **kwargs):
        
        self.type = 'C'
        self.width = 2
        self.height = 0
        self.ratio = 3.0
        self.rotation = 'N'
        self.human_readable = 'Y'
        
        super().__init__(data, **kwargs)

        self.check_attributes()

    def to_zpl(self):
        zpl = f'^FW{self.rotation}'
        zpl += f'^FO{self.x},{self.y}'
        zpl += f'^BY{self.width},{self.ratio},{self.height}'
        zpl += f'^B{self.type}{self.rotation},,{self.human_readable}'
        zpl += f'^FD{self.data}^FS'
        return zpl

    def check_attributes(self):
        super().check_attributes()
        if not re.search(r'^([0-5]|[7-9]|[A-F]|[I-M]|[O-U]|[X-Z])$', str(self.type)):
            raise ValueError(f'invalid barcode type: {self.type}')
