import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


#creating welcome page window
class WelcomePage(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('600x600')
        self.minsize(1000, 600)
        self.maxsize(1000, 1000)
        
        self.homescreeen = HomeScreen(self)
        

#creating frame for widgets
class HomeScreen(ttk.Frame):
        def __init__(self, parent):
            super().__init__(parent)
            #creating frame where you enter suvat values
            self.parent = parent
            self.place(x=0, y=0, relwidth = 1 , relheight = 1)
            
            self.createWidgets()
        
        def createWidgets(self):
            #create title
            welcome_label = tk.Label(self, text = "Welcome to" , font=(15))
            suvatTitle_label = tk.Label(self, text = "The SUVAT Calculator",font=("Arial", 36, "bold"))
            #create buttons
            suvatpage_button = ttk.Button(text = "Suvat Page", command = self.test, width = 30)
            qPage_button = ttk.Button(text = "Question Page", command = self.test, width = 30)
            login_button = ttk.Button(text = "login", command = LoginPage, width = 13)
            register_button = ttk.Button(text = 'register', command = RegisterPage, width = 13)
            
            #place title
            welcome_label.place(x = 300, y = 120 )
            suvatTitle_label.place(x = 300, y = 150)
            #place buttons
            suvatpage_button.place(x = 430, y=300)
            qPage_button.place(x=430, y=350)
            login_button.place(x=430, y=400)
            register_button.place(x=532, y=400)

        #tempoary subsitute for missing codes
        def test(self):
            print("...")

#creating login window 
class LoginPage(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('login')
        self.geometry('600x600')
        self.minsize(600, 600)
        self.maxsize(1000, 1000)
        
        self.create_widgets()
        
        self.mainloop()
    def create_widgets(self):
        #creating widgets
        Login_title = tk.Label(self, text = "Login", font=("Arial", 26, "bold"))
        username_label = tk.Label(self, text = "Username : ")
        self.username_entry = ttk.Entry(self)
        password_label = tk.Label(self, text = "Password : ")
        self.password_entry = ttk.Entry(self)
        login_button = ttk.Button(self, text = "login", command = self.Login, width = 13)
        
        #place widgets
        Login_title.place(x= 260, y= 100)
        username_label.place(x= 200, y = 200)
        self.username_entry.place(x=300 ,y=200 )
        password_label.place(x= 200,  y= 250)
        self.password_entry.place(x=300 ,y=250 )
        login_button.place(x=270 ,y=300 )

    def Login(self):
        #accessing accounts database
        login_DB = sqlite3.connect('Accounts.sqlite')
        #creating database if it doesnt exist
        login_DB.execute('CREATE TABLE IF NOT EXISTS accounts(ID INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, password TEXT)')
        #check if username and password details are in database
        cursor = login_DB.cursor()
        cursor.execute("SELECT * FROM Accounts where username=? AND password=?",(self.username_entry.get(), self.password_entry.get()))
        row = cursor.fetchone()
        #if details are correct
        if row:
            #messagebox to show success and destroy window
            messagebox.showinfo('info', 'login success')
            self.destroy()
        else:
            messagebox.showinfo('info', 'login failed')
        #saving database and closing it
        login_DB.commit()
        login_DB.close()


class RegisterPage(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Register')
        self.geometry('600x600')
        self.minsize(600, 600)
        self.maxsize(1000, 1000)
        
        self.create_widgets()
        
        self.mainloop()

    def create_widgets(self):
        #creating widgets
        Register_title = tk.Label(self, text = "Register", font=("Arial", 26, "bold"))
        username_label = tk.Label(self, text = "Username : ")
        self.username_entry = ttk.Entry(self)
        password_label = tk.Label(self, text = "Password : ")
        self.password_entry = ttk.Entry(self)
        Register_button = ttk.Button(self, text = "Register", command = self.Register, width = 13)
        
        #place widgets
        Register_title.place(x= 250, y= 100)
        username_label.place(x= 200, y = 200)
        self.username_entry.place(x=300 ,y=200 )
        password_label.place(x= 200,  y= 250)
        self.password_entry.place(x=300 ,y=250 )
        Register_button.place(x=270 ,y=300 )

    def Register(self):
        #connect to database
        conn = sqlite3.connect('Accounts.sqlite')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Accounts(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)')
        
        # Check if the username already exists
        cursor.execute('SELECT * FROM accounts WHERE username=?', (self.username_entry.get(),))
        if cursor.fetchone():
            # If a row is returned, the username exists
            messagebox.showinfo('Info', 'Account with this username already exists')
        else:
            cursor.execute('INSERT INTO Accounts(username,password) VALUES(?,?)', (self.username_entry.get(), self.password_entry.get()))
            conn.commit()
            messagebox.showinfo('info', 'Registration success')
            self.destroy()
    
    
WelcomePage('suvat calculator')








