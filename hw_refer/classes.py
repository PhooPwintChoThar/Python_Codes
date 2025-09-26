import persistent

class Course (persistent.Persistent):
    def __init__(self, id=0, name="", credit=0):
        self.id=id
        self.name=name
        self.credit=credit

    
    def printDetails(self):
        print(f"ID: {self.id}, Course Nmae : {self.name},Credit {self.credit}")
    
    def getCredit(self):
        return self.credit
    
    def setName(self, name):
        self.name=name



class Student (persistent.Persistent):
    def __init__(self, id=0, name=""):
        self.id=id
        self.name=name
        self.enrolls=[]

    def enrollCourse(self, course):
        enrolled=Enrollment(course,  self)
        self.enrolls.append(enrolled)

        #return enrolled.printDetail()
    
    def getEnrollment(self, course):
        for e in self.enrolls:
            if e.getCourse() == course:
                return  e
        return None

    def printTranscript(self):
        print("\n\t\tTranscript")
        t_credit=0
        t_gpa=0
        for e in self.enrolls:
            course=e.getCourse()
            credit=course.getCredit()
            print(f"{course.name}\t{course.getCredit()}\t{e.getGrade()}")
            t_credit+=credit
            grade=e.getGrade()
            if( grade == 'A') :
                t_gpa+=4*credit
            elif(grade == 'B+'):
                t_gpa+=3.5*credit
            elif(grade == 'B'):
                t_gpa+=3*credit
            elif(grade == 'C+'):
                t_gpa+=2.5*credit
            elif(grade == 'C'):
                t_gpa+=2*credit
            elif(grade == 'D+'):
                t_gpa+=1.5*credit
            elif(grade == 'D'):
                t_gpa+=1*credit

        gpa=t_gpa/t_credit
        print(f"GPA : {gpa}")

    def setName(self, name):
        self.name=name

    

class Enrollment (persistent.Persistent):
    def __init__ (self, course=Course(),  student=Student() ):
        self.course=course
        self.grade="B"
        self.student=student

    def __str__(self):
        return f"{self.course.id}\t{self.course.name}\t{self.course.getCredit()}\t{self.grade}"

    def getCourse(self):
        return self.course
    
    def getGrade(self):
        return self.grade
    
    def setGrade(self, grade):
        self.grade=grade

    def printDetail(self):
        print(f"\n\n{self.student.name}'s Enrollment :")
        print(f"ID:\t{self.course.id}\tCourse:{self.course.name}\tCredit {self.course.getCredit()}\tGrade:{self.grade}")

            

python=Course(1, "python", 4)
math=Course(2, "Math", 3)
rust=Course(3, "Rust", 4)
python.printDetails()
math.printDetails()
rust.printDetails()
student1=Student( 1, "Thar")
print(student1.getEnrollment(rust))
student1.enrollCourse(rust)
print(student1.getEnrollment(rust))
student1.printTranscript()

oop=Course(4, "OOP", 4)
