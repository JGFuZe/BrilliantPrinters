
import time
from django.test import TestCase, LiveServerTestCase, Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from django.contrib.auth.models import User, Group, Permission
from .models import Question, Respondent, QuestionFile
from .views import *
# Create your tests here.



# Model Tests

class RegisterFromTest(LiveServerTestCase):
    
    def test_register_form(self):
        driver = webdriver.Chrome()
        
        driver.get(('%s%s' % (self.live_server_url, '/accounts/register')))

        username = driver.find_element(By.NAME, "username")
        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME,"password1")
        passwordConfirm = driver.find_element(By.NAME,"password2")
        submit = driver.find_element(By.ID,"submit")
        
        username.send_keys('testname')
        email.send_keys('test@gmail.com')
        password.send_keys('testing123')
        passwordConfirm.send_keys('testing123')
        

        submit.send_keys(Keys.RETURN)
        
        assert 'login' in driver.page_source
        
        
class LoginFormTest(LiveServerTestCase):
     def test_login_form(self):
        driver = webdriver.Chrome()
        
        driver.get(('%s%s' % (self.live_server_url, '/accounts/login')))
        time.sleep(3)
        lusername = driver.find_element(By.NAME, "username")
        lpassword = driver.find_element(By.NAME, "password")
        lsubmit = driver.find_element(By.ID, "submit")
        time.sleep(3)
        lusername.send_keys('JGFuZe')
        lpassword.send_keys('poopoo123')
        
        
        time.sleep(3)
        
        lsubmit.send_keys(Keys.RETURN)
        time.sleep(3)
        #assert "testname" in driver.page_source
####



# View Tests

#def test_question_list_view(self):