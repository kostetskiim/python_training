from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_header="header", group_name="team", group_footer="footer"))
    app.group.delete_group()
