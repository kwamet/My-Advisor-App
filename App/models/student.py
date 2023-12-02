from App.models import User  
from App.database import db

class Student(User):
    id = db.Column(db.String(10), db.ForeignKey('user.id'), primary_key=True)
    name = db.Column(db.String(50))
    programme = db.Column(db.ForeignKey('programme.id'))
    courseHistory = db.relationship('Course', backref='student', lazy=True, uselist=True)
    coursePlan = db.relationship('Course', backref='student', lazy=True, uselist=True)
    
    """
    program_id = db.Column(db.ForeignKey('program.id'))
    associated_program = db.relationship('Program', back_populates='students', overlaps="program")
    courses = db.relationship('StudentCourseHistory', backref='student', lazy=True)
    """

    def __init__(self, username, password, name, programme, courseHistory, coursePlan):
        super().__init__(username, password)
        self.id = username
        self.name = name
        self.programme = programme
        self.courseHistory = courseHistory
        self.coursePlan = coursePlan

    def get_json(self):
        return{'student_id': self.id,
            'name': self.name,
            'programme' : self.programme,
            'courseHistory' : self.courseHistory,
            'coursePlan' : self.coursePlan
        }
