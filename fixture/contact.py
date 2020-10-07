class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        self.condition_edit(contact.firstname, "firstname")
        self.condition_edit(contact.lastname, "lastname")
        self.condition_edit(contact.address, "address")
        self.condition_edit(contact.home, "home")
        self.condition_edit(contact.mobile, "mobile")
        self.condition_edit(contact.work, "work")
        self.condition_edit(contact.fax, "fax")
        self.condition_edit(contact.email, "email")
        self.condition_edit(contact.email, "email2")
        self.condition_edit(contact.email, "email3")


    def condition_edit(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def edit_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

