from tkinter import *
from tkinter import messagebox, filedialog
import smtplib
from email.message import EmailMessage
import os
import imghdr
import pandas

check = False

def browse():
    path = filedialog.askopenfilename(initialdir='c:/', title='Select Excel File')

    if path == '':
        messagebox.showerror('Error','Please select an excel file')

    else:
        data = pandas.read_excel(path)
        if 'Email' in data.columns:
            emails = list(data['Email'])

def button_check():
    if choice.get() == 'multiple':
        browseButton.config(state=NORMAL)
        toEntryField.config(state='readonly')

    if choice.get() == 'single':
        browseButton.config(state=DISABLED)
        toEntryField.config(state=NORMAL)


        
def iexit():
    result = messagebox.askyesno('Notification', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def clear():
    toEntryField.delete(0, END)
    subjectEntryField.delete(0, END)
    textarea.delete(1.0, END)

def login():
    def clear1():
        fromEntryField.delete(0, END)
        passwordEntryField.delete(0, END)


    def save():
        if fromEntryField.get() == '' or passwordEntryField.get() == '':
            messagebox.showerror('Error', 'All Fields Are Required', parent=root1)

        else:
            f = open('credentials.txt', 'w')
            f.write(fromEntryField.get() +','+ passwordEntryField.get())
            f.close()
            messagebox.showinfo('Information', 'CREDENTIALS SAVED SUCCESSFULLY', parent=root1)
            


        
    root1 = Toplevel(root)
    root1.title('Login')
    root1.geometry('650x340+350+90')
    root1.configure(bg='gray10')

    loginFrame = Frame(root1, bg='salmon')
    loginFrame.grid(row=0, column=0)

    Label(loginFrame, width=37, bg='salmon').grid(row=0, column=0)

    loginLabel = Label(loginFrame, text='Login', font=('Chesna Grotesk', 40), bg='salmon', fg='white')
    loginLabel.grid(row=0, column=1)

    Label(loginFrame, width=40, bg='salmon').grid(row=0, column=2)

    fromLabelFrame = LabelFrame(root1, text='From (Email address)', font=('Chesna Grotesk', 16), bd=5, fg='salmon', bg='gray10')
    fromLabelFrame.grid(row=1, column=0, pady=20)

    fromEntryField = Entry(fromLabelFrame, font=('Chesna Grotesk', 11), width=50)
    fromEntryField.grid(row=0, column=0)

    passwordLabelFrame = LabelFrame(root1, text='Password', font=('Chesna Grotesk', 16), bd=5, fg='salmon', bg='gray10')
    passwordLabelFrame.grid(row=2, column=0, pady=20)

    passwordEntryField = Entry(passwordLabelFrame, font=('Chesna Grotesk', 11), width=50, show='*')
    passwordEntryField.grid(row=0, column=0)

    Button(root1, text='LOGIN', font=('Chesna Grotesk', 18), cursor='hand2', bg='salmon', fg='black', command=save).place(x=240, y=265)
    Button(root1, text='CLEAR', font=('Chesna Grotesk', 18), cursor='hand2', bg='salmon', fg='black', command=clear1).place(x=360, y=265)

    '''
    f = open('credentials.txt', 'r')
    for i in f:
        credentials = i.split(',')

    fromEntryField.insert(0, credentials[0])
    passwordEntryField.insert(0, credentials[1])
    '''



    
    root1.mainloop()

def sendingEmail(toAddress, subject, body):
    f = open('credentials.txt', 'r')
    for i in f:
        credentials = i.split(',')

        
    message = EmailMessage()
    message['subject'] = subject
    message['to'] = toAddress
    message['from'] = credentials[0]
    message.set_content(body)

    if check:
        if filetype == 'png' or filetype == 'jpg' or filetype == 'jpeg':
            f = open(filepath, 'rb')
            file_data = f.read()
            subtype = imghdr.what(filepath)
        
            message.add_attachment(file_data, maintype='image', subtype=subtype, filename=filename)

        else:
            f = open(filepath, 'rb')
            file_data = f.read()
            message.add_attachment(file_data, maintype = 'application', subtype='octet-stream', filename=filename)



    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(credentials[0], credentials[1])
    s.send_message(message)

    messagebox.showinfo('Information', 'Email is sent successfully')

    

def send_email():
    if toEntryField.get() == '' or subjectEntryField.get() == '' or textarea.get(1.0, END) =='\n':
        messagebox.showerror('Error', 'All Fields Are Required', parent=root)

    else:
        if choice.get() == 'single':
            sendingEmail(toEntryField.get(), subjectEntryField.get(), textarea.get(1.0, END))

def attachment():
    global filename, filetype, filepath, check
    check = True
    filepath = filedialog.askopenfilename(initialdir='c:/', title='Select File')
    filetype = filepath.split('.')
    filetype = filetype[1]
    filename = os.path.basename(filepath)
    textarea.insert(END, f'\n{filename}\n')
    


    
root = Tk()
root.title('Email app')
root.geometry('780x620+100+50')
root.resizable(0,0)
root.config(bg='gray10')

titleFrame = Frame(root, bg='salmon')
titleFrame.grid(row=0, column=0)

Label(titleFrame, width=40, bg='salmon').grid(row=0, column=0)

titleLabel = Label(titleFrame, text='Email sender', font=('Chesna Grotesk', 28), bg='salmon', fg='white')
titleLabel.grid(row=0, column=1)

Label(titleFrame, width=20, bg='salmon').grid(row=0, column=2)

loginImage = PhotoImage(file='login.png')
Button(titleFrame, image=loginImage, bd=0, bg='salmon', cursor='hand2', activebackground='salmon', height='100px', width='100px', command=login).grid(row=0, column=3)

#Label(root, height=1, bg='gray10').grid(row=1, column=0)

chooseFrame = Frame(root, bg='gray10')
chooseFrame.grid(row=1, column=0, pady=10)
choice = StringVar()

singleRadioButton = Radiobutton(chooseFrame, text='Single', font=('Chesna Grotesk', 20), variable=choice, value='single', bg='gray10', fg='salmon', activebackground='gray10', command=button_check)
singleRadioButton.grid(row=0, column=0, padx=20)

multipleRadioButton = Radiobutton(chooseFrame, text='Multiple', font=('Chesna Grotesk', 20), variable=choice, value='multiple', bg='gray10', fg='salmon', activebackground='gray10', command=button_check)
multipleRadioButton.grid(row=0, column=1, padx=20)

choice.set('single')

#Label(root, height=1, bg='gray10').grid(row=3, column=0)

toLabelFrame = LabelFrame(root, text='To (Email address)', font=('Chesna Grotesk', 16), bd=5, fg='salmon', bg='gray10')
toLabelFrame.grid(row=2, column=0, padx=100)

toEntryField = Entry(toLabelFrame, font=('Chesna Grotesk', 11), width=50)
toEntryField.grid(row=0, column=0)

browseImage = PhotoImage(file='browse1.png')

browseButton = Button(toLabelFrame, text=' Browse', image=browseImage, compound=LEFT, font=('arial', 12, 'bold'), cursor='hand2', bd=0, fg='salmon', bg='gray10', activebackground='gray10', state=DISABLED, command=browse)
browseButton.grid(row=0, column=1, padx=20)

#Label(root, height=1, bg='gray10').grid(row=5, column=0)

subjectLabelFrame = LabelFrame(root, text='Subject', font=('Chesna Grotesk', 16), bd=5, fg='salmon', bg='gray10')
subjectLabelFrame.grid(row=3, column=0, pady=10)

subjectEntryField = Entry(subjectLabelFrame, font=('Chesna Grotesk', 11), width=50)
subjectEntryField.grid(row=0, column=0)

emailLabelFrame = LabelFrame(root, text='Compose Email', font=('Chesna Grotesk', 16), bd=5, fg='salmon', bg='gray10')
emailLabelFrame.grid(row=4, column=0, padx=20)

Button(emailLabelFrame, bd=0, fg='gray10', bg='gray10', activebackground='gray10').grid(row=0, column=0)


attachImage = PhotoImage(file='attachments5.png')
Button(emailLabelFrame, text='Attachment', image=attachImage, compound=LEFT, font=('arial', 12, 'bold'),  cursor='hand2', bd=0, fg='salmon', bg='gray10', activebackground='gray10', command=attachment).grid(row=0, column=1)

textarea = Text(emailLabelFrame, font=('Chesna Grotesk', 12,), height=8)
textarea.grid(row=1, column=0, columnspan=3)

sendImage = PhotoImage(file='send4.png')
Button(root, image=sendImage, bd=0, command=send_email, fg='salmon', bg='gray10', cursor='hand2', activebackground='gray10').place(x=490, y=550)

clearImage = PhotoImage(file='clear4.png')
Button(root, image=clearImage, command=clear, bd=0, fg='salmon', bg='gray10', cursor='hand2', activebackground='gray10').place(x=590, y=550)

exitImage = PhotoImage(file='exit3.png')
Button(root, image=exitImage, command = iexit, bd=0, fg='salmon', bg='gray10', cursor='hand2', activebackground='gray10').place(x=690, y=550)

totalLabel = Label(root, font=('Chesna Grotesk', 18), bg='gray10', fg='salmon')
totalLabel.place(x=10, y=560)

sentLabel = Label(root, font=('Chesna Grotesk', 18), bg='gray10', fg='salmon')
sentLabel.place(x=100, y=560)

leftLabel = Label(root, font=('Chesna Grotesk', 18), bg='gray10', fg='salmon')
leftLabel.place(x=190, y=560)

failedLabel = Label(root, font=('Chesna Grotesk', 18), bg='gray10', fg='salmon')
failedLabel.place(x=280, y=560)





root.mainloop()





















































