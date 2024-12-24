from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from task import Task
from db_controller import DBController
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/tasks":
            self.send_response(HTTPStatus.OK) # Отправляем статус 200
            self.send_header("Content-type", "application/json") # Указываем в заголовке, что возврат будет в формате json
            self.end_headers()
            json_data = DBController.GetAll() # Упаковываем список json-ов(всех объектов task, которые вернет GetAll()) в один большой json
            self.wfile.write(json_data.encode("utf-8")) # Отправляем клиенту большой список в формате json
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>404 Not Found</h1>")
    

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)

        if self.path == "/tasks":
            try:
                DBController.Add(Task(json.loads(data.decode("utf-8")), DBController.GetNewID()))
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps('{"message":"Task created"}').encode("utf-8"))
            except json.JSONDecodeError:
                self.send_response(HTTPStatus.BAD_REQUEST)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps('{"message":"Invalid data"}').encode("utf-8"))


server = HTTPServer(("localhost", 8000), HTTPRequestHandler)
print("start...")
server.serve_forever()