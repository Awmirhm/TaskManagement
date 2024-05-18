import sqlite3
from CommonLayer.task import Task


class TaskDataAccess:
    def __init__(self):
        self.data_base_name = "TaskManagement.db"

    def create_task(self, title, description, start_time, end_time, current_user_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
                    INSERT INTO Task (
                             title,
                             description,
                             start_time,
                             end_time,
                             status,
                             user_id
                         )
                         VALUES (
                             ?,
                             ?,
                             ?,
                             ?,
                             ?,
                             ?
                        )""", [title, description, start_time, end_time, 1, current_user_id])
            connection.commit()

    def get_tasks(self, current_user_id):
        tasks = []
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           title,
                           description,
                           start_time,
                           end_time,
                           status,
                           user_id
                    FROM Task
                    WHERE  user_id = ?""", [current_user_id]).fetchall()

            for item in data:
                task = Task.create_with_list(item)
                tasks.append(task)
            return tasks

    def update_status(self, status, task_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE Task
                    SET  status = ?
                    WHERE id = ?""", [status, task_id])
            connection.commit()

    def delete_task(self, task_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM Task
                WHERE id = ?""", [task_id])
            connection.commit()

    def edit_task(self, title, description, start_time, end_time, task_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                    UPDATE Task
                    SET    title = ?,
                           description = ?,
                           start_time = ?,
                           end_time = ?
                    WHERE id = ?""", [title, description, start_time, end_time, task_id])
            connection.commit()

    def get_one_task(self, task_id):
        with sqlite3.connect(self.data_base_name) as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
                    SELECT id,
                           title,
                           description,
                           start_time,
                           end_time,
                           status,
                           user_id
                    FROM Task
                    WHERE  id = ?""", [task_id]).fetchone()
            if data:
                task = Task.create_with_tuple(data)
                return task
            else:
                return None
