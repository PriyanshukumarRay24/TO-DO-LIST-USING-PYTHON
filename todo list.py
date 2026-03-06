import tkinter as tk

root=tk.Tk()
root.geometry("600x400")
root.title("To-Do list")

def add_command():
    task=entry.get()
    lbox.insert(tk.END,task)
    entry.delete(0,tk.END)
    print("ADDED SUCCESSFULLY")

def mark_command():
    pos=lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END,f"{text} \u2713")
    print("MARKED")

def del_command():
    pos=lbox.curselection()[0]
    lbox.delete(pos)
    print("REMOVED SUCCESSFULLY")

lb1=tk.Label(root,text="Enter task: ", font=('calibri',15))
lb1.place(x=10,y=15)

entry=tk.Entry(root,width=50)
entry.place(x=120,y=20)

lbox=tk.Listbox(root,width=50,height=10)
lbox.place(x=120,y=70)

btn1=tk.Button(root,text="ADD",font=('calibri',15),width=15,command=add_command)
btn1.place(x=50,y=250)

btn2=tk.Button(root,text="MARK",font=('calibri',15),width=15, command=mark_command)
btn2.place(x=230,y=250)

btn3=tk.Button(root,text="DELETE",font=('calibri',15),width=15,command=del_command)
btn3.place(x=400,y=250)
root.mainloop()



