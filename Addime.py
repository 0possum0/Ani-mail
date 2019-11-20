import tkinter as tk
from tkinter import messagebox as mb
from os import path

#######################

root = tk.Tk()

root.title("Add Anime")

##########################

def retrievedata():
    global list_data
    global link_data
    link_data = []
    list_data = []

    URL_list.config(state='normal')
    try:
        with open("db/links.txt","r",encoding="utf-8") as file:
            for f in file:
                URL_list.insert(tk.END,f.strip())
                link_data.append(f.strip())
                print(link_data)
    except:
        pass
    URL_list.config(state='disabled')

    try:
        with open("db/Anime.txt","r",encoding="utf-8") as file:
            for f in file:
                listbox.insert(tk.END,f.strip())
                list_data.append(f.strip())
                print(list_data)
    except:
        pass

def clicked():
    global list_data
    global link_data
    if content.get() is '' or anime_link.get() is '':
        notenough()
    else:
        #insert anime name into listbox
        listbox.insert(tk.END,content.get())
        list_data.append(content.get())
        #insert url into url_list
        URL_list.config(state='normal')
        URL_list.insert(tk.END,anime_link.get())
        URL_list.config(state='disabled')
        link_data.append(anime_link.get())
def delete_selected():
    global list_data
    global link_data
    selected = listbox.get(listbox.curselection())
    selindex = list_data.index(selected)
    listbox.delete(tk.ANCHOR)
    list_data.pop(list_data.index(selected))
    #URL list deletion
    URL_list.config(state='normal')
    URL_list.delete(selindex)
    link_data.pop(selindex)
    URL_list.config(state='disabled')

def quit():
    global root
    with open("db/Anime.txt","w",encoding="utf-8") as file:
        for d in list_data:
            file.write(d+"\n")

    with open("db/links.txt","w",encoding="utf-8") as file:
        for d in link_data:
            file.write(d+"\n")

    root.destroy()
def notenough():
    mb.showerror("Warning!","You must provide a name AND a URL!")

#Text inputs
label1 = tk.Label(root,text="Add Anime",fg='blue')
label1.pack()

topframe = tk.Frame(root)
topframe.pack( side = "top" )

urlframe = tk.Frame(root)
urlframe.pack(side = "top")

name = tk.Label(topframe, text="Anime Name")
name.pack(side="left")

content = tk.StringVar()
entry = tk.Entry(topframe, textvariable=content)
entry.pack(side="right")

linktext = tk.Label(urlframe, text="        URL")
linktext.pack(side="left")

anime_link = tk.StringVar()
entry2 = tk.Entry(urlframe,textvariable=anime_link)
entry2.pack(side="right")

#BUTTONS
button = tk.Button(root,text= "Add Item",command = clicked)
button.pack()

button_delete_selected = tk.Button(text="Delete Selected",command = delete_selected)
button_delete_selected.pack()

bquit = tk.Button(root,text="Quit and save",command=quit)
bquit.pack(side='bottom')

#LISTBOX
listboxFrame = tk.Frame(root)
listboxFrame.pack(side="bottom")



listbox = tk.Listbox(listboxFrame)
listbox.pack(side='left')

URL_list = tk.Listbox(listboxFrame)
URL_list.pack(side='right')
URL_list.config(state="disabled")






#################
retrievedata()
root.mainloop()