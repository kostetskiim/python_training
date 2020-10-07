from model.group import Group


def test_edit_header(app):
    app.group.edit_group(Group(group_header="edik1"))



def test_edit_name(app):
    app.group.edit_group(Group(group_name="edik2"))



def test_edit_footer(app):
    app.group.edit_group(Group(group_footer="edik3"))
