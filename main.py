# from typing import Union

# from fastapi import FastAPI

# import new as n

# app = FastAPI()
# system = n.System()

# @app.post("/register")
# async def register(fname : str, lname : str, email : str, password : str, confirmed_password : str, phone_number : str):
#     if len(fname) < 3:
#         return {"message" : "First name need to be more then 3 characters"}
#     if len(lname) < 3:
#         return {"message" : "Last name need to be more then 3 characters"}
#     if password != confirmed_password:
#         return {"message" : "Password Invalid"}
#     if len(phone_number) != 10:
#         return {"message" : "Phone number Invalid"}
#     else:
#         system.create_user(fname, lname, email, password, phone_number)
#         return {"message" : "Register success"}

# @app.get("/show_account_list")
# async def show_account_list():
#     return {"account_list" : system.acc_list}
# from typing import Union

from typing import Union
from fastapi import FastAPI
import requests
import new as n

app = FastAPI()
system = n.System()

@app.post("/register")
async def register(fname: str, lname: str, email: str, password: str, confirmed_password: str, phone_number: str):
    if len(fname) < 3:
        return {"message": "First name needs to be more than 3 characters"}
    if len(lname) < 3:
        return {"message": "Last name needs to be more than 3 characters"}
    if password != confirmed_password:
        return {"message": "Password Invalid"}
    if len(phone_number) != 10:
        return {"message": "Phone number Invalid"}
    else:
        system.create_user(fname, lname, email, password, phone_number)
        return {"message": "Register success"}
        return fname, lname, email, password, phone_number
