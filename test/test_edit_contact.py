from model.contact import Contact


def test_edit_first_name(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="SERE"))
    app.session.logout()


def test_edit_last_name(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(lastname="SERE"))
    app.session.logout()


def test_edit_address(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(address="SERE"))
    app.session.logout()


def test_edit_home_phone(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(home="SERE"))
    app.session.logout()


def test_edit_mobile_phone(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(mobile="SERE"))
    app.session.logout()


def test_edit_work_phone(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(work="SERE"))
    app.session.logout()


def test_edit_fax_phone(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(fax="SERE"))
    app.session.logout()


def test_edit_email_add(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(email="SERE"))
    app.session.logout()


def test_edit_email2_add(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(email2="SERE"))
    app.session.logout()


def test_edit_email3_add(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(email3="SERE"))
    app.session.logout()
