import tkinter
import tkinter.messagebox
import pickle


#Creating window for to do task
root=tkinter.Tk()
root.title("To Do Task by @IshaShukla")

def add_task():
    task = entry_task.get()
    if task!="":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def del_task():
    try:  
        task_index=listbox_task.curselection()[0] #command(task) that is selected
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_task():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_task.delete(0,tkinter.END)
        for task in tasks:
            listbox_task.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannnot find task.dat")

def save_task():
    tasks=listbox_task.get(0,listbox_task.size())
    pickle.dump(tasks, open("tasks.dat","wb"))

#Creating GUI
frame_task=tkinter.Frame(root)
frame_task.pack()

listbox_task=tkinter.Listbox(frame_task, height=8, width=50)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task=tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_task=tkinter.Entry(root, width=50)
entry_task.pack()

btn_add_task=tkinter.Button(root, text="ADD TASK", width=48, command=add_task)
btn_add_task.pack()

btn_del_task=tkinter.Button(root, text="DELETE TASK", width=48, command=del_task)
btn_del_task.pack()

btn_load_task=tkinter.Button(root, text="LOAD TASK", width=48, command=load_task)
btn_load_task.pack()

btn_save_task=tkinter.Button(root, text="SAVE TASK", width=48, command=save_task)
btn_save_task.pack()

root.mainloop() #Ending of the window