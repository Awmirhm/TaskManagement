from DataAccessLayer.task_data_access import TaskDataAccess
from datetime import date, datetime


class TaskBusiness:
    def __init__(self):
        self.task_data_access = TaskDataAccess()

    def create_task(self, title, description, start_time, end_time, current_user):
        if len(title) < 4:
            return [None, "Length should be least 4"]
        if len(description) < 6:
            return [None, "Length should be least 4"]
        try:
            start_time_value = datetime.fromisoformat(start_time)
        except:
            return [None, "Invalid Start time for example : 2024-01-01 09:09:00"]
        try:
            end_time_value = datetime.fromisoformat(end_time)
        except:
            return [None, "Invalid End time for example : 2024-01-01 09:09:00"]
        else:
            self.task_data_access.create_task(title, description, start_time_value, end_time_value, current_user.id)
            return [None, None]

    def get_tasks(self, current_user, sort):
        tasks = self.task_data_access.get_tasks(current_user.id)
        if sort == "Status":
            sort_by_status = sorted(tasks, key=lambda status: status.status)
            return sort_by_status
        if sort == "Title":
            sort_by_title = sorted(tasks, key=lambda title: title.title)
            return sort_by_title
        return tasks

    def update_to_done(self, task_id):
        self.task_data_access.update_status(2, task_id)

    def update_to_doing(self, task_id):
        self.task_data_access.update_status(1, task_id)

    def delete_task(self, task_id):
        self.task_data_access.delete_task(task_id)

    def edit_task_information(self, title, description, start_time, end_time, selected_task):
        if title == "" or description == "":
            return [None, "Length should be least 0"]
        if not selected_task:
            return [None, "Please Select task"]
        try:
            start_time_value = datetime.fromisoformat(start_time)
        except:
            return [None, "Invalid Start time for example : 2024-01-01 09:09:00"]
        try:
            end_time_value = datetime.fromisoformat(end_time)
        except:
            return [None, "Invalid End time for example : 2024-01-01 09:09:00"]
        else:
            self.task_data_access.edit_task(title, description, start_time_value, end_time_value, selected_task)
            return ["Your Data Changed", None]

    def get_one_task(self, task_id):
        if not task_id:
            return [None, "Invalid Task"]
        else:
            task = self.task_data_access.get_one_task(task_id)
            return [task, None]
