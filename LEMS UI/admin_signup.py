import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class adminsignup:
    def __init__(self, root4):
        self.root4 = root4
        self.root4.geometry("1550x850+0+0")
        self.root4.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root4.config(bg="white")
        self.root4.focus_force()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_pass = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root4, text="Signup for Admin", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        preview_frame = Frame(self.root4, bd=10, relief=RIDGE).place(
            x=0, y=150, relwidth=1, height=555)
        signup = Frame(self.root4, bd=3, relief=RIDGE, bg="white").place(
            x=425, y=225, width=705, height=400)
        txt = Entry(signup, textvariable=self.var_name, font=(
            "Century Gothic", 18), bg="#a8dadc").place(x=800, y=275, width=250, height=50)
        cmb = ttk.Combobox(signup, textvariable=self.var_designation, values=(
            "Student", "Professor", "Assistant Professor", "Lab Incharge", "Lab Assistant", "Coordinator"), state="readonly", justify=CENTER, font=("Century Gothic", 18)).place(x=800, y=365, width=250, height=50)
        pas = Entry(signup, textvariable=self.var_pass, font=(
            "Century Gothic", 18), bg="#a8dadc").place(x=800, y=450, width=250, height=50)
        self.var_name.set("Enter your name")
        self.var_designation.set("Select")
        self.var_pass.set("Enter your Password")
        lbl_name = Label(signup, text="Enter your Name :", font=(
            "Century Gothic", 18, "bold"),bg="white").place(x=500, y=275, width=300, height=50)
        lbl_cmb = Label(signup, text="Select your Designation :", font=(
            "Century Gothic", 18, "bold"),bg="white").place(x=500, y=365, width=300, height=50)
        lbl_pass = Label(signup, text="Enter your Password :", font=(
            "Century Gothic", 18, "bold"),bg="white").place(x=500, y=450, width=300, height=50)
        signupbtn = Button(signup, text="Signup", command=self.add, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=680, y=550, width=75, height=30)
        clearbtn = Button(signup, text="Clear", command=self.clear, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=830, y=550, width=75, height=30)
        lbl_menu = Label(self.root4, text="Enter your Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=100, relwidth=1, height=50)
        lbl_footer = Label(self.root4, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        self.clock()

    def clear(self):
        self.var_name.set("")
        self.var_designation.set("Select")
        self.var_pass.set("")

    def add(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        if self.var_name.get()=="" or self.var_designation.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror(
                "Error", "All fields are mandatory to be filled!", parent=self.root4)
        cur.execute("INSERT INTO admin (name,desig) VALUES(?,?)",(self.var_name.get(),self.var_designation.get()))
        con.commit()
        messagebox.showinfo(
                "Congatulations", "Signed up successfully!", parent=self.root4)

    def clock(self):
        hh = time.strftime("%H")
        min = time.strftime("%M")
        ss = time.strftime("%S")
        am_pm = time.strftime("%p")
        dd = time.strftime("%d")
        mm = time.strftime("%B")
        yyyy = time.strftime("%Y")
        lbl_clock = Label(self.root4, text=("DATE: "+dd+"-"+mm+"-"+yyyy+"\nTIME: "+hh+":"+min+":"+ss+" "+am_pm), font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=225, height=75)
        lbl_clock.after(1000, self.clock)

# if __name__ == "__main_":
root4 = Tk()
obj = adminsignup(root4)
root4.mainloop()