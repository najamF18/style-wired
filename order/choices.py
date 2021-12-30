from enum import Enum
from men.models import StyleProfileMen
from women.models import StyleProfileWomen

class SpendingRangeEnum(Enum):
    RANGE1 = '40-80'
    RANGE2 = '80-150'
    RANGE3 = '150-300'
    RANGE4 = '300-500'
    RANGE5 = '500-open end'
    RANGE6 = 'Female'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
    
class AddOnEnum(Enum):
    ADD_ON1 = 'Add-on1'
    ADD_IN2 = 'Add-on2'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    

class StatusEnum(Enum):
    PENDING = 'Pending'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class PaymentMethodEnum(Enum):
    Credit_CARD = 'Credit-Card'
    PAYPAL = 'Paypal'
    MASTER_CARD = 'Master-Card'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
