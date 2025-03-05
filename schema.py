from pydantic import BaseModel



class Alpha(BaseModel):
    title:str
    body:str
    number:int


class ShowAlpha(BaseModel):
    title:str
    number:int
    class Config():
        # orm_mode= True   #this is the old model of v1
        from_attributes = True  


class User(BaseModel):
    name : str
    email : str
    password : str


class ShowUser(BaseModel):
    name : str
    email : str
    class Config():
        from_attributes = True
    