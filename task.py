import json


class Task:
    def __init__(self, ID: int, Title: str, Priority: str = "normal"):
        if ID < 0:
            raise ValueError("ID error")
        self.id = ID
        self.title = Title
        self.priority = Priority
        self.isDone = False

    
    def __init__(self, dbstr: str):
        obj = json.loads(dbstr)
        self.id = obj["id"]
        self.title = obj["title"]
        self.priority = obj["priority"]
        self.isDone = obj["isDone"]

    
    def ChangeStatus(self):
        self.isDone = not self.isDone
    

    def GetInformation(self):
        data = {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "isDone": self.isDone
        }

        return json.dumps(data)