#dinking around with tk

from tkinter import *
import random
import os
import SimpleEncryption
import time
##-------------------------------------------------------------------------------
#create collections of messages
#need to change so it merges messages together that were meant to be sent as one message
key=";bln]E94{Lkc1-zY`myvTUV'(Z8jg6a7.dK<i/p%t>_ =#oq+MRCxS0HGPFI:BXDhN?!J&}e|u*[3,A@f$2sWQ5)rwO^"
alphabet="abcdefghijklmnopqrstuvwxyz123456 7890ABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()-_=+[{]}|;:',<.>/?"
def gettxts(newfile):
    if os.path.isfile('tempfs.txt') is False:
        tfiles = open('tempfs.txt','w')
        tfiles.close()
    if os.path.isfile('tempfa.txt') is False:
        tfilea = open('tempfa.txt','w')
        tfilea.close()
        
    rfile = open(newfile,'r')
    tfiles =open('tempfs.txt','r+')
    tfilea =open('tempfa.txt','r+')
    i=0
    
    for line in rfile:
        if line[0]=='S':
            if line not in tfiles:
                tf=SimpleEncryption.encryptMsg(line,key,alphabet)
                tfiles.write(tf+'\n')
                #print(SimpleEncryption.decryptMsg(tf,key,alphabet))
        elif line[0]=='R':
            if line not in tfilea:
                tf=SimpleEncryption.encryptMsg(line,key,alphabet)
                tfilea.write(tf+'\n')
                #print(SimpleEncryption.encryptMsg(line,key,alphabet))

    tfiles.close()
    tfilea.close()
    print('Done!\n')
#------------------------------------------------------------------------------------------
    
#display a random message and start game

#problems:
#join cut off messages together

##-------------------------------------------------------------------------------
class counter():
    def __init__(self):
        self.wins=0
        self.total=0

    def total(self):
        return self.total
    
    def wins(self):
        return self.wins

class gamevar(): 
    def __init__(self):
        self.counter = counter()
        self.newcf()
        self.game()
        
    def game(self):
        self.makeArrays()            
        self.tfiles.close()
        self.tfilea.close()
        
    def newcf(self):
        self.cf=random.randint(0,1)
        self.msg=''
        if self.cf==0:
            self.whose='Seth'
        elif self.cf==1:
            self.whose="Alysala"
            
    def getcf(self):
        return self.cf

    def newMsg(self):
        self.newcf()

        if self.getcf() == 0:
            z=random.randint(0,len(self.sl)-1)
            self.msg=self.sl[z][6:25]+self.sl[z][29:-1]
            a1=1
            ans='Seth'
            
        elif self.getcf() == 1: 
            z=random.randint(0,len(self.al)-1)
            self.msg=self.al[z][10:29]+self.al[z][33:-1]
            a1=2
            ans='Alysala'
    
    def setmsg(self,inp):
        self.msg=inp

    def setMsg(self):        
        if self.cf == 0:
            z=random.randint(0,len(self.sl)-1)
            self.msg=self.sl[z][6:25]+self.sl[z][29:-1]
            a1=1
            ans='Seth'
        elif whomsg==1:
            z=random.randint(0,len(self.al)-1)
            self.msg=self.al[z][10:29]+self.al[z][33:-1]
            a1=2
            ans='Alysala'
        print('msg '+str(self.msg))
        print('a.getwhose() '+str(a.getwhose()))
        
    def getMsg(self):
        return self.msg
        
    def getWhose(self):
        return self.whose
    
    def newgame(self):
        self.game()
        
    def makeArrays(self):
        self.al = []
        self.sl = []
        self.tfiles =open('tempfs.txt','r')
        self.tfilea =open('tempfa.txt','r')
        self.key=";bln]E94{Lkc1-zY`myvTUV'(Z8jg6a7.dK<i/p%t>_ =#oq+MRCxS0HGPFI:BXDhN?!J&}e|u*[3,A@f$2sWQ5)rwO^"
        self.alphabet="abcdefghijklmnopqrstuvwxyz123456 7890ABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()-_=+[{]}|;:',<.>/?"
                     
        for line in self.tfiles:
            self.sl.append(SimpleEncryption.decryptMsg(line,self.key,self.alphabet))
        for line in self.tfilea:
            self.al.append(SimpleEncryption.decryptMsg(line,self.key,self.alphabet))
      
        self.tfiles.close()
        self.tfilea.close()

#-------------------------------------------------------------------
#Main


##SimpleEncryption.outAllMsg(key,alphabet)
