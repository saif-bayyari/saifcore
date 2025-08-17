from typing import Annotated
from annotated_types import Len
from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber





class Ticket(BaseModel):

    f_name: Annotated[str, Len(min_length=2, max_length=50)]
    l_name: Annotated[str, Len(min_length=2, max_length=50)]
    contact_number: PhoneNumber
    my_list: list[Annotated[str, Len(min_length=5)]]






test = Ticket(f_name="saif", l_name = "bayyari", contact_number= "+1513-601-4831", my_list=["testy", "testy2", "testy3", "testy4", "testy5"])




