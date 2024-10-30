from flask import Blueprint, request, jsonify
from app.models import db, Student, Project

api = Blueprint('api', __name__)

@api.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], email=data['email'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created"}), 201

@api.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(title=data['title'], description=data['description'], student_id=data['student_id'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({"message": "Project created"}), 201