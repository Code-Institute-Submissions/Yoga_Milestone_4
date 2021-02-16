from django.test import TestCase

import html

from profiles.models import UserProfile
from lessons.models import Subscription, Lesson


class TestLessonsView(TestCase):
    fixtures = ['profiles/fixtures/sample_fixtures.json', ]

    def setUp(self):
        self.instructor = UserProfile.objects.filter(is_instructor=True).first()

        profile = UserProfile.objects.get(user__username='complete_user')
        login_successful = self.client.login(username=profile.user.username,
                                             password='orange99')
        self.assertTrue(login_successful)

    def test_get_lessons(self):
        '''
        Renders a list of all lessons
        '''
        response = self.client.get('/lessons/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        self.assertContains(response, 'All Lessons')

    def test_lessons_with_valid_instructor_filter(self):
        '''
        Displays the instructors profile and all their
        lessons underneath
        '''
        response = self.client.get('/lessons/', {'instructor': self.instructor.id}, follow=True)
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        self.assertContains(response, self.instructor.user.username)
        self.assertContains(response, html.escape(self.instructor.profile_description))

    def test_invalid_query_reverts_to_defaults(self):
        '''
        Invalid get requests revert to default values
        '''
        response = self.client.get('/lessons/', {"filter": "INVALID_ENTRY",
                                                 "sort": "INVALID_ENTRY",
                                                 "direction": "INVALID_ENTRY"})
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        # All lessons show
        self.assertContains(response, 'All Lessons')
        self.assertContains(response, 'A Lesson')
        self.assertContains(response, 'B Lesson')
        self.assertContains(response, 'H Lesson')
        self.assertContains(response, 'Y Lesson')
        self.assertContains(response, 'Z Lesson')

    # Query
    def test_lesson_query(self):
        '''
        Only show queried lessons
        '''
        response = self.client.get('/lessons/?q=z')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')

        self.assertContains(response, 'All Lessons')
        self.assertContains(response, 'Z Lesson')

        self.assertNotContains(response, 'A Lesson')
        self.assertNotContains(response, 'B Lesson')
        self.assertNotContains(response, 'H Lesson')
        self.assertNotContains(response, 'Y Lesson')

    # Sort
    def test_sort_name_ascending(self):
        response = self.client.get('/lessons/', {"sort": "lesson_name", "direction": "asc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('A Lesson') < html_str.index('B Lesson'))
        self.assertTrue(html_str.index('Y Lesson') < html_str.index('Z Lesson'))

    def test_sort_name_descending(self):
        response = self.client.get('/lessons/', {"sort": "lesson_name", "direction": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('A Lesson') > html_str.index('B Lesson'))
        self.assertTrue(html_str.index('Y Lesson') > html_str.index('Z Lesson'))

    def test_sort_rating_ascending(self):
        response = self.client.get('/lessons/', {"sort": "rating", "direction": "asc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('6/10') < html_str.index('10/10'))

    def test_sort_rating_descending(self):
        response = self.client.get('/lessons/', {"sort": "rating", "direction": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('6/10') > html_str.index('10/10'))

    def test_sort_price_ascending(self):
        self.client.logout() # Price does not show on purchased lessons
        response = self.client.get('/lessons/', {"sort": "price", "direction": "asc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('€35.99') > html_str.index('€4.99'))

    def test_sort_price_descending(self):
        self.client.logout() # Price does not show on purchased lessons
        response = self.client.get('/lessons/', {"sort": "price", "direction": "desc"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('€35.99') < html_str.index('€4.99'))

    # Filter
    def test_filter_subscribed_lessons(self):
        '''
        complete_user is subscribed to
        A Lesson and Z Lesson
        '''
        response = self.client.get('/lessons/', {"filter": "subscribed_lessons"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        self.assertContains(response, 'A Lesson')
        self.assertContains(response, 'Z Lesson')
        self.assertNotContains(response, 'B Lesson')
        self.assertNotContains(response, 'H Lesson')
        self.assertNotContains(response, 'Y Lesson')

    def test_filter_paid_lesson(self):
        '''
        complete_user has purchased Z Lesson
        '''
        response = self.client.get('/lessons/', {"filter": "purchased_lessons"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        self.assertContains(response, 'Z Lesson')
        self.assertNotContains(response, 'A Lesson')
        self.assertNotContains(response, 'B Lesson')
        self.assertNotContains(response, 'H Lesson')
        self.assertNotContains(response, 'Y Lesson')

    # Stacked Query / Filter / Sort
    def test_query_filter_sort(self):
        '''
        Test query / filter / sort at the same time
        '''
        response = self.client.get('/lessons/', {"filter": "subscribed_lessons",
                                                 "sort": "lesson_name",
                                                 "direction": "desc"})
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/lessons.html')
        # All lessons show
        self.assertContains(response, 'A Lesson')
        self.assertContains(response, 'Z Lesson')

        self.assertNotContains(response, 'B Lesson')
        self.assertNotContains(response, 'H Lesson')
        self.assertNotContains(response, 'Y Lesson')

        html_str = response.content.decode("utf-8")
        self.assertTrue(html_str.index('Z Lesson') < html_str.index('A Lesson'))