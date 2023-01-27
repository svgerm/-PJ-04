from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


def test_auth_page_loaded(selenium):
    """1. Проверка загрузки страницы и наличия на ней всех элементов"""
    page = AuthPage(selenium)

    assert page.auth_form_title.text == u'Авторизация'
    assert page.tab_phone.text == u'Телефон'
    assert page.tab_email.text == u'Почта'
    assert page.tab_login.text == u'Логин'
    assert page.tab_ls.text == u'Лицевой счёт'


def test_phone_valid_login(selenium):
    """2. Авторизация по номеру телефона с валидными данными"""
    page = AuthPage(selenium)
    page.phone.send_keys('+79085024080')
    page.passw.send_keys('RosTelek0m')
    page.uncheck_box()
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_email_valid_login(selenium):
    """3. Авторизация по эл. почте с валидными данными"""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.email.send_keys("clairesse@bk.ru")
    page.passw.send_keys("RosTelek0m")
    page.uncheck_box()
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_email_in_phone_tab_valid_login(selenium):
    """4. Авторизация при вводе адреса электронной почты в поле 'Номер телефона'"""
    page = AuthPage(selenium)
    page.email.send_keys("clairesse@bk.ru")
    page.passw.send_keys("RosTelek0m")
    page.uncheck_box()
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


def test_phone_unregistered_login(selenium):
    """5. Авторизация по номеру телефона с данными незарегистрированного пользователя"""
    page = AuthPage(selenium)
    page.phone.send_keys('+79085024081')
    page.passw.send_keys("Beeline")
    page.uncheck_box()
    page.btn_click()
    error_message = selenium.find_element(By.ID, "form-error-message")

    assert error_message.text == u'Неверный логин или пароль'


def test_email_unregistered_login(selenium):
    """6. Авторизация по электронной почте с данными незарегистрированного пользователя"""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.email.send_keys('clairessse@bk.ru')
    page.passw.send_keys("Beeline")
    page.uncheck_box()
    page.btn_click()
    error_message = selenium.find_element(By.ID, "form-error-message")

    assert error_message.text == u'Неверный логин или пароль'


def test_phone_empty_fields_login(selenium):
    """7. Авторизация без ввода данных в поля 'Номер телефона' и 'Пароль'"""
    page = AuthPage(selenium)
    page.uncheck_box()
    page.btn_click()
    phone_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert phone_tip.text == u'Введите номер телефона'


def test_email_empty_fields_login(selenium):
    """8. Авторизация без ввода данных в поля 'Почта' и 'Пароль'"""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.uncheck_box()
    page.btn_click()
    email_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert email_tip.text == u'Введите адрес, указанный при регистрации'


def test_login_empty_fields_login(selenium):
    """9. Авторизация без ввода данных в поля 'Логин' и 'Пароль'"""
    page = AuthPage(selenium)
    page.tab_login_click()
    page.uncheck_box()
    page.btn_click()
    email_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert email_tip.text == u'Введите логин, указанный при регистрации'


def test_ls_empty_fields_login(selenium):
    """10. Авторизация без ввода данных в поля 'Лицевой счет' и 'Пароль'"""
    page = AuthPage(selenium)
    page.tab_ls_click()
    page.uncheck_box()
    page.btn_click()
    email_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert email_tip.text == u'Введите номер вашего лицевого счета'


def test_reg_empty_fields(selenium):
    """11. Регистрация пользователя без ввода данных"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'register').click()

    selenium.save_screenshot('reg_empty_fields.png')


def test_reg_name_1_letter(selenium):
    """12. Проверка поля 'Имя' - 1 символ кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'И')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('Passw0rd')
    selenium.find_element(By.ID, 'password-confirm').send_keys('Passw0rd')
    selenium.find_element(By.NAME, 'register').click()
    name_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert name_tip.text == u'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_2_letters(selenium):
    """13. Проверка поля 'Имя' - 2 символа кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'Ив')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    conf = selenium.find_element(By.CLASS_NAME, 'card-container__title')

    assert conf.text == u'Подтверждение телефона'


def test_reg_name_3_letters(selenium):
    """14. Проверка поля 'Имя' - 3 символа кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'Ива')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    conf = selenium.find_element(By.CLASS_NAME, 'card-container__title')

    assert conf.text == u'Подтверждение телефона'


def test_reg_name_29_letters(selenium):
    """15. Проверка поля 'Имя' - 29 символов кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'жгщАёуъКкиЮфдФрБхгСёёнолщзгуш')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    conf = selenium.find_element(By.CLASS_NAME, 'card-container__title')

    assert conf.text == u'Подтверждение телефона'


def test_reg_name_30_letters(selenium):
    """16. Проверка поля 'Имя' - 30 символов кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'жгщАёуъКкиЮфдФрБхгСёёнолщзпгуш')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    conf = selenium.find_element(By.CLASS_NAME, 'card-container__title')

    assert conf.text == u'Подтверждение телефона'


def test_reg_name_31_letters(selenium):
    """17. Проверка поля 'Имя' - 31 символ кириллицы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'жгщАёуъКкиЮфдФрБхгСёёноДлщзпгуш')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    name_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert name_tip.text == u'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_latin_letters(selenium):
    """18. Проверка поля 'Имя' - 10 символов латиницы"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'gwSStPwQFn')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    name_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert name_tip.text == u'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_name_number(selenium):
    """19. Проверка поля 'Имя' - число"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys('2023')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('M0iParol22')
    selenium.find_element(By.ID, 'password-confirm').send_keys('M0iParol22')
    selenium.find_element(By.NAME, 'register').click()
    name_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert name_tip.text == u'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_pass_21_chars(selenium):
    """20. Проверка поля 'Пароль' - 21 символ"""
    page = AuthPage(selenium)
    page.reg_link_click()
    selenium.find_element(By.NAME, 'firstName').send_keys(u'Иван')
    selenium.find_element(By.NAME, 'lastName').send_keys(u'Иванов')
    selenium.find_element(By.ID, 'address').send_keys('+79044497393')
    selenium.find_element(By.ID, 'password').send_keys('FW2BBYed1mnlZaKg9OfUg')
    selenium.find_element(By.ID, 'password-confirm').send_keys('FW2BBYed1mnlZaKg9OfUg')
    selenium.find_element(By.NAME, 'register').click()
    pass_tip = selenium.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')

    assert pass_tip.text == u'Длина пароля должна быть не более 20 символов'
