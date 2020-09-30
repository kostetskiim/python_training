
def test_delete_group(app):
    app.session.login(password="secret", login="admin")
    app.group.delete_group()
    app.session.logout()