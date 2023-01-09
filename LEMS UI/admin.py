import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class adminclass:
    def __init__(self, root):
        self.root2 = root
        self.root2.geometry("1550x850+0+0")
        self.root2.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root2.config(bg="white")
        self.root2.focus_force()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_admin_id = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root2, text="Search an Admin", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        searchadmin = LabelFrame(self.root2, text="Search an Admin", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE, bg="white").place(x=450, y=100, width=705, height=100)
        cmb_search = ttk.Combobox(self.root2, textvariable=self.var_searchby, values=(
            "Admin ID", "Name", "Designation"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=475, y=150, width=180)
        self.var_searchtxt.set("Enter data to be searched")
        self.var_searchby.set("Select")
        txt_search = Entry(self.root2, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14), bg="#a8dadc").place(x=680, y=150, width=250)
        searchbtn = Button(self.root2, text="Search", command=self.search, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=955, y=145, width=75, height=30)
        clearbtn = Button(self.root2, text="Clear", command=self.clear, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=1055, y=145, width=75, height=30)
        lbl_menu = Label(self.root2, text="Admin Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=210, relwidth=1, height=50)
        preview_frame = Frame(self.root2, bd=10, relief=RIDGE).place(
            x=0, y=260, relwidth=1, height=445)
        scrollver = Scrollbar(self.root2, orient=VERTICAL)
        scrollver.place(x=1500, y=270, height=425, width=20)
        self.admintable = ttk.Treeview(
            self.root2, columns=("adminid", "name", "desig"), yscrollcommand=scrollver.set)
        self.admintable.heading("adminid", text="Admin ID")
        self.admintable.heading("name", text="Name")
        self.admintable.heading("desig", text="Designation")
        self.admintable["show"] = "headings"
        self.admintable.place(x=10, y=270, width=1490, height=425)
        scrollver.config(command=self.admintable.yview)
        self.show()
        lbl_footer = Label(self.root2, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of Administration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        self.clock()

    def show(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM admin")
        rows = cur.fetchall()
        for row in rows:
            self.admintable.insert('', END, values=row)

    def search(self):
        con = sqlite3.connect(database=r'admin.db')
        cur = con.cursor()
        if self.var_searchby.get() == "Select":
            messagebox.showerror(
                "Error", "Please select a field for searching!", parent=self.root2)
        elif self.var_searchtxt.get() == "":
            messagebox.showerror(
                "Error", "Please enter any parameter to be searched!", parent=self.root2)
        elif self.var_searchby.get() == "Name":
            cur.execute("SELECT * FROM admin WHERE name='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root2)
        elif self.var_searchby.get() == "Admin ID":
            cur.execute("SELECT * FROM admin WHERE adminid='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root2)
        elif self.var_searchby.get() == "Designation":
            cur.execute("SELECT * FROM admin WHERE desig='" +
                        self.var_searchtxt.get()+"'")
            rows = cur.fetchall()
            self.admintable.delete(*self.admintable.get_children())
            for row in rows:
                self.admintable.insert('', END, values=row)
            if len(rows) == 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root2)
        else:
            cur.execute("SELECT * FROM admin WHERE "+self.var_searchby.get() +
                        " LIKE '%"+self.var_searchtxt.get()+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root2)
            for row in rows:
                self.admintable.insert('', END, values=row)

    def clear(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.admintable.delete(*self.admintable.get_children())
        self.show()

    def clock(self):
        hh = time.strftime("%H")
        min = time.strftime("%M")
        ss = time.strftime("%S")
        am_pm = time.strftime("%p")
        dd = time.strftime("%d")
        mm = time.strftime("%B")
        yyyy = time.strftime("%Y")
        lbl_clock = Label(self.root2, text=("DATE: "+dd+"-"+mm+"-"+yyyy+"\nTIME: "+hh+":"+min+":"+ss+" "+am_pm), font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=225, height=75)
        lbl_clock.after(1000, self.clock)

if __name__ == "__main_":
    root2 = Tk()
    obj = adminclass(root2)
    root2.mainloop()
