from django.db import models


WEEKDAY = {
    "Monday" : "MONDAY",
    "Tuesday" : "TUESDAY",
    "Wednesday" : "WEDNESDAY",
    "Thrusday" : "THRUSDAY",
    "Friday" : "FRIDAY",
    "Saturday" : "SATURDAY",
    "Sunday" : "SUNDAY",
}

class RegisterStudent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()
    father_first_name = models.CharField(max_length=100)
    father_last_name = models.CharField(max_length=100)
    mother_first_name = models.CharField(max_length=100)
    mother_last_name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nickname} : {self.first_name} {self.last_name}"

class EnrollStudent(models.Model):
    student = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE)
    enroll_date = models.DateField()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    hourly_rate = models.IntegerField()

    def __str__(self):
        return f"Teacher {self.first_name} {self.last_name}"

# It's likes course format.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    course_day = models.CharField(max_length=9, choices=WEEKDAY)
    time_start = models.TimeField()
    time_end = models.TimeField()
    students = models.ManyToManyField(EnrollStudent)
    materials = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Course {self.name}"

class EnrollCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_comment = models.TextField()
    course_date = models.DateField()
    
    def __str__(self):
        return f"enroll course {self.course.name} : {self.course_date}"

class EnrollClass(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(EnrollCourse, blank=True, null=True)

    def __str__(self):
        return f"Class {self.name}"

class StudentComment(models.Model):
    student = models.ForeignKey(EnrollStudent, on_delete=models.CASCADE)
    course = models.ForeignKey(EnrollCourse, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"comment {self.student.student.nickname} : {self.course.course.name}"

