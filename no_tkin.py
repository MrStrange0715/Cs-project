import smtplib
from email.message import EmailMessage
import imghdr

print('''1. Text email
2. Email with image
3. Email with pdf
4. Help''')

ch = int(input('Enter ur choice: '))

if ch == 1:
    sender_email = input('Enter sender\'s gmail address: ')
    receiver_email = input('Enter receiver\'s gmail address: ')
    pwd = input('Enter your password: ')

    sub = input('Enter subject: ')
    content = input('Enter content:')

    newMessage = EmailMessage() 
    newMessage['Subject'] = sub
    newMessage['From'] = sender_email
    newMessage['To'] = receiver_email
    newMessage.set_content(content)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, pwd)
        smtp.send_message(newMessage)
        x = smtp.ehlo()
        if x[0] == 250:
            print('sent')
        else:
            print('failed')

elif ch == 2:
    sender_email = input('Enter sender\'s gmail address: ')
    receiver_email = input('Enter receiver\'s gmail address: ')
    pwd = input('Enter your password: ')

    sub = input('Enter subject: ')
    content = input('Enter content: ')

    newMessage = EmailMessage() 
    newMessage['Subject'] = sub
    newMessage['From'] = sender_email
    newMessage['To'] = receiver_email
    newMessage.set_content(content)

    no_images = int(input('Enter the number of images to send: '))
    files = []

    for i in range(no_images):
        filepath = input('Enter filepath: ')
        files += filepath

    for file in files:
        with open(file, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(file_data, maintype='image', subtype=image_type, filename=image_name)




    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, pwd)
        smtp.send_message(newMessage)
        x = smtp.ehlo()
        if x[0] == 250:
            print('sent')
        else:
            print('failed')


if ch == 3:
    sender_email = input('Enter sender\'s gmail address: ')
    receiver_email = input('Enter receiver\'s gmail address: ')
    pwd = input('Enter your password: ')

    sub = input('Enter subject: ')
    content = input('Enter content:')

    newMessage = EmailMessage() 
    newMessage['Subject'] = sub
    newMessage['From'] = sender_email
    newMessage['To'] = receiver_email
    newMessage.set_content(content)

    filepath = input('Enter filepath: ')

    with open(filepath, 'rb') as file1:
        file_data = file1.read()
        file_name = file1.name

    newMessage.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename = file_name)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, pwd)
        smtp.send_message(newMessage)
        x = smtp.ehlo()
        if x[0] == 250:
            print('sent')
        else:
            print('failed')
    
    
'''
filepath = input('Enter attachment\'s file path: ')
filetype = filepath.split('.')
filetype = filepath[1]
    
if filetype == 'png' or filetype == 'jpg' or filetype == 'jpeg':
    f = open(filepath, 'rb')
    file_data = f.read()
    subtype = imghdr.what(filepath)
    file_name = file1.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=file_name)

else:
    f = open(filepath, 'rb')
    file_data = f.read()
    file_name = file1.name
    
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
'''


