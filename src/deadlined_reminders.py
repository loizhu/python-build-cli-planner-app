from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass
#In the same src/deadlined_reminders.py file also import 
# the ABC class from the abc module. 
# Then create another abstract base class 
# named DeadlinedReminder. 
# Make it inherit from ABC instead of passing the 
# metaclass parameter. 
# Like above, it should also inherit from Iterable.
class DeadlinedReminder(Iterable, ABC):
    #Then add the same @abstractmethod method as before, 
    # namely is_due(), with the body pass.
    @abstractmethod
    def is_due(self):
        pass
#For convenience, in the following tasks we will use 
# the DeadlinedReminder as a base class.
#NOTE: Both DeadlinedMetaReminder and DeadlinedReminder 
# have the two abstract methods we need: 
# __iter__() comes from Iterable, while is_due() 
# was defined by us. 
# Any class that extends any of them will have to 
# implement both methods in order to be concrete.
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True

#Then, create a class named DateReminder which 
# derives from the DeadlinedReminder ABC. 
# Its __init__() method takes a text and date parameter, 
# alongside the usual self. 
# Use the parse() function that you imported to 
# store the date parameter onto self, 
# and pass it the dayfirst=True keyword 
# argument to avoid confusion for dates like 02/02/09. 
# Then store the text as it is onto the self object.
class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.text = text
        self.date = parse(date, dayfirst=True)

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])
#Your DateReminder is still abstract, 
# as it does not implement all the abstract methods of
#  the DeadlinedReminder ABC.
#Therefore, you should create the is_due() method on 
# the class, thus overriding the abstract one 
# of the base class. Inside it, you should check whether
#self.date is less than or equal to datetime.now().
    def is_due(self):
        return self.date < datetime.now()