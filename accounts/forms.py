from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from course.models import Program
# from .models import User, Student, LEVEL
from .models import *


class StaffAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Foydalanuvchi nomi", )  # Username -> Foydalanuvchi nomi
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Ism", )  # First Name -> Ism
    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Familiya", )  # Last Name -> Familiya
    address = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Manzil", )  # Address -> Manzil
    phone = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Telefon raqami", )  # Mobile No. -> Telefon raqami
    email = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Elektron pochta", )  # Email -> Elektron pochta
    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parol", )  # Password -> Parol
    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parolni tasdiqlash", )  # Password Confirmation -> Parolni tasdiqlash

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.address = self.cleaned_data.get('address')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class StudentAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'username_id'
            }
        ),
        label="Foydalanuvchi nomi", )  # Username -> Foydalanuvchi nomi
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Manzil", )  # Address -> Manzil
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Telefon raqami", )  # Mobile No. -> Telefon raqami
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Ism", )  # First name -> Ism
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Familiya", )  # Last name -> Familiya
    level = forms.CharField(
        widget=forms.Select(
            choices=LEVEL,
            attrs={
                'class': 'browser-default custom-select form-control',
            }
        ),
        label="Kurs", )  # Level -> Kurs
    department = forms.ModelChoiceField(
        queryset=Program.objects.all(),
        widget=forms.Select(attrs={'class': 'browser-default custom-select form-control'}),
        label="Bo'lim", )  # Department -> Bo'lim
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
            }
        ),
        label="Elektron pochta", )  # Email Address -> Elektron pochta
    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parol", )  # Password -> Parol
    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parolni tasdiqlash", )  # Password Confirmation -> Parolni tasdiqlash

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(
            student=user,
            level=self.cleaned_data.get('level'),
            department=self.cleaned_data.get('department')
        )
        student.save()
        return user


class ProfileUpdateForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', }),
        label="Elektron pochta", )  # Email Address -> Elektron pochta
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Ism", )  # First Name -> Ism
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Familiya", )  # Last Name -> Familiya
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Telefon raqami", )  # Phone No. -> Telefon raqami
    address = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control', }),
        label="Manzil / shahar", )  # Address / city -> Manzil / shahar

    class Meta:
        model = User
        fields = ['email', 'phone', 'address', 'picture', 'first_name', 'last_name']


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "Kiritilgan elektron pochta manziliga ro'yxatdan o'tgan foydalanuvchi topilmadi."  # English -> Uzbek
            self.add_error('email', msg)
            return email


class ParentAddForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Foydalanuvchi nomi", )  # Username -> Foydalanuvchi nomi
    address = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Manzil", )  # Address -> Manzil
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Telefon raqami", )  # Mobile No. -> Telefon raqami
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Ism", )  # First name -> Ism
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
            }
        ),
        label="Familiya", )  # Last name -> Familiya
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
            }
        ),
        label="Elektron pochta", )  # Email Address -> Elektron pochta
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.Select(attrs={'class': 'browser-default custom-select form-control'}),
        label="Talaba", )  # Student -> Talaba
    relation_ship = forms.CharField(
        widget=forms.Select(
            choices=RELATION_SHIP,
            attrs={'class': 'browser-default custom-select form-control', }
        ),
        label="Qarindoshlik darajasi", )  # Relation ship -> Qarindoshlik darajasi
    password1 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parol", )  # Password -> Parol
    password2 = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', }),
        label="Parolni tasdiqlash", )  # Password Confirmation -> Parolni tasdiqlash

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.address = self.cleaned_data.get('address')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        parent = Parent.objects.create(
            user=user,
            student=self.cleaned_data.get('student'),
            relation_ship=self.cleaned_data.get('relation_ship')
        )
        parent.save()
        return user