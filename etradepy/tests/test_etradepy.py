from etradepy.etradepy import *


def test_true():
    s = 1
    assert s == 1


def test_login():
    logged_in = login()

    assert logged_in
