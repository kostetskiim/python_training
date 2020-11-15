from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", lastname="Testoff", address="Samara",
                               home="777-77-77", mobile="+777777777", work="12-13",
                               fax="999", email="1@mail.ru",
                               email2="2@mail.ru", email3="3@mail.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)