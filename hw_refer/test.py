import ZODB, ZODB.FileStorage
import persistent
import transaction
from z_enrollment import *
import BTrees._OOBTree

# Open the database storage
storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

# Ensure that courses and students are initialized as BTrees
if 'courses' not in root:
    root.courses = BTrees.OOBTree.BTree()
if 'students' not in root:
    root.students = BTrees.OOBTree.BTree()

# Create Course objects
python = Course(1, "Python", 4)
math = Course(2, "Math", 3)
rust = Course(3, "Rust", 4)

# Store Course objects in the courses BTree
root.courses[1] = python
root.courses[2] = math
root.courses[3] = rust

# Create Student objects
student1 = Student(1, "Thar")
student2 = Student(2, "Mhar")

# Store Student objects in the students BTree
root.students[1] = student1
root.students[2] = student2

student1.enrollCourse(rust)
student2.enrollCourse(math)
student2.enrollCourse(rust)

# Commit the changes to the database
transaction.commit()


# Close the database connection
connection.close()
