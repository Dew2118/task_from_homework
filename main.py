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

    def check_task_not_in_calendar(self,hw_titles):
        print('hw',hw_titles)
        index_list = []
        req = self.task.get_all_tasks()
        if req != None:
            title_list = [dict['title'] for dict in req]
        else:
            title_list = []
        print('task',title_list)
        for i,tuple in enumerate(hw_titles):
            if tuple[1] not in title_list:
                index_list.append(tuple[0])
            
        return index_list

    def check_task_done(self,hw_title_list):
        req = self.task.get_all_tasks()
        if req != None:
            title_list = [dict['title'] for dict in req]
        else:
            title_list = []
        return list(set(title_list)-set(hw_title_list))

    def get_attribute_of_dict_list(self,dict_list, index):
        return [dict[index] for dict in dict_list]

    def main(self):
        hw_tuple, hw_list = self.get_tasks()
        all_tasks = self.task.get_all_tasks()
        df = self.get_homeworks.get_homeworks(self.check_task_not_in_calendar(hw_tuple))
        for i in range(len(df)):
            self.task.create_task(df['title'][i], df['due'][i], df['notes'][i])

        task_id_dict = dict(zip(self.get_attribute_of_dict_list(all_tasks,'title'),self.get_attribute_of_dict_list(all_tasks,'id')))
        for hw in self.check_task_done(hw_list):
            if hw == '' or hw[-11:] != '[automated]':
                continue
            self.task.complete_task(task_id_dict[hw])

        
Main().main()