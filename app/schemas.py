from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
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
    
class UserResponse(BaseModel):
  id: int
  username: str
  email:EmailStr
  
  class Config:
    orm_mode=True
    
class Token(BaseModel):
  acces_token: str
  token_type: str