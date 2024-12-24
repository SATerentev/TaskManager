from task import Task
import json


class DBController:
    @staticmethod
    def Add(task: Task):
        with open("DB.txt", "a+") as db:
            db.write(task.GetInformation() + "\n")


    @staticmethod
    def GetAll():
        with open("DB.txt", "r+") as db:
            result = []
            for object in db.readlines():
                result.append(object)
            return json.dumps(result)
    

    @staticmethod
    def GetNewID():
        with open("DB.txt", "r+") as db:
            last_task_json = json.loads(db.readlines()[-1])
            return last_task_json["id"] + 1
    

