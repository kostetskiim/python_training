# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.contact.create(Contact(firstname="Test", lastname="Testoff", address="Samara",
                               home="777-77-77", mobile="+777777777", work="12-13",
                               fax="999", email="1@mail.ru",
                               email2="2@mail.ru", email3="3@mail.ru"))



def test_contact_clear(app):
    app.contact.create(Contact(firstname="", lastname="", address="",
                               home="", mobile="", work="",
                               fax="", email="",
                               email2="", email3=""))



