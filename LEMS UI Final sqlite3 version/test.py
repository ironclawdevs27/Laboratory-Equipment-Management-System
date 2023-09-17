def valid(self):
    con = sqlite3.connect(database=r'login.db')
    cur = con.cursor()
    if self.var_id.get() == "":
        messagebox.showerror(
            "Error", "Please enter your ID!", parent=self.root)
    elif self.var_pass.get() == "":
        messagebox.showerror(
            "Error", "Please enter your Password!", parent=self.root)
