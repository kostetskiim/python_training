# -*- coding utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(password="secret", login="admin")
    app.create_group(Group(group_header="header", group_name="team", group_footer="footer"))
    app.session.logout()


def test_add_clear_group(app):
    app.session.login(password="secret", login="admin")
    app.create_group(Group(group_header="", group_name="", group_footer=""))
    app.session.logout()

