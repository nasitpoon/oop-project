from typing import Union
from fastapi import FastAPI
from tkinter import messagebox
import tkinter as tk
import requests
import new as n

app = FastAPI()
system = n.System()

# สร้างหน้าต่าง Tkinter
root = tk.Tk()
root.title("Registration")
url = "http://127.0.0.1:8000/register"

def register_to_fastapi():
    payload = {
        "fname": entry_fname.get(),
        "lname": entry_lname.get(),
        "email": entry_email.get(),
        "password": entry_password.get(),
        "confirmed_password": entry_confirmed_password.get(),
        "phone_number": entry_phone_number.get()
    }
    response = requests.post(url, json=payload)
    if response.ok:
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "Registration failed.")


# # ฟังก์ชันสำหรับการส่งข้อมูลการลงทะเบียนไปยัง FastAPI
# def register_to_fastapi():
#     payload = {
#         "fname": entry_fname.get(),
#         "lname": entry_lname.get(),
#         "email": entry_email.get(),
#         "password": entry_password.get(),
#         "confirmed_password": entry_confirmed_password.get(),
#         "phone_number": entry_phone_number.get()
#     }
#     response = requests.post(url, json=payload)
#     if response.ok:
#         message = response.json().get('message', 'Unknown error')
#     else:
#         message = "Error occurred"
#     lbl_result.config(text=message)
    # fname = entry_fname.get()
    # lname = entry_lname.get()
    # email = entry_email.get()
    # password = entry_password.get()
    # confirmed_password = entry_confirmed_password.get()
    # phone_number = entry_phone_number.get()

    # # ส่งข้อมูลการลงทะเบียนไปยัง FastAPI
    # response = requests.post("http://localhost:8000/register", data={
    #     "fname": fname,
    #     "lname": lname,
    #     "email": email,
    #     "password": password,
    #     "confirmed_password": confirmed_password,
    #     "phone_number": phone_number
    # })

    # # แสดงผลลัพธ์จาก FastAPI
    # if response.status_code == 200:
    #     message = response.json().get('message', 'Unknown error')
    # else:
    #     message = "Error occurred"

    # lbl_result.config(text=message)


# สร้างฟอร์มลงทะเบียน
lbl_fname = tk.Label(root, text="First Name:")
lbl_fname.pack()
entry_fname = tk.Entry(root)
entry_fname.pack()

lbl_lname = tk.Label(root, text="Last Name:")
lbl_lname.pack()
entry_lname = tk.Entry(root)
entry_lname.pack()

lbl_email = tk.Label(root, text="Email:")
lbl_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

lbl_password = tk.Label(root, text="Password:")
lbl_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

lbl_confirmed_password = tk.Label(root, text="Confirmed Password:")
lbl_confirmed_password.pack()
entry_confirmed_password = tk.Entry(root, show="*")
entry_confirmed_password.pack()

lbl_phone_number = tk.Label(root, text="Phone Number:")
lbl_phone_number.pack()
entry_phone_number = tk.Entry(root)
entry_phone_number.pack()

btn_register = tk.Button(root, text="Register", command=register_to_fastapi)
btn_register.pack()

# lbl_result = tk.Label(root, text="")
# lbl_result.pack()

root.mainloop()










