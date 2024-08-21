import pytest


@pytest.mark.smoke
def test_incorrect_login(login_page):
    # login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.fill_login_form("test@mail.com", "jkhkjhj")
    # WebDriverWait(driver, 10).until(ES.staleness_of(button))
    login_page.check_error_alert_text_is(
        "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    )


@pytest.mark.regression
def test_correct_email_with_incorrect_password(login_page):
    # login_page = CustomerLogin(driver)
    login_page.open_page()
    login_page.fill_login_form("test@mail.com", "wrong_password")
    login_page.check_error_alert_text_is(
        "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    )
