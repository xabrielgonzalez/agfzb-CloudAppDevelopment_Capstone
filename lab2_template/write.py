# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


def write_instructors():
    # Add instructors
    # Create a user
    user_john = User(first_name='John', last_name='Doe', dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()
    
    # Add Yan's instructor record
    user_yan = User(first_name='Yan', last_name='Luo', dob=date(1962, 7, 16))
    user_yan.save()
    instructor_yan = Instructor(full_time=True, total_learners=30050)
    instructor_yan.user = user_yan
    instructor_yan.save()

    # Add Joy's instructor record
    user_joy = User(first_name='Joy', last_name='Li', dob=date(1992, 1, 2))
    user_joy.save()
    instructor_joy = Instructor(full_time=False, total_learners=10040)
    instructor_joy.user = user_joy
    instructor_joy.save()

    # Add Peter's instructor record
    user_peter = User(first_name='Peter', last_name='Chen', dob=date(1982, 5, 2))
    user_peter.save()
    instructor_peter = Instructor(full_time=True, total_learners=2002)
    instructor_peter.user = user_peter
    instructor_peter.save()
    print("Instructor objects all saved... ")


def write_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()

    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()

    # Add more courses
    course_web_dev = Course(name="Web Development with Django",
                            description="Learn web development with Django framework")
    course_web_dev.save()

    course_java = Course(name="Java Programming",
                         description="Learn Java programming basics and advanced topics")
    course_java.save()

    course_data_science = Course(name="Data Science with Python",
                                 description="Learn data science concepts and tools with Python")
    course_data_science.save()

    print("Course objects all saved... ")


def write_lessons():
    # Add lessons
    lesson1 = Lesson(title='Lesson 1', content="Object-relational mapping project")
    lesson1.save()
    lesson2 = Lesson(title='Lesson 2', content="Django full stack project")
    lesson2.save()
    print("Lesson objects all saved... ")

def clean_data():
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()
    User.objects.all().delete()
    Learner.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Lesson.objects.all().delete()


    # Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()



def write_learners():
    # Add Learners
    learner_james = Learner(first_name='James', last_name='Smith', dob=date(1982, 7, 16),
                            occupation='data_scientist',
                            social_link='https://www.linkedin.com/james/')
    learner_james.save()
    learner_mary = Learner(first_name='Mary', last_name='Smith', dob=date(1991, 6, 12), occupation='dba',
                           social_link='https://www.facebook.com/mary/')
    learner_mary.save()
    learner_robert = Learner(first_name='Robert', last_name='Lee', dob=date(1999, 1, 2), occupation='student',
                             social_link='https://www.facebook.com/robert/')
    learner_robert.save()
    learner_david = Learner(first_name='David', last_name='Smith', dob=date(1983, 7, 16),
                            occupation='developer',
                            social_link='https://www.linkedin.com/david/')
    learner_david.save()
    learner_john = Learner(first_name='John', last_name='Smith', dob=date(1986, 3, 16),
                           occupation='developer',
                           social_link='https://www.linkedin.com/john/')
    learner_john.save()
    print("Learner objects all saved... ")
    
    # Add more learners
    learner_jane = Learner(first_name='Jane', last_name='Doe', dob=date(1995, 10, 1),
                           occupation='student',
                           social_link='https://www.linkedin.com/jane/')
    learner_jane.save()
    learner_peter = Learner(first_name='Peter', last_name='Wang', dob=date(1990, 5, 12),
                            occupation='web_developer',
                            social_link='https://www.linkedin.com/peter/')
    learner_peter.save()
    
    print("More learner objects added... ")

    # Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()


