from tkinter import*
window=Tk()
window.geometry("500x400")

#in order to prevent the resizable of the window i called the function resizable...
window.resizable(0,0)

window.title("Calculator")

 #Here down are funtion required...
 #1. whenever a button is clicked on...
def button_click(item):
 	global expression
 	expression=expression+str(item)
 	input_text.set(expression)

 #2.button clear 

def button_clear():
 	global expression
 	expression=""
 	input_text.set("")

 #3. "=" button
def button_equal():
 	global expression
 	result=str(eval(expression))
 	input_text.set(result)
 	expression=""


expression=""
 
input_text= StringVar()

 #frame
input_frame=Frame(window, width=312,height=50,bd=0,highlightbackground="black", highlightcolor="black",highlightthickness=1)
input_frame.pack(side=TOP)

#input fields

input_field=Entry(input_frame, font=('arial',18,'bold'),textvariable=input_text,width=50,bg="#eee",bd=0,justify=RIGHT)
input_field.pack(ipady=10)#'ipady' is the internal padding to increase the height of the input field

buttons_frame=Frame(window,width=312,height=272.5,bg="grey")
buttons_frame.pack()

clear=Button(buttons_frame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(buttons_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_click("/")).grid(row=0,column=3,padx=1,pady=1)


seven=Button(buttons_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(7)).grid(row=1,column=0,padx=1,pady=1)
eight=Button(buttons_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(8)).grid(row=1,column=1,padx=1,pady=1)
nine=Button(buttons_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(9)).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(buttons_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("*")).grid(row=1,column=3,padx=1,pady=1)


four=Button(buttons_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(buttons_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(buttons_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(6)).grid(row=2,column=2,padx=1,pady=1)
minus=Button(buttons_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("-")).grid(row=2,column=3,padx=1,pady=1)

one=Button(buttons_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(1)).grid(row=3,column=0,padx=1,pady=1)
two=Button(buttons_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(2)).grid(row=3,column=1,padx=1,pady=1)
three=Button(buttons_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(3)).grid(row=3,column=2,padx=1,pady=1)
plus=Button(buttons_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("+")).grid(row=3,column=3,padx=1,pady=1)


zero=Button(buttons_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(0)).grid(row=4,columnspan=2,column=0,padx=1,pady=1)
point=Button(buttons_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_click(".")).grid(row=4,column=2,padx=1,pady=1)
equals=Button(buttons_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_equal()).grid(row=4,column=3,padx=1,pady=1)

window.mainloop()