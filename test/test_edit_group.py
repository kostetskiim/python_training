from model.group import Group


def test_edit_group(app):
    app.session.login(password="secret", login="admin")
    app.group.edit_group(Group(group_header="edit", group_name="edit", group_footer="edit"))
    app.session.logout()
