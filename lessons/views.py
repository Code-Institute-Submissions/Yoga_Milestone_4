from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.db.models import Q, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import UserProfile
from lessons.models import Lesson, LessonItem, LessonReview, LessonReviewFlagged
from checkout.models import OrderLineItem
import json

from yoga.utils import get_profile_or_none

from .forms import LessonForm, ReviewForm


def lessons(request):
    """ View to return the lessons page """
    profile = get_profile_or_none(request)
    sortkey = 'lesson_name'  # Default sort parameter
    direction = None
    sort_direction = 'asc'
    lesson_filter = None
    page_title = 'All Lessons'
    sub_title = None
    filter_title = 'All Lessons'
    instructor_to_display = None
    subscribed_lesson_list = []
    paid_lesson_list = None
    valid_sort_values = ['name', 'instructor', 'rating', 'price']

    lessons = Lesson.objects.all()

    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey not in valid_sort_values:
                messages.error(request, 'Invalid sort value, displaying all \
                                         lessons by name in ascending order')
                return redirect(reverse('lessons'))

            if sortkey == 'name':
                sortkey = 'lesson_name'
            if sortkey == 'instructor':
                sortkey = 'instructor_profile'
            if sortkey == 'rating':
                sortkey = 'rating'
            if sortkey == 'price':
                sortkey = 'price'

        # Direction of resuluts
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sort_direction = 'desc'

        # Filtering
        if 'filter' in request.GET:
            if request.GET['filter'] == 'mylessons':
                lesson_filter = 'mylessons'
            if request.GET['filter'] == 'paidlessons':
                lesson_filter = 'paidlessons'

        # Instructor header
        if 'instructor' in request.GET:
            if request.GET['instructor']:
                instructor_id = request.GET['instructor']
                try:
                    instructor_to_display = get_object_or_404(UserProfile,
                                                              id=instructor_id)
                    if not instructor_to_display.is_instructor:
                        messages.error(request,
                                       'This user is not an instructor, \
                                       please pick one from the \
                                       instructor list.')
                        return redirect(reverse('instructors'))
                except Exception as e:
                    messages.error(request,
                                   'This instructor was not found, please \
                                   pick one from the instructor list.')
                    return redirect(reverse('instructors'))
                page_title = f"Welcome to {instructor_to_display}'s Studio"
                lessons = lessons.filter(
                    instructor_profile=instructor_to_display
                    )

    # If authenticated
    if request.user.is_authenticated:

        # Get a list of subscribed lesson IDs for current user
        subscribed_lessons = LessonItem.objects.filter(user=profile)
        for subscribed_lesson in subscribed_lessons:
            subscribed_lesson_list.append(subscribed_lesson.lesson.lesson_id)

        # Get a list of paid lessons
        paid_lessons = OrderLineItem.objects.filter(profile=profile)
        paid_lesson_list = []
        for paid_lesson in paid_lessons:
            paid_lesson_list.append(paid_lesson.lesson.lesson_id)

    # Apply any filters and set up redirect reverse for buttons and page title
    if lesson_filter:
        if lesson_filter == 'mylessons':
            lessons = lessons.filter(lesson_id__in=subscribed_lesson_list)
            if not lessons:
                sub_title = 'You are currently not subscribed to any lessons'
            page_title = 'Subscribed Lessons'
            filter_title = page_title

        if lesson_filter == "paidlessons":
            if paid_lesson_list:
                lessons = lessons.filter(lesson_id__in=paid_lesson_list)
                if lessons:
                    page_title = 'Purchased Lessons'
            else:
                lessons = lessons.filter(lesson_id__in=paid_lesson_list)
                page_title = 'Purchased Lessons'
                sub_title = 'You have not purchased any lessons'
            filter_title = 'Purchaed Lessons'

        # If viewing an instructor and also filtering
        if instructor_to_display:
            page_title = f"Welcome to {instructor_to_display}'s Studio"

    # Sort
    if sort_direction == 'asc':
        lessons = lessons.order_by(F(sortkey).asc(nulls_last=True))
    else:
        lessons = lessons.order_by(F(sortkey).desc(nulls_last=True))

    # Create template and context
    template = 'lessons/lessons.html'
    context = {
        'profile': profile,
        'all_lessons': lessons,
        'subscribed_lesson_list': subscribed_lesson_list,
        'paid_lesson_list': paid_lesson_list,
        'page_title': page_title,
        'sub_title': sub_title,
        'filter_title': filter_title,
        'current_filter': lesson_filter,
        'instructor_to_display': instructor_to_display
    }

    return render(request, template, context)


