import tkinter as tk
from tkinter import ttk, Canvas
from PIL import Image, ImageTk
import sqlite3
from PIL import Image, ImageTk
import io
from tkinter import messagebox


#get blob binary image from database
def getQuestionImage(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT QuestionPhoto FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No image for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving image")

#get answer for question from database
def getQuestionAnswer(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT MSAnswer FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No answer for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving image")
    
#get binary MS image from database
def getMSImage(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT MSPhoto FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No image for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving image")
    
def getHint1(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT Hint1 FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No Hint for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving hint")
    
def getHint2(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT Hint2 FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No Hint for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving hint")
        
def getHint3(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT Hint3 FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No Hint for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving hint")
    
    except sqlite3.Error:
        return print("Error retrieving hint")

def getMaxMarks(qID):
    try:
        #connect to database
        Qdb = sqlite3.connect('Questions.sqlite')
        cursor = Qdb.cursor()
        
        #fetch image from QD from id
        query = "SELECT maxMarks FROM Questions WHERE ID = ?"
        cursor.execute(query, (qID,))
        record = cursor.fetchone()
        cursor.close()
        Qdb.close()
        
        if record:
            return record[0]
        else:
            return print("No Hint for ID given")
    
    except sqlite3.Error:
        return print("Error retrieving hint")


#create window for question page
class QuestionsPage(tk.Tk):
    def __init__(self, title):
        super().__init__()
        #configuring window size and title
        self.title(title)
        self.geometry('1000x1000')
        self.minsize(600, 600)
        self.maxsize(1000, 1000)
        
        #initalize ID for questions database
        self.qID = 1
        #frames into window
        self.canvasQs = CreateQuestionCanvas(self)
        self.createWidget()
        
        self.loadQuestion()
        #run program
        self.mainloop()
        
    def createWidget(self): 
        
        QButton = ttk.Button(text = 'Q', command = self.loadQuestion)
        QButton.place(x = 80, y = 50, height = 50, width = 100)
        
        ans_label = tk.Label(self, text = 'Answer Box')
        ans_label.place(x = 475, y = 725)
        
        self.ansEntry = tk.Entry(self)
        self.ansEntry.place(x = 415, y = 750, width = 200, height = 40)
        
        Hint1Button = ttk.Button(self, text = 'hint 1', command = self.showHint1 )
        Hint1Button.place(x = 200, y = 850, height = 35, width = 175)
        
        Hint2Button = ttk.Button(self, text = 'hint 2', command = self.showHint2 )
        Hint2Button.place(x = 425, y = 850, height = 35, width = 175)
        
        Hint3Button = ttk.Button(self, text = 'hint 3', command = self.showHint3 )
        Hint3Button.place(x = 650, y = 850, height = 35, width = 175)
        
        submitAnsButton = ttk.Button(self, text = '✔', command = self.checkAnswer )
        submitAnsButton.place(x = 650, y = 750, width = 100, height = 40)
        
        backHome_button = ttk.Button(self, text = "back", command = self.test)
        backHome_button.place(x = 900 ,y = 10)
        
        #have examples of how how to format answer on left of answer entry box
        
    def test(self):
        print('meow')
        
    def loadQuestion(self):
        binaryImage = getQuestionImage(self.qID)
        self.canvasQs.displayQImage(binaryImage)
        self.qID += 1
        
    def checkAnswer(self):
        answerEntry = self.ansEntry.get()
        qid = self.qID - 1
        rightAnswer = getQuestionAnswer(qid)
        
        if answerEntry == rightAnswer:
            tk.messagebox.showinfo(title = "Correct", message = "That was correct!")
            self.loadQuestion()
            self.ansEntry.delete(0, tk.END)
        else:
            tk.messagebox.showinfo(title = "Incorrect", message = "That was wrong")
            
        self.loadMS(qid)
        
    def showHint1(self):
        qID = self.qID - 1
        hint1 = getHint1(qID)
        tk.messagebox.showinfo(title = "Hint1", message = str(hint1))
        
    def showHint2(self):
        qID = self.qID - 1
        hint2 = getHint2(qID)
        tk.messagebox.showinfo(title = "Hint1", message = str(hint2))
        
    def showHint3(self):
        qID = self.qID - 1
        hint3 = getHint3(qID)
        tk.messagebox.showinfo(title = "Hint1", message = str(hint3))
            
    def loadMS(self, qID):
        binaryMSImage = getMSImage(qID)
        if binaryMSImage:
            MSimageWindow(binaryMSImage, qID)
            
        

#creating frame
class CreateQuestionCanvas(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 100, y = 100, relwidth = 0.8, relheight = 0.6)
        
        self.canvasMS = self.createCanvas()
        
    #creating canvas to insert questions pictures onto   
    def createCanvas(self):
        self.canvas = tk.Canvas(self, bg = 'white')
        self.canvas.pack(expand = True, fill = 'both')
        
    def displayQImage(self, binaryImage):
        #blobs stored are images that are formatted into binary format
        #io module treats this binary value as file-like object and does this using memory as a buffer instead of actually read and writing it
        binaryImage = io.BytesIO(binaryImage)
        photo = Image.open(binaryImage)
        
        self.qimage = ImageTk.PhotoImage(photo)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor = "nw", image=self.qimage)
       
       
       
#create window that shows MS      
class MSimageWindow(tk.Toplevel):
    def __init__(self, binaryMSImage, qID):
        super().__init__()
        self.title('Mark Scheme Answer ')
        self.geometry('600x600')
        self.minsize(600, 600)
        self.maxsize(1000, 1000)
          
        self.binaryMSImage = binaryMSImage
        self.qID = qID   
           
        self.canvas = self.createCanvas()
           
    def createCanvas(self):
        canvas = tk.Canvas(self, bg = 'white')
        canvas.pack(expand = True, fill = 'both')
        
        self.marksEntry = tk.Entry(self)
        self.marksEntry.place(x = 350, y = 500)
        
        
        AttemptMarks = getMaxMarks(self.qID)
        maxAttemptMarks = AttemptMarks - 1
        self.marksButton = ttk.Spinbox(self, from_=0, to=maxAttemptMarks )
        
        
        #self.marksButton = ttk.Button(self, text = "Marks Achieved", command = self.test)
        self.marksButton.place(x = 100, y = 500)
        
        self.tryAgainButton = ttk.Button(self, text = "Try again", command = self.tryAgain)
        self.tryAgainButton.place(x = 200 ,y = 200 )
        
        self.showMSButton = ttk.Button(self, text = "Show mark scheme", command = self.showMS)
        self.showMSButton.place(x = 200 ,y = 300 )
        
        return canvas
    
    def displayMSImage(self, binaryMSImage):
        #blobs stored are images that are formatted into binary format
        #io module treats this binary value as file-like object and does this using memory as a buffer instead of actually read and writing it
        binaryImage = io.BytesIO(binaryMSImage)
        photo = Image.open(binaryImage)
        
        self.msimage = ImageTk.PhotoImage(photo)
        
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor = "nw", image=self.msimage)
        
    def test(self):
        print('meow')
        
    def tryAgain(self):
        self.destroy()
        
    def showMS(self):
        #append database info into userInfo database
        self.tryAgainButton.destroy()
        self.showMSButton.destroy()
        self.displayMSImage(self.binaryMSImage)


QuestionsPage('Question Page')
        
#NEED TO FIX ATTEMPTS
#NEED TO APPEND DATA INTO USERINFO DATABASE
#KEEP TRACK OF NUMBER OF HINTS USED AND APPEND INTO USERINFO DATABASE
#INCLUDE A TIMER

        

