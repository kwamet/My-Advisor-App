from App.models import Program, Course
from App.database import db


def add_program(self, program_name, description):
    try:
        new_program = Program(name=program_name, description=description)
        db.session.add(new_program)
        db.session.commit()
        return new_program
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while adding the program: {e}")


def remove_program(self, program_name):
    try:
        program = Program.query.filter_by(name=program_name).first()
        if program:
            db.session.delete(program)
            db.session.commit()
        else:
            print(f"Program '{program_name}' not found.")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while removing the program: {e}")


def add_course(self, course_code, course_name, credits):
    try:
        new_course = Course(code=course_code, name=course_name, credits=credits)
        db.session.add(new_course)
        db.session.commit()
        return new_course
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while adding the course: {e}")


def remove_course(self, course_code):
    try:
        course = Course.query.filter_by(code=course_code).first()
        if course:
            db.session.delete(course)
            db.session.commit()
        else:
            print(f"Course '{course_code}' not found.")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred while removing the course: {e}")