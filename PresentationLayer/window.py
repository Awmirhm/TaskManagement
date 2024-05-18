from ttkbootstrap import Window


class Page(Window):
    def __init__(self, weight=1800, height=1100):
        super().__init__(title="Task Management", themename="cyborg")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.geometry(f"{weight}x{height}")
        self.minsize(width=950, height=750)

    def show(self):
        self.mainloop()
