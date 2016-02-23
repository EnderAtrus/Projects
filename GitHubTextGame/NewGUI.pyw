from tkinter import *
import cleaned_tkdink

class window:
    
    def __init__(self):
        self.auth = False
        self.authCount = 1
        self.master = Tk()
        self.master.title('Text Message Guessing Game!')
        self.master.minsize(400,200)
        self.password = "Password"
        
        self.l1 = Label(self.master, text="Enter Password")
        self.l1.pack(side ='top')
        
        self.e1 = Entry(self.master)
        self.e1.bind("<Return>", lambda e:self.slowLogin()) 
        self.e1.pack()
        
        self.b1 = Button(self.master, text='Quit', command=self.master.quit)
        self.b2 = Button(self.master, text='Enter', command=self.login)
        self.b1.pack(side='bottom')
        self.b2.pack(side='top')

        self.master.mainloop()
    def slowLogin(self):
        self.l1['text'] = 'Loading...'
        if self.auth != True:
            self.login()
        
    def start(self):
        if self.auth:
            self.l1['text'] = 'Loading...'
            
            self.e1.pack_forget()
            self.b2.pack_forget()

            #self.l0 = Label(self.master, text = 'Welcome! :)')
            #self.l0.pack(side='top')
            self.Game = cleaned_tkdink.gamevar()
            self.Game.makeArrays()

            self.l1['text'] = 'Who said this? '
            self.updateMsg()
            self.lmsg1 = Label(self.master, text = '')
            self.lmsg2 = Label(self.master, text = '')
            self.lmsg3 = Label(self.master, text = '')
            self.lmsg4 = Label(self.master, text = '')
            
            self.lmsg1.pack(expand=0)
            self.lmsg2.pack(expand=0)
            self.lmsg3.pack(expand=0)
            self.lmsg4.pack(expand=0)

            self.b2 = Button(self.master, text ='Seth?', command=self.guessSeth)
            self.b2.pack(side='bottom')
            
            self.b3 = Button(self.master, text='Alysala?',command=self.guessAlysala)
            self.b3.pack(side='bottom')

            self.loutcome = Label(self.master, text ='')
            self.loutcome.pack()

            self.lwin = Label(self.master, text ='')
            self.lwin.pack()

            self.printMsg()

            
    def login(self):
##  TEMP REMOVAL OF PASSWORD CHECK
        if self.authCount >= 3:
            self.master.quit()
        if self.e1.get() == self.password:
            self.l1['text'] = 'Loading...'
            self.auth = True
            self.start()            
        self.authCount += 1
##        self.auth = True #Remove this later
##        self.start()#remove this later
        
    def show_entry_fields(self):
        print("Password: %s\n" % (self.e1.get()))

    def updateMsg(self):
        self.Game.newcf()
        self.Game.newMsg()
        while len(self.Game.getMsg()) < 34:
            self.Game.newMsg()

    def printMsg(self):
        self.lwin['text'] = str(self.Game.counter.wins)+' wins out of '+str(self.Game.counter.total)
        self.resetMsg()

        #for debugging
##        print(self.Game.getMsg())
##        print('')
        
        if len(self.Game.getMsg())//3 > 150:
            self.lmsg1['text'] = self.Game.getMsg()[0:(len(self.Game.getMsg())//4)+1]
            self.lmsg2['text'] = self.Game.getMsg()[(len(self.Game.getMsg())//4):2*(len(self.Game.getMsg())//4)+1]
            self.lmsg3['text'] = self.Game.getMsg()[2*(len(self.Game.getMsg())//4):3*(len(self.Game.getMsg())//4)+1]
            self.lmsg4['text'] = self.Game.getMsg()[3*(len(self.Game.getMsg())//4):-1]
        elif len(self.Game.getMsg())//2 > 150:
            self.lmsg1['text'] = self.Game.getMsg()[0:(len(self.Game.getMsg())//3)]
            self.lmsg2['text'] = self.Game.getMsg()[(len(self.Game.getMsg())//3):2*(len(self.Game.getMsg())//3)]
            self.lmsg3['text'] = self.Game.getMsg()[2*(len(self.Game.getMsg())//3):-1]
        elif len(self.Game.getMsg()) > 150:
            self.lmsg1['text'] = self.Game.getMsg()[0:(len(self.Game.getMsg())//2)]
            self.lmsg2['text'] = self.Game.getMsg()[(len(self.Game.getMsg())//2):-1]
        else:
            self.lmsg1['text'] = self.Game.getMsg()

    def resetMsg(self):
        self.lmsg1['text'] = '' 
        self.lmsg2['text'] = ''
        self.lmsg3['text'] = ''
        self.lmsg4['text'] = ''
        
    def guessSeth(self):
        if self.Game.getWhose() == 'Seth':
            self.loutcome['text']='Correct! Good Job! :)'
            self.Game.counter.wins += 1
        else:
            self.loutcome['text']='Wrong, Sorry. Alysala said that.'
        self.Game.counter.total +=1
        self.updateMsg()
        self.printMsg()
    def guessAlysala(self):
        if self.Game.getWhose() == 'Alysala':
            self.loutcome['text']='Correct! Good Job! :)'
            self.Game.counter.wins += 1
        else:
            self.loutcome['text']='Wrong, Sorry. Seth said that.'
        self.Game.counter.total +=1
        self.updateMsg()
        self.printMsg()
        
#starts the window            
a = window()
