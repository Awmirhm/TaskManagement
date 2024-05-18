from ttkbootstrap import Frame, Labelframe, Label, Entry, Button, END, WARNING, OUTLINE, SUCCESS, DARK, DANGER
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness


class LoginFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.user_business = UserBusiness()

        self.view = view

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Login", bootstyle=DANGER)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Username
        self.username_label = Label(self.header, text="Username  : ")
        self.username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=DARK)
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Password
        self.password_label = Label(self.header, text="Password  : ")
        self.password_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=DARK, show="*")
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Login Button
        self.login_button = Button(self.header, text="Login", command=self.login_button_clicked,
                                   bootstyle=OUTLINE + SUCCESS)
        self.login_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Back To Wellcome Page
        self.back_to_wellcome_page_button = Button(self, text="Back To Wellcome Page",
                                                   command=self.back_to_wellcome_page_button_clicked, bootstyle=WARNING)
        self.back_to_wellcome_page_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business.login(username, password)
        user = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            home_frame = self.view.switch("home")
            home_frame.set_current_user(user)

    def back_to_wellcome_page_button_clicked(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.view.switch("wellcome")
