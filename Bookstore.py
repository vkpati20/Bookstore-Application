from tkinter import *
import backend


def view_func():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)#every new row is inserted at the end of the list


def search_func():
    list1.delete(0, END)
    for row in backend.search(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get() ):
        list1.insert(END, row)

def add_func():
    backend.insert(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    view_func()

def get_selected_row(event):
    global selected_row
    try:
        index=list1.curselection()[0]
        selected_row=list1.get(index)
        #fills the text areas with the selected book info
        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0,END)
        e2.insert(END,selected_row[2])
        e3.delete(0,END)
        e3.insert(END,selected_row[3])
        e4.delete(0,END)
        e4.insert(END,selected_row[4])
    except:
        pass

def delete_func():
    backend.delete(selected_row[0])
    view_func()
 
def update_func():
    backend.update(selected_row[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    view_func()



window = Tk()

window.wm_title("BookStore")
window.configure(bg='lightblue')

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l1.configure(bg='orange')

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l2.configure(bg='orange')

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l3.configure(bg='orange')

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
l4.configure(bg='orange')

title_entry = StringVar()
e1 = Entry(window, textvariable=title_entry)
e1.grid(row=0, column=1)

author_entry = StringVar()
e2 = Entry(window, textvariable=author_entry)
e2.grid(row=0, column=3)

year_entry = StringVar()
e3 = Entry(window, textvariable=year_entry)
e3.grid(row=1, column=1)

isbn_entry = StringVar()
e4 = Entry(window, textvariable=isbn_entry)
e4.grid(row=1, column=3)


list1=Listbox(window, height=6, width=25)
list1.grid(row=2, column=0, rowspan = 6, columnspan = 2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window, text="View all", width=12, command=view_func)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Book", width=12, command=search_func)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Book", width=12, command=add_func)
b3.grid(row=4, column=3)

b4=Button(window, text="Update Selected", width=12, command=update_func)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete Selected", width=12, command=delete_func)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
