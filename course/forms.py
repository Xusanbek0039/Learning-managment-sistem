from django import forms
from django.db import transaction
from django.conf import settings
from django.contrib.auth.models import User

from accounts.models import User
from .models import Program, Course, CourseAllocation, Upload, UploadVideo

# User = settings.AUTH_USER_MODEL

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})

        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['title'].label = "Yo'nalish nomi"
        self.fields['summary'].label = "Qisqacha mazmuni"


class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        self.fields['credit'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['program'].widget.attrs.update({'class': 'form-control'})
        self.fields['level'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['semester'].widget.attrs.update({'class': 'form-control'})

        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['title'].label = "Kurs nomi"
        self.fields['code'].label = "Kurs kodi"
        self.fields['credit'].label = "Kredit miqdori"
        self.fields['summary'].label = "Qisqacha mazmuni"
        self.fields['program'].label = "Yo'nalish"
        self.fields['level'].label = "Bosqich"
        self.fields['year'].label = "Yil"
        self.fields['semester'].label = "Semestr"


class CourseAllocationForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all().order_by('level'),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'browser-default checkbox'}),
        required=True
    )
    lecturer = forms.ModelChoiceField(
        queryset=User.objects.filter(is_lecturer=True),
        widget=forms.Select(attrs={'class': 'browser-default custom-select'}),
        label="O'qituvchi",  # O'zbek tiliga o'zgartirildi
    )

    class Meta:
        model = CourseAllocation
        fields = ['lecturer', 'courses']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CourseAllocationForm, self).__init__(*args, **kwargs)
        self.fields['lecturer'].queryset = User.objects.filter(is_lecturer=True)


class EditCourseAllocationForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all().order_by('level'),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    lecturer = forms.ModelChoiceField(
        queryset=User.objects.filter(is_lecturer=True),
        widget=forms.Select(attrs={'class': 'browser-default custom-select'}),
        label="O'qituvchi",  # O'zbek tiliga o'zgartirildi
    )

    class Meta:
        model = CourseAllocation
        fields = ['lecturer', 'courses']

    def __init__(self, *args, **kwargs):
        super(EditCourseAllocationForm, self).__init__(*args, **kwargs)
        self.fields['lecturer'].queryset = User.objects.filter(is_lecturer=True)


# Fayllarni kursga yuklash
class UploadFormFile(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('title', 'file', 'course',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['file'].widget.attrs.update({'class': 'form-control'})

        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['title'].label = "Fayl nomi"
        self.fields['file'].label = "Fayl"
        self.fields['course'].label = "Kurs"


# Videoni kursga yuklash
class UploadFormVideo(forms.ModelForm):
    class Meta:
        model = UploadVideo
        fields = ('title', 'video', 'course',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['video'].widget.attrs.update({'class': 'form-control'})

        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['title'].label = "Video nomi"
        self.fields['video'].label = "Video"
        self.fields['course'].label = "Kurs"