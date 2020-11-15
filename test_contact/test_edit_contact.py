from model.contact import Contact
from random import randrange

def test_edit_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_edit_address(app):
#    if app.contact.count() == 0:
 #       app.contact.create(Contact(address="Samara",))
#    app.contact.edit_contact(Contact(address="qaz"))



#def test_edit_home_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(home="777-77-77"))
#    app.contact.edit_contact(Contact(home="qaz"))



#def test_edit_mobile_phone(app):
#    if app.contact.count() == 0:
 #       app.contact.create(Contact(mobile="+777777777"))
  #  app.contact.edit_contact(Contact(mobile="qaz"))



#def test_edit_work_phone(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(work="12-13"))
   # app.contact.edit_contact(Contact(work="qaz"))



#def test_edit_fax_phone(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(fax="999"))
   # app.contact.edit_contact(Contact(fax="qaz"))



#def test_edit_email_add(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(email="1@mail.ru"))
   # app.contact.edit_contact(Contact(email="qaz"))



#def test_edit_email2_add(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(email2="2@mail.ru"))
   # app.contact.edit_contact(Contact(email2="qaz"))



#def test_edit_email3_add(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(email3="3@mail.ru"))
   # app.contact.edit_contact(Contact(email3="qaz"))

