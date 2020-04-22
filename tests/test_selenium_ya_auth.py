from selenium import webdriver
import unittest
import ya_auth as app


class TestYandexAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_openURL(self):
        self.driver.get(app.URL)

    def test_login(self):
        login_field = app.get_login_field(self.driver)
        self.assertIsNotNone(login_field, 'поле для ввода логина не найдено')
        app.fill_login_field(login_field)
        self.assertEqual(app.LOGIN, login_field.get_attribute('value'), 'Поле Логин содержит неверное значение')

    def test_enter(self):
        enter_button = app.get_enter_button(self.driver)
        self.assertIsNotNone(enter_button, 'кнопка Войти не найдена')
        enter_button.click()

        err_message = app.get_element(self.driver,".passp-form-field__error")
        self.assertIsNotNone(err_message, 'нет сообщения об ошибки (логин не найден), а должна быть')
        self.assertEqual(err_message.text,'Такой логин не подойдет', 'Сообщение о неверном логине некорректно')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestYandexAuth('test_openURL'))
    suite.addTest(TestYandexAuth('test_login'))
    suite.addTest(TestYandexAuth('test_enter'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())


