from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('humanities', 'Humanities'),
    ]

    name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    phone_number = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id_number})"

    class Meta:
        ordering = ['id_number']


class IssuedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='issued_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issued_to')
    quantity = models.IntegerField(default=1)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.student.name}"

    class Meta:
        ordering = ['-issue_date']
