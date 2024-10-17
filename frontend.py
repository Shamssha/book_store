from ast import Not
import email
from tkinter import *
import smtplib

from numpy import pad
import backend


def clear_list():
    listbox1.delete(0, END)


def fill_list(books):
    for book in books:
        listbox1.insert(END, book)


root = Tk()
root.title("shams")
root.geometry("1550x850")


# ====================Fanctions================
def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)


def search_command():
    clear_list()
    books = backend.search(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    )
    fill_list(books)


def insert_command():
    if title_text and author_text and year_text and isbn_text is not None:
        backend.insert(
            title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
        )
        view_command()
    else:
        print("not be null.")


#       ==========select item======
def select_item(event):
    global select_element
    index1 = listbox1.curselection()[0]
    select_element = listbox1.get(index1)

    entry1.delete(0, END)
    entry1.insert(END, select_element[1])
    # 
    entry2.delete(0, END)
    entry2.insert(END, select_element[2])
    # 
    entry3.delete(0, END)
    entry3.insert(END, select_element[3])
    # 
    entry4.delete(0, END)
    entry4.insert(END, select_element[4])



def delete_command():
    backend.delete(select_element[0]) 
    view_command()


def update_command():
    backend.update(select_element[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def  send_email():
    sender = sender_email_text.get()
    receivers =recive_email_text.get()
    message = message_text.get()
    print (sender)
    print (receivers)
    print (message)
    try:
        smtpObj = smtplib.SMTP('gmail.com')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print ("Error: unable to send email")

# =====================Frames==================
fram1 = Frame(root, width=500, height=800)
fram1.place(x=1100, y=50),
# /
fram2 = Frame(root, width=1600, height=50, bg="lightgray")
fram2.place(x=0, y=0)
fram3 = Frame(root, width=100, height=200, bg="lightgray")
fram3.place(x=900, y=50)
# ====================Button============================
btn1 = Button(fram3, width=27, height=2, text="viewall", command=view_command)
btn1.grid(row=0, column=0)
btn2 = Button(fram3, width=27, height=2, text="Search", command=search_command)
btn2.grid(row=1, column=0)
btn3 = Button(fram3, width=27, height=2, text="Insert", command=insert_command)
btn3.grid(row=2, column=0)
btn4 = Button(fram3, width=27, height=2, text="Delete", command=delete_command)
btn4.grid(row=3, column=0)
btn5 = Button(fram3, width=27, height=2, text="Update", command=update_command)
btn5.grid(row=4, column=0)
btn6 = Button(fram3, width=27, height=2, text="Clear", command=clear_list)
btn6.grid(row=5, column=0)
btn7 = Button(fram3, width=27, height=2, text="Exit", command=lambda: root.quit())
btn7.grid(row=6, column=0)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# ====================================Listboxs============================
listbox1 = Listbox(root, width=150, height=40,selectbackground='red',selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
listbox1.place(x=20, y=50,)

listbox1.bind("<<ListboxSelect>>", select_item)
# =========================Entrys=========================
label_1 = Label(fram2, text="title")
label_1.grid(row=0, column=0, padx=10, pady=4)
title_text = StringVar()
entry1 = Entry(fram2, width=50, textvariable=title_text)
entry1.grid(row=0, column=1, ipady=5, pady=4)

label_2 = Label(fram2, text="author")
label_2.grid(row=0, column=2, padx=5, pady=4)
author_text = StringVar()
entry2 = Entry(fram2, width=50, textvariable=author_text)
entry2.grid(row=0, column=3, ipady=5, pady=4)
#
label_3 = Label(fram2, text="year")
label_3.grid(row=0, column=4, padx=5, pady=4)
year_text = StringVar()
entry3 = Entry(fram2, width=50, textvariable=year_text) 
entry3.grid(row=0, column=5, ipady=5, pady=4)
#
label_4 = Label(fram2, text="isbn")
label_4.grid(row=0, column=6, padx=5, pady=4)
isbn_text = StringVar()
entry4 = Entry(fram2, width=50, textvariable=isbn_text)
entry4.grid(row=0, column=7, ipady=5, pady=4)
# ======================send email===========================
label_sender = Label(fram1,text='your email')
label_sender.grid(row=0,column=0)
sender_email_text = StringVar()
senderEntry = Entry(fram1,width=30, textvariable=sender_email_text)
senderEntry.grid(row=0,column=1, ipady=5, pady=4)
# /
recive_label = Label(fram1,text='sent email')
recive_label.grid(row=1,column=0)
recive_email_text = StringVar()
reciv_entry = Entry(fram1, width=30, textvariable=recive_email_text)
reciv_entry.grid(row=1,column=1, ipady=5, pady=4)
# 
message_label = Label(fram1,text='your message')
message_label.grid(row=2,column=0, ipady=5, pady=4)
message_text = StringVar()
message_entry = Entry(fram1,width=30, textvariable=message_text)
message_entry.grid(row=2,column=1, ipady=5, pady=4)
# Button
send_btn = Button(fram1,text='send email', width=20, command=send_email)
send_btn.grid(row=3,column=1) 

view_command()
root.mainloop()
