from tkinter import *

master=Tk()
master.title('CODER')

t1=StringVar()
s1=IntVar()
coded=StringVar()

def cc():
    cipherText = ""
    #plainText = ""
    plainText=t1.get()
    print(plainText)
    shift=int(s1.get())
    print(shift)

    for ch in plainText:
        if ch.isalpha() and ch.islower():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        elif ch.isalpha() and ch.isupper():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        elif ch.isdigit():
            shift = shift % 10
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('9'):
                stayInAlphabet -= 10
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        else:
            cipherText += ch

    print("Your cipher text is: ", cipherText)
    #return:nothing
    coded.set(cipherText)

L1=Label(master, text="Enter plain text").grid(row=0)
e1 = Entry(master, textvariable=t1)
e1.grid(row=0, column=1)

L2=Label(master, text="Enter shift").grid(row=1)
e2 = Entry(master, textvariable=s1)
e2.grid(row=1, column=1)

L3=Label(master, text="Coded message is:").grid(row=2)
L4=Label(master, textvariable=coded).grid(row=2, column=1)

button3 = Button(master, text="Encrypt",command=cc).grid(row=3, column=0)

mainloop()