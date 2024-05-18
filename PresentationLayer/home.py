from ttkbootstrap import Frame, Label, Button, WARNING, INFO, OUTLINE


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Wellcome")
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        # Task Management
        self.task_management_list = Button(self, text="Task Management", command=self.show_task,
                                           bootstyle=OUTLINE + INFO)
        self.task_management_list.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

        # Back To Wellcome Page
        self.back_to_wellcome_page_button = Button(self, text="Back To Wellcome Page",
                                                   command=self.back_to_wellcome_page_button_clicked, bootstyle=WARNING)
        self.back_to_wellcome_page_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def set_current_user(self, current_user):
        self.current_user = current_user
        self.header.config(text=f"Wellcome, {self.current_user.firstname} {self.current_user.lastname}")

    def show_task(self):
        task_management = self.view.switch("task_management")
        task_management.load_data(self.current_user)

    def back_to_wellcome_page_button_clicked(self):
        self.view.switch("wellcome")
