import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from accounts.forms import EditProfileForm
from accounts.models import CustomUser, Region, Status, Institution
from .models import Department, Topic, ResultExam


@login_required(login_url='account/login')
def home_view(request):
    departments = Department.objects.all()
    results = ResultExam.objects.filter(
        user=request.user).order_by('-created_at').all()
    regions = Region.objects.all()
    status = Status.objects.all()
    institutions = Institution.objects.all()

    if request.method == "POST":
        print(request.POST)
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi.")
            return redirect("home")

    context = {
        'departments': departments,
        'results': results,
        'regions': regions,
        'status': status,
        'institutions': institutions
    }
    return render(request, 'index.html', context)


@login_required(login_url='account/login')
def detail_view(request, pk):
    topic = Topic.objects.get(pk=pk)
    departments = Department.objects.all()
    context = {
        'topic': topic,
        'departments': departments
    }
    return render(request, 'detail_topic.html', context)


def my_view(request):
    query = request.GET.get('q')
    if query:
        instances = Topic.objects.filter(
            Q(titleicontains=query) | Q(bodyicontains=query) |
            Q(department__name__icontains=query) | Q(bodyicontains=query)
        )
    else:
        instances = Topic.objects.none()

    context = {'instances': instances}
    return render(request, 'search_results.html', context)


def quiz_view(request, pk):
    department = Department.objects.get(pk=pk)
    questions = department.exams_department.all()
    context = {
        'questions': questions,
        'department': department,
    }
    return render(request, 'quiz.html', context)


@csrf_exempt
def add_result(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(pk=request.POST.get('user'))
        department = Department.objects.get(
            pk=int(request.POST.get('department')))
        wrong = request.POST.get('wrong')
        correct = request.POST.get('correct')

        new_object = ResultExam(
            user=user,
            department=department,
            wrong=wrong,
            correct=correct
        )
        new_object.save()

        return JsonResponse({'success': True, 'message': 'Object added successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
