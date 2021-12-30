from enum import Enum


class GenderEnum(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class SizeEnum(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    EXTRA_LARGE = 'Extra-Large'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class ShoeCharacteristicEnum(Enum):
    COMFORT = 'Comfort'
    STYLE = 'Style'
    Quality = 'Quality'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class EyeColorEnum(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class HairColorEnum(Enum):
    BLONDE = 'Blonde'
    BLACK = 'Black'
    BROWN = 'Brown'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)