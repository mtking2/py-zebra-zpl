class Printable(object):

    def __init__(self, data, **kwargs):

        # print(kwargs)

        self.data = data
        self.x = 0
        self.y = 0
        self.width = 0
        self.rotation = 'N'
        self.justification = 'L'
        
        # get a list of all predefined values directly from __dict__
        allowed_keys = list(self.__dict__.keys())

        # Update __dict__ but only for keys that have been predefined 
        # (silently ignore others)
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)

    def check_attributes(self):
        if not self.data:
            raise ValueError('no data given')
        if not self.rotation in ['N','R','I','B']:
            raise ValueError(f'invalid rotation value {self.rotation}')
        if not self.justification in ['L','C','R','J']:
            raise ValueError(f'invalid justification value {self.justification}')
