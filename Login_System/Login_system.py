import json
from tkinter import *
import tkinter.messagebox as tkm
w = Tk()
v = StringVar()
def Click_button(User = str, Pass_ = str):
    User = username.get()
    Pass_ = password.get()
    with open('user.json', 'r') as f_:
        d = json.load(f_)
    d[User] = Pass_
    while check_userwithpassword(User, Pass_):
        w.destroy()
        w_1 = Tk()
        w_1.title('Main window')
        w_1.mainloop()
        break
    if not check_userwithpassword(User, Pass_):
        warning_3 = tkm.showwarning('User not exist.','This account not exist, please create in "sign up".')

def remember_():
    global d_3, a ,b, User_v, Pass_v
    with open('User_save.json', 'r') as f_2:
        d_3 = json.load(f_2)
    if bool(d_3):
        d_3 = str(d_3)
        c = str({'' ''})
        for i in range(0, len(c)):
            d_3 = d_3.replace(c[i], "")
        d_3 = d_3.split(':')
        User_v = d_3[0]
        Pass_v = d_3[1].strip()
        a = username.insert(0, User_v)
        b = password.insert(0, Pass_v)                         
    else:
        pass

def check_in():
    global check
    User = username.get()
    Pass_ = password.get()
    with open('User_save.json', 'r') as f_2:
        d_2 = json.load(f_2)
    d_2 = {User : Pass_}
    with open('User_save.json', 'w') as f_2:
        json.dump(d_2, f_2)
    if v.get() == "Cheked.":
        check.destroy()
        check = Checkbutton(w, text = "Remembed!", fg = 'green', command = check_in, variable = v, onvalue = "Cheked.", offvalue = "Uncheked.")
        check.place(x = 10, y = 70)
    elif v.get() == "Uncheked.":
        check.destroy()
        check = Checkbutton(w, text = "Remember me", command = check_in, variable = v, onvalue = "Cheked.", offvalue = "Uncheked.")
        check.place(x = 10, y = 70)
        with open('User_save.json', 'r') as f_2:
            d_2 = json.load(f_2)
        d_2 = dict()
        with open('User_save.json', 'w') as f_2:
            json.dump(d_2, f_2)

def confirm_register(User_new = False):
    def Main_menu_again():
        w_1.destroy()
        b_1 = Button(w, width = 5, text = "Sign up", command = sign_up, activebackground = 'white', bg = 'blue', fg = 'white')
        b_1.place(x = 300,y = 70) 
    global Pass_new
    up_= False
    low_ = False
    condition_ = False
    not_r = False
    if User_new == False:
        User_new = username_new.get()
    Pass_new = password_new.get()
    if condition_ == False:
        if not_r == False:
            while check_ifexist(User_new):
                warning_3 = tkm.showwarning('User found.','This account already exist, please key other User.')
                not_r = True
                break
        if not_r == False:
            if len(Pass_new) < 8:
                warning_3 = tkm.showwarning('Password wrong.','Please key a password with at least 8 digits.')
                not_r = True
            else:
                pass
        if not_r == False:
                if Pass_new.isalnum():
                    warning_3 = tkm.showwarning('Password wrong.', 'Please key a password with a special character.')
                    not_r = True
                else:
                    pass
        if not_r == False:
                for i in range(0, len(Pass_new)):
                    if Pass_new[i].isupper():
                        up_ = True
                        break
                else:
                    pass
                if not up_ == True:
                    warning_3 = tkm.showwarning('Password wrong.', 'Please key a password with a upper letter.')
                    not_r = True
                    
        if not_r == False:
            for i in range(0, len(Pass_new)):
                if Pass_new[i].islower():
                    low_ = True
                    break
                else:
                    pass
        
            if not low_ == True:
                warning_3 = tkm.showwarning('Password wrong.', 'Please key a password with a a lower letter.')
                not_r = True
        
        if not_r == False:
            condition_ = True
            
    if condition_ == True:
        if not check_ifexist(User_new):
            register = Label(w_1, text = "Register successfully", fg = "Green")
            register.place(x = 160 , y = 90 )
        with open('user.json', 'r') as f_:
            d = json.load(f_)
        d[User_new] = Pass_new
        with open('user.json', 'w') as f_:
            json.dump(d, f_)
        b_2.config(text = "Exit", bg = "Red", command = Main_menu_again)
        b_2.place(x = 190,y = 110)   
    
def sign_up():
    global w_1, username_new, password_new, b_2
    w_1 = Tk()
    w_1.title("Sign Up")
    w_1.geometry("420x140+100+50")
    password_new = Entry(w_1, show = "*")
    password_new.place(x = 160, y= 40)
    username_new = Entry(w_1)
    username_new.place(x = 160,y = 10)
    b_2 = Button(w_1, width = 6, text = "Confirm", command = confirm_register, bg = 'green', fg = 'white', activebackground = 'white')
    b_2.place(x = 190,y = 110)
    name = Label(w_1, text="Username")
    name.place(x = 100, y = 10)
    Pass = Label(w_1, text = "Password")
    Pass.place(x = 100, y = 40)
    b_1 = Button(w, width = 5, text = "Sign up", command = sign_up,state = DISABLED, disabledforeground = 'red' )
    b_1.place(x = 300,y = 70)
    condition_pass = Label(w_1, text = 'Password must have at least: \n Eight characters, One uppper letter, One lower letter, One special character.', fg = 'red')
    condition_pass.place(x = 10, y = 60)
    w_1.mainloop()

def check_ifexist(Name_3):
    global d_3
    with open('user.json', 'r') as f_:
        d_3 = json.load(f_)
    if Name_3 in d_3:
        return True
    else:
        return False

def check_userwithpassword(Name_2, Pass_2):
    global d_
    with open('user.json', 'r') as f_:
        d_ = json.load(f_)
    if Name_2 in d_:
        if d_[Name_2] == Pass_2:
            return True
        else:
            return False

        
w.title("Sign In")
b = Button(w, width = 5, text = "log in", command = Click_button, activebackground = 'white', bg = 'green', fg = 'white')
b.place(x = 350,y = 70)
b_1 = Button(w, width = 5, text = "Sign up", command = sign_up, activebackground = 'white', bg = 'blue', fg = 'white')
b_1.place(x = 300,y = 70)
name = Label(w, text="Username")
name.place(x = 100, y = 10)
Pass = Label(w, text = "Password")
Pass.place(x = 100, y = 40)
username = Entry(w)
username.place(x = 160,y=10)
password = Entry(w, show = "*")
password.place(x = 160, y= 40)
check = Checkbutton(w, text = "Remember me", command = check_in, variable = v, onvalue = "Cheked.", offvalue = "Uncheked.")
check.place(x = 10, y = 70)
remember_()
w.geometry("400x100+100+50")
w.mainloop()
