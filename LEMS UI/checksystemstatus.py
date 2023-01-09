import time
import webbrowser
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class checksystem:
    def __init__(self, root):
        self.root8 = root
        self.root8.geometry("1550x850+0+0")
        self.root8.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root8.config(bg="white")
        self.root8.focus_force()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root8, text="Check System Status", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        preview_frame = Frame(self.root8, bd=10, relief=RIDGE).place(
            x=0, y=150, relwidth=1, height=555)
        self.lbl_admin = Label(self.root8, text="Lab 1: OOPS", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=75, y=225, height=100, width=650)
        self.lbl_admin = Label(self.root8, text="Lab 2: Multimedia", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=75, y=375, height=100, width=650)
        self.lbl_admin = Label(self.root8, text="Lab 3: Data Structures", bg="#023047", fg="white", font=(
            "Century Gothic", 27, "bold"), relief=RIDGE).place(x=75, y=525, height=100, width=650)
        self.lbl_admin = Label(self.root8, text="Lab 4: Database", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=800, y=225, height=100, width=650)
        self.lbl_admin = Label(self.root8, text="Lab 5: Software", bg="#023047", fg="white", font=(
            "Century Gothic", 30, "bold"), relief=RIDGE).place(x=800, y=375, height=100, width=650)
        check1 = Button(self.root8, text="Check", font=(
            "Century Gothic", 14),command=self.openoops, bg="#ff9f1c", cursor="hand2").place(x=612, y=262, width=75, height=30)
        check2 = Button(self.root8, text="Check", font=(
            "Century Gothic", 14),command=self.openmultimedia, bg="#ff9f1c", cursor="hand2").place(x=612, y=412, width=75, height=30)
        check3 = Button(self.root8, text="Check", font=(
            "Century Gothic", 14),command=self.opendatastructures, bg="#ff9f1c", cursor="hand2").place(x=612, y=562, width=75, height=30)
        check4 = Button(self.root8, text="Check", font=(
            "Century Gothic", 14),command=self.opendatabase, bg="#ff9f1c", cursor="hand2").place(x=1337, y=262, width=75, height=30)
        check5 = Button(self.root8, text="Check", font=(
            "Century Gothic", 14),command=self.opensoftware, bg="#ff9f1c", cursor="hand2").place(x=1337, y=412, width=75, height=30)
        lbl_menu = Label(self.root8, text="Check for each Lab:", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=100, relwidth=1, height=50)
        lbl_footer = Label(self.root8, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of studentistration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        self.clock()

    def clock(self):
        hh = time.strftime("%H")
        min = time.strftime("%M")
        ss = time.strftime("%S")
        am_pm = time.strftime("%p")
        dd = time.strftime("%d")
        mm = time.strftime("%B")
        yyyy = time.strftime("%Y")
        lbl_clock = Label(self.root8, text=("DATE: "+dd+"-"+mm+"-"+yyyy+"\nTIME: "+hh+":"+min+":"+ss+" "+am_pm), font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=225, height=75)
        lbl_clock.after(1000, self.clock)

    def openoops(self):
        f = open("oops.html","r")
        f.close()
        webbrowser.open_new_tab("oops.html")

    def openmultimedia(self):
        f = open("multimedia.html","r")
        f.close()
        webbrowser.open_new_tab("multimedia.html")

    def opendatastructures(self):
        f = open("datastructures.html","r")
        f.close()
        webbrowser.open_new_tab("datastructures.html")

    def opendatabase(self):
        f = open("database.html","r")
        f.close()
        webbrowser.open_new_tab("database.html")

    def opensoftware(self):
        f = open("software.html","r")
        f.close()
        webbrowser.open_new_tab("software.html")
# if __name__ == "__main_":
root8 = Tk()
obj = checksystem(root8)
root8.mainloop()
