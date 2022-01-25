
from flask import Flask
from flask_restful import Api, Resource

import json
app = Flask(__name__)
api = Api(app)

version = "v1"


class Home(Resource):
    def get(self):
        home = open("home.json", "r")
        jsonHome = json.load(home)
        return {"home": jsonHome}


class about(Resource):
    def get(self):
        about = open("about.json", "r")
        jsonabout = json.load(about)
        return {"about": jsonabout}


class blog(Resource):
    def get(self):
        home = open("blog.json", "r")
        jsonblog = json.load(blog)
        return {"blog": jsonblog}


class course(Resource):
    def get(self):
        course = open("course.json", "r")
        jsoncourse = json.load(course)
        return {"course": jsoncourse}


class staff(Resource):
    def get(self):
        staff = open("staff.json", "r")
        jsonstaff = json.load(staff)
        return {"staff": jsonstaff}


class contact(Resource):
    def get(self):
        home = open("contact.json", "r")
        jsoncontact = json.load(contact)
        return {"contact": jsoncontact}


api.add_resource(Home, f'/{version}/home/')
api.add_resource(about, f'/{version}/about/')
api.add_resource(blog, f'/{version}/blog/')
api.add_resource(course, f'/{version}/course/')
api.add_resource(staff, f'/{version}/staff/')
api.add_resource(contact, f'/{version}/contact/')


if __name__ == '__main__':
    app.run()
