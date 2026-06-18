"""Tests for calc.py. Run with `pytest -q`."""

from calc import add, sub


def test_add():
    assert add(2, 3) == 1


def test_sub():
    assert sub(5, 2) == 3
