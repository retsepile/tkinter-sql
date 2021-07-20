from tkinter import *
import mysql.connector
window = Tk()
window.geometry('500x500')
window.title("LOGIN")

label1 = Label(window, text='Please enter username:')
label1.place(x=0, y=10)
entry_name = Entry(window)
entry_name.place(x=200, y=10)
label2 = Label(window, text="Please enter password:")
label2.place(x=0, y=100)
password = Entry(window, show="*")
password.place(x=200, y=100)


def info():
    mydb = mysql.connector.connect(user='Lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='HOSPITAL', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from dentist')
    for i in mycursor:
        return mycursor


def login():
    window.destroy()


login_btn = Button(window, text="LOGIN", command=login)
login_btn.place(x=200, y=250)


def new_user():
    window.destroy()


user_btn = Button(window, text='Register new user', command=new_user)
user_btn.place(x=300, y=250)


window.mainloop()
