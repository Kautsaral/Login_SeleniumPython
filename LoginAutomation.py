import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome()
    
    #TestCase1    
    def test_a_failed_login_with_empty_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Cek Formulir Anda', response_data)
        self.assertEqual(response_message, 'Password tidak boleh kosong')
        browser.get_screenshot_as_file("test_a_failed_login_with_empty_password.png") #screenshot 
    
    #TestCase2 
    def test_a_failed_login_with_empty_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Cek Formulir Anda', response_data)
        self.assertEqual(response_message, 'Email tidak boleh kosong')
        browser.get_screenshot_as_file("test_a_failed_login_with_empty_email.png") #screenshot

    #TestCase3 
    def test_a_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Cek Formulir Anda', response_data)
        self.assertEqual(response_message, 'Email & Password tidak boleh kosong')
        browser.get_screenshot_as_file("test_a_failed_login_with_empty_email_and_password.png") #screenshot

    #TestCase4 
    def test_a_failed_login_with_error_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago5") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        browser.get_screenshot_as_file("test_a_failed_login_with_error_email.png") #screenshot
    
    #TestCase5 
    def test_a_failed_login_with_error_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago5") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("User's not found", response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        browser.get_screenshot_as_file("test_a_failed_login_with_error_password.png") #screenshot
    
    #TestCase6 
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("testerjago") # isi password
        time.sleep(3)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome tester jago', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')
        browser.get_screenshot_as_file("test_a_success_login.png") #screenshot

    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()