class SessionHelper:


    def __init__(self, app):
        self.app = app


    def login(self, password, login):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")


    def ensure_logout(self):
        wd = self.app.wd
        if self.logged_in():
            self.logout()


    def ensure_login(self,password, login):
        wd = self.app.wd
        if self.logged_in():
            if self.logged_in_as(login):
                return
            else:
                self.logout()
        self.login(password, login)

    def logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0


    def logged_in_as(self, login):
        wd = self.app.wd
        return wd.find_element_by_xpath('//div/div[1]/form/b').text == "("+login+")"