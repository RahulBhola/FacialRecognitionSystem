from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
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

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1545, height=45)




        # student button
        img7 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        self.b1_1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b1_1.place(x=200, y=300, width=220, height=40)

        # Hover effect bindings
        self.b1_1.bind("<Enter>", self.on_enter_b1)
        self.b1_1.bind("<Leave>", self.on_leave_b1)




        # Detect face button
        img8 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        self.b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b2_1.place(x=500, y=300, width=220, height=40)

        # Hover effect bindings
        self.b2_1.bind("<Enter>", self.on_enter_b2)
        self.b2_1.bind("<Leave>", self.on_leave_b2)




        # Attendence face button
        img9 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b3 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        self.b3_1 = Button(bg_img, text="Attendence", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b3_1.place(x=800, y=300, width=220, height=40)

        # Hover effect bindings
        self.b3_1.bind("<Enter>", self.on_enter_b3)
        self.b3_1.bind("<Leave>", self.on_leave_b3)




        # Help button
        img10 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b4 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        self.b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b4_1.place(x=1100, y=300, width=220, height=40)

        # Hover effect bindings
        self.b4_1.bind("<Enter>", self.on_enter_b4)
        self.b4_1.bind("<Leave>", self.on_leave_b4)




        # Train Face button
        img11 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b5 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b5.place(x=200, y=380, width=220, height=220)

        self.b5_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b5_1.place(x=200, y=580, width=220, height=40)

        # Hover effect bindings
        self.b5_1.bind("<Enter>", self.on_enter_b5)
        self.b5_1.bind("<Leave>", self.on_leave_b5)




        # Photos button
        img12 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\background.jpeg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b6 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)

        self.b6_1 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b6_1.place(x=500, y=580, width=220, height=40)

        # Hover effect bindings
        self.b6_1.bind("<Enter>", self.on_enter_b6)
        self.b6_1.bind("<Leave>", self.on_leave_b6)




        # Developer button
        img13 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\developer.jpg")
        img13 = img13.resize((240, 220), Image.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        b7 = Button(bg_img, image=self.photoimg13, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        self.b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b7_1.place(x=800, y=580, width=220, height=40)

        # Hover effect bindings
        self.b7_1.bind("<Enter>", self.on_enter_b7)
        self.b7_1.bind("<Leave>", self.on_leave_b7)




        # Exit button
        img14 = Image.open(r"D:\Projects\FacialRecognisationSystem\college_images\exit.jpg")
        img14 = img14.resize((220, 220), Image.LANCZOS)
        self.photoimg14 = ImageTk.PhotoImage(img14)

        b8 = Button(bg_img, image=self.photoimg14, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)

        self.b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        self.b8_1.place(x=1100, y=580, width=220, height=40)

        # Hover effect bindings
        self.b8_1.bind("<Enter>", self.on_enter_b8)
        self.b8_1.bind("<Leave>", self.on_leave_b8)






    def on_enter_b1(self, event):
        # Function to be executed when mouse enters the b1_1 button
        self.b1_1.config(bg="gray")

    def on_leave_b1(self, event):
        # Function to be executed when mouse leaves the b1_1 button
        self.b1_1.config(bg="black")

    def on_enter_b2(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b2_1.config(bg="gray")

    def on_leave_b2(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b2_1.config(bg="black")

    def on_enter_b3(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b3_1.config(bg="gray")

    def on_leave_b3(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b3_1.config(bg="black")
    
    def on_enter_b4(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b4_1.config(bg="gray")

    def on_leave_b4(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b4_1.config(bg="black")

    def on_enter_b5(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b5_1.config(bg="gray")

    def on_leave_b5(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b5_1.config(bg="black")

    def on_enter_b6(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b6_1.config(bg="gray")

    def on_leave_b6(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b6_1.config(bg="black")

    def on_enter_b7(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b7_1.config(bg="gray")

    def on_leave_b7(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b7_1.config(bg="black")

    def on_enter_b8(self, event):
        # Function to be executed when mouse enters the b2_1 button
        self.b8_1.config(bg="gray")

    def on_leave_b8(self, event):
        # Function to be executed when mouse leaves the b2_1 button
        self.b8_1.config(bg="black")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
