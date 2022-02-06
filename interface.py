from tkinter import *
import functions

def convert():
    global radiobuttonvar ,toconvert, converted
    converted.delete(0, END)
    radiobutton = radiobuttonvar.get()
    numberconvert = toconvert.get()
    if radiobutton == 1:
        result = functions.dectobin(int(numberconvert))
    elif radiobutton == 2:
        result = functions.dectooct(int(numberconvert))
    elif radiobutton == 3:
        result = functions.dectohex(int(numberconvert))
    elif radiobutton == 4:
        result = functions.bintodec(numberconvert)
    elif radiobutton == 5:
        result = functions.bintooct(numberconvert)
    elif radiobutton == 6:
        result = functions.bintohex(numberconvert)
    elif radiobutton == 7:
        result = functions.octtodec(numberconvert)
    elif radiobutton == 8:
        result = functions.octtobin(numberconvert)
    elif radiobutton == 9:
        result = functions.octtohex(numberconvert)
    elif radiobutton == 10:
        result = functions.hextodec(numberconvert)
    elif radiobutton == 11:
        result = functions.hextobin(numberconvert)
    elif radiobutton == 12:
        result = functions.hextooct(numberconvert)
    converted.insert(0, str(result))

root = Tk()
root.title('Numerical Bases Converter')

radiobuttonvar = IntVar()

frametop = Frame(root)
frametop.grid(row=0)

framemidle = Frame(root)
framemidle.grid(row=1)

framedown = Frame(root)
framedown.grid(row=2)

labelconvert = Label(frametop,text='Number to convert:')
labelconvert.grid(row=0, column=0)
labeltoconvert = Label(frametop,text='Converted number:')
labeltoconvert.grid(row=0, column=2)
toconvert = Entry(frametop)
toconvert.grid(row=1, column=0, columnspan = 1)
converted = Entry(frametop)
converted.grid(row=1, column=2, columnspan = 1)

dectobin = Radiobutton(framedown, text = 'Decimal to Binary',value=1,variable=radiobuttonvar)
dectobin.grid(row=0, column = 0)
dectooct = Radiobutton(framedown, text = 'Decimal to Octal',value=2,variable=radiobuttonvar)
dectooct.grid(row=0, column = 1)
dectohex = Radiobutton(framedown, text = 'Decimal to Hex',value=3,variable=radiobuttonvar)
dectohex.grid(row=0, column = 2)
bintodec = Radiobutton(framedown, text = 'Binary to Decimal',value=4,variable=radiobuttonvar)
bintodec.grid(row=1, column = 0)
bintooct = Radiobutton(framedown, text = 'Binary to Octal',value=5,variable=radiobuttonvar)
bintooct.grid(row=1, column = 1)
bintohex = Radiobutton(framedown, text = 'Binary to Hex',value=6,variable=radiobuttonvar)
bintohex.grid(row=1, column = 2)
octtodec = Radiobutton(framedown, text = 'Octal to Deciaml',value=7,variable=radiobuttonvar)
octtodec.grid(row=2, column = 0)
octtobin = Radiobutton(framedown, text = 'Octal to Binary',value=8,variable=radiobuttonvar)
octtobin.grid(row=2, column = 1)
octtohex = Radiobutton(framedown, text = 'Octal to Hex',value=9,variable=radiobuttonvar)
octtohex.grid(row=2, column = 2)
hextodec = Radiobutton(framedown, text = 'Hex to Decimal',value=10,variable=radiobuttonvar)
hextodec.grid(row=3, column = 0)
hextobin = Radiobutton(framedown, text = 'Hex to Binary',value=11,variable=radiobuttonvar)
hextobin.grid(row=3, column = 1)
hextooct = Radiobutton(framedown, text = 'Hex to Octal',value=12,variable=radiobuttonvar)
hextooct.grid(row=3, column = 2)


buttonconvert = Button(framemidle, text='Convert', command=convert)
buttonconvert.grid(row=0, column = 0)
buttonquit = Button(framemidle, text='exit',command = root.destroy)
buttonquit.grid(row=0, column=1)

root.mainloop()
