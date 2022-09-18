from tkinter import *
import functions

def convert():
    global radiobuttonvar, converted
    radiobutton = radiobuttonvar.get()
    numberconvert = converted.get()
    if radiobutton == 1:
        if
        result = functions.dectobin(int(numberconvert))
    elif radiobutton == 2:
        result = functions.dectooct(int(numberconvert))
    elif radiobutton == 3:
        result = functions.dectohex(int(numberconvert))
    elif radiobutton == 4:
        result = functions.bintodec(numberconvert)
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

labelconvert = Label(frametop,text='Number:')
labelconvert.grid(row=0, column=0)
converted = Entry(frametop)
converted.grid(row = 0, column=1, columnspan = 2)

todec = Radiobutton(framemidle, text = 'To decimal', value = 1, variable = radiobuttonvar)
todec.grid(row = 0, column = 0)
tobin = Radiobutton(framemidle, text = 'To Binary',value=2,variable=radiobuttonvar)
tobin.grid(row=0, column = 1)
tooct = Radiobutton(framemidle, text = 'To Octal',value=3,variable=radiobuttonvar)
tooct.grid(row=0, column = 2)
tohex = Radiobutton(framemidle, text = 'To Hex',value=4,variable=radiobuttonvar)
tohex.grid(row=0, column = 3)

buttonconvert = Button(framedown, text='Convert', command=convert)
buttonconvert.grid(row=0, column = 0)
buttonquit = Button(framedown, text='exit',command = root.destroy)
buttonquit.grid(row=0, column=1)

root.mainloop()
