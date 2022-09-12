from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import messagebox
import os
import tkinter
#from Face_Recognition_Software import Face_Recognition_Software

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")
        self.root.wm_iconbitmap("faceicon.ico")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()
        self.var_cpassword=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"Images\bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        

        # img1=Image.open(r"E:\Face-Recognition-Attendence-System\Images\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

        get_str = Label(frame,text="Registration",font=("Blackadder ITC",45,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=300,y=130)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("Goudy Old Style",12,"bold"))
        self.txtuser.place(x=103,y=225,width=270)



        #label2 
        email =lb1= Label(frame,text="Email:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=100,y=270)

        #entry2 
        self.txtpassword=ttk.Entry(frame,textvariable=self.var_email,font=("Goudy Old Style",12,"bold"))
        self.txtpassword.place(x=103,y=295,width=270)


         #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=530,y=200)

        #entry2 
        self.txtpassword=ttk.Entry(frame,textvariable=self.var_lname,font=("Goudy Old Style",12,"bold"))
        self.txtpassword.place(x=533,y=225,width=270)



        #label1 
        contact =lb1= Label(frame,text="Contact No:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=530,y=270)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_contact,font=("Goudy Old Style",12,"bold"))
        self.txtuser.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        question =lb1= Label(frame,text="Select Security Question:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        question.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_question,font=("Goudy Old Style",12,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book","Your Birth Place")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        answer =lb1= Label(frame,text="Security Answer:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        answer.place(x=530,y=350)

        #entry2 
        self.txtpassword=ttk.Entry(frame,textvariable=self.var_answer,font=("Goudy Old Style",12,"bold"))
        self.txtpassword.place(x=533,y=375,width=270)

        # ========================= Section 4-----Column 2=============================
        
        #label1 
        password =lb1= Label(frame,text="Password:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        password.place(x=100,y=420)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_password,font=("Goudy Old Style",12,"bold"),show="*")
        self.txtuser.place(x=103,y=445,width=270)


        #label2 
        cpassword =lb1= Label(frame,text="Confirm Password:",font=("Goudy Old Style",12,"bold"),fg="#002B53",bg="#F2F2F2")
        cpassword.place(x=530,y=420)

        #entry2 
        self.txtpassword=ttk.Entry(frame,textvariable=self.var_cpassword,font=("Goudy Old Style",12,"bold"),show="*")
        self.txtpassword.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Goudy Old Style",11,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)

        checkbutton = Checkbutton(frame,textvariable=self.var_password,text="Show Password",font=("Goudy Old Style",11,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbutton.place(x=533,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("Blackadder ITC",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Creating Button Login
        loginbtn=Button(frame,command=root.destroy,text="Login",font=("Blackadder ITC",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=533,y=510,width=270,height=35)
    
    #def Log(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Face_Recognition_Software(self.new_window)
       



    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_question.get()=="Select" or self.var_answer.get()=="" or self.var_password.get()=="" or self.var_cpassword.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_password.get() != self.var_cpassword.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into register (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_question.get(),
                    self.var_answer.get(),
                    self.var_password.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()