from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from ItemDatabase import ItemsDB
import json


class MyRequestHandler(BaseHTTPRequestHandler):
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control_Allow-Headers", "Content-Type")
        self.end_headers()
        
    def do_DELETE(self):
        print("The PATH is:", self.path)
        if self.path.startswith("/iceboxrewards/"):
            parts = self.path.split("/")
            member_id = parts[2]
            db = ItemsDB()
            db.delete_Member(member_id)
            #check existence of "name" cause or else it will always fail.......
            self.send_response(201)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.handleNotFound()

    def do_GET(self):
        print("The PATH is:", self.path)
        if self.path == "/iceboxrewards":
            self.getAllData()
        elif self.path.startswith("/iceboxrewards/"):
            self.getOneData()
        else:
            self.handleNotFound()          
            # respond 404

    def do_POST(self):
        if self.path == "/iceboxrewards":
            length = self.headers["Content-Length"]
            body = self.rfile.read(int(length)).decode("utf-8")
            print("BODY:", body)
            #
            parsed_body = parse_qs(body)
            print("parsed body", parsed_body)
            #
            name = parsed_body["name"][0]
            email = parsed_body["email"][0]
            phone = parsed_body["phone"][0]
            birthday = parsed_body["birthday"][0]
            zipcode = parsed_body["zipcode"][0]
            level = parsed_body["level"][0]
            # repeat for each item, accessing through keys.
            db = ItemsDB()
            db.insert_Member( name, email, phone, birthday, zipcode, level )
            #check existence of "name" cause or else it will always fail.......
            self.send_response(201)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
        else:
            self.handleNotFound()

    def do_PUT(self):
        if self.path.startswith("/iceboxrewards/"):
            length = self.headers["Content-Length"]
            body = self.rfile.read(int(length)).decode("utf-8")

            parts = self.path.split("/")
            member_id = parts[2]
            if member_id != None:
                db = ItemsDB()
                parsed_body = parse_qs(body)
                name = parsed_body["name"][0]
                email = parsed_body["email"][0]
                phone = parsed_body["phone"][0]
                birthday = parsed_body["birthday"][0]
                zipcode = parsed_body["zipcode"][0]
                level = parsed_body["level"][0]
            
                db.edit_Member( member_id, name, email, phone, birthday, zipcode, level )

                self.send_response(201)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
            else: 
                self.handleNotFound()
        else:
            self.handeNotFound()

    def getAllData(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        # send a body
        db = ItemsDB()
        items = db.get_Members()
        self.wfile.write(bytes(json.dumps(items), "utf-8"))

    def getOneData(self):
        parts = self.path.split("/")
        member_id = parts[2]
        db = ItemsDB()
        selected_member = db.get_one_Member(member_id)
        if selected_member != None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow_Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(selected_member), "utf-8"))
        else:
            self.handleNotFound()

    def handleNotFound(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes("Not found.", "utf-8"))

def run():
    db = ItemsDB()
    db.createTable()
    db = None
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    listen = ("0.0.0.0", port)
    server = HTTPServer(listen, MyRequestHandler)
    print("working")
    server.serve_forever()

    print("If you see this it stopped working..................")

run()


