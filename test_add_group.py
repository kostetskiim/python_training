# -*- coding utf-8 -*-

from group import Group
from application import Application
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    
    def test_add_group(self):
        self.app.login(password="secret", login="admin")
        self.app.create_group(Group(group_header="header", group_name="team", group_footer="footer"))
        self.app.logout()


    def test_add_clear_group(self):
        self.app.login(password="secret", login="admin")
        self.app.create_group(Group(group_header="", group_name="", group_footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
