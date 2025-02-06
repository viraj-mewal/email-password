from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pickle
import pyperclip as pc

email_password = {}


def check_files():
    try:
        with open("email_password.dat", "rb") as f:
            email_password = pickle.load(f)
    except:
        with open("email_password.dat", "wb") as f:
            pickle.dump(dict(), f)
            email_password = dict()
    return email_password


email_password = check_files()


class set_password:
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="black")
        self.win.resizable(False, False)
        self.win.title("Email and Password - Set password")
        self.width = 500
        self.height = 200
        self.x, self.y = 500, 200
        self.win.geometry("500x200")
        self.win.geometry(
            str(self.width)
            + "x"
            + str(self.height)
            + "+"
            + str(self.x)
            + "+"
            + str(self.y)
        )
        self.draw()
        self.win.bind("<Return>", self.check)
        self.win.mainloop()

    def check(self, event=None):
        self.password_value = self.password_input.get()
        self.confirm_value = self.confirm_password_input.get()

        if self.password_value == self.confirm_value:
            with open("password.dat", "wb") as f:
                pickle.dump(self.password_value, f)
            messagebox.showinfo("Info", "Password Setted !")
            self.win.destroy()
        else:
            messagebox.showinfo(
                "Info", "Confirm password does not match to password ! Please try again"
            )
            self.win.destroy()
            self.new_window = set_password()

    def draw(self):
        # enter password

        self.password_enter_label = Label(
            self.win,
            text="Password :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.password_enter_label.place(x=10, y=10)

        self.var = StringVar()
        self.password_input = Entry(
            self.win,
            textvariable=self.var,
            font=("Comic Sans MS", 25, "bold"),
            width=14,
            show="*",
        )
        self.password_input.place(x=210, y=20)

        # enter password

        self.confirm_password_label = Label(
            self.win,
            text="Confirm :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.confirm_password_label.place(x=10, y=80)

        self.var1 = StringVar()
        self.confirm_password_input = Entry(
            self.win,
            textvariable=self.var1,
            show="*",
            font=("Comic Sans MS", 25, "bold"),
            width=14,
        )
        self.confirm_password_input.place(x=210, y=90)

        self.set_button = Button(
            self.win,
            text="Set Password",
            font=("Comic Sans MS", 14, "bold"),
            activebackground="pink",
            fg="black",
            bg="yellow",
            command=self.check,
        )
        self.set_button.place(x=self.width // 2 - 55, y=self.height - 55)


class add_win:
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="black")
        self.win.resizable(False, False)
        self.win.title("Email and Password - Add")
        self.width = 500
        self.height = 200
        self.x, self.y = 500, 200
        self.win.geometry("500x200")
        self.win.geometry(
            str(self.width)
            + "x"
            + str(self.height)
            + "+"
            + str(self.x)
            + "+"
            + str(self.y)
        )
        self.draw()
        self.win.bind("<Return>", self.add_details)
        self.win.mainloop()

    def check_show_value(self):
        self.show_value = self.checkbutton_var.get()
        print(self.show_value)
        if self.show_value == 0:
            self.password_input.config(show="")
            self.checkbutton_var.set(1)
        elif self.show_value == 1:
            self.password_input.config(show="*")
            self.checkbutton_var.set(0)

    def add_details(self, event=None):
        self.email = self.email_input.get()
        self.password = self.password_input.get()

        if self.email.isdigit():
            messagebox.showerror("Error", "Please enter an email")

        elif not ("@" in self.email):
            messagebox.showerror("Error", "Email should contain '@'")

        else:
            email_password[self.email] = self.password
            with open("email_password.dat", "wb") as f:
                pickle.dump(email_password, f)

            messagebox.showinfo("Info", "Added successfully")

    def draw(self):
        # enter mail

        self.email_enter_label = Label(
            self.win,
            text="Enter email :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.email_enter_label.place(x=10, y=10)

        self.var = StringVar()
        self.email_input = Entry(
            self.win, textvariable=self.var, font=("Serif", 25, "bold"), width=13
        )
        self.email_input.place(x=250, y=20)

        # enter password

        self.password_enter_label = Label(
            self.win,
            text="Password :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.password_enter_label.place(x=10, y=80)

        self.password_var = StringVar()
        self.password_input = Entry(
            self.win,
            textvariable=self.password_var,
            show="*",
            font=("Serif", 25, "bold"),
            width=10,
        )
        self.password_input.place(x=210, y=90)

        # show checkbutton

        self.checkbutton_var = IntVar()
        self.checkbutton = Checkbutton(
            self.win,
            text="Show",
            variable=self.checkbutton_var,
            onvalue=1,
            offvalue=0,
            font=("Comic Sans MS", 15, "bold"),
            command=self.check_show_value,
        )
        self.checkbutton.place(x=400, y=90)

        # add button

        self.add_button = Button(
            self.win,
            text="Add",
            bg="orange",
            fg="white",
            font=("Comic Sans MS", 17, "bold"),
            command=self.add_details,
        )
        self.add_button.place(x=self.width // 2 - 10, y=self.height - 60)


class open_win:
    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="black")
        self.win.resizable(False, False)
        self.win.title("Email and Password - Open")
        self.width = 500
        self.height = 200
        self.x, self.y = 500, 200
        self.win.geometry("500x200")
        self.win.geometry(
            str(self.width)
            + "x"
            + str(self.height)
            + "+"
            + str(self.x)
            + "+"
            + str(self.y)
        )
        self.draw()
        self.win.bind("<Return>", self.show_password)
        self.win.mainloop()

    def show_password(self, even=None):
        self.email = self.email_input.get()
        try:
            self.password_show.insert(END, email_password[self.email])
        except:
            messagebox.showinfo("Info", f"No email added named :- {self.email}")

    def copy_password(self):
        self.copy_text = self.password_show.get("1.0", END)
        pc.copy(self.copy_text)
        messagebox.showinfo("Info", "Copied")

    def draw(self):

        self.email_input_label = Label(
            self.win,
            text="Enter email :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.email_input_label.place(x=10, y=10)

        self.var = StringVar()
        self.email_input = Entry(
            self.win,
            textvariable=self.var,
            font=("Comic Sans MS", 25, "bold"),
            width=10,
        )
        self.email_input.place(x=250, y=20)

        # Password_show label

        self.password_show_label = Label(
            self.win,
            text="Password :-",
            font=("Comic Sans MS", 25, "bold"),
            bg="black",
            fg="white",
        )
        self.password_show_label.place(x=10, y=80)

        # password_show

        self.password_show = Text(
            self.win, width=10, height=1, font=("Comic Sans MS", 22, "bold")
        )
        self.password_show.place(x=220, y=80)

        # Copy button

        self.copy_button = Button(
            self.win,
            text="Copy",
            bg="pink",
            fg="white",
            font=("Comic Sans MS", 15, "bold"),
            activebackground="light green",
            command=self.copy_password,
        )
        self.copy_button.place(x=self.width - 80, y=self.height - 120)

        # Show button

        self.show_button = Button(
            self.win,
            text="Show",
            bg="orange",
            fg="white",
            font=("Comic Sans MS", 17, "bold"),
            command=self.show_password,
        )
        self.show_button.place(x=self.width // 2 - 10, y=self.height - 60)


class password:
    def __init__(self, user_class):
        self.user_class = user_class
        self.boolean = self.get_password()
        if self.boolean:
            self.win = Tk()
            self.win.configure(bg="black")
            self.win.resizable(False, False)
            self.win.title("Email and Password - Open")
            self.width = 500
            self.height = 200
            self.x, self.y = 500, 200
            self.win.geometry("500x200")
            self.win.geometry(
                str(self.width)
                + "x"
                + str(self.height)
                + "+"
                + str(self.x)
                + "+"
                + str(self.y)
            )
            self.draw()
            self.win.bind("<Return>", self.check)
            self.win.mainloop()
        else:
            pass

    def get_password(self):
        try:
            with open("password.dat", "rb") as f:
                self.password = pickle.load(f)
                return True
        except:
            self.new_window = set_password()

    def check(self, event=None):
        with open("password.dat", "rb") as f:
            self.password = pickle.load(f)

        self.user_password = self.input.get()
        if not (self.user_password):
            messagebox.showinfo("Info", "Enter some password")
        elif self.user_password == self.password:
            self.win.destroy()
            self.new_window = self.user_class()
        elif self.user_password != self.password:
            messagebox.showinfo("Info", "Wrong password !")

    def draw(self):
        # enter password entry and label

        # -> Label

        self.enter_password = Label(
            self.win,
            text="Enter password :-",
            bg="black",
            fg="white",
            font=("Comic Sans MS", 25, "bold"),
        )
        self.enter_password.place(x=self.width // 2 - 230, y=self.height // 2 - 90)

        self.var = StringVar()
        self.input = Entry(
            self.win,
            textvariable=self.var,
            width=7,
            font=("Helvetica", 25, "bold"),
            show="*",
        )
        self.input.place(x=self.width // 2 + 80, y=self.height // 2 - 80)

        # check - button

        self.check_button = Button(
            self.win,
            text="Check",
            activebackground="aqua",
            font=("Comic Sans MS", 20, "bold"),
            bg="orange",
            fg="white",
            command=self.check,
        )
        self.check_button.place(x=self.width // 2 - 60, y=self.height - 100)


class window:
    def __init__(self):
        self.win = Tk()
        self.width = 500
        self.height = 200
        self.x, self.y = 500, 200
        self.win.geometry(
            str(self.width)
            + "x"
            + str(self.height)
            + "+"
            + str(self.x)
            + "+"
            + str(self.y)
        )
        self.win.title("Email and Password")
        self.win.configure(bg="black")
        self.win.resizable(False, False)
        self.draw()
        self.win.mainloop()

    def open(self):
        # self.win.destroy()
        try:
            with open("password.dat", "rb") as f:
                self.data = pickle.load(f)
        except:
            with open("password.dat", "wb"):
                pass

        self.open_win_screen = password(open_win)

    def add(self):
        self.new_window = password(add_win)

    def exit(self):
        self.confirm = messagebox.askyesno(
            "Confirmation", "Do you really want to exit !"
        )
        if self.confirm == True:
            self.win.destroy()

    def info(self):
        messagebox.showinfo(
            "Info",
            """This is an software where you can store your email and their
passwords with encryption and high security of .dat file extension

Developed by :- Viraj Mewal""",
        )

    def reset(self):
        self.confirm = messagebox.askyesno(
            "Sure",
            "Do you really want to Reset software !\n(All your data will be cleared)",
        )
        if self.confirm == True:
            with open("email_password.dat", "wb") as f:
                pass
            with open("password.dat", "wb") as f:
                pass
            messagebox.showinfo("Info", "Software Reseted !")

    def draw(self):
        # Heading

        self.heading = Label(
            self.win,
            text="Email and Password",
            bg="black",
            fg="white",
            font=("Comic Sans MS", 20, "bold"),
        )
        self.heading.place(x=self.width // 2 - 140, y=10)

        # buttons

        # -> add button

        self.add = Button(
            self.win,
            text="Add",
            bg="light green",
            fg="white",
            activebackground="pink",
            font=("Comic Sans MS", 20, "bold"),
            command=self.add,
        )
        self.add.place(x=50, y=self.height // 2 - 10)

        # -> open button

        self.open = Button(
            self.win,
            text="Open",
            bg="light blue",
            fg="white",
            activebackground="pink",
            font=("Comic Sans MS", 20, "bold"),
            command=self.open,
        )
        self.open.place(x=self.width // 2 - 50, y=self.height // 2 - 10)

        self.exit = Button(
            self.win,
            text="Exit",
            bg="red",
            fg="white",
            activebackground="pink",
            font=("Comic Sans MS", 20, "bold"),
            command=self.exit,
        )
        self.exit.place(x=self.width - 130, y=self.height // 2 - 10)

        self.info_button = Button(
            self.win,
            text="Info",
            bg="aqua",
            fg="white",
            activebackground="purple",
            font=("Comic Sans MS", 12, "bold"),
            command=self.info,
        )
        self.info_button.place(x=self.width - 110, y=5)

        self.reset_button = Button(
            self.win,
            text="Reset",
            bg="pink",
            fg="white",
            activebackground="gold",
            font=("Comic Sans MS", 12, "bold"),
            command=self.reset,
        )
        self.reset_button.place(x=self.width - 60, y=5)


if __name__ == "__main__":
    win = window()
