from typing import Annotated, ClassVar, Optional
from annotated_types import Len
from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber



#subclasses: TH_Ticket, TCH_Ticket
#subclasses of TH_Ticket and TCH_Ticket will essentially be Ticket templates

class Ticket(BaseModel):

    customer_name: Annotated[str, Len(min_length=2, max_length=50)]
    contact_number: PhoneNumber
    location: Optional[Annotated[str, Len(min_length=2, max_length=80)]]
    department: Optional[Annotated[str, Len(min_length=2, max_length=80)]]
    issue: Annotated[str, Len(min_length=5, max_length=150)]
    device_list: Optional[list[Annotated[str, Len(min_length=5)]]]
   # desc: ClassVar[str] = """

   #    • Install Python on your system
    #{self.f_name} is an awesome dude
#"""
    
    

    @property
    def desc(self) -> str:
        return f"""
        Name: {self.customer_name}
        Contact Number: {self.contact_number}
        Location: {self.location if self.location else ""}
        Department: {self.department if self.department else ""}
        Device(s): {self.device_list.__str__}

        """

    
    

class TH_Ticket(Ticket):
    pass

class TCH_Ticket(Ticket):
    pass
#append before object instantiation

ext = "+1"
number = "513-992-9949"
full_number = f"{ext}{number}"

#print(full_number)

test = Ticket(customer_name="saif", location="accounting", department="idk", issue="can't get into pc" ,contact_number= full_number, device_list=["testy", "testy2", "testy3", "testy4", "testy5"])

print(test.desc)
