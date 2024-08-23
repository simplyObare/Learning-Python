class OnlineCourse:
   def __init__(self, course, instructor):
      self.course = course
      self.instructor = instructor
      self.students = []
      
   def enroll_student(self, name):
      self.students.append(name)
      print(f'{name} has been enrolled in {self.course} course.')
      
   def course_details(self):
      print(f'Course: {self.course}\nInstructor: {self.instructor}\nStudents: {self.students}')
      
   def completed_course(self, name):
      if name in self.students:
         self.students.remove(name)
         print(f'{name} has completed {self.course} course.')
      else:
         print(f'{name} is not enrolled in {self.course} course.')
         
   def avg_grade(self, grades):
      total= sum(grades)
      average = total / len(grades)
      print(f'Course: {self.course}\nAverage Grade: {average}')
      
      
course_input = input('Enter course name: ').lower()
instructor = input('Enter instructor name: ').lower()
student = input('Enter student name: ').lower()

course = OnlineCourse(course_input, instructor)
grades = [90, 85, 95, 80]
course.enroll_student(student)
course.course_details()
course.completed_course(student)
course.avg_grade(grades)