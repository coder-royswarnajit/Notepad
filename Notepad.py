from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def new():
    root = Tk()
    root.title("Notepad")
    root.geometry("600x700")


    txt = Text(root,width=600,height=700,font=12)
    txt.pack(pady=20)

    menu = Menu(root)
    root.config(menu=menu)


    def file_new():
        #top = Text(txt,width=600,height=700,font=12)
        #top.pack(pady=20)
        new()
    
    def file_save():
        file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_name:
            with open(file_name, 'w') as file:
                text = txt.get("1.0", END)
                file.write(text)
        
    def file_open():
        file_name = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
                txt.delete("1.0", END)
                txt.insert("1.0", text)

    def clear():
        txt.delete(0,END)
        
    def copy():
        selected_text = txt.get("sel.first","sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected_text)

    def cut():    
        selected_text = txt.get("sel.first","sel.last")
        root.clipboard_clear()
        root.clipboard_append(selected_text)
        txt.delete("sel.first","sel.last")

    def paste():
        selected_text = root.clipboard_get()
        txt.insert(INSERT,selected_text)

    def deleted():
        selected_text = txt.get("sel.first","sel.last")
        if selected_text:
            txt.delete("sel.first","sel.last")
        
    def select_all():
        txt.tag_add('sel','1.0','end')



    file = Menu(menu)
    menu.add_cascade(label="File",menu=file)
    file.add_command(label="New",command=file_new)
    file.add_command(label="Save",command=file_save)
    file.add_command(label="Open",command=file_open)
    file.add_separator()
    file.add_command(label="Clear All",command=clear)
    file.add_separator()
    file.add_command(label="Exit",command=root.quit)


    edit = Menu(menu)
    menu.add_cascade(label="Edit",menu=edit)
    edit.add_command(label="Copy",command=copy)
    edit.add_command(label="Cut",command=cut)
    edit.add_command(label="Paste",command=paste)
    edit.add_command(label="Delete",command=deleted)
    edit.add_separator()
    edit.add_command(label="Select All",command=select_all)




    mainloop()

new()