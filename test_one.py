import pytest


def test_one():
    print("pass")

@pytest.mark.smoke
def test_two():
    print("failed")