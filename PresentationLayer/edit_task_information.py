from ttkbootstrap import Frame, Labelframe, Label, Entry, END, Button, DARK, OUTLINE, SECONDARY, DateEntry, READONLY, \
    INFO, DANGER, SUCCESS, PRIMARY, WARNING
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
from BusinessLogicLayer.task_business import TaskBusiness


class EditTaskInformationFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.task_business = TaskBusiness()

        self.view = view

        self.current_user = None

        self.select_task_id = None

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Edit Task Information", bootstyle=SUCCESS)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # New Title
        self.new_title_label = Label(self.header, text=" New Title  :")
        self.new_title_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.new_title_entry = Entry(self.header, bootstyle=SUCCESS)
        self.new_title_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # New Description
        self.new_description_label = Label(self.header, text=" New Description  : ")
        self.new_description_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_description_entry = Entry(self.header, bootstyle=SUCCESS)
        self.new_description_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # New Start Time
        self.new_start_time_label = Label(self.header, text=" New Start Time  :")
        self.new_start_time_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_start_time_entry = DateEntry(self.header, dateformat="%Y-%m-%d %H:%M:%S",
                                              startdate=datetime.now(),
                                              bootstyle=SUCCESS)
        self.new_start_time_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # New  End Time (Optional)
        self.new_end_time_label = Label(self.header, text=" New End Time Range  :")
        self.new_end_time_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.new_end_time_entry = DateEntry(self.header, dateformat="%Y-%m-%d %H:%M:%S",
                                            startdate=datetime.now(),
                                            bootstyle=SUCCESS)
        self.new_end_time_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Save
        self.new_save_button = Button(self.header, text="Save", command=self.new_save_button_clicked,
                                      bootstyle=PRIMARY + OUTLINE)
        self.new_save_button.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Old Task Information Frame
        self.old_task_frame = Labelframe(self, text="Old Task Information", bootstyle=DANGER)
        self.old_task_frame.grid_columnconfigure(1, weight=1)
        self.old_task_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        # OLd Title
        self.old_title_label = Label(self.old_task_frame, text="Old Title Task  :")
        self.old_title_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.old_title_entry = Entry(self.old_task_frame, bootstyle=DANGER)
        self.old_title_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Old Description
        self.old_description_label = Label(self.old_task_frame, text="Old Description Task  :")
        self.old_description_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.old_description_entry = Entry(self.old_task_frame, bootstyle=DANGER)
        self.old_description_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Old Start Time
        self.old_start_time_label = Label(self.old_task_frame, text="Old Start Time Task  :")
        self.old_start_time_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.old_start_time_entry = Entry(self.old_task_frame, bootstyle=DANGER)
        self.old_start_time_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Old End Time
        self.old_end_time_label = Label(self.old_task_frame, text="Old End Time Task  :")
        self.old_end_time_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.old_end_time_entry = Entry(self.old_task_frame, bootstyle=DANGER)
        self.old_end_time_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Back To Task Management
        self.back_to_task_management_button = Button(self, text="Back To Task Management Page", bootstyle=WARNING,
                                                     command=self.back_to_task_management_button_clicked)
        self.back_to_task_management_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def set_task_id(self, task_id):
        self.select_task_id = task_id
        result = self.task_business.get_one_task(self.select_task_id)
        task = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.old_title_entry.insert(0, task.title)
            self.old_description_entry.insert(0, task.description)
            self.old_start_time_entry.insert(0, task.start_time)
            self.old_end_time_entry.insert(0, task.end_time)

    def set_current_user_for_edit_task(self, current_user):
        self.current_user = current_user

    def new_save_button_clicked(self):
        new_title = self.new_title_entry.get()
        new_description = self.new_description_entry.get()
        new_start_time = self.new_start_time_entry.entry.get()
        new_end_time = self.new_end_time_entry.entry.get()

        result = self.task_business.edit_task_information(new_title, new_description, new_start_time, new_end_time,
                                                          self.select_task_id)

        save_message = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            Messagebox.show_info(title="Info", message=save_message, alert=True)

    def back_to_task_management_button_clicked(self):
        task_management = self.view.switch("task_management")
        task_management.load_data(self.current_user)
        self.old_title_entry.delete(0, END)
        self.old_description_entry.delete(0, END)
        self.old_start_time_entry.delete(0, END)
        self.old_end_time_entry.delete(0, END)
        self.new_title_entry.delete(0, END)
        self.new_description_entry.delete(0, END)
