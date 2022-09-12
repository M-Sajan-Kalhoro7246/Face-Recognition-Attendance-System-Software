from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport
#=========================================



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
    obj=Face_Recognition_System(root)
    root.mainloop()
