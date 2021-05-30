class student:
    'common base class ofr all students'
    student_count = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        student.student_count+=1
    
    def printStudentData(self):
        print("name :", self.name)
        print("id :",self.id)
student1 = student("Muhamad Rafla", 10001)
student2 = student("Muhamad Rafli", 10002)
student3 = student("Muhamad Raflu", 10003)
student4 = student("Muhamad Rafle", 10004)
student5 = student("Muhamad Raflo", 10005)
student1.printStudentData()
student2.printStudentData()
student3.printStudentData()
student4.printStudentData()
student5.printStudentData()
print("Jumlah Student :", student.student_count)
# print(hasattr(student1, "id")) # menampilkan nilai true jika atribute "id" terpakai
# print(getattr(student1, "id")) # menampilkan value dari atribute "id" 
# setattr(student1, "id",104) # untuk merubah atau mengatur atribute pada "id"
# delattr(student1, "id") # untuk menghapusas attribute id

# built-in Class Attribute
print('student.__doc__:', student.__doc__) # Class documentary string or none, if undefined 
print('student.__name__:', student.__name__)# Class name. 
print('student.__bases__:', student.__bases__)# A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list
print('student.__dict__', student.__dict__) # Dictonary containg the class's namespace