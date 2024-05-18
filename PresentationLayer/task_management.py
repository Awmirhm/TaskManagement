from ttkbootstrap import Frame, Labelframe, Label, Entry, END, Button, DateEntry, Scrollbar, Treeview, VERTICAL, \
    WARNING, INFO, SUCCESS, PRIMARY, SECONDARY, DARK, DANGER, OUTLINE, LIGHT, Combobox, StringVar, READONLY, \
    Meter
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime
from BusinessLogicLayer.task_business import TaskBusiness
from CommonLayer.task_ststaus_data_type import TaskStatus
from BusinessLogicLayer.user_business import UserBusiness


class TaskManagementFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.task_business = TaskBusiness()

        self.user_business = UserBusiness()

        self.view = view

        self.task_id = None

        self.current_user = None

        self.sort = None

        self.treeview_items = []

        self.grid_columnconfigure(0, weight=1)

        self.header = Labelframe(self, text="Add Task", bootstyle=INFO)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Title
        self.title_label = Label(self.header, text="Title  :")
        self.title_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.title_entry = Entry(self.header, bootstyle=DARK)
        self.title_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Description
        self.description_label = Label(self.header, text="Description  :")
        self.description_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.description_entry = Entry(self.header, bootstyle=DARK)
        self.description_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Start Time
        self.start_time_label = Label(self.header, text="Start Time  :")
        self.start_time_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.start_time_entry = DateEntry(self.header, dateformat="%Y-%m-%d %H:%M:%S", startdate=datetime.now(),
                                          bootstyle=DARK)
        self.start_time_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # End Time (Optional)
        self.end_time_label = Label(self.header, text=" End Time Range  :")
        self.end_time_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.end_time_entry = DateEntry(self.header, dateformat="%Y-%m-%d %H:%M:%S", startdate=datetime.now(),
                                        bootstyle=DARK)
        self.end_time_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Save
        self.save_button = Button(self.header, text="Save", command=self.save_button_clicked,
                                  bootstyle=SECONDARY + OUTLINE)
        self.save_button.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Treeview
        self.treeview_label_frame = Labelframe(self, text="Task Information", bootstyle=PRIMARY)
        self.treeview_label_frame.grid_columnconfigure(0, weight=1)
        self.treeview_label_frame.grid_rowconfigure(1, weight=1)
        self.treeview_label_frame.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Scrollbar
        self.y_scrollbar = Scrollbar(self.treeview_label_frame, orient=VERTICAL)
        self.y_scrollbar.grid(row=1, column=2, padx=(10, 10), pady=(10, 10), sticky="ns")

        self.columns = ["title", "description", "start_time", "end_time", "status"]
        self.table = Treeview(self.treeview_label_frame, columns=self.columns, yscrollcommand=self.y_scrollbar.set,
                              bootstyle=LIGHT)

        self.table.heading("#0", text="NO")
        self.table.heading("title", text="Title")
        self.table.heading("description", text="Description")
        self.table.heading("start_time", text="Start Time")
        self.table.heading("end_time", text="End Time")
        self.table.heading("status", text="Status")

        self.table.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.y_scrollbar.config(command=self.table.yview)

        # Done Button
        self.done_button = Button(self.treeview_label_frame, text="Done", command=self.done_button_clicked,
                                  bootstyle=SUCCESS + OUTLINE)
        self.done_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="e")

        # Doing Button
        self.doing_button = Button(self.treeview_label_frame, text="Doing", command=self.doing_button_clicked,
                                   bootstyle=DANGER + OUTLINE)
        self.doing_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="w")

        # Delete Button
        self.delete_button = Button(self.treeview_label_frame, text="Delete", bootstyle=DANGER + OUTLINE,
                                    command=self.delete_button_clicked)
        self.delete_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="e")

        # Sort
        self.sort_combobox_var = StringVar(value="None")
        self.sort_combobox = Combobox(self.treeview_label_frame, values=["Status", "Title"],
                                      textvariable=self.sort_combobox_var, state=READONLY, bootstyle=DARK)
        self.sort_combobox.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        self.sort_button = Button(self.treeview_label_frame, text="Sort By", command=self.sort_button_clicked,
                                  bootstyle=OUTLINE + INFO)
        self.sort_button.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

        # Edit Task Information Button
        self.edit_task_button = Button(self.treeview_label_frame, text="Edit Task Information",
                                       bootstyle=OUTLINE + WARNING, command=self.edit_task_button_clicked)
        self.edit_task_button.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        # Meter
        self.meter = Meter(self.treeview_label_frame, bootstyle=SUCCESS, subtextstyle=LIGHT, subtext="Task Done!",
                           interactive=True,
                           textright="%",
                           stripethickness=10, metersize=180, amounttotal=100)
        self.meter.grid(row=4, column=0, padx=(10, 10), pady=(10, 10))

        self.meter_button = Button(self.treeview_label_frame, text="Save Meter", command=self.meter_button_clicked,
                                   bootstyle=OUTLINE)
        self.meter_button.grid(row=5, column=0, padx=(10, 10), pady=(10, 10))

        # Back To Home Page
        self.back_to_home_page_button = Button(self, text="Back To Home Page",
                                               command=self.back_to_home_page_button_clicked, bootstyle=WARNING)
        self.back_to_home_page_button.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def load_data(self, current_user):
        for item in self.treeview_items:
            self.table.delete(item)
        self.treeview_items.clear()

        self.current_user = current_user
        tasks = self.task_business.get_tasks(self.current_user, self.sort)
        row_number = 1
        for item in tasks:
            data_task = item.status
            task = TaskStatus(data_task)

            items = self.table.insert("", END, text=str(row_number), iid=item.id, values=(
                item.title,
                item.description,
                item.start_time,
                item.end_time,
                f"{task.name if tasks == TaskStatus.DOING else task.name}"
            ))
            row_number += 1
            self.treeview_items.append(items)

        self.table.column("#0", width=200, anchor="w")
        for column in self.columns:
            self.table.column(column, width=600, anchor="center")

        result = self.user_business.get_meter_size(self.current_user)
        meter_size = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.meter.amountusedvar.set(meter_size)

    def save_button_clicked(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        start_time = self.start_time_entry.entry.get()
        end_time = self.end_time_entry.entry.get()

        result = self.task_business.create_task(title, description, start_time, end_time, self.current_user)
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            self.load_data(self.current_user)
            self.title_entry.delete(0, END)
            self.description_entry.delete(0, END)

    def done_button_clicked(self):
        for task_id in self.table.selection():
            self.task_business.update_to_done(task_id)
        self.load_data(self.current_user)

    def doing_button_clicked(self):
        for task_id in self.table.selection():
            self.task_business.update_to_doing(task_id)
        self.load_data(self.current_user)

    def delete_button_clicked(self):
        for task_id in self.table.selection():
            self.task_business.delete_task(task_id)
        self.load_data(self.current_user)

    def sort_button_clicked(self):
        sort_by = self.sort_combobox_var.get()
        if sort_by == "Status":
            self.sort = sort_by
            self.sort_button.config(text=f"Sort By {self.sort}")
        if sort_by == "Title":
            self.sort = sort_by
            self.sort_button.config(text=f"Sort By {self.sort}")
        self.load_data(self.current_user)

    def meter_button_clicked(self):
        amount = self.meter.amountusedvar.get()
        self.user_business.set_meter_size(amount, self.current_user)

    def edit_task_button_clicked(self):
        task_id_tuple = self.table.selection()
        self.task_id = task_id_tuple

        if not self.task_id or len(self.task_id) > 1:
            Messagebox.show_error(title="Error", message="Please select only one task to edit")
        else:
            edit_task_frame = self.view.switch("edit_task")
            edit_task_frame.set_task_id(self.task_id[0])
            edit_task_frame.set_current_user_for_edit_task(self.current_user)

    def back_to_home_page_button_clicked(self):
        self.view.switch("home")
