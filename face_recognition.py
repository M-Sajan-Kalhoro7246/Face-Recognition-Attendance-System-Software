
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
#========= functions =============
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")
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
        bg1=Image.open(r"Images\bg12.jpg")
        bg1=bg1.resize((1366,600),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=580)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #Note Message Button1
        Note_lb1 = Label(bg_img,text="Press Enter Button to Destroy Camera Section ->",font=("verdana",11,"bold"),bg="darkred",fg="white")
        Note_lb1.place(x=80,y=530,width=420,height=30)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images\bv.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="darkblue",fg="white")
        std_b1_1.place(x=200,y=350,width=180,height=45)

        
        #Back Button
        tra_b1_1 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b1_1.place(x=1200,y=10,width=150,height=30)

    
    #=====================Attendance===================

    def mark_attendance(self,Student_ID,Roll_No,Name,Department):
        with open(r"Attendence_Data\Attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))

                name_list.append(entry[0])

            if((Student_ID not in name_list)) and ((Roll_No not in name_list)) and ((Name not in name_list)) and ((Department not in name_list)):
                now=datetime.now()
                d1=now.strftime("%Y/%m/%d")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{Student_ID}, {Roll_No}, {Name},{Department}, {dtString}, {d1}, Present")




    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(user='root', password='',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                Name=cursor.fetchone()
                Name="+".join(Name)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                Roll_No=cursor.fetchone()
                Roll_No="+".join(Roll_No)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                Student_ID=cursor.fetchone()
                Student_ID="+".join(Student_ID)

                cursor.execute("select Department from student where Student_ID="+str(id))
                Department=cursor.fetchone()
                Department="+".join(Department)
                       


                if confidence > 77:
                    cv2.putText(img,f"Student.ID: {Student_ID}",(x,y-88),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name: {Name}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll.No: {Roll_No}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Department: {Department}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(Student_ID,Name,Roll_No,Department)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    



        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)
        #address ="http://192.168.43.96:8080/video"
        #videoCap.open(address)
        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)
            
            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        
        cv2.destroyAllWindows()

#================ FUNCTION ==================

    




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()