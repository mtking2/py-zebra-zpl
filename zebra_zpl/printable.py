class InvalidAttributeError(Exception):
    pass

class Printable(object):

    def __init__(self, data, **kwargs):

        # print(kwargs)

        self.data = data
        self.x = 0
        self.y = 0
        self.width = 0
        self.orientation = 'N'
        self.justification = 'L'
        
        # get a list of all predefined values directly from __dict__
        # allowed_keys = list(self.__dict__.keys())

        # Update __dict__ but only for keys that have been predefined 
        # (silently ignore others)
        # self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)

        # Update __dict__ for all kwargs
        self.__dict__.update((key, value) for key, value in kwargs.items())
        if 'position' in kwargs.keys() and len(kwargs['position']) == 2:
            self.x, self.y = kwargs['position']


    def _check_attributes(self):
        if not self.data:
            raise ValueError('no data given')
        if not self.orientation in ['N','R','I','B']:
            raise ValueError(f'invalid orientation value {self.orientation}')
        if not self.justification in ['L','C','R','J']:
            raise ValueError(f'invalid justification value {self.justification}')
