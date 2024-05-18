from ttkbootstrap import Frame, Label, Button, OUTLINE, SUCCESS, PRIMARY


class WellcomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = Label(self, text=f"Hi, Wellcome To Task Management Application \n \t Do you Have a Account ? ",
                            font="Courier")
        self.header.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0))

        self.yes_button = Button(self, text="Yes", command=self.yes_button_clicked, bootstyle=OUTLINE + SUCCESS)
        self.yes_button.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="ne", ipadx=10)

        self.no_button = Button(self, text="No", command=self.no_button_clicked, bootstyle=OUTLINE + PRIMARY)
        self.no_button.grid(row=1, column=1, padx=(10, 10), pady=(0, 10), sticky="nw", ipadx=10)

    def yes_button_clicked(self):
        self.view.switch("login")

    def no_button_clicked(self):
        self.view.switch("signin")
