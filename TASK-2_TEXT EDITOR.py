#code by vandita gopal
from tkinter import*
from tkinter import  filedialog #module used to access files from system

root=Tk()
root.title('My text editor')
root.geometry("800x600")

global open_file_name
open_file_name=False

global selected
selected=False

#main frame
main_frame=Frame(root)
main_frame.pack(pady=5)

#scroll bar
scroll_bar=Scrollbar(main_frame)
scroll_bar.pack(side=RIGHT,fill=Y)

main_text=Text(main_frame,width=97,height=25,font=("Poppins",16),undo=True,yscrollcommand=scroll_bar.set)
main_text.pack()

scroll_bar.config(command=main_text.yview)

#new file
def new_file():
    main_text.delete('1.0',END)
    root.title("New file")
    status_bar.config(text="New file     ")

#open file
def open_file():
     main_text.delete('1.0',END) 
     text_file=filedialog.askopenfilename(initialdir=" ",title="Open file",filetypes=(("Text files","*.txt"),("Html files",".html"))) 
     if text_file:
        global open_file_name
        open_file_name=text_file
     name=text_file
     status_bar.config(text=name)  
     root.title(f'{name}')
     text_file=open(text_file,'r')
     stuff=text_file.read()
     main_text.insert(END,stuff)
     text_file.close()

#save as 
def save_as():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir=" ",title="Save file as",filetypes=(("Text files","*.txt"),("Html files",".html")))
    if text_file:
        name=text_file
        root.title(f'{name}')
        status_bar.config(text=name)  
    #save the file
    text_file=open(text_file,'w')
    text_file.write(main_text.get(1.0,END))
    text_file.close()

#save file
def save_file():
    global open_file_name
    #if file name does exist
    if open_file_name:
        text_file=open(open_file_name,'w')
        text_file.write(main_text.get(1.0,END))
        text_file.close()
        status_bar.config(text=open_file_name)  
    #if file does not exist
    else:
        save_as()

#cut text
def cut_text():
    global selected
    if main_text.selection_get():
        selected=main_text.selection_get()
        main_text.delete("sel.first ","sel.last")

 #copy text
def copy_text(e):
    global selected
    if main_text.selection_get():
        selected=main_text.selection_get()
#paste text
def paste_text(e):
    if selected:
        position=main_text.index(INSERT)
        main_text.insert(position,selected)
#menu bar
main_menu=Menu(root)
root.config(menu=main_menu)

#file 
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='SaveAs',command=save_as)
file_menu.add_command(label='Exit',command=root.quit)

#edit 
edit_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label='Cut',command=cut_text)
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')

#status bar
status_bar=Label(root,text="My editor     ",anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)
root.mainloop()