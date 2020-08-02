import re
from .printable import Printable

class Text(Printable):

    def __init__(self, data, **kwargs):
        
        self.font_type = 0
        self.font_size = 12
        self.max_lines = 1
        self.line_spacing = 0
        self.hanging_indent = 0

        super().__init__(data, **kwargs)

        self.check_attributes()

    def to_zpl(self):
        zpl = f'^FW{self.rotation}'
        zpl += f'^CF{self.font_type},{self.font_size}'
        zpl += f'^CI28^FO{self.x},{self.y}'
        zpl += f'^FB{self.width},{self.max_lines},{self.line_spacing},{self.justification},{self.hanging_indent}'
        zpl += f'^FD{self.data}^FS'
        return zpl

    def check_attributes(self):
        super().check_attributes()
        
        if not re.match(r'^[A-Z0-9]$', str(self.font_type)):
            raise ValueError(f'invalid font type: {self.font_type}')
        if not (0 <= self.font_size <= 32000):
            raise ValueError(f'invalid font size: {self.font_size}')
