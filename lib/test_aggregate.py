from enrollment import Student, Course, Enrollment
from datetime import datetime

# Create instances
student1 = Student("Alice")
student2 = Student("Bob")
course1 = Course("Math")
course2 = Course("Science")

# Enroll
student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

# Test course_count
print("Student1 course count:", student1.course_count())  # Should be 2
print("Student2 course count:", student2.course_count())  # Should be 1

# Test aggregate_enrollments_per_day
enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
print("Enrollments per day:", enrollments_per_day)

# Set grades
enrollment1 = student1.get_enrollments()[0]
enrollment2 = student1.get_enrollments()[1]
student1.set_grade(enrollment1, 90)
student1.set_grade(enrollment2, 85)

# Test average grade
print("Student1 average grade:", student1.aggregate_average_grade())  # Should be 87.5

print("All tests passed!")
