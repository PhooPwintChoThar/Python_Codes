import ZODB, ZODB.FileStorage
import persistent
import transaction


storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


if __name__ == "__main__":
    # Print all courses
    courses = root.courses
    for course_id in courses:
        course = courses[course_id]
        course.printDetails()
        print()

    # Print all students' transcripts
    students = root.students
    for student_id in students:
        student = students[student_id]
        student.printTranscript()
        print()