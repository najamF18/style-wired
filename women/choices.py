from enum import Enum

    
class SizeEnum(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    EXTRA_LARGE = 'Extra-Large'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class FeminineShapeEnum(Enum):
    DIAMOND = 'Diamond'
    INVERTED_TRIANGLE = 'Inverted-Triangle'
    RECTANGLE = 'Rectangle'
    OVAL = 'Oval'
    Trianlge = 'Trianlge'
    HOUR_GLASS = 'Hour-Glass'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class TopStyleEnum(Enum):
    FITTED = 'Fitted'
    STRAIGHT = 'Straight'
    LOOSE = 'Loose'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class HeelHeightEnum(Enum):
    FLAT = 'Flat'
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'HIGH'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class ShoeStyleEnum(Enum):
    FLAT_SHOES = 'Flat-Shoes'
    HEELED_SHOES = 'Heeled-Shoes'
    SANDALS = 'Sandals'
    SNEAKERS = 'Sneakers'
    BOOTS = 'Boots'
    HEELED_BOOTS = 'Heeled-Boots'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class CasualPreferenceEnum(Enum):
    FEMININE = 'Feminine'
    EDGY = 'Edgy'
    CASUAL = 'Casual'
    SMART_CASUAL = 'Smart-Casual'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class WorkPreferenceEnum(Enum):
    CASUAL = 'Casual'
    SMART_CASUAL = 'Smart-Casual'
    BUSINESS_CASUAL = 'Business-Casual'
    BUSINESS = 'Business'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class PrintsEnum(Enum):
    LARGE_PRINTS = 'Large-Prints'
    GEOMETRIC_PRINTS = 'Geometric-Prints'
    FLORAL_PRINTS = 'Floral-Prints'
    ANIMAL_PRINTS = 'Animal-Prints'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class ColorsEnum(Enum):
    BLACK = 'Black'
    BLUE = 'Blue'
    BROWN = 'Brown'
    GREY = 'Grey'
    KHAKI = 'Khaki'
    LIGHT_BLUE = 'Light-Blue'
    NAVY = 'Navy'
    OLIVE = 'Olive'
    PINK = 'Pink'
    PURPLE = 'Purple'
    RED = 'Red'
    GREEN = 'Green'
    SALMON = 'Salmon'
    WHITE = 'White'
    YELLOW = 'Yellow'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)