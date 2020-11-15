from model.group import Group
from random import randrange

#def test_edit_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
#    group = Group(group_header="edik1")
#    group.id = old_groups[0].id
#    app.group.edit_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name="edik2")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_edit_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#       app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
#    group = Group(group_footer="edik3")
#    group.id = old_groups[0].id
#    app.group.edit_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
