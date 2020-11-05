# -*- coding utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)



def test_add_clear_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_header="", group_name="", group_footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

