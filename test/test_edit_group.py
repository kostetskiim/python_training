from model.group import Group


def test_edit_header(app):
    app.session.login(password="secret", login="admin")
    app.group.edit_group(Group(group_header="edik1"))
    app.session.logout()


def test_edit_name(app):
    app.session.login(password="secret", login="admin")
    app.group.edit_group(Group(group_name="edik2"))
    app.session.logout()


def test_edit_footer(app):
    app.session.login(password="secret", login="admin")
    app.group.edit_group(Group(group_footer="edik3"))
    app.session.logout()