import tkinter as tk
from tkinter import ttk
from sympy import symbols, solveset, Eq, solve
from sympy.abc import S,U,V,A,T
from tkinter import messagebox
import math


#creating suvat window
class SuvatPage(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry('1000x1000')
        self.minsize(600, 600)
        self.maxsize(1000, 1000)
        #suvatmenu where you input known suvat values for x and y components
        self.Suvatmenu = SuvatMenu(self)
        #suvat diagram
        self.Diagram = Diagram(self)
        #suvat tips and back button
        self.tips = Tips(self)
        #run
        self.mainloop()
#creating fram for suvat menu     
class SuvatMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #creating frame where you enter suvat values
        self.parent = parent
        self.place(x=0, y=0, relwidth = 0.4 , relheight = 0.5)
        
        self.create_SuvatWidgets()
               
    def gettingSuvatValues(self, component):
        
        s, u, v, a, t = component

        if s == None and u == None and v == None and a == None and t == None:
            return print("no values entered")        
        
        temp = component.copy()
        
        component.clear()
        
        for item in temp:
            if item != "":
                component.append(float(item))
            else:
                component.append(None)

        #component[0] = s
        #component[1] = u 
        #component[2] = v
        #component[3] = a
        #component[4] = t

        #equations
               
        SUAT = Eq(S, 0.5*A*T**2 + U*T)
        VUAT = Eq(V, U + A*T)
        UASV = Eq(V**2, U**2 + 2*A*S)
        SUVT = Eq(S, (U+V)/2 * T)
        SVAT = Eq(S, V*T - 0.5*A*T**2)
        SVT  = Eq(S, V*T)
        
        '''SVAT has problems'''
        
        #while None in component:
            
        s, u, v, a, t = component
        
        #if a = 0, u = v
        if component[3] == 0 and component[1] != None and component[2] == None:
            component[2] = component[1]
        
        if s == None and u == None and v == None and a == None and t == None:
            return print("no values entered")
         
        #finds s value
        if s == None :
            if component[4] != None and component[1] != None and component[3] != None:
                s = solve(SUAT.subs({T: t, U: u, A: a}), S)
            elif component[4] != None and component[1] != None and component[2] != None:
                s = solve(SUVT.subs({T: t, U: u, V: v}), S)
            elif component[3] != None and component[1] != None and component[2] != None:
                s = solve(UASV.subs({A: a, U: u, V: v}), S)
            elif component[2] != None and component[3] != None and component[4] != None:
                s = solve(SVAT.subs({V: v, A: a, T: t}), S)
            elif component[3] == 0 and component[2] != None and component[4] != None:
                    s = solve(SVT.subs({V: v, T: t}), S)
            s = s[0]
            s = round(s, 2)
            print("s: ", s)
        #finds u value  
        if u == None:
            if component[0] != None and component[2] != None and component[3] != None:
                u = solve(UASV.subs({S: s, A: a, V: v}), U)
            elif component[0] != None and component[4] != None and component[3] != None:
                u = solve(SUAT.subs({S: s, T: t, A: a}), U)
            elif component[2] != None and component[4] != None and component[3] != None:
                u = solve(VUAT.subs({V: v, T: t, A: a}), U)
            elif component[2] != None and component[4] != None and component[0] != None:
                u = solve(SUVT.subs({V: v, T: t, S: s}), U)
            print("u: ", u)
            
            try:
                if len(u) > 1:    
                    for items in u:
                        items = float(items)
                    u = round(u[1], 2)
                    u = ("± " + str(u))
                else:
                    u = round(u[0], 2)
                print("u:", u)
            except TypeError:
                print("complex number is impossible)")
            
            
            #finds v value ±
        if v == None:
            if component[3] != None and component[4] != None and component[1] != None:
                v = solve(VUAT.subs({A: a, T: t, U: u}), V)
            elif component[3] != None and component[0] != None and component[1] != None:
                v = solve(UASV.subs({A: a, S: s, U: u}), V)
            elif component[4] != None and component[0] != None and component[1] != None:
                v = solve(SUVT.subs({T: t, S: s, U: u}), V)
            elif component[0] != None and component[3] != None and component[4] != None:
                v = solve(SVAT.subs({S: s, A: a, T: t}), V)
            elif component[3] == 0 and component[0] != None and component[4] != None:
                    v = solve(SVT.subs({S: s, T: t}), V)
            print("v: ", v)
            
            try:
                if len(v) > 1:    
                    for items in v:
                        items = float(items)
                    v = round(v[1], 2)
                    v = ("± " + str(v))
                else:
                    v = round(v[0],2)
                print("v:", v)
            except TypeError:
                print("complex number is impossible)")

        #finds a value
        if a == None:
                if component[0] != None and component[4] != None and component[1] != None:
                    a = solve(SUAT.subs({S: s, T: t, U: u}), A)
                elif component[2] != None and component[4] != None and component[1] != None:
                    a = solve(VUAT.subs({V: v, T: t, U: u}), A)
                elif component[0] != None and component[2] != None and component[1] != None:
                    a = solve(UASV.subs({S: s, V: v, U: u}), A)
                elif component[2] != None and component[0] != None and component[4] != None:
                    a = solve(SVAT.subs({V: v, S: s, T: t}), A)
                a = a[0]
                a = round(a, 2)
                print("a: ", a)
        #finds t values
        if t == None :
            t_values = []
            if component[2] != None and component[1] != None and component[3] != None:
                t = solve(VUAT.subs({V: v, U: u, A: a}), T)
            elif component[0] != None and component[1] != None and component[2] != None:
                t = solve(SUVT.subs({S: s, U: u, V: v}), T)
            elif component[0] != None and component[1] != None and component[3] != None:
                t = solveset(SUAT.subs({S: s, U: u, A: a}), T)
            elif component[3] != None and component[3] != None and component[0] != None:
                t = solveset(SVAT.subs({V: v, A: a, S: s}), T)
            elif component[3] == 0 and component[2] != None and component[0] != None:
                    t = solve(SVT.subs({V: v, S: s}), T)
            print("t: ", t)
            #removing negative t values
            t = list(t)
            for i in t:
                try:
                    if i < 0:
                        str(t)
                        t.remove(i)
                except TypeError:
                    print("carnt compare complex numbers")
                if len(t) == 0:
                    tk.messagebox.showwarning(title = "Warning", message = "there are no solutions for time, so values are impossible")
                else:
                    i = round(i, 2)
                    
                print("t: ",str(t))
               
        '''
        NEED TO REMOVE COMPLEX VALUES
        AND NEED TO ROUND SOME NUMBERS
        '''
                 
        component[0] = s
        component[1] = u
        component[2] = v
        component[3] = a
        component[4] = t
        
        
        return component
    
    def create_SuvatWidgets(self):
        #labels of x and y compononents and suvat labels
        x_label = tk.Label(self, text = "x")
        y_label = tk.Label(self, text = "y")
        s_label = tk.Label(self, text = "s")
        u_label = tk.Label(self, text = "u")
        v_label = tk.Label(self, text = "v")
        a_label = tk.Label(self, text = "a")
        t_label = tk.Label(self, text = "t")
        
        #create entrys
        #x components
        self.sx_Entry = ttk.Entry(self)
        self.ux_Entry = ttk.Entry(self)
        self.vx_Entry = ttk.Entry(self)
        self.ax_Entry = ttk.Entry(self)
        #y components
        self.sy_Entry = ttk.Entry(self)
        self.uy_Entry = ttk.Entry(self)
        self.vy_Entry = ttk.Entry(self)
        self.ay_Entry = ttk.Entry(self)
        #t component
        self.t_Entry = ttk.Entry(self)
        #button to get missing values button
        getVals = ttk.Button(self, text = "get missing values", command = self.getValues)
        #button to clear values
        clearVals = ttk.Button(self, text = "clear", command = self.clear)
        
        #create grid
        self.columnconfigure((0,1,2), weight = 1, uniform ='a')
                             
        #placing widgets
        #placing labels
        x_label.grid(row = 0, column = 1)
        y_label.grid(row = 0, column = 2)
        s_label.grid(row = 1, column = 0)
        u_label.grid(row = 2, column = 0)
        v_label.grid(row = 3, column = 0)
        a_label.grid(row = 4, column = 0)
        t_label.grid(row = 5, column = 0)
        
        #placing entrys
        self.sx_Entry.grid(row = 1, column = 1, padx = 3, pady= 3)
        self.ux_Entry.grid(row = 2, column = 1, padx = 3, pady= 3)
        self.vx_Entry.grid(row = 3, column = 1, padx = 3, pady= 3)
        self.ax_Entry.grid(row = 4, column = 1, padx = 3, pady= 3)
        
        self.sy_Entry.grid(row = 1, column = 2)
        self.uy_Entry.grid(row = 2, column = 2)
        self.vy_Entry.grid(row = 3, column = 2)
        self.ay_Entry.grid(row = 4, column = 2)
        
        self.t_Entry.grid(row = 5, column = 1, columnspan = 2)
        
        #place getVals button
        getVals.grid(row = 6, column = 1, columnspan = 2, padx = 3, pady= 10)
        #place clearVals button
        clearVals.grid(row = 6, column = 0, padx = 3, pady= 10)
        
    def getValues(self):
        
        # getting values from entrys
        sx = self.sx_Entry.get()
        ux = self.ux_Entry.get()
        vx = self.vx_Entry.get()
        ax = self.ax_Entry.get()
        
        sy = self.sy_Entry.get()
        uy = self.uy_Entry.get()
        vy = self.vy_Entry.get()
        ay = self.ay_Entry.get()
        
        t  = self.t_Entry.get()
    
        #getting values if diagram info is given
        inital_s, angle, inital_u = self.parent.Diagram.getDiagramValues()
        
        if angle != "" and inital_u != "":
            angle = float(angle)
            inital_u = float(inital_u)
            angle_radians = (math.radians(angle))
            
            #getting components of u with angle
            ux = math.cos(angle_radians) * (inital_u)
            uy = math.sin(angle_radians) * (inital_u)       
        
        #appending values into component lists
        xcomponent = [sx, ux, vx, ax, t]
        ycomponent = [sy, uy, vy, ay, t]
        
        '''NOT SURE THIS PART WORKS'''
        if inital_s != "":
            ycomponent[0] += (inital_s)
        
        '''
        ENSURING THERE ARE ENOUGH VALUES
        ENSURE THAT ATLEAST 3 INPUTS ARE INPUTED IN MENU/ 2 INPUTS EACH COMPONENT AND T/ 2 COMPONENTS AND ANGLE AND U
        '''
        
        '''AllowSuvat = True
        enough_xVals = 0
        for item in xcomponent:
            if item != "":
                enough_xVals += 1
        enough_yVals = 0
        for item in ycomponent:
            if item != "":
                enough_yVals += 1    
        
        enough_t = len(t)
    
        if 0 < enough_xVals < 2:
            AllowSuvat = False
        elif 0 < enough_yVals < 2:
            AllowSuvat = False
        elif enough_t == 0 and 0 < enough_xVals < 2: 
            AllowSuvat = False
        elif enough_t == 0 and 0 < enough_yVals < 2:
            AllowSuvat = False
        
        
        if AllowSuvat == False:
            tk.messagebox.showwarning(title = "Warning", message = "Must input atleast 3 inputs to get all values")
        
        if AllowSuvat == True:'''
        
        #getting missing suvat values for x and y components
        self.gettingSuvatValues(xcomponent)
        self.gettingSuvatValues(ycomponent)

        print(xcomponent, ycomponent)
        
        
        #putting x componenets entrys all in one list
        xentrys = [self.sx_Entry, self.ux_Entry,self.vx_Entry,self.ax_Entry, self.t_Entry]
        
        #as t isnt in x entry it is seperate
        t = xcomponent[4]
        
        #entering xvalues into entrys again
        for entry, value in zip(xentrys, xcomponent): #matches xentrys[i] to xcomponents[i]
            if value != None:
                if isinstance(value, list): #sees if value is a list or not
                    value = value[0]
                #value = round(value, 2)
                entry.delete(0, tk.END)
                entry.insert(0, str(value))
        
        #doing same for y component
        yentrys = [self.sy_Entry, self.uy_Entry,self.vy_Entry,self.ay_Entry, self.t_Entry]
        
        for entry, value in zip(yentrys, ycomponent): #matches xentrys[i] to xcomponents[i]
            if value != None:
                if isinstance(value, list): #sees if value is a list or not
                    value = value[0]
                #value = round(value, 2)
                entry.delete(0, tk.END)
                entry.insert(0, str(value))
        
        #inserting t into t_Entry
        try:
            if isinstance(t, list):
                t1 = t[0]
                t2 = t[1]
                t1 = round(t1, 2)
                t2 = round(t2, 2)
                print(t1, t2)
                t = str(t1) + "," + str(t2)
        except IndexError:
            t = str(round(t[0],2))
             
        '''ROUNDING DOES NOT WORK'''
        
        self.t_Entry.delete(0, tk.END)
        self.t_Entry.insert(0, str(t))
        
    #clearing all entrys
    def clear(self):
        
        entrys = [ self.sx_Entry, self.ux_Entry,self.vx_Entry,self.ax_Entry, self.t_Entry,
                   self.sy_Entry, self.uy_Entry,self.vy_Entry,self.ay_Entry, self.t_Entry ]
        
        for entry in entrys:
            entry.delete(0, tk.END)

#creating frame for diagram
class Diagram(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #creating frame for diagram
        self.place(x=0, y=220, relwidth = 1 , relheight = 1)
    
        self.createDiagram()
    
    #actually creating diagram
    def createDiagram(self):
        #creating canvas 
        canvas = tk.Canvas(self, bg='white')
        canvas.pack(expand = True, fill = 'both')
        #creating rectangle where you input inital height
        canvas.create_rectangle((0, 450, 200, 850), outline = 'black')
        #creating arc of projectile
        canvas.create_arc((70, 200, 920 ,1500),start = 0, extent = 142, outline = 'black', style = tk.ARC)
        #create arc of angle
        canvas.create_arc((94, 400 , 194 ,500),start = 0, extent = 45, outline = 'black', style = tk.ARC)
        
        #create intial height label
        initialS_label = tk.Label(self, text = "inital height")
        angle_label = tk.Label(self, text = "angle")
        initalU_label = tk.Label(self, text = "U of projectile")
        #create inital height, inital u and angle entry box
        self.initalS_Entry = ttk.Entry(self)
        self.angle_Entry = ttk.Entry(self)
        self.initalU_Entry = ttk.Entry(self)
        
        #placing labels
        intitalS_label_window = canvas.create_window(100, 570, window = initialS_label)
        angle_lable_window = canvas.create_window(300, 390, window = angle_label)
        initalU_lable_window = canvas.create_window(100, 350, window = initalU_label)
        #placing entry box
        initalS_Entry_window = canvas.create_window(100, 600, window = self.initalS_Entry)
        angle_Entry_window = canvas.create_window(300, 420, window = self.angle_Entry)
        initalU_Entry_window = canvas.create_window(100, 380, window = self.initalU_Entry)

        ''' NEED TO MAKE CANVAS REACTIVE TO WHAT ANGLE AND INITAL HEIGHT IS GIVEN'''

    def getDiagramValues(self):
        initial_s = self.initalS_Entry.get()
        angle = self.angle_Entry.get()
        initial_u = self.initalU_Entry.get()
        
        return initial_s, angle, initial_u

class Tips(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #creating frame for diagram
        self.place(x=420, y=0, relwidth = 1 , relheight = 0.2)
        
        #creating labels of tips
        tips1_label = tk.Label(self, text = "the acceleration of the xcomponent of a projectile is 0 ms^-2, so u = v")
        tips2_label = tk.Label(self, text = "there are still rounding error")
        tips3_label = tk.Label(self, text = "there may be complex numbers returned, please note that is means values are impossible")
        tips4_label = tk.Label(self, text = "if there are ± v/u solutsions and only one t value, remove v/u value and retry missing values button")
        
        #self.columnconfigure((0), weight = 1, uniform ='a')
        self.rowconfigure((0,1,2), weight = 0, uniform = 'a')
        #creating button to go back to home screen
        backHome_button = ttk.Button(self, text = "back", command = self.test)

        #placing labels
        tips1_label.grid(row = 2, column = 0)
        tips2_label.grid(row = 3, column = 0)
        tips3_label.grid(row = 4, column = 0)
        tips4_label.grid(row = 5, column = 0)

        backHome_button.place(x = 480 ,y = 10)
    
    def test(self):
        print("meow")

SuvatPage('suvat calculator')

#could try make it find max height for y and x
#make clear button clear canvas entries
#have a calculator title