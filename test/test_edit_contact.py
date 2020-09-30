from model.contact import Contact


def test_edit_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_contact(Contact(first_name="Te", last_name="Te", address="Smara",
                               home_phone="7777", mobile_phone="+7777777", work_phone="12-13",
                               fax_phone="99", email_add="1@.ru",
                               email2_add="ail.ru", email3_add="3.ru"))
    app.session.logout()