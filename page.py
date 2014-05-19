from holmium.core import PageObject, Element, Locators 


class Figshare(PageObject):
    login_btn_1 = Element(Locators.ID, "user_login_but")
    email_login = Element(Locators.ID, "log_email")
    password_signup = Element(Locators.ID, "log_pass")
    login_btn_2 = Element(Locators.ID, "log_but")
    first_name = Element(Locators.ID, "first_name")
    last_name = Element(Locators.ID, "last_name")
    email_sign_up = Element(Locators.ID, "email")
    confirm_email = Element(Locators.ID, "confirm_email")
    fake_password = Element (Locators.ID, "fake_password")
    password_sign_up = Element (Locators.ID, "password_signup")
    sign_up = Element (Locators.CSS_SELECTOR, "button.styled-btn.clear-btn-style")
    
    def login_email(self,  query ):
        self.login_btn_1.click()
        self.email_login.send_keys( query )
        
    def login_password(self,  query ):
        self.password_signup.send_keys( query )
        self.login_btn_2.click()
    
    def sign_up_first_name(self,  query ):
        self.first_name.send_keys( query )
        
    def sign_up_last_name(self,  query ):
        self.last_name.send_keys( query )

    def sign_up_email(self,  query ):
        self.email_signup.send_keys( query )
        self.confirm_email.send_keys( query )
        
    def sign_up_password(self,  query ):
        self.fake_password.clear()
        self.password_signup.send_keys( query )
        self.sign_up.click()
