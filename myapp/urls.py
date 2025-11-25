from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # Authentication URLs (Phase 4)
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    
    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
    
    # Issue/Return URLs
    path('issued-books/', views.issued_books_list, name='issued_books_list'),
    path('issued-books/issue/', views.issue_book, name='issue_book'),
    path('issued-books/<int:pk>/return/', views.return_book, name='return_book'),
]
