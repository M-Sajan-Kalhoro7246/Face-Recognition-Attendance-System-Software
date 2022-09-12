from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
import webbrowser

class Developer:
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
        bg1=Image.open(r"Images\creative-image-many-business-people-conference-group-meeting_31965-7388.png")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        det_img_btn=Image.open(r"Images\M Sajan.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        #button back
        tra_b1_1 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b1_1.place(x=1200,y=10,width=150,height=30)


        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=600,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.LinkedIn,text="M Sajan Kalhoro",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        det_b1_1.place(x=600,y=380,width=180,height=45)

        # Detect Face  button 2

        # Attendance System  button 3
    def LinkedIn(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/M-Sajan-Kalhoro7246"
        webbrowser.open(self.url,new=self.new)

        # Help  Support  button 4
    def Face_Recognition_System(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()