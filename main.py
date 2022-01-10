from task_from_homework import Get_homeworks
from task_to_calendar import Task
import pandas as pd

class Main:
    def __init__(self) -> None:
        self.get_homeworks = Get_homeworks()
        self.task = Task()

    def get_tasks(self):
        #return as list
        self.get_homeworks.go_to_homeworks()
        return self.get_homeworks.get_all_homeworks()

    def create_task(self,title,due):
        #create in google calendar
        self.task.create_task(title=title, due=due)

    def check_task(self,hw_titles):
        index_list = []
        req = self.task.get_all_tasks()
        title_list = [dict['title'] for dict in req]
        for i,tuple in enumerate(hw_titles):
            if tuple[1] not in title_list:
                index_list.append(tuple[0])
        return index_list
#test
    def main(self):
        df = self.get_homeworks.get_homeworks(self.check_task(self.get_tasks()))
        for i in range(len(df)):
            self.task.create_task(df['title'][i], df['due'][i], df['notes'][i])
Main().main()