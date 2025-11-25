from django import forms
from django.contrib.auth.models import User
from .models import Book, Student, IssuedBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'quantity']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'required': True
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
                'required': True
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN (13 characters)',
                'maxlength': '13',
                'required': True
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity',
                'min': '0',
                'required': True
            }),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'isbn': 'ISBN',
            'quantity': 'Quantity',
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'id_number', 'department', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name',
                'required': True
            }),
            'id_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ID number',
                'required': True
            }),
            'department': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number (e.g., +1-123-456-7890)',
                'required': True
            }),
        }
        labels = {
            'name': 'Student Name',
            'id_number': 'ID Number',
            'department': 'Department',
            'phone_number': 'Phone Number',
        }


class IssuedBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['student', 'book', 'quantity']
        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'book': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity',
                'min': '1',
                'required': True
            }),
        }
        labels = {
            'student': 'Select Student',
            'book': 'Select Book',
            'quantity': 'Quantity to Issue',
        }

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        quantity = cleaned_data.get('quantity')

        if book and quantity and quantity > book.quantity:
            raise forms.ValidationError(
                f"Not enough books available. Available: {book.quantity}"
            )
        return cleaned_data


class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity to return',
                'min': '1',
                'required': True
            }),
        }
        labels = {
            'quantity': 'Quantity to Return',
        }

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        # quantity validation will be done in the view
        return cleaned_data


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose a username',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter a strong password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'form-control'
        })
    )
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('librarian', 'Librarian')],
        initial='student',
        widget=forms.RadioSelect()
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered. Please use another.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match. Please try again.")
            if len(password1) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long.")

        return cleaned_data