@login_required
def subscriptions(request):
    """ View to remove a subscribed lesson from a UserProfile """
    if request.method == 'GET':
        profile = get_object_or_404(UserProfile, user=request.user)
        try:
            lesson_id = request.GET['lesson_id']
            lesson_object = Lesson.objects.get(lesson_id=lesson_id)
        except Exception as e:
            messages.error(request,
                           'Invalid request, no lessons have been subscribed \
                           or unsubscribed to.')
            return redirect(reverse('lessons'))

        if request.GET['subscribe'] == 'false':
            unsubscribe = LessonItem.objects.filter(lesson=lesson_object,
                                                    user=profile)
            unsubscribe.delete()
            json_response = json.dumps({'subscription_status': 'unsubscribed'})
            return HttpResponse(json_response, content_type='application/json')

        elif request.GET['subscribe'] == 'true':
            if not LessonItem.objects.filter(lesson=lesson_object,
                                             user=profile).exists():
                LessonItem.objects.create(lesson=lesson_object, user=profile)
            json_response = json.dumps({'subscription_status': 'subscribed'})
            return HttpResponse(json_response, content_type='application/json')

        else:
            messages.error(request, 'Invalid request, no lessons have been \
                                    subscribed or unsubscribed to.')
            return redirect(reverse('lessons'))


@login_required
def instructor_created_lessons(request):
    """ View admin for lessons instructors have created """

    profile = get_object_or_404(UserProfile, user=request.user)
    if not profile.is_instructor:
        messages.error(request, 'Only instructors can do this.')
        return redirect('home')

    template = 'lessons/instructor_created_lessons.html'

    # Get lesson items bound to student
    instructor_created_lessons = Lesson.objects.filter(
        instructor_profile=profile)

    context = {
        'profile': profile,
        'instructor_created_lessons': instructor_created_lessons,
    }

    return render(request, template, context)


@login_required
def delete_instructor_created_lesson(request, id):
    """ A view to delete a lesson given an id for instructor created lessons """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not profile.is_instructor:
        messages.error(request, 'Only instructors can do this.')
        return redirect('home')

    try:
        instructor_created_lesson = get_object_or_404(Lesson, lesson_id=id)
    except Exception as e:
        messages.error(request, 'Invalid lesson ID, no lessons were deleted.')
        return redirect(reverse('instructor_created_lessons'))

    if instructor_created_lesson.instructor_profile == profile:
        instructor_profile = instructor_created_lesson.instructor_profile
        instructor_created_lesson.delete()
        total_lessons = Lesson.objects.filter(instructor_profile=instructor_profile).count()
        instructor_profile._update_lesson_count(total_lessons)
        return redirect('instructor_created_lessons')
    else:
        messages.error(request, 'This lesson does not belong to you and has \
                                not been deleted, please check your username \
                                and try again.')
        return redirect(reverse('instructor_created_lessons'))


@login_required
def create_lesson(request):
    """ View to create an instructor lesson """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not profile.is_instructor:
        messages.error(request, 'Only instructors can do this.')
        return redirect('home')

    if request.method == 'POST':
        # Get lesson name form data
        lesson_name = request.POST.get('lesson_name')

        # Check for duplicate names
        instructor_created_lessons = Lesson.objects.filter(
            instructor_profile=profile).values_list('lesson_name', flat=True)

        if lesson_name not in instructor_created_lessons:
            # Create lesson
            form = LessonForm(request.POST, request.FILES)
            if form.is_valid():
                lesson = form.save(commit=False)
                lesson.instructor_profile = profile
                lesson.save()
                return redirect('instructor_created_lessons')
            return redirect('instructor_created_lessons')
        else:
            messages.error(request, 'You already have a lesson named this.')
            return redirect(reverse('instructor_created_lessons'))

    else:
        form = LessonForm(initial={'instructor_profile': profile})
        template = 'lessons/create_lesson.html'
        context = {
            'form': form
        }
        return render(request, template, context)


@login_required
def edit_lesson(request, lesson_id):
    """ A view to edit and update an instructors lesson """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not profile.is_instructor:
        messages.error(request, 'Only instructors can do this.')
        return redirect('home')

    try:
        instructor_lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    except Exception as e:
        messages.error(request, 'Invalid lesson ID, no lessons were updated.')
        return redirect(reverse('instructor_created_lessons'))

    if request.method == 'POST':
        form = LessonForm(request.POST,
                          request.FILES,
                          instance=instructor_lesson)
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
            messages.error(request, 'You can only edit your own lessons, \
                                     please check your username.')
            return redirect(reverse('instructor_created_lessons'))


