class Student:
  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(students):
  """Sorts the list of students based on their CGPA in descending order.

  Args:
    students: A list of Student objects.

  Returns:
    A list of Student objects sorted by CGPA in descending order.
  """

  students.sort(key=lambda student: student.cgpa, reverse=True)
  return students

# Test the function with different input lists of students.

students1 = [
    Student("Luffy", "1", 9.5),
    Student("Nanika", "2", 9.0),
    Student("Issac", "3", 8.5),
]

students2 = [
    Student("David", "4", 8.0),
    Student("Eve", "5", 7.5),
    Student("Frank", "6", 7.0),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Sorted students 1:")
for student in sorted_students1:
  print(f"{student.name} ({student.roll_number}): {student.cgpa}")
print("Sorted students 2:")
for student in sorted_students2:
  print(f"{student.name} ({student.roll_number}): {student.cgpa}")