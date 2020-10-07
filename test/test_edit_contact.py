from model.contact import Contact


def test_edit_first_name(app):
    app.contact.edit_contact(Contact(firstname="SERE"))



def test_edit_last_name(app):
    app.contact.edit_contact(Contact(lastname="SERE"))



def test_edit_address(app):
    app.contact.edit_contact(Contact(address="SERE"))



def test_edit_home_phone(app):
    app.contact.edit_contact(Contact(home="SERE"))



def test_edit_mobile_phone(app):
    app.contact.edit_contact(Contact(mobile="SERE"))



def test_edit_work_phone(app):
    app.contact.edit_contact(Contact(work="SERE"))



def test_edit_fax_phone(app):
    app.contact.edit_contact(Contact(fax="SERE"))



def test_edit_email_add(app):
    app.contact.edit_contact(Contact(email="SERE"))



def test_edit_email2_add(app):
    app.contact.edit_contact(Contact(email2="SERE"))



def test_edit_email3_add(app):
    app.contact.edit_contact(Contact(email3="SERE"))

