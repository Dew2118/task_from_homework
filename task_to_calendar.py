from Google import Create_Service
from __pycache__ import extra_byte

class Task:
    def __init__(self):
        client_secret_file = 'client_secret.json'
        api_name = 'tasks'
        api_version = 'v1'
        scopes = ['https://www.googleapis.com/auth/tasks']
        self.service = Create_Service(client_secret_file, api_name, api_version, scopes)

    def get_task_list(self):
        response = self.service.tasklists().list().execute()
        listitems = response.get('items')
        return listitems

    def get_all_tasks(self):
        #only come with incomplete tasks
        response = self.service.tasks().list(tasklist=extra_byte.tasklists).execute()
        items = response.get('items')
        return items

    def create_task(self, title, due, notes):
        status='needsAction'
        deleted = 'False'
        request_body = {
            'title':title,
            'notes':notes,
            'due':due,
            'deleted':deleted,
            'status':status,
        }
        response = self.service.tasks().insert(
            tasklist = extra_byte.tasklists,
            body = request_body
        ).execute()

    def complete_task(self,id):
        print('task_id',id)
        status='completed'
        request_body = {
            'id':id,
            'status':status
        }
        response = self.service.tasks().update(
            task=id,
            tasklist = extra_byte.tasklists,
            body = request_body
        ).execute()
