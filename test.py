
from typing import List, Optional
from pydantic import BaseModel


#IT'S A COLON!!!! NOT A EQUAL SIGN!!!! REMEMBER THAT !!!!!
class Test(BaseModel):
    test : List[str]



test1 = Test(test=["device1", "device2", "device3"])

for device in test1.test:
    print(device)       
        