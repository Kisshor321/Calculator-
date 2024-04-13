from tkinter import*

def buttonk(num):
    global  equation
    equation+=str(num)
    equation_label.set(equation)
    
def equal():
    
    try:
       global equation
       total=str(eval(equation))
       equation_label.set(total)
       equation=total
    except  SyntaxError:
        equation_label.set("arthmetic error")
        equation=""
def clear():
     
    global equation
    equation_label.set("")
    equation=""

window=Tk()
window.title("calculator")
window.geometry("300x300")
equation=""
equation_label=StringVar()
label=Label(window,textvariable=equation_label,width=24,height=1,font=("Ariral",25),bg="black",fg="white")
label.pack()
frame=Frame(window)
frame.pack()

button1=Button(frame,text="1",height=2,width=5,font=35,command=lambda:buttonk(1))
button1.grid(row=2,column=1)

button2=Button(frame,text="2",height=2,width=5,font=35,command=lambda:buttonk(2))
button2.grid(row=2,column=2)
button3=Button(frame,text="3",height=2,width=5,font=35,command=lambda:buttonk(3))
button3.grid(row=2,column=3)
button4=Button(frame,text="4",height=2,width=5,font=35,command=lambda:buttonk(4))
button4.grid(row=3,column=1)
button5=Button(frame,text="5",height=2,width=5,font=35,command=lambda:buttonk(5))
button5.grid(row=3,column=2)
button6=Button(frame,text="6",height=2,width=5,font=35,command=lambda:buttonk(6))
button6.grid(row=3,column=3)
button7=Button(frame,text="7",height=2,width=5,font=35,command=lambda:buttonk(7))
button7.grid(row=4,column=1)
button8=Button(frame,text="8",height=2,width=5,font=35,command=lambda:buttonk(8))
button8.grid(row=4,column=2)
button9=Button(frame,text="9",height=2,width=5,font=35,command=lambda:buttonk(9))
button9.grid(row=4,column=3)
but_0=Button(frame,text="0",height=2,width=5,font=35,command=lambda:buttonk(0))
but_0.grid(row=5,column=2)
buttonn=Button(frame,text="(",height=2,width=5,font=35,command=lambda:buttonk('('))
buttonn.grid(row=5,column=1)
buttonc=Button(frame,text=")",height=2,width=5,font=35,command=lambda:buttonk(')'))
buttonc.grid(row=5,column=3)
buttonp=Button(frame,text="+",height=2,width=5,font=35,command=lambda:buttonk('+'))
buttonp.grid(row=2,column=4)
buttonm=Button(frame,text="-",height=2,width=5,font=35,command=lambda:buttonk('-'))
buttonm.grid(row=3,column=4)
buttond=Button(frame,text="*",height=2,width=5,font=35,command=lambda:buttonk('*'))
buttond.grid(row=4,column=4)
buttonf=Button(frame,text="/",height=2,width=5,font=35,command=lambda:buttonk('/'))
buttonf.grid(row=5,column=4)
buttone=Button(frame,text="=",height=2,width=11,font=35,command=equal)
buttone.grid(row=6,column=1,columnspan=2)
buttonc=Button(frame,text="c",height=2,width=11,font=35,command=clear)
buttonc.grid(row=6,column=3,columnspan=2)

window.mainloop()