@login_required
def review_lesson(request, lesson_id):
    """ A view to create a profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    # Make sure lesson is valid
    try:
        lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    except Exception as e:
        messages.error(request, 'Cannot create/edit a review for \
                                 an invalid lesson.')
        return redirect(reverse('home'))

    existing_review = LessonReview.objects.filter(profile=profile,
                                                  lesson=lesson).first()
    # Check existing review belongs to current users profile
    if existing_review:
        if not existing_review.profile == profile:
            messages.error(request, 'Cannot complete request, this \
                                     review is not yours.')
            return redirect(reverse('home'))

    template = "lessons/create_review.html"
    context = {
        'profile': profile,
        'lesson': lesson,
    }

    # Submit review form
    if request.method == 'POST':
        post_data = request.POST.copy()
        # Validate rating
        rating_value = request.POST['rating_dropdown']
        if int(rating_value) not in range(1, 11):
            messages.error(request, 'You entered an invalid rating, \
                                     please try again.')
            return redirect('studio', lesson.lesson_id)
        else:
            rating_value = int(rating_value)
            post_data.update({'rating': rating_value})

        # Create or fetch existing review       
        if not existing_review:
            form = ReviewForm(post_data)
        else:
            form = ReviewForm(post_data, instance=existing_review)
        # Update form or return error message
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = rating_value
            review.save()
            return redirect('studio', lesson.lesson_id)
        else:
            error = form.errors
            messages.error(request, f'Error in review form: {error}')
            return redirect('studio', lesson.lesson_id)
    # Send user to create/update review form
    else:
        if existing_review:
            form = ReviewForm(instance=existing_review)
            form.fields["rating_dropdown"].initial = existing_review.rating
            context['form'] = form
            return render(request, template, context)
        else:
            form = ReviewForm(initial={'profile': profile, 'lesson': lesson})
            context['form'] = form
            return render(request, template, context)


@login_required
def delete_review(request, review_pk):
    profile = get_object_or_404(UserProfile, user=request.user)

    # Get review
    try:
        review = get_object_or_404(LessonReview, pk=review_pk)
        lesson = review.lesson
    except Exception as e:
        messages.error(request, 'Cannot delete review, review not found.')
        return redirect(reverse('home'))

    if review.profile == profile or request.user.is_superuser:
        review.delete()
        lesson._update_rating()
        if request.user.is_superuser and request.method == 'POST':
            # Stay on superuser admin page
            json_response = json.dumps({'success': 'True'})
            return HttpResponse(json_response, content_type='application/json')
        else:
            # Reload lesson page
            messages.success(request, 'Review deleted.')
            return redirect(reverse('studio', args=(lesson.lesson_id,)))
    else:
        messages.error(request, 'Cannot delete review, it does not belong to this account.')
        return redirect(reverse('studio', args=(lesson.lesson_id,)))


@login_required
def flag_review(request, review_pk, lesson_id):
    """ Allows user to flag a review to admin """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        review = get_object_or_404(LessonReview, pk=review_pk)
    except Exception as e:
        messages.error(request, "Invalid review, please contact support if you think this is an error")
        return redirect(reverse('studio', args=(lesson_id,)))

    if LessonReviewFlagged.objects.filter(profile=profile, review=review).exists():
        messages.error(request, f"You have already flagged {review.profile}'s review, it will be reviewd by an administrator soon")
        return redirect(reverse('studio', args=(review.lesson.lesson_id,)))

    flag = LessonReviewFlagged(profile=profile, review=review)
    flag.save()
    messages.success(request, f"{review.profile}'s review has been flagged and will be reviewed by an administrator soon")
    return redirect(reverse('studio', args=(review.lesson.lesson_id,)))


@login_required
def remove_flag(request):
    """ Removes a flag from a review """
    if not request.user.is_superuser:
        messages.error('Only administrators can perform this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        try:
            flagged_pk = request.POST['flagged_pk']
            flagged = get_object_or_404(LessonReviewFlagged, pk=flagged_pk)
            review_to_ignore = flagged.review
        except Exception as e:
            json_response = json.dumps({'message': 'No lesson flag found with that primary key'})
            return HttpResponse(json_response, content_type='application/json')
        
        # Remove all flags for this review
        LessonReviewFlagged.objects.filter(review=review_to_ignore).delete()
        json_response = json.dumps({'message': 'All flags for this review have been removed'})
        return HttpResponse(json_response, content_type='application/json')

    else:
        messages.error(request, "Remove flag does not accept GET requests")
        return redirect(reverse('superuser_admin'))


def get_modal_data(request):
    """ Get data for lesson extra detail modal """
    if request.method == 'POST':
        if 'lesson_id' in request.POST:
            lesson_id = request.POST['lesson_id']
            # Get lesson, pass it to lesson_modal template and turn to string
            if not Lesson.objects.filter(lesson_id=lesson_id).exists():
                json_response = json.dumps({'status': 'invalid_lesson'})
                return HttpResponse(json_response, content_type='application/json')
            lesson = Lesson.objects.get(lesson_id=lesson_id)
            modal_string = render_to_string(
                'lessons/snippets/lesson_modal.html',
                {'lesson': lesson}
            )
            json_response = json.dumps({'status': 'valid_lesson',
                                        'modal': modal_string,
                                        })
            return HttpResponse(json_response, content_type='application/json')
        else:
            json_response = json.dumps({'status': 'invalid_request'})
            return HttpResponse(json_response, content_type='application/json')
    else:
        messages.error(request, 'You cannot perform this action')
        return redirect(reverse('home'))