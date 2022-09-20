from tkinter import *
import functions

def convert():
    global radiobuttonvar, converted
    radiobutton = radiobuttonvar.get()
    numberconvert = converted.get()
    converted.delete(0, END)
    if radiobutton == 1:
        if numberconvert[0:2] == '0x':
            result = functions.hextodec(numberconvert)
        elif numberconvert[0:2] == '0b':
            result = functions.bintodec(numberconvert)
        elif numberconvert[:2] == '0o':
            result = functions.octtodec(numberconvert)
        else:
            result = numberconvert
    elif radiobutton == 2:
        if numberconvert[0:2] == '0x':
            result = functions.hextobin(numberconvert)
        elif numberconvert[:2] == '0o':
            result = functions.octtobin(numberconvert)
        elif numberconvert[0:2] != '0x' or '0b' or '0o':
            result = functions.dectobin(numberconvert)
        else:
            result = numberconvert
       
    elif radiobutton == 3:
        if numberconvert[0:2] == '0x':                
            result = functions.hextooct(numberconvert)
        elif numberconvert[:2] == '0b':               
            result = functions.bintooct(numberconvert)
        elif numberconvert[0:2] != '0x' or '0b' or '0o':                                                          
            result = functions.dectooct(numberconvert)
        else:                                         
            result = numberconvert   
    elif radiobutton == 4:
        if numberconvert[0:2] == '0o':                
            result = functions.octtohex(numberconvert)
        elif numberconvert[:2] == '0b':               
            result = functions.bintohex(numberconvert)
        elif numberconvert[0:2] != '0x' or '0b' or '0o':                                                          
            result = functions.dectohex(numberconvert)                                                            
        else:                                         
            result = numberconvert                  
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
