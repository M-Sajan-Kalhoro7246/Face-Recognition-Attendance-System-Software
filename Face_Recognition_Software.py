from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import tkinter
import mysql.connector
# --------------------------
from train import Train
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os



class Face_Recognition_Software:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1366x768+0+0")
        self.root.wm_iconbitmap("faceicon.ico")

        # variables 
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_password=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"Images\1_FOT7m7RYX4bLcEBGthowkQ.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=365,y=170,width=625,height=400)

        img1=Image.open(r"Images\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=645,y=170, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("Blackadder ITC",25,"bold"),fg="white",bg="#002B53")
        get_str.place(x=290,y=100)

        #label1 
        username =lb1= Label(frame1,text="Email:",font=("Goudy Old Style",15,""),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("Goudy Old Style",15,""))
        self.txtuser.place(x=30,y=190,width=570)


        #label2 
        password =lb1= Label(frame1,text="Password:",font=("Goudy Old Style",15,"bold"),fg="white",bg="#002B53")
        password.place(x=30,y=230)

        #entry2 
        self.txtpassword=ttk.Entry(frame1,font=("Goudy Old Style",15,"bold"),show="*")
        self.txtpassword.place(x=33,y=260,width=570)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("Blackadder ITC",22,"bold"),bd=0,relief=RIDGE,fg="white",bg="#007ACC",activeforeground="#007ACC",activebackground="white")
        loginbtn.place(x=33,y=320,width=570,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("Goudy Old Style",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_password,text="Forget",font=("Goudy Old Style",12,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)

     #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def face_R(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_Software(self.new_window)

    def close_window(self):
        #self.var_question.set("Selete")
        self.txtuser.delete(0,END)
        self.txtpassword.delete(0,END)
        #self.var_answer.delete(0,END)
        #self.new_password.delete(0,END)

    def login(self):
        if (self.txtuser.get()==""):
            messagebox.showerror("Error","Please Enter the Email!",parent=self.root)
        elif(self.txtpassword.get()==""):
            messagebox.showerror("Error","Please Enter the Password!",parent=self.root)
        elif(self.txtuser.get()=="admin" and self.txtpassword.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System",parent=self.root)
        else:
            try:
                # messagebox.showerror("Error","Please Check Username or Password !")
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from register where email=%s and password=%s",(
                    self.txtuser.get(),
                    self.txtpassword.get()
                ))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email and Password!",parent=self.root)
                else:
                    open_min=messagebox.askyesno("YesNo","Qulity Authoeised Persons Only Signs")
                    messagebox.showinfo("Successfully","Welcome to Attendance Managment System",parent=self.root)
                    if open_min>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_min:
                        
                            return
                conn.commit()

                conn.close()
            except Exception as es:
                 messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root)
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_question.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
            
        elif(self.var_answer.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
            
        elif(self.var_password.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s and question=%s and answer=%s")
                value=(self.txtuser.get(),self.var_question.get(),self.var_answer.get())
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Veryfy Correct Question & Answer!",parent=self.root2)
                    messagebox.showerror("Error","Don't Wry Try Again...!!",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.var_password.get(),self.txtuser.get())
                    mycursor.execute(query,value)

                    conn.commit()
                    conn.close()  
                    messagebox.showinfo("Info","Process has been Successfully....! \nYour Password Has Been Reset....!\nlogin with new Password!",parent=self.root2)
                    self.close_window()
                    self.root2.destroy()
                    self.face_R()
            except Exception as es:
                 messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root2)       
               
       


   

# =====================Forget window=========================================
    def forget_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to Reset Password!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                # print(row)

                if row==None:
                    messagebox.showerror("Error","Please Enter the Valid Email Address!",parent=self.root)
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+610+170")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                    l.place(x=0,y=10,relwidth=1)
                    # -------------------fields-------------------
                    #label1 
                    question =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    question.place(x=70,y=80)

                    #Combo Box1
                    self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_question,font=("times new roman",12,"bold"),state="readonly")
                    self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                    self.combo_security.current(0)
                    self.combo_security.place(x=70,y=110,width=270)

                

                    #label2 
                    answer =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    answer.place(x=70,y=150)

                    #entry2 
                    self.txtpassword=ttk.Entry(self.root2,textvariable=self.var_answer,font=("times new roman",12,"bold"))
                    self.txtpassword.place(x=70,y=180,width=270)

                    #label2 
                    new_password =lb1= Label(self.root2,text="New Password:",font=("times new roman",12,"bold"),fg="#002B53",bg="#F2F2F2")
                    new_password.place(x=70,y=220)

                    #entry2 
                    self.new_password=ttk.Entry(self.root2,textvariable=self.var_password,font=("times new roman",12,"bold"),show="*")
                    self.new_password.place(x=70,y=250,width=270)

                    #checkPassword
                    checkbtn = Checkbutton(self.root2,textvariable=self.var_password,font=("Goudy Old Style",11,"bold"),fg="#002B53",bg="#F2F2F2")
                    checkbtn.place(x=70,y=280,width=270)


                    # Creating Button New Password
                    loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",12,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                    loginbtn.place(x=70,y=310,width=270,height=35)

                    #Button BACK
                    #backbutton=Button(self.root2.destroy,text="Back",font=("times new roman",12,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                    #backbutton.place(x=70,y=330,width=270,height=25) 
            except Exception as es:
                 messagebox.showerror("Error",f" Error Due to: {str(es)}",parent=self.root)
               

            

# =====================main program Face deteion system====================

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.wm_iconbitmap("faceicon.ico")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="FACE RECOGNITION ATTENDENCE MANAGEMENT SYSTEM",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"Images\student .jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="STUDENT PANNEL",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"Images\FACE.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2")
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="FACE DETECTOR",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"Images\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2")
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="ATTENDANCE",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        att_b1_1.place(x=710,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"Images\istockphoto-523819264-612x612.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2")
        hlp_b1.place(x=940,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="HELP SUPPORT",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        hlp_b1_1.place(x=940,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"Images\communications_technology_1574868315.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2")
        tra_b1.place(x=250,y=330,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="DATA TRAIN",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        tra_b1_1.place(x=250,y=510,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"Images\deep-face-recognition-02.WEBP")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2")
        pho_b1.place(x=480,y=330,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="IMAGE SAMPLE",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        pho_b1_1.place(x=480,y=510,width=180,height=45)

        # Developers   button 7
        dev_img_btn=Image.open(r"Images\devl.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2")
        dev_b1.place(x=710,y=330,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="DEVELOPERS",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        dev_b1_1.place(x=710,y=510,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"Images\exit.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.iExit,image=self.exi_img1,cursor="hand2")
        exi_b1.place(x=940,y=330,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.iExit,text="EXIT ->",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        exi_b1_1.place(x=940,y=510,width=180,height=45)

# ==================Funtion for Open Images Folder ==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure To Exit This Project",parent=self.root)
         if self.iExit>0:
             self.root.destroy()
         else:
             return
    





if __name__ == "__main__":
    root=Tk()
    app=Face_Recognition_Software(root)
    root.mainloop()