# -*- coding utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))




def test_add_clear_group(app):
    app.group.create(Group(group_header="", group_name="", group_footer=""))


