from django.contrib import admin
from .models import Book, Student, IssuedBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'quantity', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number', 'department', 'phone_number', 'created_at')
    search_fields = ('name', 'id_number', 'phone_number')
    list_filter = ('department', 'created_at')
    ordering = ('id_number',)


@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'quantity', 'issue_date', 'is_returned', 'return_date')
    search_fields = ('book__title', 'student__name', 'student__roll')
    list_filter = ('is_returned', 'issue_date', 'return_date')
    readonly_fields = ('issue_date', 'created_at', 'updated_at')
    ordering = ('-issue_date',)
