from tkinter import *

master=Tk()
master.title('DECODER')

t2=StringVar()
s2=IntVar()
decoded=StringVar()

def rev_caesar():
  cipherText = ""

  plainText=t2.get()
  print(plainText)

  shift=s2.get()
  print(shift)

  for ch in plainText:
    if ch.isalpha() and ch.islower():
      stayInAlphabet = ord(ch) - shift
      if stayInAlphabet < ord('a'):
        stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    elif ch.isalpha() and ch.isupper():
      stayInAlphabet = ord(ch) - shift
      if stayInAlphabet < ord('A'):
        stayInAlphabet += 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    elif ch.isdigit():
      shift = shift % 10
      stayInAlphabet = ord(ch) - shift
      if stayInAlphabet < ord('0'):
        stayInAlphabet += 10
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
    else:
      cipherText += ch
  print("Your deciphered text is: ", cipherText)
  decoded.set(cipherText)
  #return(cipherText)

L4=Label(master, text="Enter coded text").grid(row=0)
e3 = Entry(master, textvariable=t2)
e3.grid(row=0, column=1)

L5=Label(master, text="Enter shift").grid(row=1)
e4 = Entry(master, textvariable=s2)
e4.grid(row=1, column=1)

L6=Label(master, text="Decoded message is:").grid(row=2)
L6=Label(master, textvariable=decoded).grid(row=2, column=1)

button3 = Button(master, text="Dcrypt",command=rev_caesar).grid(row=3, column=0)
#button3.bind("<Button-1>", cc(t1.get(),s1.get()))
#button3.pack()

mainloop()