import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #Website Dummy: http://barru.pythonanywhere.com/daftar

    #LOGIN SUCCESS
    def test_a_success_login(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('jagoqaindonesia@gmail.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)

        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, 'Welcome Jago QA')
        self.assertEqual(respon2, 'Anda Berhasil Login')

    #LOGIN EMAIL NOT REGISTERED
    def test_b_failed_login_email_not_registered(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60jakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "User's not found")
        self.assertEqual(respon2, 'Email atau Password Anda Salah')

    #LOGIN FAILED (EMAIL/PASSWORD MAX CHARACTERS)
    def test_c_failed_login_email_max_characters(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('sman60daskjjdaskkdasjkdsajkadjkljdsdakdskljsklkdaslkldsaklkdalsldasklkdslakdlsa2u38823hdewdhkjsdjakarta')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "Oops...")
        self.assertEqual(respon2, 'Gagal Login!')

    #LOGIN FAILED (EMAIL/PASSWORD EMPTY)
    def test_d_failed_login_password_empty(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[1]").send_keys('tester.ganteng@jumawa.com')
        time.sleep(1)
        driver.find_element_by_id("password").send_keys('')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/input[3]').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "User's not found")
        self.assertEqual(respon2, 'Email atau Password Anda Salah')

    #REGISTER SUCCESS
    def test_e_register_success(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_id('signUp').click()
        time.sleep(1)
        driver.find_element_by_id("name_register").send_keys('Riris Melissa')
        time.sleep(1)
        driver.find_element_by_id("email_register").send_keys('emailbaru@mail.com')
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('riris123')
        time.sleep(1)
        driver.find_element_by_id('signup_register').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "berhasil")
        self.assertEqual(respon2, 'created user!')

    #REGISTER FAILED (EMAIL/PASSWORD/NAME EMPTY)
    def test_f_register_failed_empty(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_id('signUp').click()
        time.sleep(1)
        driver.find_element_by_id("name_register").send_keys('Riris Melissa')
        time.sleep(1)
        driver.find_element_by_id("email_register").send_keys('riris.melissa@lala.com')
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('')
        time.sleep(1)
        driver.find_element_by_id('signup_register').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "Oops...")
        self.assertEqual(respon2, 'Gagal Register!')

    #REGISTER FAILED (EMAIL REGISTERED)
    def test_g_register_failed_registered_email(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_id('signUp').click()
        time.sleep(1)
        driver.find_element_by_id("name_register").send_keys('Riris Melissa')
        time.sleep(1)
        driver.find_element_by_id("email_register").send_keys('riris.melissa@lala.com')
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('')
        time.sleep(1)
        driver.find_element_by_id('signup_register').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "Oops...")
        self.assertEqual(respon2, 'Gagal Register!')

    #REGISTER FAILED (EMAIL MELEBIHIN CHARACTER)
    def test_h_register_failed_registered_email(self):
        driver = self.driver

        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(1)
        driver.find_element_by_id('signUp').click()
        time.sleep(1)
        driver.find_element_by_id("name_register").send_keys('Riris Melissa')
        time.sleep(1)
        driver.find_element_by_id("email_register").send_keys('riris.melissa@lala.com')
        time.sleep(1)
        driver.find_element_by_id("password_register").send_keys('adsjkhdakskdjaskjdklsjkldjskjkladsjkljdskajdskljakldsj87q7821hjhkhjdshjakysd8')
        time.sleep(1)
        driver.find_element_by_id('signup_register').click()
        time.sleep(2)
        respon1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/h2').text
        respon2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]').text

        self.assertEqual(respon1, "Oops...")
        self.assertEqual(respon2, 'Gagal Register!')

    # #Website Dummy: http://myappventure.herokuapp.com/registration
    # def test_register_myapp(self):
    #     driver = self.driver

    #     driver.get("https://myappventure.herokuapp.com/registration")
    #     time.sleep(2)
    #     driver.find_element_by_name("username").send_keys("abdvc")
    #     time.sleep(1)
    #     driver.find_element_by_name("email").send_keys("dimas@yahoo.com") 
    #     time.sleep(1)
    #     driver.find_element_by_name("password").send_keys("abjh6767hc")
    #     time.sleep(1)
    #     driver.find_element_by_xpath("/html/body/div/main/div/div/form/div[5]/button").click()
    #     time.sleep(5)

    #     respon = self.driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/form/div[2]/p').text
    #     self.assertIn("Alamat email atau kata sandi yang anda masukan tidak valid", respon)
    #     self.driver.close()

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()