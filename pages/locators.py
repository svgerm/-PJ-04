from selenium.webdriver.common.by import By


class AuthLocators:
    auth_form_title = (By.CLASS_NAME, "card-container__title")
    tab_phone = (By.ID, "t-btn-tab-phone")
    tab_email = (By.ID, "t-btn-tab-mail")
    tab_login = (By.ID, "t-btn-tab-login")
    tab_ls = (By.ID, "t-btn-tab-ls")
    input_field_user = (By.ID, "username")
    user_field_name = (By.CLASS_NAME, "rt-input__placeholder")
    input_field_pass = (By.ID, "password")
    auth_btn = (By.ID, "kc-login")
    check_box = (By.CLASS_NAME, 'rt-checkbox')
    reg_link = (By.ID, 'kc-register')