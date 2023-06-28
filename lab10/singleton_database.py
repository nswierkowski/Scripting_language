class Database_name():

    _instance = None
    _name = None

    def __new__(cls, name, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, name):
        if not self._name:
            self._name = name

    