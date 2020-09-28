# -*- coding utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(password="secret", login="admin")
    app.create_group(Group(group_header="header", group_name="team", group_footer="footer"))
    app.logout()


def test_add_clear_group(app):
    app.login(password="secret", login="admin")
    app.create_group(Group(group_header="", group_name="", group_footer=""))
    app.logout()

