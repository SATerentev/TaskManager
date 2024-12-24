import json


class Task:
    def __init__(self, ID: int, Title: str, Priority: str = "normal"):
        if ID < 0:
            raise ValueError("ID error")
        self.id = ID
        self.title = Title
        self.priority = Priority
        self.isDone = False

    
    def __init__(self, dbstr: dict, ID: int):
        self.title = dbstr["title"]
        self.priority = dbstr["priority"]
        self.isDone = False
        self.id = ID

    
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