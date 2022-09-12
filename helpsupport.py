from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
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
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"Images\images.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.LinkedIn,image=self.std_img1,cursor="hand2")
        std_b1.place(x=310,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.LinkedIn,text="LinkedIn",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1.place(x=310,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"Images\fb.png")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=510,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        det_b1_1.place(x=510,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"Images\nav.jpeg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.Official_Web,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=910,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.Official_Web,text="Official Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        att_b1_1.place(x=910,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"Images\g.jpeg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=710,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        hlp_b1_1.place(x=710,y=380,width=180,height=45)
       
        #button back
        tra_b1_1 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b1_1.place(x=1200,y=10,width=150,height=30)

        # create function for button 
    
    
    def LinkedIn(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/M-Sajan-Kalhoro7246"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/mrabbasisajan/"
        webbrowser.open(self.url,new=self.new)
    
    def Official_Web(self):
        self.new = 1
        self.url = "https://navttc.gov.pk/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)



    



if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()