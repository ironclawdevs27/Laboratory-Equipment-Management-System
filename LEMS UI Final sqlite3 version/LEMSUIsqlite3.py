import sqlite3
import time
import webbrowser
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
root = Tk()


class LEMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x850+0+0")
        self.root.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root.config(bg="white")
        self.footer()
        self.root.focus_force()
        self.selectlogintype()

    def footer(self):
        lbl_footer = Label(self.root, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of studentistration",
                           font=("Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        hh = time.strftime("%H")
        min = time.strftime("%M")
        ss = time.strftime("%S")
        am_pm = time.strftime("%p")
        dd = time.strftime("%d")
        mm = time.strftime("%B")
        yyyy = time.strftime("%Y")
        lbl_clock = Label(self.root, text=("DATE: "+dd+"-"+mm+"-"+yyyy+"\nTIME: "+hh+":"+min+":"+ss+" "+am_pm), font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=225, height=75)
        lbl_clock.after(1000, self.footer)

    def clear(self):
        self.var_name.set("")
        self.var_designation.set("Select")
        self.var_pass.set("")
        self.var_id.set("")
        self.var_department.set("Select")

    def clearadmins(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.admintable.delete(*self.admintable.get_children())
        self.showadmins()

    def addadmin(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        if self.var_name.get() == "" or self.var_designation.get() == "Select" or self.var_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are mandatory to be filled!", parent=self.root)
        cur.execute("INSERT INTO admin (name,desig) VALUES(?,?)",
                    (self.var_name.get(), self.var_designation.get()))
        con.commit()
        messagebox.showinfo(
            "Congatulations", "Signed up successfully!", parent=self.root)

    def addstudent(self):
        con = sqlite3.connect(database=r'student.db')
        cur = con.cursor()
        if self.var_name.get() == "" or self.var_department.get() == "Select" or self.var_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are mandatory to be filled!", parent=self.root)
        cur.execute("INSERT INTO student (name,dept) VALUES(?,?)",
                    (self.var_name.get(), self.var_department.get()))
        con.commit()
        messagebox.showinfo(
            "Congatulations", "Signed up successfully!", parent=self.root)

    def selectlogintype(self):
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Welcome To UIET's\nLaboratory Equipment Management System", font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white").place(x=10, y=10, width=1515, height=200)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=485)
        self.bgpic = Image.open("uiet.png")
        self.bgpic = self.bgpic.resize((1490, 460), Image.ANTIALIAS)
        self.bgpic = ImageTk.PhotoImage(self.bgpic)
        lbl_bgpic = Label(self.root, image=self.bgpic)
        lbl_bgpic.place(x=20, y=220)
        self.leftlogo = Image.open("lemslogo.png")
        self.leftlogo = self.leftlogo.resize((160, 160), Image.ANTIALIAS)
        self.leftlogo = ImageTk.PhotoImage(self.leftlogo)
        lbl_leftlogo = Label(self.root, image=self.leftlogo, bg="#023047")
        lbl_leftlogo.place(x=20, y=20)
        self.rightlogo = Image.open("UIET_logo.png")
        self.rightlogo = self.rightlogo.resize((160, 160), Image.ANTIALIAS)
        self.rightlogo = ImageTk.PhotoImage(self.rightlogo)
        lbl_rightlogo = Label(self.root, image=self.rightlogo, bg="#023047")
        lbl_rightlogo.place(x=1350, y=20)
        select = Frame(self.root, bd=3, relief=RIDGE).place(
            x=425, y=250, width=705, height=400)
        self.selectlogo = Image.open("login.png")
        self.selectlogo = self.selectlogo.resize((160, 160), Image.ANTIALIAS)
        self.selectlogo = ImageTk.PhotoImage(self.selectlogo)
        lbl_selectlogo = Label(self.root, image=self.selectlogo)
        lbl_selectlogo.place(x=700, y=275)
        adminbtn = Button(self.root, text="Admin", command=self.loginadmin, font=(
            "Century Gothic", 25, "bold"), bg="#e07a5f", cursor="hand2").place(x=530, y=525, width=200, height=75)
        studentbtn = Button(self.root, text="Student", command=self.loginstudent, font=(
            "Century Gothic", 25, "bold"), bg="#e07a5f", cursor="hand2").place(x=825, y=525, width=200, height=75)
        self.lbl_select = Label(self.root, text="Select Login Option:", font=(
            "Century Gothic", 20, "bold")).place(x=630, y=450, height=50, width=300)

    def loginadmin(self):
        self.var_id = StringVar()
        self.var_pass = StringVar()
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Welcome To UIET's\nLaboratory Equipment Management System", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=10, y=10, width=1515, height=150)
        lbl_menu = Label(self.root, text="Enter your Login Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=485)
        self.bgpic = Image.open("uiet.png")
        self.bgpic = self.bgpic.resize((1490, 460), Image.ANTIALIAS)
        self.bgpic = ImageTk.PhotoImage(self.bgpic)
        lbl_bgpic = Label(self.root, image=self.bgpic)
        lbl_bgpic.place(x=20, y=220)
        self.leftlogo = Image.open("lemslogo.png")
        self.leftlogo = self.leftlogo.resize((130, 130), Image.ANTIALIAS)
        self.leftlogo = ImageTk.PhotoImage(self.leftlogo)
        lbl_leftlogo = Label(self.root, image=self.leftlogo, bg="#023047")
        lbl_leftlogo.place(x=120, y=20)
        self.rightlogo = Image.open("UIET_logo.png")
        self.rightlogo = self.rightlogo.resize((130, 130), Image.ANTIALIAS)
        self.rightlogo = ImageTk.PhotoImage(self.rightlogo)
        lbl_rightlogo = Label(self.root, image=self.rightlogo, bg="#023047")
        lbl_rightlogo.place(x=1280, y=20)
        select = Frame(self.root, bd=3, relief=RIDGE).place(
            x=425, y=250, width=705, height=400)
        lbl_id = LabelFrame(self.root, text="Enter your Admin ID:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=310, width=400, height=80)
        lbl_pass = LabelFrame(self.root, text="Enter your Password:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=420, width=400, height=80)
        lbl_signup = Label(self.root, text="New User? To register in LEMS as an Admin, Signup:", font=(
            "Century Gothic", 12, "bold")).place(x=530, y=603, width=400, height=20)
        txt = Entry(self.root, textvariable=self.var_id, font=(
            "Century Gothic", 15)).place(x=655, y=350, width=250, height=30)
        pas = Entry(self.root, textvariable=self.var_pass, font=(
            "Century Gothic", 15)).place(x=655, y=460, width=250, height=30)
        self.var_id.set("Enter your name")
        self.var_pass.set("Enter your Password")
        signinbtn = Button(self.root, text="Signin", command=self.admindash, font=(
            "Century Gothic", 16, "bold"), bg="#ff9f1c", cursor="hand2").place(x=660, y=535, width=90, height=40)
        signupbtn = Button(self.root, text="Signup", command=self.signupadmin, font=(
            "Century Gothic", 14, "bold"), bg="#e07a5f", cursor="hand2").place(x=925, y=600, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearsys, font=(
            "Century Gothic", 16, "bold"), bg="#2a9d8f", cursor="hand2").place(x=830, y=535, width=90, height=40)
        backbtn = Button(self.root, text="< Back", command=self.selectlogintype, font=("Century Gothic", 15, "bold"),
                         bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)

    def loginstudent(self):
        self.var_id = StringVar()
        self.var_pass = StringVar()
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Welcome To UIET's\nLaboratory Equipment Management System", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=10, y=10, width=1515, height=150)
        lbl_menu = Label(self.root, text="Enter your Login Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=485)
        self.bgpic = Image.open("uiet.png")
        self.bgpic = self.bgpic.resize((1490, 460), Image.ANTIALIAS)
        self.bgpic = ImageTk.PhotoImage(self.bgpic)
        lbl_bgpic = Label(self.root, image=self.bgpic)
        lbl_bgpic.place(x=20, y=220)
        self.leftlogo = Image.open("lemslogo.png")
        self.leftlogo = self.leftlogo.resize((130, 130), Image.ANTIALIAS)
        self.leftlogo = ImageTk.PhotoImage(self.leftlogo)
        lbl_leftlogo = Label(self.root, image=self.leftlogo, bg="#023047")
        lbl_leftlogo.place(x=120, y=20)
        self.rightlogo = Image.open("UIET_logo.png")
        self.rightlogo = self.rightlogo.resize((130, 130), Image.ANTIALIAS)
        self.rightlogo = ImageTk.PhotoImage(self.rightlogo)
        lbl_rightlogo = Label(self.root, image=self.rightlogo, bg="#023047")
        lbl_rightlogo.place(x=1280, y=20)
        select = Frame(self.root, bd=3, relief=RIDGE).place(
            x=425, y=250, width=705, height=400)
        lbl_id = LabelFrame(self.root, text="Enter your Student ID:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=310, width=400, height=80)
        lbl_pass = LabelFrame(self.root, text="Enter your Password:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=420, width=400, height=80)
        lbl_signup = Label(self.root, text="New User? To register in LEMS as a Student, Signup:", font=(
            "Century Gothic", 12, "bold")).place(x=530, y=603, width=400, height=20)
        txt = Entry(self.root, textvariable=self.var_id, font=(
            "Century Gothic", 15)).place(x=655, y=350, width=250, height=30)
        pas = Entry(self.root, textvariable=self.var_pass, font=(
            "Century Gothic", 15)).place(x=655, y=460, width=250, height=30)
        self.var_id.set("Enter your name")
        self.var_pass.set("Enter your Password")
        signinbtn = Button(self.root, text="Signin", command=self.studentdash, font=(
            "Century Gothic", 16, "bold"), bg="#ff9f1c", cursor="hand2").place(x=660, y=535, width=90, height=40)
        signupbtn = Button(self.root, text="Signup", command=self.signupstudent, font=(
            "Century Gothic", 14, "bold"), bg="#e07a5f", cursor="hand2").place(x=925, y=600, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearsys, font=(
            "Century Gothic", 16, "bold"), bg="#2a9d8f", cursor="hand2").place(x=830, y=535, width=90, height=40)
        backbtn = Button(self.root, text="< Back", command=self.selectlogintype, font=("Century Gothic", 15, "bold"),
                         bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)

    def signupadmin(self):
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_pass = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Welcome To UIET's\nLaboratory Equipment Management System", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=10, y=10, width=1515, height=150)
        lbl_menu = Label(self.root, text="Enter your Admin Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=485)
        self.bgpic = Image.open("uiet.png")
        self.bgpic = self.bgpic.resize((1490, 460), Image.ANTIALIAS)
        self.bgpic = ImageTk.PhotoImage(self.bgpic)
        lbl_bgpic = Label(self.root, image=self.bgpic)
        lbl_bgpic.place(x=20, y=220)
        self.leftlogo = Image.open("lemslogo.png")
        self.leftlogo = self.leftlogo.resize((130, 130), Image.ANTIALIAS)
        self.leftlogo = ImageTk.PhotoImage(self.leftlogo)
        lbl_leftlogo = Label(self.root, image=self.leftlogo, bg="#023047")
        lbl_leftlogo.place(x=120, y=20)
        self.rightlogo = Image.open("UIET_logo.png")
        self.rightlogo = self.rightlogo.resize((130, 130), Image.ANTIALIAS)
        self.rightlogo = ImageTk.PhotoImage(self.rightlogo)
        lbl_rightlogo = Label(self.root, image=self.rightlogo, bg="#023047")
        lbl_rightlogo.place(x=1280, y=20)
        select = Frame(self.root, bd=3, relief=RIDGE).place(
            x=425, y=250, width=705, height=400)
        lbl_name = LabelFrame(self.root, text="Enter your Name:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=275, width=400, height=80)
        lbl_cmb = LabelFrame(self.root, text="Select your Designation:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=375, width=400, height=80)
        lbl_pass = LabelFrame(self.root, text="Enter your Password:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=470, width=400, height=80)
        txt = Entry(self.root, textvariable=self.var_name, font=(
            "Century Gothic", 15)).place(x=655, y=315, width=250, height=30)
        cmb = ttk.Combobox(self.root, textvariable=self.var_designation, values=(
            "Student", "Professor", "Assistant Professor", "Lab Incharge", "Lab Assistant", "Coordinator"), state="readonly", justify=CENTER, font=("Century Gothic", 15)).place(x=655, y=415, width=250, height=30)
        pas = Entry(self.root, textvariable=self.var_pass, font=(
            "Century Gothic", 15)).place(x=655, y=510, width=250, height=30)
        self.var_name.set("Enter your name")
        self.var_designation.set("Select")
        self.var_pass.set("Enter your Password")
        signupbtn = Button(self.root, text="Signup", command=self.addadmin, font=(
            "Century Gothic", 16, "bold"), bg="#ff9f1c", cursor="hand2").place(x=660, y=575, width=90, height=40)
        clearbtn = Button(self.root, text="Clear", command=self.clear, font=(
            "Century Gothic", 16, "bold"), bg="#2a9d8f", cursor="hand2").place(x=830, y=575, width=90, height=40)
        backbtn = Button(self.root, text="< Back", command=self.loginadmin, font=("Century Gothic", 15, "bold"),
                         bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)

    def signupstudent(self):
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_pass = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Welcome To UIET's\nLaboratory Equipment Management System", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=10, y=10, width=1515, height=150)
        lbl_menu = Label(self.root, text="Enter your Student Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=485)
        self.bgpic = Image.open("uiet.png")
        self.bgpic = self.bgpic.resize((1490, 460), Image.ANTIALIAS)
        self.bgpic = ImageTk.PhotoImage(self.bgpic)
        lbl_bgpic = Label(self.root, image=self.bgpic)
        lbl_bgpic.place(x=20, y=220)
        self.leftlogo = Image.open("lemslogo.png")
        self.leftlogo = self.leftlogo.resize((130, 130), Image.ANTIALIAS)
        self.leftlogo = ImageTk.PhotoImage(self.leftlogo)
        lbl_leftlogo = Label(self.root, image=self.leftlogo, bg="#023047")
        lbl_leftlogo.place(x=120, y=20)
        self.rightlogo = Image.open("UIET_logo.png")
        self.rightlogo = self.rightlogo.resize((130, 130), Image.ANTIALIAS)
        self.rightlogo = ImageTk.PhotoImage(self.rightlogo)
        lbl_rightlogo = Label(self.root, image=self.rightlogo, bg="#023047")
        lbl_rightlogo.place(x=1280, y=20)
        select = Frame(self.root, bd=3, relief=RIDGE).place(
            x=425, y=250, width=705, height=400)
        lbl_name = LabelFrame(self.root, text="Enter your Name:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=275, width=400, height=80)
        lbl_cmb = LabelFrame(self.root, text="Select your Department:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=375, width=400, height=80)
        lbl_pass = LabelFrame(self.root, text="Enter your Password:", font=(
            "Century Gothic", 18, "bold")).place(x=575, y=470, width=400, height=80)
        txt = Entry(self.root, textvariable=self.var_name, font=(
            "Century Gothic", 15)).place(x=655, y=315, width=250, height=30)
        cmb = ttk.Combobox(self.root, textvariable=self.var_department, values=(
            "CSE", "IT", "Mech", "ECE", "EEE", "BioT"), state="readonly", justify=CENTER, font=("Century Gothic", 15)).place(x=655, y=415, width=250, height=30)
        pas = Entry(self.root, textvariable=self.var_pass, font=(
            "Century Gothic", 15)).place(x=655, y=510, width=250, height=30)
        self.var_name.set("Enter your name")
        self.var_department.set("Select")
        self.var_pass.set("Enter your Password")
        signupbtn = Button(self.root, text="Signup", command=self.addstudent, font=(
            "Century Gothic", 16, "bold"), bg="#ff9f1c", cursor="hand2").place(x=660, y=575, width=90, height=40)
        clearbtn = Button(self.root, text="Clear", command=self.clear, font=(
            "Century Gothic", 16, "bold"), bg="#2a9d8f", cursor="hand2").place(x=830, y=575, width=90, height=40)
        backbtn = Button(self.root, text="< Back", command=self.loginstudent, font=("Century Gothic", 15, "bold"),
                         bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)

    def admindash(self):
        icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Admin Dashboard", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="Logout", command=self.selectlogintype, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl = Label(self.root, text="Welcome back Admin!", font=(
            "Century Gothic", 15), bg="#4d636d", fg="white").place(x=10, y=110, width=1515, height=35)
        self.menulogo = Image.open("UIET_logo.png")
        self.menulogo = self.menulogo.resize((300, 300), Image.ANTIALIAS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo)
        lbl_menu = Label(self.root, text="MENU", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=145, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        lbl_menulogo = Label(self.root, image=self.menulogo)
        lbl_menulogo.place(x=615, y=300)
        Admin_btn = Button(self.root, text="Search an Admin", command=self.searchanadmin, font=("Century Gothic", 15, "bold"),
                           bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=10, y=196, height=43, width=252)
        Student_btn = Button(self.root, text="Search a Student", command=self.searchastudent, font=("Century Gothic", 15, "bold"),
                             bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=262, y=196, height=43, width=252)
        Complaints_btn = Button(self.root, text="Complaints System", command=self.complaintsys, font=("Century Gothic", 15, "bold"),
                                bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=514, y=196, height=43, width=252)
        Equipment_btn = Button(self.root, text="System Management", command=self.systemmgmt, font=("Century Gothic", 14, "bold"),
                               bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=766, y=196, height=43, width=252)
        Labs_btn = Button(self.root, text="View Lab Details", command=self.labdetails, font=("Century Gothic", 15, "bold"),
                          bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=1018, y=196, height=43, width=252)
        Contactus_btn = Button(self.root, text="Contact us", command=self.contactus, font=("Century Gothic", 15, "bold"),
                               bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=1270, y=196, height=43, width=255)
        lbl_footer = Label(self.root, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        self.lbl_admin = Label(self.root, text="Total Admins: [ 6 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=60, y=265, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Total Students: [ 60 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=60, y=375, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Total Labs: [ 5 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=60, y=485, height=80, width=500)
        self.lbl_admin = Label(self.root, text="New Complaints: [ 10 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=60, y=595, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Resolved Complaints: [ 27 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=975, y=265, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Pending Complaints: [ 13 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=975, y=375, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Working Equipments: [ 48 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=975, y=485, height=80, width=500)
        self.lbl_admin = Label(self.root, text="Non-working Equipments: [ 12 ] ", bg="#023047", fg="white", font=(
            "Century Gothic", 16, "bold")).place(x=975, y=595, height=80, width=500)

    def searchanadmin(self):
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_admin_id = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Search an Admin", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl_menu = Label(self.root, text="Admin Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=190, width=1515, height=50)
        searchadmin = LabelFrame(self.root, text="Search an Admin", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=450, y=110, width=705, height=75)
        cmb_search = ttk.Combobox(self.root, textvariable=self.var_searchby, values=(
            "Admin ID", "Name", "Designation"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=475, y=145, width=180)
        self.var_searchtxt.set("Enter data to be searched")
        self.var_searchby.set("Select")
        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14)).place(x=680, y=145, width=250)
        searchbtn = Button(self.root, text="Search", command=self.searchadmins, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=955, y=142, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearadmins, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=1055, y=142, width=75, height=30)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        scrollver = Scrollbar(self.root, orient=VERTICAL)
        scrollver.place(x=1495, y=250, height=432, width=20)
        self.admintable = ttk.Treeview(
            self.root, columns=("adminid", "name", "desig"), yscrollcommand=scrollver.set)
        self.admintable.heading("adminid", text="Admin ID")
        self.admintable.heading("name", text="Name")
        self.admintable.heading("desig", text="Designation")
        self.admintable["show"] = "headings"
        self.admintable.place(x=20, y=250, width=1475, height=432)
        scrollver.config(command=self.admintable.yview)
        self.showadmins()

    def showadmins(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM admin")
        rows = cur.fetchall()
        for row in rows:
            self.admintable.insert('', END, values=row)

    def searchadmins(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        if self.var_searchby.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a field for searching!", parent=self.root)
        elif self.var_searchtxt.get() == "":
            messagebox.showerror(
                "Error", "Please enter any parameter to be searched!", parent=self.root)
        elif self.var_searchby.get() == "Name":
            cur.execute("SELECT * FROM admin WHERE name='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        elif self.var_searchby.get() == "Admin ID":
            cur.execute("SELECT * FROM admin WHERE adminid='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        elif self.var_searchby.get() == "Designation":
            cur.execute("SELECT * FROM admin WHERE desig='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)

    def showstudents(self):
        con = sqlite3.connect(database=r'student.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        for row in rows:
            self.studenttable.insert('', END, values=row)

    def searchstudents(self):
        con = sqlite3.connect(database=r'student.db')
        cur = con.cursor()
        if self.var_searchby.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a field for searching!", parent=self.root3)
        elif self.var_searchtxt.get() == "":
            messagebox.showerror(
                "Error", "Please enter any parameter to be searched!", parent=self.root3)
        elif self.var_searchby.get() == "Name":
            cur.execute("SELECT * FROM student WHERE name='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root3)
        elif self.var_searchby.get() == "Student ID":
            cur.execute("SELECT * FROM student WHERE studentid='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root3)
        elif self.var_searchby.get() == "Department":
            cur.execute("SELECT * FROM student WHERE dept='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.studenttable.delete(*self.studenttable.get_children())
            for row in rows:
                self.studenttable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root3)

    def clearstudents(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.studenttable.delete(*self.studenttable.get_children())
        self.showstudents()

    def searchastudent(self):
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Search a Student", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl_menu = Label(self.root, text="Student Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=190, width=1515, height=50)
        searchadmin = LabelFrame(self.root, text="Search a Student", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=450, y=110, width=705, height=75)
        cmb_search = ttk.Combobox(self.root, textvariable=self.var_searchby, values=(
            "Student ID", "Name", "Department"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=475, y=145, width=180)
        self.var_searchtxt.set("Enter data to be searched")
        self.var_searchby.set("Select")
        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14)).place(x=680, y=145, width=250)
        searchbtn = Button(self.root, text="Search", command=self.searchstudents, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=955, y=142, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearstudents, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=1055, y=142, width=75, height=30)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        scrollver = Scrollbar(self.root, orient=VERTICAL)
        scrollver.place(x=1495, y=250, height=432, width=20)
        self.studenttable = ttk.Treeview(
            self.root, columns=("studentid", "name", "dept"), yscrollcommand=scrollver.set)
        self.studenttable.heading("studentid", text="Student ID")
        self.studenttable.heading("name", text="Name")
        self.studenttable.heading("dept", text="Department")
        self.studenttable["show"] = "headings"
        self.studenttable.place(x=20, y=250, width=1475, height=432)
        scrollver.config(command=self.studenttable.yview)
        self.showstudents()

    def complaintsys(self):
        self.var_searchby = StringVar()
        self.var_searchcmp = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Complaint System", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl_menu = Label(self.root, text="Complaints", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=190, width=1515, height=50)
        searchadmin = LabelFrame(self.root, text="Search a Complaint", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=375, y=110, width=825, height=75)
        cmb_search = ttk.Combobox(self.root, textvariable=self.var_searchby, values=(
            "Complaint ID", "Lab Number", "System Number"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=400, y=145, width=180)
        txt_search = Entry(self.root, textvariable=self.var_searchcmp, font=(
            "Century Gothic", 14)).place(x=615, y=145, width=250)
        self.var_searchcmp.set("Enter data to be searched")
        self.var_searchby.set("Select")
        searchbtn = Button(self.root, text="Search", command=self.searchcomp, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=905, y=142, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearcomp, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=1005, y=142, width=75, height=30)
        resolvebtn = Button(self.root, text="Resolve", command=self.deletecomp, font=(
            "Century Gothic", 14), bg="#e07a5f", cursor="hand2").place(x=1105, y=142, width=75, height=30)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        self.var_searchcmp.set("Enter")
        self.var_searchby.set("Select")
        refresh_btn = Button(self.root, text="Refresh", command=self.refreshcomp, font=("Century Gothic", 15, "bold"),
                             bg="#ffd166", cursor="hand2").place(x=1400, y=198, height=35, width=100)
        scrollver = Scrollbar(self.root, orient=VERTICAL)
        scrollver.place(x=1495, y=250, height=432, width=20)
        self.comptable = ttk.Treeview(
            self.root, columns=("complaintid", "labno", "sysno", "complaint"), yscrollcommand=scrollver.set)
        self.comptable.heading("complaintid", text="Complaint ID")
        self.comptable.heading("labno", text="Lab Number")
        self.comptable.heading("sysno", text="System Number")
        self.comptable.heading("complaint", text="Complaint")
        self.comptable["show"] = "headings"
        self.comptable.place(x=20, y=250, width=1475, height=432)
        scrollver.config(command=self.comptable.yview)
        self.comptable.bind("<ButtonRelease-1>", self.getcomp_id)
        self.showcomp()

    def refreshcomp(self):
        self.var_searchcmp.set("Enter")
        self.var_searchby.set("Select")
        self.comptable.delete(*self.comptable.get_children())
        self.showcomp()

    def clearcomp(self):
        self.var_searchcmp.set("")
        self.var_searchby.set("Select")
        self.comptable.delete(*self.comptable.get_children())
        self.showcomp()

    def deletecomp(self):
        con = sqlite3.connect(database=r'complaint.db')
        cur = con.cursor()
        deleteid = self.getcomp_id()
        cur.execute("DELETE FROM complaint where complaintid=?", (deleteid,))
        con.commit()
        messagebox.showinfo(
            "Congatulations", "Complaint Resolved successfully!", parent=self.root)

    def showcomp(self):
        con = sqlite3.connect(database=r'complaint.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM complaint")
        rows = cur.fetchall()
        for row in rows:
            self.comptable.insert('', END, values=row)

    def getcomp_id(self):
        f = self.comptable.focus()
        content = (self.comptable.item(f))
        row = content['values']
        return row[0]

    def searchcomp(self):
        con = sqlite3.connect(database=r'complaint.db')
        cur = con.cursor()
        if self.var_searchby.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a field for searching!", parent=self.root)
        elif self.var_searchcmp.get() == "":
            messagebox.showerror(
                "Error", "Please enter any parameter to be searched!", parent=self.root)
        elif self.var_searchby.get() == "Lab Number":
            cur.execute("SELECT * FROM complaint WHERE labno='" +
                        self.var_searchcmp.get()+"'")
            rows = cur.fetchall()
            self.comptable.delete(*self.comptable.get_children())
            for row in rows:
                self.comptable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        elif self.var_searchby.get() == "Complaint ID":
            cur.execute("SELECT * FROM complaint WHERE complaintid='" +
                        self.var_searchcmp.get()+"'")
            rows = cur.fetchall()
            self.comptable.delete(*self.comptable.get_children())
            for row in rows:
                self.comptable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        elif self.var_searchby.get() == "System Number":
            cur.execute("SELECT * FROM complaint WHERE sysno='" +
                        self.var_searchcmp.get()+"'")
            rows = cur.fetchall()
            self.comptable.delete(*self.comptable.get_children())
            for row in rows:
                self.comptable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        elif self.var_searchby.get() == "Complaint":
            cur.execute("SELECT * FROM complaint WHERE complaint='" +
                        self.var_searchcmp.get()+"'")
            rows = cur.fetchall()
            self.comptable.delete(*self.comptable.get_children())
            for row in rows:
                self.comptable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
        else:
            cur.execute("SELECT * FROM complaint WHERE "+self.var_searchby.get() +
                        " LIKE '%"+self.var_searchcmp.get()+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root)
            for row in rows:
                self.comptable.insert('', END, values=row)

    def systemmgmt(self):
        self.var_searchby = StringVar()
        self.var_searchcmp = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="System Management", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl_menu = Label(self.root, text="Working Status of System along with its Individaual Peripheral's Working Status", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=190, width=1515, height=50)
        searchadmin = LabelFrame(self.root, text="Update Working Status", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=600, y=110, width=350, height=75)
        cmb_search = ttk.Combobox(self.root, textvariable=self.var_searchby, values=(
            "Overall Working Status", "Mouse Working Status", "Keyboard Working Status", "Monitor Working Status", "CPU Working Status"), state="readonly", justify=CENTER, font=("Century Gothic", 10)).place(x=615, y=145, width=180)
        self.var_searchby.set("Select")
        updatebtn = Button(self.root, text="Update", command=self.updatesys, font=(
            "Century Gothic", 14), bg="#e07a5f", cursor="hand2").place(x=830, y=142, width=75, height=30)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        refresh_btn = Button(self.root, text="Refresh", command=self.refreshsys, font=("Century Gothic", 15, "bold"),
                             bg="#ffd166", cursor="hand2").place(x=1400, y=198, height=35, width=100)
        scrollver = Scrollbar(self.root, orient=VERTICAL)
        scrollver.place(x=1495, y=250, height=432, width=20)
        self.systable = ttk.Treeview(
            self.root, columns=("sysid", "labno", "overallstat", "mousestat", "keybstat", "monistat", "cpustat"), yscrollcommand=scrollver.set)
        self.systable.heading("sysid", text="Complaint ID")
        self.systable.heading("labno", text="Lab Number")
        self.systable.heading("overallstat", text="Overall Working Status")
        self.systable.heading("mousestat", text="Mouse Working Status")
        self.systable.heading("keybstat", text="Keyboard Working Status")
        self.systable.heading("monistat", text="Monitor Working Status")
        self.systable.heading("cpustat", text="CPU Working Status")
        self.systable["show"] = "headings"
        self.systable.place(x=20, y=250, width=1475, height=432)
        scrollver.config(command=self.systable.yview)
        self.systable.bind("<ButtonRelease-1>", self.getsys_id)
        self.showsys()

    def refreshsys(self):
        self.var_searchcmp.set("Enter")
        self.var_searchby.set("Select")
        self.systable.delete(*self.systable.get_children())
        self.showsys()

    def clearsys(self):
        self.var_id.set("")
        self.var_pass.set("")
        self.var_searchcmp.set("")
        self.var_searchby.set("Select")
        self.systable.delete(*self.systable.get_children())
        self.showsys()

    def updatesys(self):
        con = sqlite3.connect(database=r'system.db')
        cur = con.cursor()
        values = self.getsys_id()
        print(self.var_searchby)
        updateid = values[0]
        if self.var_searchby.get() == "Overall Working Status":
            if values[2] == 'Working':
                cur.execute(
                    "UPDATE system set overallstat='Not Working' where sysid=?", (updateid,))
                con.commit()
            elif values[2] == 'Not Working':
                cur.execute(
                    "UPDATE system set overallstat='Working' where sysid=?", (updateid,))
                con.commit()
        elif self.var_searchby.get() == "Mouse Working Status":
            if values[3] == 'Working':
                cur.execute(
                    "UPDATE system set mousestat='Not Working' where sysid=?", (updateid,))
                con.commit()
            elif values[3] == 'Not Working':
                cur.execute(
                    "UPDATE system set mousestat='Working' where sysid=?", (updateid,))
                con.commit()
        elif self.var_searchby.get() == "Keyboard Working Status":
            if values[4] == 'Working':
                cur.execute(
                    "UPDATE system set keybstat='Not Working' where sysid=?", (updateid,))
                con.commit()
            elif values[4] == 'Not Working':
                cur.execute(
                    "UPDATE system set keybstat='Working' where sysid=?", (updateid,))
                con.commit()
        elif self.var_searchby.get() == "Monitor Working Status":
            if values[5] == 'Working':
                cur.execute(
                    "UPDATE system set monistat='Not Working' where sysid=?", (updateid,))
                con.commit()
            elif values[5] == 'Not Working':
                cur.execute(
                    "UPDATE system set monistat='Working' where sysid=?", (updateid,))
                con.commit()
        elif self.var_searchby.get() == "CPU Working Status":
            if values[6] == 'Working':
                cur.execute(
                    "UPDATE system set cpustat='Not Working' where sysid=?", (updateid,))
                con.commit()
            elif values[6] == 'Not Working':
                cur.execute(
                    "UPDATE system set cpustat='Working' where sysid=?", (updateid,))
                con.commit()
        messagebox.showinfo(
            "Congatulations", "Equipment Working Status updated successfully!", parent=self.root)

    def showsys(self):
        con = sqlite3.connect(database=r'system.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM system")
        rows = cur.fetchall()
        for row in rows:
            self.systable.insert('', END, values=row)

    def getsys_id(self):
        f = self.systable.focus()
        content = (self.systable.item(f))
        row = content['values']
        return row

    def labdetails(self):
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Lab Details", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        lbl_menu = Label(self.root, text="Active Hours: 9 AM to 5 PM | Labs are closed on every Saturday, Sunday and Holidays declared by PU", font=(
            "Century Gothic", 20, "bold"), bg="#457b9d", fg="white").place(x=10, y=110, width=1515, height=50)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=160, width=1515, height=535)
        lab1 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=30, y=175, width=250, height=500)
        lab2 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=335, y=175, width=250, height=500)
        lab3 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=645, y=175, width=250, height=500)
        lab4 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=955, y=175, width=250, height=500)
        lab5 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=1255, y=175, width=250, height=500)
        lbl_name1 = Label(self.root, text="Lab 1:\nOOPS", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=33, y=205, width=244, height=150)
        lbl_labi1 = Label(self.root, text="Honey Singh", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=33, y=335, width=244, height=150)
        lbl_laba11 = Label(self.root, text="J Star", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=33, y=500, width=244, height=30)
        lbl_laba12 = Label(self.root, text="Alfaaz", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=33, y=530, width=244, height=30)
        lbl_cno1 = Label(self.root, text="0172-2541241", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=33, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=605, width=244, height=20)
        lbl_name2 = Label(self.root, text="Lab 2:\nMultimedia", font=(
            "Century Gothic", 32, "bold"), bg="#023047", fg="white").place(x=338, y=205, width=244, height=150)
        lbl_labi2 = Label(self.root, text="KK", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=338, y=335, width=244, height=150)
        lbl_laba21 = Label(self.root, text="Shaan", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=338, y=500, width=244, height=30)
        lbl_laba22 = Label(self.root, text="Pritam", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=338, y=530, width=244, height=30)
        lbl_cno2 = Label(self.root, text="0172-2541242", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=338, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=605, width=244, height=20)
        lbl_name3 = Label(self.root, text="Lab 3:\nData\nStructures", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=648, y=195, width=244, height=150)
        lbl_labi3 = Label(self.root, text="Shawn Mendes", font=(
            "Century Gothic", 23, "bold"), bg="#023047", fg="white").place(x=648, y=335, width=244, height=150)
        lbl_laba31 = Label(self.root, text="Camila Cabello", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=648, y=500, width=244, height=30)
        lbl_laba32 = Label(self.root, text="Dua Lipa", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=648, y=530, width=244, height=30)
        lbl_cno3 = Label(self.root, text="0172-2541243", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=648, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=605, width=244, height=20)
        lbl_name4 = Label(self.root, text="Lab 4:\nDatabase", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=958, y=205, width=244, height=150)
        lbl_labi4 = Label(self.root, text="Charlie Puth", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=958, y=335, width=244, height=150)
        lbl_laba41 = Label(self.root, text="DJ Snake", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=958, y=500, width=244, height=30)
        lbl_laba42 = Label(self.root, text="Selena Gomez", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=958, y=530, width=244, height=30)
        lbl_cno4 = Label(self.root, text="0172-2541244", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=958, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=605, width=244, height=20)
        lbl_name5 = Label(self.root, text="Lab 5:\nSoftware", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=1258, y=205, width=244, height=150)
        lbl_labi5 = Label(self.root, text="Anuv Jain", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=1258, y=335, width=244, height=150)
        lbl_laba51 = Label(self.root, text="Zaeden", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=1258, y=500, width=244, height=30)
        lbl_laba52 = Label(self.root, text="Dikshant", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=1258, y=530, width=244, height=30)
        lbl_cno5 = Label(self.root, text="0172-2541245", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=1258, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=605, width=244, height=20)

    def contactus(self):
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Contact Us", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        lbl_menu = Label(self.root, text="LEMS is owned by MoonDancers Pvt. Ltd.", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=110, width=1515, height=50)
        logout_btn = Button(self.root, text="< Back", command=self.admindash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=160, width=1515, height=533)
        cus1 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=30, y=190, width=250, height=475)
        cus2 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=330, y=190, width=250, height=475)
        cus3 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=640, y=190, width=250, height=475)
        cus4 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=950, y=190, width=250, height=475)
        cus5 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=1255, y=190, width=250, height=475)
        lbl_name1 = Label(self.root, text="Anavi\nSharma", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=33, y=200, width=244, height=150)
        lbl_cno1 = Label(self.root, text="7889156406", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=33, y=390, width=244, height=150)
        lbl_email1 = Label(self.root, text="20anavisharma@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=33, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=580, width=244, height=20)
        lbl_name2 = Label(self.root, text="Arshia\nDhiman", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=333, y=200, width=244, height=150)
        lbl_cno2 = Label(self.root, text="7717494596", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=333, y=390, width=244, height=150)
        lbl_email2 = Label(self.root, text="arshiadhiman189@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=333, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=580, width=244, height=20)
        lbl_name3 = Label(self.root, text="Aryan\nRaj", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=643, y=200, width=244, height=150)
        lbl_cno3 = Label(self.root, text="7355285828", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=643, y=390, width=244, height=150)
        lbl_email3 = Label(self.root, text="aryarasin@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=643, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=580, width=244, height=20)
        lbl_name4 = Label(self.root, text="Ayush\nGautam", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=953, y=200, width=244, height=150)
        lbl_cno4 = Label(self.root, text="7831989601", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=953, y=390, width=244, height=150)
        lbl_email4 = Label(self.root, text="ayugautam12@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=953, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=580, width=244, height=20)
        lbl_name5 = Label(self.root, text="Himanshu\nKaushal", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=1258, y=200, width=244, height=150)
        lbl_cno5 = Label(self.root, text="8376874442", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=1258, y=390, width=244, height=150)
        lbl_email5 = Label(self.root, text="kaushalhimanshu80@gmail.com", font=(
            "Century Gothic", 11, "bold"), bg="#023047", fg="white").place(x=1258, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=580, width=244, height=20)

    def studentdash(self):
        icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Student Dashboard", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        logout_btn = Button(self.root, text="Logout", command=self.selectlogintype, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        lbl = Label(self.root, text="Welcome back Student!", font=(
            "Century Gothic", 15), bg="#4d636d", fg="white").place(x=10, y=110, width=1515, height=35)
        self.menulogo = Image.open("UIET_logo.png")
        self.menulogo = self.menulogo.resize((300, 300), Image.ANTIALIAS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo)
        lbl_menu = Label(self.root, text="MENU", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=145, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=240, width=1515, height=453)
        lbl_menulogo = Label(self.root, image=self.menulogo)
        lbl_menulogo.place(x=615, y=300)
        Filecomp_btn = Button(self.root, text="File a Complaint", command=self.filecomp, font=("Century Gothic", 15, "bold"),
                              bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=10, y=196, height=43, width=375)
        Labstatus_btn = Button(self.root, text="View Lab Status Map", command=self.viewsystemstatusmap, font=("Century Gothic", 15, "bold"),
                               bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=385, y=196, height=43, width=380)
        Labs_btn = Button(self.root, text="Contact Admins", command=self.contactadmins, font=("Century Gothic", 15, "bold"),
                          bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=765, y=196, height=43, width=380)
        Contactus2_btn = Button(self.root, text="Contact us", command=self.contactus2, font=("Century Gothic", 15, "bold"),
                                bg="#e07a5f", bd=3, cursor="hand2", relief=RIDGE).place(x=1145, y=196, height=43, width=380)
        lbl_footer = Label(self.root, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        self.lbl_admin = Label(self.root, text="Total Login Sessions: [ 11 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=60, y=265, height=100, width=500)
        self.lbl_admin = Label(self.root, text="Average Login Session: [ 2.5 hrs ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=60, y=415, height=100, width=500)
        self.lbl_admin = Label(self.root, text="Student Admin: [ No ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=60, y=565, height=100, width=500)
        self.lbl_admin = Label(self.root, text="Total Complaints filed: [ 4 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=975, y=265, height=100, width=500)
        self.lbl_admin = Label(self.root, text="Total Systems used: [ 19 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=975, y=415, height=100, width=500)
        self.lbl_admin = Label(self.root, text="Total Systems reported: [ 2 ]", bg="#023047", fg="white", font=(
            "Century Gothic", 20, "bold")).place(x=975, y=565, height=100, width=500)

    def contactus2(self):
        self.icon_title = PhotoImage(file="default.png")
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        title = Label(self.root, text="Contact Us", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        lbl_menu = Label(self.root, text="LEMS is owned by MoonDancers Pvt. Ltd.", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white").place(x=10, y=110, width=1515, height=50)
        logout_btn = Button(self.root, text="< Back", command=self.studentdash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=160, width=1515, height=533)
        cus1 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=30, y=190, width=250, height=475)
        cus2 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=330, y=190, width=250, height=475)
        cus3 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=640, y=190, width=250, height=475)
        cus4 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=950, y=190, width=250, height=475)
        cus5 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=1255, y=190, width=250, height=475)
        lbl_name1 = Label(self.root, text="Anavi\nSharma", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=33, y=200, width=244, height=150)
        lbl_cno1 = Label(self.root, text="7889156406", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=33, y=390, width=244, height=150)
        lbl_email1 = Label(self.root, text="20anavisharma@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=33, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=580, width=244, height=20)
        lbl_name2 = Label(self.root, text="Arshia\nDhiman", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=333, y=200, width=244, height=150)
        lbl_cno2 = Label(self.root, text="7717494596", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=333, y=390, width=244, height=150)
        lbl_email2 = Label(self.root, text="arshiadhiman189@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=333, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=580, width=244, height=20)
        lbl_name3 = Label(self.root, text="Aryan\nRaj", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=643, y=200, width=244, height=150)
        lbl_cno3 = Label(self.root, text="7355285828", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=643, y=390, width=244, height=150)
        lbl_email3 = Label(self.root, text="aryarasin@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=643, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=580, width=244, height=20)
        lbl_name4 = Label(self.root, text="Ayush\nGautam", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=953, y=200, width=244, height=150)
        lbl_cno4 = Label(self.root, text="7831989601", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=953, y=390, width=244, height=150)
        lbl_email4 = Label(self.root, text="ayugautam12@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=953, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=580, width=244, height=20)
        lbl_name5 = Label(self.root, text="Himanshu\nKaushal", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=1258, y=200, width=244, height=150)
        lbl_cno5 = Label(self.root, text="8376874442", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=1258, y=390, width=244, height=150)
        lbl_email5 = Label(self.root, text="kaushalhimanshu80@gmail.com", font=(
            "Century Gothic", 11, "bold"), bg="#023047", fg="white").place(x=1258, y=565, width=244, height=90)
        lbl_h1 = Label(self.root, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=425, width=244, height=20)
        lbl_h2 = Label(self.root, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=580, width=244, height=20)

    def contactadmins(self):
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="Contact Admins", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=100)
        lbl_menu = Label(self.root, text="Active Hours: 9 AM to 5 PM | Labs are closed on every Saturday, Sunday and Holidays declared by PU", font=(
            "Century Gothic", 20, "bold"), bg="#457b9d", fg="white").place(x=10, y=110, width=1515, height=50)
        logout_btn = Button(self.root, text="< Back", command=self.studentdash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=40, height=35, width=100)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=160, width=1515, height=535)
        lab1 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=30, y=175, width=250, height=500)
        lab2 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=335, y=175, width=250, height=500)
        lab3 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=645, y=175, width=250, height=500)
        lab4 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=955, y=175, width=250, height=500)
        lab5 = Frame(self.root, bd=3, relief=RIDGE, bg="#023047").place(
            x=1255, y=175, width=250, height=500)
        lbl_name1 = Label(self.root, text="Lab 1:\nOOPS", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=33, y=205, width=244, height=150)
        lbl_labi1 = Label(self.root, text="Honey Singh", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=33, y=335, width=244, height=150)
        lbl_laba11 = Label(self.root, text="J Star", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=33, y=500, width=244, height=30)
        lbl_laba12 = Label(self.root, text="Alfaaz", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=33, y=530, width=244, height=30)
        lbl_cno1 = Label(self.root, text="0172-2541241", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=33, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=33, y=605, width=244, height=20)
        lbl_name2 = Label(self.root, text="Lab 2:\nMultimedia", font=(
            "Century Gothic", 32, "bold"), bg="#023047", fg="white").place(x=338, y=205, width=244, height=150)
        lbl_labi2 = Label(self.root, text="KK", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=338, y=335, width=244, height=150)
        lbl_laba21 = Label(self.root, text="Shaan", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=338, y=500, width=244, height=30)
        lbl_laba22 = Label(self.root, text="Pritam", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=338, y=530, width=244, height=30)
        lbl_cno2 = Label(self.root, text="0172-2541242", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=338, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=338, y=605, width=244, height=20)
        lbl_name3 = Label(self.root, text="Lab 3:\nData\nStructures", font=(
            "Century Gothic", 30, "bold"), bg="#023047", fg="white").place(x=648, y=195, width=244, height=150)
        lbl_labi3 = Label(self.root, text="Shawn Mendes", font=(
            "Century Gothic", 23, "bold"), bg="#023047", fg="white").place(x=648, y=335, width=244, height=150)
        lbl_laba31 = Label(self.root, text="Camila Cabello", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=648, y=500, width=244, height=30)
        lbl_laba32 = Label(self.root, text="Dua Lipa", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=648, y=530, width=244, height=30)
        lbl_cno3 = Label(self.root, text="0172-2541243", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=648, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=648, y=605, width=244, height=20)
        lbl_name4 = Label(self.root, text="Lab 4:\nDatabase", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=958, y=205, width=244, height=150)
        lbl_labi4 = Label(self.root, text="Charlie Puth", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=958, y=335, width=244, height=150)
        lbl_laba41 = Label(self.root, text="DJ Snake", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=958, y=500, width=244, height=30)
        lbl_laba42 = Label(self.root, text="Selena Gomez", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=958, y=530, width=244, height=30)
        lbl_cno4 = Label(self.root, text="0172-2541244", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=958, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=958, y=605, width=244, height=20)
        lbl_name5 = Label(self.root, text="Lab 5:\nSoftware", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=1258, y=205, width=244, height=150)
        lbl_labi5 = Label(self.root, text="Anuv Jain", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=1258, y=335, width=244, height=150)
        lbl_laba51 = Label(self.root, text="Zaeden", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=1258, y=500, width=244, height=30)
        lbl_laba52 = Label(self.root, text="Dikshant", font=(
            "Century Gothic", 20, "bold"), bg="#023047", fg="white").place(x=1258, y=530, width=244, height=30)
        lbl_cno5 = Label(self.root, text="0172-2541245", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=1258, y=625, width=244, height=30)
        lbl_h1 = Label(self.root, text="Lab Incharge:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=370, width=244, height=20)
        lbl_h2 = Label(self.root, text="Lab Assistants:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=475, width=244, height=20)
        lbl_h3 = Label(self.root, text="Telephone:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1258, y=605, width=244, height=20)

    def filecomp(self):
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        self.var_labno = StringVar()
        self.var_sysno = StringVar()
        self.var_comp = StringVar()
        title = Label(self.root, text="File a Complaint", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=150)
        logout_btn = Button(self.root, text="< Back", command=self.studentdash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=65, height=35, width=100)
        lbl_menu = Label(self.root, text="Select the Type of Complaint", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        self.beginfilecomp()

    def beginfilecomp(self):
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="File a Complaint", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=150)
        logout_btn = Button(self.root, text="< Back", command=self.studentdash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=65, height=35, width=100)
        lbl_menu = Label(self.root, text="Select the Type of Complaint", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=483)
        equipbc = LabelFrame(self.root, text="Equipment based Complaint", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=50, y=325, width=650, height=200)
        labbc = LabelFrame(self.root, text="Lab based Complaint", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE).place(x=840, y=325, width=650, height=200)
        filebtneq = Button(self.root, text="File", command=self.equipcomp, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=560, y=425, width=75, height=30)
        filebtnla = Button(self.root, text="File", command=self.labcomp, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=1350, y=425, width=75, height=30)
        equiptext = Label(self.root, text="For complaints like Equipment(Mouse, Keyboard,\n Monitor, CPU) damaged or not working.", compound=LEFT, font=(
            "Century Gothic", 14), anchor="w", padx=20).place(x=60, y=360, width=470, height=150)
        labtext = Label(self.root, text="For complaints like Short Circuit/Electricity issue, Socket\ndamaged or not working, Switch damaged or not working,\nBroken Chair/Seat.", compound=LEFT, font=(
            "Century Gothic", 11), anchor="w", padx=20).place(x=850, y=360, width=475, height=150)

    def equipcomp(self):
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="File a Complaint", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=150)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=483)
        lbl_menu = Label(self.root, text="Enter the Complaint Details", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        comp = Frame(self.root, bd=3, relief=RIDGE, bg="white").place(
            x=375, y=250, width=705, height=400)
        cmb_lab = ttk.Combobox(self.root, textvariable=self.var_labno, values=(
            "1", "2", "3", "4", "5"), state="readonly", justify=CENTER, font=("Century Gothic", 18)).place(x=750, y=300, width=250, height=50)
        cmb_sys = ttk.Combobox(self.root, textvariable=self.var_sysno, values=(
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"), state="readonly", justify=CENTER, font=("Century Gothic", 18)).place(x=750, y=390, width=250, height=50)
        cmb_complaint = ttk.Combobox(self.root, textvariable=self.var_comp, values=(
            "CPU damaged or not working", "Monitor damaged or not working", "Mouse damaged or not working", "Keyboard damaged or not working"), state="readonly", justify=CENTER, font=("Century Gothic", 10)).place(x=750, y=475, width=250, height=50)
        self.var_labno.set("Select")
        self.var_sysno.set("Select")
        self.var_comp.set("Select")
        lbl_lab = Label(self.root, text="Select the Lab Number :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=300, width=300, height=50)
        lbl_sys = Label(self.root, text="Select the System :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=390, width=300, height=50)
        lbl_complaint = Label(self.root, text="Select the Complaint :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=475, width=300, height=50)
        filebtn = Button(self.root, text="File", command=self.addfcomp, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=630, y=575, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearfcomp, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=780, y=575, width=75, height=30)
        back_btn = Button(self.root, text="< Back", command=self.beginfilecomp, font=("Century Gothic", 15, "bold"),
                          bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)
        lbl_instruction = Label(self.root, text=("For OOPS Lab,\nSelect Lab Number:1.\n\nFor Multimedia Lab,\nSelect Lab Number:2.\n\nFor Data Structures Lab,\nSelect Lab Number:3.\n\nFor Database Lab,\nSelect Lab Number:4.\n\nFor Software Lab,\nSelect Lab Number:5."), font=(
            "Century Gothic", 12, "bold"), bg="#a8dadc").place(x=1135, y=250, width=350, height=400)
        lbl_impinst = Label(self.root, text="Important Instruction:", font=(
            "Century Gothic", 20, "bold"), bg="#a8dadc").place(x=1135, y=265, width=350, height=50)

    def labcomp(self):
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="File a Complaint", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=150)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=483)
        lbl_menu = Label(self.root, text="Enter the Complaint Details", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        comp = Frame(self.root, bd=3, relief=RIDGE, bg="white").place(
            x=375, y=250, width=705, height=400)
        cmb_lab = ttk.Combobox(self.root, textvariable=self.var_labno, values=(
            "1", "2", "3", "4", "5"), state="readonly", justify=CENTER, font=("Century Gothic", 18)).place(x=750, y=300, width=250, height=50)
        cmb_sys = ttk.Combobox(self.root, textvariable=self.var_sysno, values=(
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"), state="readonly", justify=CENTER, font=("Century Gothic", 18)).place(x=750, y=390, width=250, height=50)
        cmb_complaint = ttk.Combobox(self.root, textvariable=self.var_comp, values=(
            "Socket damaged or not working", "Wires damaged or not working", "Short Circuit/Electricity issue", "Broken Chair/Seat"), state="readonly", justify=CENTER, font=("Century Gothic", 10)).place(x=750, y=475, width=250, height=50)
        self.var_labno.set("Select")
        self.var_sysno.set("Select")
        self.var_comp.set("Select")
        lbl_lab = Label(self.root, text="Select the Lab Number :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=300, width=300, height=50)
        lbl_sys = Label(self.root, text="Select the System :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=390, width=300, height=50)
        lbl_complaint = Label(self.root, text="Select the Complaint :", font=(
            "Century Gothic", 18, "bold"), bg="white").place(x=450, y=475, width=300, height=50)
        filebtn = Button(self.root, text="File", command=self.addfcomp, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=630, y=575, width=75, height=30)
        clearbtn = Button(self.root, text="Clear", command=self.clearfcomp, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=780, y=575, width=75, height=30)
        back_btn = Button(self.root, text="< Back", command=self.beginfilecomp, font=("Century Gothic", 15, "bold"),
                          bg="#ffd166", cursor="hand2").place(x=35, y=235, height=35, width=100)
        lbl_instruction = Label(self.root, text=("For OOPS Lab,\nSelect Lab Number:1.\n\nFor Multimedia Lab,\nSelect Lab Number:2.\n\nFor Data Structures Lab,\nSelect Lab Number:3.\n\nFor Database Lab,\nSelect Lab Number:4.\n\nFor Software Lab,\nSelect Lab Number:5."), font=(
            "Century Gothic", 12, "bold"), bg="#a8dadc").place(x=1135, y=250, width=350, height=400)
        lbl_impinst = Label(self.root, text="Important Instruction:", font=(
            "Century Gothic", 20, "bold"), bg="#a8dadc").place(x=1135, y=265, width=350, height=50)

    def clearfcomp(self):
        self.var_labno.set("Select")
        self.var_sysno.set("Select")
        self.var_comp.set("Select")

    def addfcomp(self):
        con = sqlite3.connect(database=r'complaint.db')
        cur = con.cursor()
        if self.var_labno.get() == "" or self.var_sysno.get() == "Select" or self.var_comp.get() == "":
            messagebox.showerror(
                "Error", "All fields are mandatory to be filled!", parent=self.root)
        cur.execute("INSERT INTO complaint (labno,sysno,complaint) VALUES(?,?,?)",
                    (self.var_labno.get(), self.var_sysno.get(), self.var_comp.get()))
        con.commit()
        messagebox.showinfo(
            "Thank You!", "Complaint Filed successfully!", parent=self.root)

    def viewsystemstatusmap(self):
        mainframe = Frame(self.root, bd=10, relief=RIDGE).place(
            x=0, y=0, relwidth=1, height=705)
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root, text="View System Status Map", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=10, y=10, width=1515, height=150)
        logout_btn = Button(self.root, text="< Back", command=self.studentdash, font=("Century Gothic", 15, "bold"),
                            bg="#ffd166", cursor="hand2").place(x=1400, y=65, height=35, width=100)
        lbl_menu = Label(self.root, text="Check for each Lab", font=(
            "Century Gothic", 25, "bold"), bg="#457b9d", fg="white").place(x=10, y=160, width=1515, height=50)
        data = Frame(self.root, bd=10, relief=RIDGE).place(
            x=10, y=210, width=1515, height=483)
        self.lbl_admin = Label(self.root, text="Lab 1: OOPS", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=75, y=250, height=100, width=650)
        self.lbl_admin = Label(self.root, text="Lab 2: Multimedia", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=75, y=400, height=100, width=650)
        self.lbl_admin = Label(self.root, text="Lab 3: Data Structures", bg="#023047", fg="white", font=(
            "Century Gothic", 27, "bold"), relief=RIDGE).place(x=75, y=550, height=100, width=650)
        self.lbl_admin = Label(self.root, text="Lab 4: Database", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=800, y=250, height=100, width=650)
        self.lbl_admin = Label(self.root, text="Lab 5: Software", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=800, y=400, height=100, width=650)
        check1 = Button(self.root, text="Check", font=(
            "Century Gothic", 14), command=self.openoops, bg="#ff9f1c", cursor="hand2").place(x=612, y=287, width=75, height=30)
        check2 = Button(self.root, text="Check", font=(
            "Century Gothic", 14), command=self.openmultimedia, bg="#ff9f1c", cursor="hand2").place(x=612, y=437, width=75, height=30)
        check3 = Button(self.root, text="Check", font=(
            "Century Gothic", 14), command=self.opendatastructures, bg="#ff9f1c", cursor="hand2").place(x=612, y=587, width=75, height=30)
        check4 = Button(self.root, text="Check", font=(
            "Century Gothic", 14), command=self.opendatabase, bg="#ff9f1c", cursor="hand2").place(x=1337, y=287, width=75, height=30)
        check5 = Button(self.root, text="Check", font=(
            "Century Gothic", 14), command=self.opensoftware, bg="#ff9f1c", cursor="hand2").place(x=1337, y=437, width=75, height=30)

    def openoops(self):
        f = open("oops.html", "r")
        f.close()
        webbrowser.open_new_tab("oops.html")

    def openmultimedia(self):
        f = open("multimedia.html", "r")
        f.close()
        webbrowser.open_new_tab("multimedia.html")

    def opendatastructures(self):
        f = open("datastructures.html", "r")
        f.close()
        webbrowser.open_new_tab("datastructures.html")

    def opendatabase(self):
        f = open("database.html", "r")
        f.close()
        webbrowser.open_new_tab("database.html")

    def opensoftware(self):
        f = open("software.html", "r")
        f.close()
        webbrowser.open_new_tab("software.html")


obj = LEMS(root)
root.mainloop()
