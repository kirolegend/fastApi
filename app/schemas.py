from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
  name: str
  last_name: str
  username: str
  email: EmailStr
  password: str
  
class UserLogin(BaseModel):
  username_or_email: str
  password: str
  
# Схема для вывода данных пользователя (выход)
class UserOut(BaseModel):
  id: int
  username: str
  email: EmailStr
  name: str
  last_name: str

  class Config:
    orm_mode = True
    
class UserResponse(BaseModel):
  id: int
  username: str
  email:EmailStr
  
  class Config:
    orm_mode=True
    
class Token(BaseModel):
  access_token: str
  token_type: str