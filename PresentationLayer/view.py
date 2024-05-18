from .window import Page
from .wellcome_frame import WellcomeFrame
from .sign_in import SignInFrame
from .login import LoginFrame
from .home import HomeFrame
from .task_management import TaskManagementFrame
from .edit_task_information import EditTaskInformationFrame


class MainView:
    def __init__(self):
        self.window = Page()

        self.frames = {}

        self.add_frames("edit_task", EditTaskInformationFrame(self, self.window))
        self.add_frames("task_management", TaskManagementFrame(self, self.window))
        self.add_frames("home", HomeFrame(self, self.window))
        self.add_frames("login", LoginFrame(self, self.window))
        self.add_frames("signin", SignInFrame(self, self.window))
        self.add_frames("wellcome", WellcomeFrame(self, self.window))
        self.window.show()

    def add_frames(self, frame_name, frame):
        self.frames[frame_name] = frame
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]
