from django.db import models
from django.utils import timezone
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    class_10_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    class_12_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    degree_name = models.CharField(max_length=255)
    degree_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    opinion = models.TextField()

    def __str__(self):
        return self.name
class TutorApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    class_of_study = models.CharField(max_length=50)
    subjects = models.TextField()
    num_children = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.class_of_study}"
    


class Student(models.Model):
    student_name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.student_name} - {self.roll_no}"

class SubjectResult(models.Model):
    student_result = models.ForeignKey(Student, related_name="subjects", on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    full_marks = models.IntegerField()
    passing_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.subject_name
class Payment(models.Model):
    name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=255,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.student_id} - {self.transaction_id}"
