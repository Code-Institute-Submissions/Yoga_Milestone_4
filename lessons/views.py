from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.db.models import Q
from .models import UserProfile
from lessons.models import Lesson, LessonItem
import json

from yoga.utils import get_profile_or_none

from .forms import LessonForm


def lessons(request):
    """ View to return the lessons page """
    profile = get_profile_or_none(request)
    sortkey = 'lesson_name'  # Default sort parameter
    direction = None
    lesson_filter = None
    page_title = 'All Lessons'
    sub_title = None

    lessons = Lesson.objects.all()

    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lesson_name'
            if sortkey == 'instructor':
                sortkey = 'instructor_profile'
            if sortkey == 'rating':
                sortkey = 'rating'
            if sortkey == 'subscribers':
                sortkey = 'subscribers'
            if sortkey == 'price':
                sortkey = 'price'

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'

        # Filtering
        if 'filter' in request.GET:
            if request.GET['filter'] == 'mylessons':
                print('sett my lesson var')
                lesson_filter = 'mylessons'

    # If authenticated get a list of subscribed lesson IDs for current user
    subscribed_lesson_list = []
    if request.user.is_authenticated:
        lesson_items = LessonItem.objects.filter(user=profile)
        for each in lesson_items:
            subscribed_lesson_list.append(each.lesson.lesson_id)

    # Apply any filters and set up redirect reverse for buttons and page title
    if lesson_filter == 'mylessons':
        lessons = lessons.filter(lesson_id__in=subscribed_lesson_list)
        if lessons:
            page_title = 'My Lessons'
        else:
            page_title = 'My Lessons'
            sub_title = 'You are currently not subscribed to any lessons'

    # Sort
    lessons = lessons.order_by(sortkey)

    # Create template and context
    template = 'lessons/lessons.html'
    context = {
        'profile': profile,
        'all_lessons': lessons,
        'subscribed_lesson_list': subscribed_lesson_list,
        'page_title': page_title,
        'sub_title': sub_title,
        'current_filter': lesson_filter,
    }

    return render(request, template, context)


def subscriptions(request):
    """ View to remove a subscribed lesson from a UserProfile """
    if request.method == 'GET':
        lesson_id = request.GET['lesson_id']
        profile = get_object_or_404(UserProfile, user=request.user)
        lesson_object = Lesson.objects.get(lesson_id=lesson_id)        

        if request.GET['subscribe'] == 'false':
            unsubscribe = LessonItem.objects.filter(lesson=lesson_object, user=profile)
            unsubscribe.delete()
            json_response = json.dumps({'subscription_status': 'unsubscribed'})
            return HttpResponse(json_response, content_type='application/json')

        elif request.GET['subscribe'] == 'true':
            if not LessonItem.objects.filter(lesson=lesson_object, user=profile).exists():
                LessonItem.objects.create(lesson=lesson_object, user=profile)
            json_response = json.dumps({'subscription_status': 'subscribed'})
            return HttpResponse(json_response, content_type='application/json')

        else:
            return HttpResponse('<h1>Something went wrong, no lessons have been subscribed or unsubscribed to.</h1>', status=500)


def instructor_created_lessons(request):
    """ View admin for lessons instructors have created """

    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'lessons/instructor_created_lessons.html'

    # Get lesson items bound to student
    instructor_created_lessons = Lesson.objects.filter(instructor_profile=profile)

    context = {
        'profile': profile,
        'instructor_created_lessons': instructor_created_lessons,
    }

    return render(request, template, context)


def delete_instructor_created_lesson(request, id):
    """ A view to delete a lesson given an id for instructor created lessons """
    profile = get_object_or_404(UserProfile, user=request.user)
    instructor_created_lesson = get_object_or_404(Lesson, lesson_id=id)

    if instructor_created_lesson.instructor_profile == profile:
        instructor_created_lesson.delete()
        return redirect('instructor_created_lessons')
    else:
        return HttpResponse('<h1>Error, this user did not create the lesson, please log in with the correct profile to delete it<h1>', status=500)


def create_lesson(request):
    """ View to create an instructor lesson """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Get lesson name form data
        lesson_name = request.POST.get('lesson_name')

        # Check for duplicate names
        instructor_created_lessons = Lesson.objects.filter(instructor_profile=profile).values_list('lesson_name', flat=True)

        if lesson_name not in instructor_created_lessons:
            # Create lesson
            form = LessonForm(request.POST, request.FILES)
            if form.is_valid():
                lesson = form.save(commit=False)  # Delay commit of for to enter profile on next line
                lesson.instructor_profile = profile
                lesson.save()
                return redirect('instructor_created_lessons')
            return redirect('instructor_created_lessons')
        else:
            return HttpResponse('<h1>You already have a lesson named this<h1>', status=500)

    else:
        form = LessonForm(initial={'instructor_profile':profile})  # Insert current user in this field
        template = 'lessons/create_lesson.html'
        context = {
            'form': form
        }
        return render(request, template, context)


def edit_lesson(request, lesson_id):
    """ A view to edit and update an instructors lesson """
    profile = get_object_or_404(UserProfile, user=request.user)
    instructor_lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=instructor_lesson)
        if form.is_valid():
            form.save()
        return redirect('instructor_created_lessons')

    else:
        form = LessonForm(instance=instructor_lesson)

        if instructor_lesson.instructor_profile == profile:
            template = 'lessons/edit_lesson.html'
            context = {
                'profile': profile,
                'lesson': instructor_lesson,
                'form': form,
            }
            return render(request, template, context)
        else:
            return HttpResponse('<h1>You can only edit your own lessons, check your login details and try again<h1>', status=500)
            