from model.contact import Contact

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
        self.contact_cache = None

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
        self.contact_cache = None


    def condition_edit(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()


    def delete_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def edit_contact(self):
        self.edit_contact_by_index(0)


    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.edit_page_open()
        self.fill_contact_form(contact)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.return_to_home_page()

    def edit_page_open(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php?id=") and len(wd.find_elements_by_name("update")) > 0):
            wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for cont in wd.find_elements_by_name("entry"):
                id = cont.find_element_by_name("selected[]").get_attribute("id")
                lastname = cont.find_element_by_xpath("./td[2]").text
                firstname = cont.find_element_by_xpath("./td[3]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_cache)