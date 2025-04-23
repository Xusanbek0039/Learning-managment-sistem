from django import forms
from django.db import transaction

from .models import NewsAndEvents, Session, Semester, SEMESTER


# Yangiliklar va tadbirlar uchun forma
class NewsAndEventsForm(forms.ModelForm):
    class Meta:
        model = NewsAndEvents
        fields = ('title', 'summary', 'posted_as',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['posted_as'].widget.attrs.update({'class': 'form-control'})

        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['title'].label = "Sarlavha"
        self.fields['summary'].label = "Qisqacha mazmuni"
        self.fields['posted_as'].label = "Nima sifatida joylashtirilgan"


# Sessiya uchun forma
class SessionForm(forms.ModelForm):
    next_session_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
            }
        ),
        required=True)

    class Meta:
        model = Session
        fields = ['session', 'is_current_session', 'next_session_begins']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['session'].label = "Sessiya nomi"
        self.fields['is_current_session'].label = "Joriy sessiya"
        self.fields['next_session_begins'].label = "Keyingi sessiya boshlanish sanasi"


# Semestr uchun forma
class SemesterForm(forms.ModelForm):
    semester = forms.CharField(
        widget=forms.Select(
            choices=SEMESTER,
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="Semestr",  # O'zbek tiliga o'zgartirildi
    )
    is_current_semester = forms.CharField(
        widget=forms.Select(
            choices=((True, 'Ha'), (False, 'Yo\'q')),  # O'zbek tiliga o'zgartirildi
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="Joriy semestr",  # O'zbek tiliga o'zgartirildi
    )
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        required=True
    )

    next_semester_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        ),
        required=True)

    class Meta:
        model = Semester
        fields = ['semester', 'is_current_semester', 'session', 'next_semester_begins']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Label-larni o'zbek tiliga o'zgartiramiz
        self.fields['session'].label = "Sessiya"
        self.fields['next_semester_begins'].label = "Keyingi semestr boshlanish sanasi"