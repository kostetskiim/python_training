
def test_add_group(app):
    app.session.login(password="secret", login="admin")
    app.group.delete_group()
    app.session.logout()