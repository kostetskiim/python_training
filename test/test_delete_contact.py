from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", lastname="Testoff", address="Samara",
                               home="777-77-77", mobile="+777777777", work="12-13",
                               fax="999", email="1@mail.ru",
                               email2="2@mail.ru", email3="3@mail.ru"))
    app.contact.delete_contact()
