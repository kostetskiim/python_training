# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", lastname="Testoff", address="Samara",
                               homephone="777-77-77", mobilephone="+777777777", workphone="12-13",
                               secondaryphone="999", email="1@mail.ru",
                               email2="2@mail.ru", email3="3@mail.ru")
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_clear(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", lastname="", address="",
                               homephone="", mobilephone="", workphone="",
                               secondaryphone="", email="",
                               email2="", email3="")
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


