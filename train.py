from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")
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
        bg1=Image.open(r"Images\t_bg1.jpg")
        bg1=bg1.resize((1366,660),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=100,width=1366,height=660)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images\images (11).jpeg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=586,y=225,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="TRAIN DATASET",cursor="hand2",font=("tahoma",15,"bold"),bg="darkgreen",fg="white")
        std_b1_1.place(x=586,y=405,width=180,height=45)

        #button back
        tra_b1_1 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b1_1.place(x=1200,y=10,width=150,height=30)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier and save =============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

    
    


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()