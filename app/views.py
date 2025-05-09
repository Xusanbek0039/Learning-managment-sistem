from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.decorators import admin_required, lecturer_required
from .forms import SessionForm, SemesterForm, NewsAndEventsForm
from .models import *


# Yangiliklar va Tadbirlar
@login_required
def home_view(request):
    items = NewsAndEvents.objects.all().order_by('-updated_date')
    context = {
        'title': "Yangiliklar va Tadbirlar | IT Creative LMS",
        'items': items,
    }
    return render(request, 'app/index.html', context)


@login_required
def post_add(request):
    if request.method == 'POST':
        form = NewsAndEventsForm(request.POST)
        title = request.POST.get('title')
        if form.is_valid():
            form.save()
            messages.success(request, (title + ' joylashtirildi.'))
            return redirect('home')
        else:
            messages.error(request, 'Iltimos, quyidagi xatolikni to\'g\'rilang.')
    else:
        form = NewsAndEventsForm()
    return render(request, 'app/post_add.html', {
        'title': 'Post qo\'shish | IT Creative LMS',
        'form': form,
    })


@login_required
@lecturer_required
def edit_post(request, pk):
    instance = get_object_or_404(NewsAndEvents, pk=pk)
    if request.method == 'POST':
        form = NewsAndEventsForm(request.POST, instance=instance)
        title = request.POST.get('title')
        if form.is_valid():
            form.save()
            messages.success(request, (title + ' yangilandi.'))
            return redirect('home')
        else:
            messages.error(request, 'Iltimos, quyidagi xatolikni to\'g\'rilang.')
    else:
        form = NewsAndEventsForm(instance=instance)
    return render(request, 'app/post_add.html', {
        'title': 'Post tahrirlash | IT Creative LMS',
        'form': form,
    })


@login_required
@lecturer_required
def delete_post(request, pk):
    post = get_object_or_404(NewsAndEvents, pk=pk)
    title = post.title
    post.delete()
    messages.success(request, (title + ' o\'chirildi.'))
    return redirect('home')


# Sessiya
@login_required
@lecturer_required
def session_list_view(request):
    """ Barcha sessiyalarni ro'yxatini ko'rsatish """
    sessions = Session.objects.all().order_by('-is_current_session', '-session')
    return render(request, 'app/session_list.html', {"sessions": sessions})


@login_required
@lecturer_required
def session_add_view(request):
    """ Agar POST bo'lsa, sessiya qo'shamiz, aks holda bo'sh forma ko'rsatamiz """
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            data = form.data.get('is_current_session')  # 'True' string qaytaradi agar foydalanuvchi "Ha" ni tanlagan bo'lsa
            print(data)
            if data == 'true':
                sessions = Session.objects.all()
                if sessions:
                    for session in sessions:
                        if session.is_current_session == True:
                            unset = Session.objects.get(is_current_session=True)
                            unset.is_current_session = False
                            unset.save()
                    form.save()
                else:
                    form.save()
            else:
                form.save()
            messages.success(request, 'Sessiya muvaffaqiyatli qo\'shildi.')
            return redirect('session_list')
    else:
        form = SessionForm()
    return render(request, 'app/session_update.html', {'form': form})


@login_required
@lecturer_required
def session_update_view(request, pk):
    session = Session.objects.get(pk=pk)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        data = form.data.get('is_current_session')
        if data == 'true':
            sessions = Session.objects.all()
            if sessions:
                for session in sessions:
                    if session.is_current_session == True:
                        unset = Session.objects.get(is_current_session=True)
                        unset.is_current_session = False
                        unset.save()
            if form.is_valid():
                form.save()
                messages.success(request, 'Sessiya muvaffaqiyatli yangilandi.')
                return redirect('session_list')
        else:
            form = SessionForm(request.POST, instance=session)
            if form.is_valid():
                form.save()
                messages.success(request, 'Sessiya muvaffaqiyatli yangilandi.')
                return redirect('session_list')
    else:
        form = SessionForm(instance=session)
    return render(request, 'app/session_update.html', {'form': form})


@login_required
@lecturer_required
def session_delete_view(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if session.is_current_session:
        messages.error(request, "Joriy sessiyani o'chirib bo'lmaydi")
        return redirect('session_list')
    else:
        session.delete()
        messages.success(request, "Sessiya muvaffaqiyatli o'chirildi")
    return redirect('session_list')


# Semestr
@login_required
@lecturer_required
def semester_list_view(request):
    semesters = Semester.objects.all().order_by('-is_current_semester', '-semester')
    return render(request, 'app/semester_list.html', {"semesters": semesters, })


@login_required
@lecturer_required
def semester_add_view(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            data = form.data.get('is_current_semester')  # 'True' string qaytaradi agar foydalanuvchi "Ha" ni tanlagan bo'lsa
            if data == 'True':
                semester = form.data.get('semester')
                ss = form.data.get('session')
                session = Session.objects.get(pk=ss)
                try:
                    if Semester.objects.get(semester=semester, session=ss):
                        messages.error(request, semester + " semestr " + session.session + " sessiyasida allaqachon mavjud")
                        return redirect('add_semester')
                except:
                    semesters = Semester.objects.all()
                    sessions = Session.objects.all()
                    if semesters:
                        for semester in semesters:
                            if semester.is_current_semester == True:
                                unset_semester = Semester.objects.get(is_current_semester=True)
                                unset_semester.is_current_semester = False
                                unset_semester.save()
                        for session in sessions:
                            if session.is_current_session == True:
                                unset_session = Session.objects.get(is_current_session=True)
                                unset_session.is_current_session = False
                                unset_session.save()
                    new_session = request.POST.get('session')
                    set_session = Session.objects.get(pk=new_session)
                    set_session.is_current_session = True
                    set_session.save()
                    form.save()
                    messages.success(request, 'Semestr muvaffaqiyatli qo\'shildi.')
                    return redirect('semester_list')
            form.save()
            messages.success(request, 'Semestr muvaffaqiyatli qo\'shildi.')
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'app/semester_update.html', {'form': form})


@login_required
@lecturer_required
def semester_update_view(request, pk):
    semester = Semester.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('is_current_semester') == 'True':  # 'True' string qaytaradi agar foydalanuvchi "Ha" ni tanlagan bo'lsa
            unset_semester = Semester.objects.get(is_current_semester=True)
            unset_semester.is_current_semester = False
            unset_semester.save()
            unset_session = Session.objects.get(is_current_session=True)
            unset_session.is_current_session = False
            unset_session.save()
            new_session = request.POST.get('session')
            form = SemesterForm(request.POST, instance=semester)
            if form.is_valid():
                set_session = Session.objects.get(pk=new_session)
                set_session.is_current_session = True
                set_session.save()
                form.save()
                messages.success(request, 'Semestr muvaffaqiyatli yangilandi!')
                return redirect('semester_list')
        else:
            form = SemesterForm(request.POST, instance=semester)
            if form.is_valid():
                form.save()
                return redirect('semester_list')
    else:
        form = SemesterForm(instance=semester)
    return render(request, 'app/semester_update.html', {'form': form})


@login_required
@lecturer_required
def semester_delete_view(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if semester.is_current_semester:
        messages.error(request, "Joriy semestrni o'chirib bo'lmaydi")
        return redirect('semester_list')
    else:
        semester.delete()
        messages.success(request, "Semestr muvaffaqiyatli o'chirildi")
    return redirect('semester_list')


@login_required
@admin_required
def dashboard_view(request):
    return render(request, 'app/dashboard.html')