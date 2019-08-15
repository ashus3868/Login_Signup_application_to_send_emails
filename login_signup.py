from tkinter import *
import os
import csv
import time
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
count,c=0,0
creds = 'tempfile.temp' #this just sets the creds to 'tempfile.temp'
def mail():
    def attach():
        global count
        count+=1
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
										filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        
        file=Label(root,text=root.filename)
        file.grid(row=7,column=0,sticky=W)

    def Pass():
        pass
    def Sendmail():
        global count
        global c
        msg=MIMEMultipart()
        msg['From']='ashus3868@gmail.com'      
        msg['To']= Toe.get()     #send to multiple users
        msg['Subject']= Subjecte.get()
        
        body = texte.get("1.0","end-1c")
        msg.attach(MIMEText(body,'plain'))
        if count>0:
            filename = root.filename
            attachment=open(filename,'rb')
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename="+filename)
            msg.attach(part)
        else:
            pass
        text=msg.as_string()
        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login("sender_email","password")
        
        try:
            mail.sendmail("sender_email",msg['To'],text)
            c+=1
            print('email sent')
        except:
            print ('error sending email')

        mail.quit()
        root.destroy()
        if c >= 1:
            
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[+] Email sent')
            rlbl.pack()
            r.mainloop()

        else:
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[!] Error Sending Email')
            rlbl.pack()
            r.mainloop()
        



    root=Tk()
    root.title('New Message')
    root.iconbitmap(r'20170115_144259.ico')
    To=Label(root,text="To:")
    Subject=Label(root,text="Subject:")
    text=Label(root,text="Message:")
    To.grid(row=1,column=0,sticky=W)
    Subject.grid(row=2,column=0,sticky=W)
    text.grid(row=3,column=0,sticky=NW)

    Toe=Entry(root,width=67)
    Subjecte=Entry(root,width=67)
    texte=Text(root,width=50,height=5)
    Toe.grid(row=1,column=1,sticky=W)
    Subjecte.grid(row=2,column=1,sticky=W)
    texte.grid(row=3,column=1,sticky=W)

    attach=Button(root,text="Attach",relief=GROOVE,command=attach)
    attach.grid(row=6,column=1,sticky=W)
    send=Button(root,text="Send",relief=GROOVE,command=Sendmail)
    send.grid(row=6,column=0,sticky=W)
    file=Label(root,text='')
    file.grid(row=7,column=0,sticky=W)
    root.geometry('500x170')
    root.mainloop()
   
def send():
    global ro
    ro=Tk()
    ro.title('Send Message')
    ro.iconbitmap(r'20170115_144259.ico') #changing the window icon 
    ro.geometry('200x100')
    new=Button(ro,text='New Message',relief=GROOVE,command=mail)
    new.grid(row=1,column=0,sticky=N)
    #new=Button(ro,text='Sent Messages',command=sent)
    #new.grid(row=1,column=1,sticky=N)
    new=Button(ro,text='Log Out',relief=GROOVE,command=logout)
    new.grid(row=1,column=2,sticky=N)
    ro.mainloop()
def logout():
    ro.destroy()
    r=Tk()
    r.title(':D')
    r.iconbitmap(r'20170115_144259.ico')
    r.geometry('150x100')
    rlbl=Label(r,text='\n[+] Logged Out Successfully.')
    rlbl.pack()
    r.mainloop()
    login()
def Signup():   #this is the signup defination
    global pwordE  #these globals just make the variables global to the entire script , meaning any defination can use them 
    global nameE
    global roots
    rootA.destroy()
    roots=Tk()  #this creates the window just a blank one
    roots.title("Signup")   #these renames the title of said window to signup
    roots.iconbitmap(r'20170115_144259.ico')
    intruction=Label(roots,text='Please Enter new Credidentials\n') #this puts a label so just a piece of text saying 'please enter ...' 
    intruction.grid(row=0,column=0,sticky=E)    #this just puts it in the window on row 0 and column 0 

    nameL=Label(roots,text='New Username: ') #this just does the same as above, instead with the text new username
    pwordL=Label(roots,text='New Password: ')
    nameL.grid(row=1,column=0,sticky=W) #same thing as the intruction var just on different rows 
    pwordL.grid(row=2,column=0,sticky=W)
    
    nameE=Entry(roots)  #this now puts on text box waiting for input 
    pwordE=Entry(roots,show='*')    #same as above ,yet show ='*' what this does is just replace the text with the '*' like a password box :D
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)
    
    signupButton=Button(roots,text='Signup',relief=GROOVE,command=FSSignup)   #this create the button with the text 'signup', when you click the command FSSignup will run
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()    #this just make the window keep open, we will destro it soon

def FSSignup():
    with open(creds,'a') as f:  #creates the documents using the variables we made at the top 
        
        f.write(nameE.get())    #nameE is the variable we were storing the input to 
        f.write(',')
        f.write(pwordE.get())   #same as nameE
        f.write('\n')
        f.close()   #closes the file
    roots.destroy() #this will destroy the signup window
    login()     #this will move us on to the login defination

def login():
    global nameEL
    global pwordEL
    global rootA
    rootA=Tk()
    rootA.title('Login')
    rootA.iconbitmap(r'20170115_144259.ico')
    intruction=Label(rootA,text='Please Login\n')
    intruction.grid(sticky=E)

    nameL=Label(rootA,text='Username: ')
    pwordL=Label(rootA,text='Password: ')
    nameL.grid(row=1,sticky=W)
    pwordL.grid(row=2,sticky=W)

    nameEL=Entry(rootA)
    pwordEL=Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)

    loginB=Button(rootA,text='Login',relief=GROOVE,command=CheckLogin)
    loginB.grid(columnspan=2,sticky=W)
    loginB=Button(rootA,text='Signup',relief=GROOVE,command=Signup)
    loginB.grid(columnspan=2,sticky=W)
    
    rmuser=Button(rootA,text='Delete User',fg='red',relief=GROOVE,command=DelUser)
    rmuser.grid(column=2,sticky=W)
    rootA.mainloop()
    
    
def CheckLogin():
    global ro
    with open(creds) as f:
        data=csv.reader(f)
        for line in data:
            try:
                uname=line[0]
                pword=line[1]
                if nameEL.get() == uname and pwordEL.get() == pword:
                    rootA.destroy()
                    r=Tk()
                    r.title(':D')
                    r.iconbitmap(r'20170115_144259.ico') 
                    r.geometry('150x50')
                    rlbl=Label(r,text='\n[+] Logged In')
                    rlbl.pack()
                    r.mainloop()
                    send()
            except IndexError:
                pass
        else:
            #rootA.destroy()
            r=Tk()
            r.title(':D')
            r.iconbitmap(r'20170115_144259.ico')
            r.geometry('150x50')
            rlbl=Label(r,text='\n[!] Invalid Login')
            rlbl.pack()
            r.mainloop()
            login()
                    
def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()

if os.path.isfile(creds):
    login()
else:
    Signup()
