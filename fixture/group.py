class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init_group_form
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group, wd)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def delete_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def edit_group(self,group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group, wd)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
