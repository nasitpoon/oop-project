from typing import Union
from registernew import System
from registernew import Account
from fastapi import FastAPI


app = FastAPI()


@app.get("/login")
async def loginacc(email : str, password : str):
    if s.login(email,password) == 'Pass':
        return 'pass'
    elif s.login(email,password) == 'Incorrect password':
        return 'Incorrect password'
    elif s.login(email,password) == 'Not found user':
        return 'Not found user'

s = System()
poon = Account('P','o')
park = Account('Pa','r')
s.add_account(poon)
s.add_account(park)

