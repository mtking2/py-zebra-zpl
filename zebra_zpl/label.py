import sys
from .printable import Printable

class InvalidElementError(Exception):
    pass

class Label:

    def __init__(self, width=100, length=100, dpi=203, print_speed=2, copies=1):
        self.width = width
        self.length = length
        self.dpi = dpi
        self.print_speed = print_speed
        self.copies = copies

        self.elements = []

    def add(self, element):
        self._check_element(element)
        self.elements.append(element)

    def dump_contents(self, io=sys.stdout):
        # Start format
        io.write('^XA')
        # ^LL<label height in dots>,<space between labels in dots>
        io.write(f'^LL{self.length}')
        # ^LH<label home - x,y coordinates of top left label>
        io.write('^LH0,0')
        # ^LS<shift the label to the left(or right)>
        io.write('^LS10')
        # ^PW<label width in dots>
        io.write(f'^PW{self.width}')
        # Print Rate(speed) (^PR command)
        io.write(f'^PR{self.print_speed}')

        for e in self.elements:
            io.write(e.to_zpl())
        
        # Specify how many copies to print
        io.write(f'^PQ{self.copies}')
        # End format
        io.write('^XZ\n')

    def _check_element(self, element):
        if not isinstance(element, Printable):
            raise InvalidElementError(f'Label elements must be a Printable (supported instance of the Printable class): {element}')
