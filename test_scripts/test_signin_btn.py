"""
this module is for test case regarding sign in btn in register page
"""
import pytest
from time import sleep
from src_code.register_page import Register
from inclusive_function.configure import Config
from inclusive_function.examination import Examination


@pytest.mark.usefixtures("launch_browser", "log")
@pytest.mark.parametrize("username, password",Config.CREDENTIAL)
class TestSignInBtn:

    def test_signinbtn(self, username, password):
        self.logger.info("TESTING SIGNIN BUTTON")

        obj = Register(self.driver, self.logger)

        self.logger.info("Handling Cookies")
        assert obj.cookies_btn(), "cannot be able to handle cookies"

        self.logger.info("click on profile btn button")
        assert obj.profile_btn(), "profile button not working"

        self.logger.info("click on signup link in home page")
        assert obj.sign_up_link(),   "signup link not working"

        self.logger.info("click on signin button in register page")
        assert obj.sign_in_btn(), "signup button not working"

        self.logger.info("providing email in email_txt")
        assert obj.email_txt(username), "email text not working"

        self.logger.info("click on continue_btn")
        assert obj.continue_btn(), "continue btn not working"

        self.logger.info("providing password in password_txt")
        assert obj.pwd_txt(password), "password txt not working"

        self.logger.info("testing signin btn in register page")
        assert obj.sign_in_for_product_btn(), "signin btn not working"

        self.logger.info("checking profile page ")
        result = obj.check_page(Examination.RESULT_AFTER_SIGN_IN)
        assert result, "page not load"


