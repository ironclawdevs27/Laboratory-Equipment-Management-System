import time
from tkinter import *
from PIL import Image, ImageTk


class contactusclass:
    def __init__(self, root):
        self.root6 = root
        self.root6.geometry("1550x850+0+0")
        self.root6.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root6.config(bg="white")
        self.root6.focus_force()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root6, text="Contact Us", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        preview_frame = Frame(self.root6, bd=10, relief=RIDGE).place(
            x=0, y=150, relwidth=1, height=555)
        cus1 = Frame(self.root6, bd=3, relief=RIDGE, bg="#023047").place(
            x=25, y=180, width=250, height=500)
        cus2 = Frame(self.root6, bd=3, relief=RIDGE, bg="#023047").place(
            x=330, y=180, width=250, height=500)
        cus3 = Frame(self.root6, bd=3, relief=RIDGE, bg="#023047").place(
            x=640, y=180, width=250, height=500)
        cus4 = Frame(self.root6, bd=3, relief=RIDGE, bg="#023047").place(
            x=950, y=180, width=250, height=500)
        cus5 = Frame(self.root6, bd=3, relief=RIDGE, bg="#023047").place(
            x=1260, y=180, width=250, height=500)
        lbl_name1 = Label(self.root6, text="Anavi\nSharma", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=28, y=200, width=244, height=150)
        lbl_cno1 = Label(self.root6, text="7889156406", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=28, y=390, width=244, height=150)
        lbl_email1 = Label(self.root6, text="20anavisharma@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=28, y=565, width=244, height=90)
        lbl_h1 = Label(self.root6, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=28, y=425, width=244, height=20)
        lbl_h2 = Label(self.root6, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=28, y=580, width=244, height=20)
        lbl_name2 = Label(self.root6, text="Arshia\nDhiman", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=333, y=200, width=244, height=150)
        lbl_cno2 = Label(self.root6, text="7717494596", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=333, y=390, width=244, height=150)
        lbl_email2 = Label(self.root6, text="arshiadhiman189@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=333, y=565, width=244, height=90)
        lbl_h1 = Label(self.root6, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=425, width=244, height=20)
        lbl_h2 = Label(self.root6, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=333, y=580, width=244, height=20)
        lbl_name3 = Label(self.root6, text="Aryan\nRaj", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=643, y=200, width=244, height=150)
        lbl_cno3 = Label(self.root6, text="7355285828", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=643, y=390, width=244, height=150)
        lbl_email3 = Label(self.root6, text="aryarasin@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=643, y=565, width=244, height=90)
        lbl_h1 = Label(self.root6, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=425, width=244, height=20)
        lbl_h2 = Label(self.root6, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=643, y=580, width=244, height=20)
        lbl_name4 = Label(self.root6, text="Ayush\nGautam", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=953, y=200, width=244, height=150)
        lbl_cno4 = Label(self.root6, text="7831989601", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=953, y=390, width=244, height=150)
        lbl_email4 = Label(self.root6, text="ayugautam12@gmail.com", font=(
            "Century Gothic", 12, "bold"), bg="#023047", fg="white").place(x=953, y=565, width=244, height=90)
        lbl_h1 = Label(self.root6, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=425, width=244, height=20)
        lbl_h2 = Label(self.root6, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=953, y=580, width=244, height=20)
        lbl_name5 = Label(self.root6, text="Himanshu\nKaushal", font=(
            "Century Gothic", 35, "bold"), bg="#023047", fg="white").place(x=1263, y=200, width=244, height=150)
        lbl_cno5 = Label(self.root6, text="8376874442", font=(
            "Century Gothic", 25, "bold"), bg="#023047", fg="white").place(x=1263, y=390, width=244, height=150)
        lbl_email5 = Label(self.root6, text="kaushalhimanshu80@gmail.com", font=(
            "Century Gothic", 11, "bold"), bg="#023047", fg="white").place(x=1263, y=565, width=244, height=90)
        lbl_h1 = Label(self.root6, text="Contact Number:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1263, y=425, width=244, height=20)
        lbl_h2 = Label(self.root6, text="e-mail:", font=(
            "Century Gothic", 10, "bold"), bg="#023047", fg="white").place(x=1263, y=580, width=244, height=20)
        lbl_menu = Label(self.root6, text="LEMS is owned by MoonDancers Pvt. Ltd.", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=100, relwidth=1, height=50)
        lbl_footer = Label(self.root6, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
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
        lbl_clock = Label(self.root6, text=("DATE: "+dd+"-"+mm+"-"+yyyy+"\nTIME: "+hh+":"+min+":"+ss+" "+am_pm), font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=225, height=75)
        lbl_clock.after(1000, self.clock)


if __name__ == "__main_":
    root6 = Tk()
    obj = contactusclass(root6)
    root6.mainloop()
