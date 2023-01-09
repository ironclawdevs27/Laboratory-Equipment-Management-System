import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class studentclass:
    def __init__(self, root):
        self.root3 = root
        self.root3.geometry("1550x850+0+0")
        self.root3.title(
            "Laboratory Equipment Management System | Developed by Anavi, Arshia, Aryan, Ayush and Himanshu")
        self.root3.config(bg="white")
        self.root3.focus_force()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.icon_title = PhotoImage(file="default.png")
        title = Label(self.root3, text="Search a Student", image=self.icon_title, compound=LEFT, font=(
            "Century Gothic", 40, "bold"), bg="#023047", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=100)
        searchstudent = LabelFrame(self.root3, text="Search a student", font=(
            "Century Gothic", 20, "bold"), bd=3, relief=RIDGE, bg="white").place(x=450, y=100, width=705, height=100)
        cmb_search = ttk.Combobox(self.root3, textvariable=self.var_searchby, values=(
            "Student ID", "Name", "Department"), state="readonly", justify=CENTER, font=("Century Gothic", 14)).place(x=475, y=150, width=180)
        self.var_searchtxt.set("Enter data to be searched")
        self.var_searchby.set("Select")
        txt_search = Entry(self.root3, textvariable=self.var_searchtxt, font=(
            "Century Gothic", 14), bg="#a8dadc").place(x=680, y=150, width=250)
        searchbtn = Button(self.root3, text="Search", command=self.search, font=(
            "Century Gothic", 14), bg="#ff9f1c", cursor="hand2").place(x=955, y=145, width=75, height=30)
        clearbtn = Button(self.root3, text="Clear", command=self.clear, font=(
            "Century Gothic", 14), bg="#2a9d8f", cursor="hand2").place(x=1055, y=145, width=75, height=30)
        lbl_menu = Label(self.root3, text="Student Details", font=(
            "Century Gothic", 30, "bold"), bg="#457b9d", fg="white")
        lbl_menu.place(x=0, y=210, relwidth=1, height=50)
        preview_frame = Frame(self.root3, bd=10, relief=RIDGE).place(
            x=0, y=260, relwidth=1, height=450)
        scrollver = Scrollbar(self.root3, orient=VERTICAL)
        scrollver.place(x=1500, y=270, height=425, width=20)
        self.studenttable = ttk.Treeview(
            self.root3, columns=("studentid", "name", "dept"), yscrollcommand=scrollver.set)
        self.studenttable.heading("studentid", text="Student ID")
        self.studenttable.heading("name", text="Name")
        self.studenttable.heading("dept", text="Department")
        self.studenttable["show"] = "headings"
        self.studenttable.place(x=10, y=270, width=1490, height=430)
        scrollver.config(command=self.studenttable.yview)
        self.show()
        lbl_footer = Label(self.root3, text="LEMS - Laboratory Equipment Management System\n\nAutomative Simplification of studentistration", font=(
            "Century Gothic", 14), bg="#4d636d", fg="white").place(x=0, y=705, relwidth=1, height=90)
        lbl_clock = Label(self.root3, text="DATE: DD-MM-YYYY\nTIME: HH-MM-SS", font=(
            "Century Gothic", 14, "bold"), bg="#457b9d", fg="white")
        lbl_clock.place(x=1300, y=712, width=200, height=75)

    def show(self):
        con = sqlite3.connect(database=r'student.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        for row in rows:
            self.studenttable.insert('', END, values=row)

    def search(self):
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
        else:
            cur.execute("SELECT * FROM student WHERE "+self.var_searchby.get() +
                        " LIKE '%"+self.var_searchtxt.get()+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                messagebox.showerror(
                    "Error", "No Record found!", parent=self.root3)
            for row in rows:
                self.studenttable.insert('', END, values=row)

    def clear(self):
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.studenttable.delete(*self.studenttable.get_children())
        self.show()


if __name__ == "__main_":
    root3 = Tk()
    obj = studentclass(root3)
    root3.mainloop()
