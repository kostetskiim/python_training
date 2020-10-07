from model.group import Group


def test_edit_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    app.group.edit_group(Group(group_header="edik1"))



def test_edit_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    app.group.edit_group(Group(group_name="edik2"))



def test_edit_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    app.group.edit_group(Group(group_footer="edik3"))
