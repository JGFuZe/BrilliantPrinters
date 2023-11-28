
import time
from django.test import TestCase, LiveServerTestCase, Client
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from django.contrib.auth.models import User, Group, Permission
from .models import Question, Respondent, QuestionFile
from .views import *
# Create your tests here.



# Form Tests
"""""
class RegisterFromTest(LiveServerTestCase):
    
    def test_register_form(self):
        # Set the web driver to the chrome browser
        driver = webdriver.Chrome()
        
        # Based over the base server url go to the user registration page
        driver.get(('%s%s' % (self.live_server_url, '/accounts/register')))

        # Get all field elements by name
        username = driver.find_element(By.NAME, "username")
        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME,"password1")
        passwordConfirm = driver.find_element(By.NAME,"password2")
        submit = driver.find_element(By.ID,"submit")
        
        # send testing information to field elements
        username.send_keys('testname')
        email.send_keys('test@gmail.com')
        password.send_keys('testing123')
        passwordConfirm.send_keys('testing123')
        
        # Press submit button
        submit.send_keys(Keys.RETURN)
        
        # Test to see if on login page
        assert 'login' in driver.page_source
        
        
class LoginFormTest(LiveServerTestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", "test@gmail.com", "testing123")
        self.user.save()

    def test_login_form(self):
        # Set the web driver to the chrome browser
        driver = webdriver.Chrome()
        
        # Based over the base server url go to the login page
        driver.get(('%s%s' % (self.live_server_url, '/accounts/login')))

        # Get elements from the name atributes for username, password, and submit
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.ID, "submit")

        # Fill in username and password fields
        username.send_keys('testuser')
        password.send_keys('testing123')
        
        # Press submit button
        submit.send_keys(Keys.RETURN)
        
        time.sleep(3)

        # Confrim Users name shows up in top right so look for that element
        assert "testuser" in driver.page_source

"""""


# Model Tests

class QuestionTests(LiveServerTestCase):
    
    def setUp(self):
        # Create group object to add user to for views validation
        self.group = Group(name="regular_user")
        self.group.save()
        
        # Create user
        self.user = User.objects.create_user("testuser", "test@gmail.com", "testing123")
        self.user.save()

        # Add user to group and save
        self.user.groups.add(self.group)
        self.user.save()

        # Create question for testing
        self.question = Question.objects.create(title="testing title", description="test desc", answered=False, respondent=None)

        #
        client = Client()


    # Regular Tests

    # Test that __str__ override in question model returns the questions title
    def test_question_str_return(self):
        self.assertEqual(str(self.question), "testing title")

    def test_questions_url_exists(self):
        responce = self.client.get("/questions")
        self.assertEqual(responce.status_code, 200)
        
    def test_questions_list_available_by_name(self):
        responce = self.client.get(reverse("question_list"))
        self.assertEqual(responce.status_code, 200)


    def test_questions_list_template_exists(self):
        responce = self.client.get(reverse("question_list"))
        self.assertTemplateUsed(responce, 'BrilliantPrinters_app/question_list.html')

    """""
    def test_questions_details_template_exists(self):
        url = ("questions/" + str(self.question.pk))
        responce = self.client.get(reverse(url))
        self.assertTemplateUsed(responce, 'BrilliantPrinters_app/question_detail.html')

    def test_questions_details_available_by_name(self):
        questionId = self.question.pk
        url = ("questions/" + str(self.question.pk))
        responce = self.client.get(reverse(url))
        self.assertEqual(responce.status_code, 200)

    """""

    # Selenium Tests
 #   def test_question_list_view_no_questions(self):
 #       client.login(username="testuser", password="testing123")



#    def test_question_list_view_has_questions(self):
#        client.login(username="testuser", password="testing123")



class HomepageTests(LiveServerTestCase):

    def test_homepage_url_exists(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)
        
    def test_homepage_available_by_name(self):
        responce = self.client.get(reverse("index"))
        self.assertEqual(responce.status_code, 200)

    def test_homepage_template_exists(self):
        responce = self.client.get(reverse("index"))
        self.assertTemplateUsed(responce, 'BrilliantPrinters_app/index.html')



