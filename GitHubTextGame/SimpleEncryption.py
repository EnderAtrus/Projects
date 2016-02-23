
import random
import os


key=";bln]E94{Lkc1-zY`myvTUV'(Z8jg6a7.dK<i/p%t>_ =#oq+MRCxS0HGPFI:BXDhN?!J&}e|u*[3,A@f$2sWQ5)rwO^"
alphabet="abcdefghijklmnopqrstuvwxyz123456 7890ABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()-_=+[{]}|;:',<.>/?"

def encryptMsg(plaintext,key,alphabet):
    em=''
##    print('Alphabet: '+str(alphabet))
##    print('Key:      '+str(key))
##    print('Inputed plaintext: '+str(plaintext))
    plaintext=plaintext
    i=0
    cm=''
    sm=''
    while i < len(plaintext):
        if alphabet.find(plaintext[i]) != -1:
            cm=cm+plaintext[i]
        i+=1
    i=0
    for char in cm:
        sm=sm+key[alphabet.find(char)]
    return str(sm)

    
def decryptMsg(cyphertext,key,alphabet):
    pm=''
    for char in cyphertext:
        pm=pm+alphabet[key.find(char)]
    return str(pm)

def makeKey(alphabet):
    al=list(alphabet)
    random.shuffle(al)
    key=''
    i=0
    while i < len(al):
        if alphabet.find(al[i]) != -1:
            key=key+str(al[i])
        i+=1
    return key


def outMsg(key,alphabet):
    easyfs=open('easyfs.txt','w')
    olds=open('tempfs.txt','r')
    easyfa=open('easyfa.txt','w')
    olda=open('tempfa.txt','r')
    

    for line in olds:
        tf=decryptMsg(line,key,alphabet)
        easyfs.write(tf[:-1]+'\n')
    for line in olda:
        tf=decryptMsg(line,key,alphabet)
        easyfa.write(tf[:-1]+'\n')
    easyfa.close()
    easyfs.close()
    olds.close()
    olda.close()
    print('OutMsg Done!')

def outAllMsg(key,alphabet):
    easyAll=open('easyall.txt','w')
    olds=open('easyfs.txt','r')
    olda=open('easyfa.txt','r')
    sCount=0
    aCount=0
    aList=[]
    sList=[]
    for i in olds:
        sCount=sCount+1
        sList.append(i)
    for i in olda:
        aCount=aCount+1
        aList.append(i)
    length = max(aCount,sCount)
    i=0
    
    while i<length:
        try:
            tf=sList[i][:-1]+'\n'
            easyAll.write(tf)
            #print(tf)
        except:
            print('easyAll.write error for s')

        try:
            tf=aList[i][:-1]+'\n'
            easyAll.write(tf)
        except:
            print('easyAll.write error for a')
        i=1+i

    easyAll.close()
    olds.close()
    olda.close()
    print('OutAllMsg Done!')





    
