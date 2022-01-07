from task_from_homework import Zoom_link
from task_to_calendar import Task
import pandas as pd

class Main:
    def __init__(self) -> None:
        self.zoom_link = Zoom_link()
        self.task = Task()

    def get_tasks(self):
        #return as df
        return self.zoom_link.go_to_homeworks()

    def create_task(self,title,due):
        #create in google calendar
        self.task.create_task(title=title, due=due)

    def check_task(self,df):
        df2 = pd.DataFrame(columns = ['title','due','notes'])
        req = self.task.get_all_tasks()
        title_list = [dict['title'] for dict in req]
        for i,title in enumerate(df['title']):
            if title not in title_list:
                df2.loc[i] = df.iloc[i]
        print(df2)
        return df2
#test
    def main(self):
        df = self.check_task(self.get_tasks())
        for i in range(len(df)):
            self.task.create_task(df['title'][i], df['due'][i], df['notes'][i])
Main().main()