import peewee
import pytest
from astrosql import AstroSQL


def test_constructor():
    db = AstroSQL("test")
    assert db


def test_bad_login_manual():
    with pytest.raises(peewee.OperationalError):
        db = AstroSQL("test", user="FAKEUSER", password="FAKEPASSWORD")


def test_bad_login_cnf():
    with pytest.raises(peewee.OperationalError):
        db = AstroSQL("test", read_default_file="/path/to/fake/my.cnf")
