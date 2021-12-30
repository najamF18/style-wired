from enum import Enum
    
class SizeEnum(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    EXTRA_LARGE = 'Extra-Large'

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
    
class CasualPreferenceEnum(Enum):
    CASUAL_CHIC = 'Casual-Chic'
    EDGY = 'Edgy'
    CASUAL = 'Casual'
    SMART_CASUAL = 'Smart-Casual'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class TopFitEnum(Enum):
    REGULAR = 'Regular'
    SLIM = 'Slim'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class BottomFitEnum(Enum):
    SKINNY = 'Skinny'
    SLIM = 'Slim'
    NORMAL = 'Normal'
    LOOSE = 'Loose'
    TAPERED = 'Tapered'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class ShoeTypeEnum(Enum):
    LOAFERS = 'Loafers'
    LEATHER_SNEAKERS = 'Leather-Sneakers'
    DRESS_SHOES = 'Dress-Shoes'
    HI_TOP_SNEAKERS = 'Hi-Top-Sneakers'
    CHELSEA_BOOTS = 'Chelsea-Boots'
    BOOTS = 'BOOTS'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class NonosEnum(Enum):
    LARGE_PRINTS = 'Large-Prints'
    SHORTS = 'Shorts'
    COLORED_TROUSERS = 'Colored-Trousers'
    SHIRTS = 'Shirts'
    POLO_SHIRTS = 'Polo-Shirts'
    PLAID_SHIRTS = 'Plaid-Shirts'

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