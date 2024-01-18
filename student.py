from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1545x840+0+0")  # Adjusted size to match background image
        self.root.title("Face Recognition System")

        # First Image 
        img1 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\college2.webp")
        img1 = img1.resize((350, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=350, height=130)

        # Second Image
        img2 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\facialRecognition.jpeg")
        img2 = img2.resize((300, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=350, y=0, width=300, height=130)

        # Third Image
        img3 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\facialRecognition3.jpeg")
        img3 = img3.resize((300, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=650, y=0, width=300, height=130)

        # Fourth Image
        img4 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\facialRecognition2.jpeg")
        img4 = img4.resize((300, 130), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl4 = Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=950, y=0, width=300, height=130)

        # Fifth Image
        img5 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\college1.webp")
        img5 = img5.resize((350, 130), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl5 = Label(self.root, image=self.photoimg5)
        f_lbl5.place(x=1250, y=0, width=350, height=130)

         # bg image
        img6 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img6 = img6.resize((1545, 710), Image.LANCZOS)
        
        # Adding Opacity
        img6 = img6.convert("RGBA")
        img6.putalpha(128)  # Adjust the alpha value (0 to 255) for the desired opacity
        
        self.photoimg6 = ImageTk.PhotoImage(img6)

        bg_img = Label(self.root, image=self.photoimg6)
        bg_img.place(x=0, y=130, width=1545, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)

        # Frame i.e White background
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)


        img_left = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\college2.webp")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)


        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)


        # Department 
        dep_label = Label(current_course_frame, text="Department", font=("times new roman",13,"bold"), bg="white")
        dep_label.grid(row=0,column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,  font=("times new roman",13,"bold"), state="read only", width=20)
        dep_combo["value"] = ("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)


        # course
        course_label = Label(current_course_frame, text="Course", font=("times new roman",13,"bold"), bg="white")
        course_label.grid(row=0,column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,  font=("times new roman",13,"bold"),width=20, state="read only")
        course_combo["value"] = ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman",13,"bold"), bg="white")
        year_label.grid(row=1,column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,  font=("times new roman",12,"bold"),width=17, state="read only")
        year_combo["value"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)


        # Semester
        semester_label = Label(current_course_frame, text="Year", font=("times new roman",13,"bold"), bg="white")
        semester_label.grid(row=1,column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,  font=("times new roman",12,"bold"),width=17, state="read only")
        semester_combo["value"] = ("Select Year","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)


         # class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5, y=135, width=720, height=150)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()