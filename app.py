import tkinter as t

main_win = t.Tk()
main_win.title("to do list")
main_win.geometry("280x250")

entry = t.Entry(font="Arial 12")
entry.grid(row=0, column=0)
    
def add_item():
    if (entry.get().strip() != ""):
        lst.insert(t.END, entry.get())
        entry.delete(0, t.END)

btn = t.Button(text="Добавить", command=add_item)
btn.grid(row=0,column=1, sticky="e")

lst = t.Listbox(font="Arial 12", width=30)
lst.grid(row=2, column=0, columnspan=2, sticky="w")

def del_item():
    if (len(lst.curselection()) > 0):
        index = lst.curselection()[0]
        lst.delete(index)

btn_del = t.Button(text="Удалить", command=del_item)
btn_del.grid(row=3, column=1, sticky="e")

main_win.mainloop()