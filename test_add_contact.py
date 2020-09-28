# -*- coding: utf-8 -*-
from application_c import Application
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(first_name="Test", last_name="Testoff", address="Samara",
                            home_phone="777-77-77", mobile_phone="+777777777", work_phone="12-13",
                            fax_phone="999", email_add="1@mail.ru",
                            email2_add="2@mail.ru", email3_add="3@mail.ru"))
    app.logout()


def test_contact_clear(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(first_name="", last_name="", address="",
                            home_phone="", mobile_phone="", work_phone="",
                            fax_phone="", email_add="",
                            email2_add="", email3_add=""))
    app.logout()
