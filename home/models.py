from django.db import models

# Create your models here.
class Permissions(models.Model):
    #faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    RNO = models.CharField(max_length=10)
    SName = models.CharField (max_length=122)
    Reason = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('denied', 'Denied')])
    
    def __str__(self):
        return f"{self.RNO} - {self.status}"

class Student(models.Model):
    RNO = models.CharField(max_length=10)
    SName = models.CharField (max_length=122)
    Year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.RNO

class Faculty(models.Model):
    faculty_id = models.CharField(max_length=10, unique=True)
    Name = models.CharField (max_length=122)
    Year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.Name