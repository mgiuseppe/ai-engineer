import os
import sys

import pytest

# ASSERT that a STATEMENT is true
# TEST FUNCTIONS should start with test_
def inc(x):
    return x + 1
def test_anwer():
    assert inc(3) == 4

# ASSERT that some code raises an EXCEPTION
def f_with_raise():
    raise SystemExit(1)
def test_raise():
    with pytest.raises(SystemExit):
        f_with_raise()

# you can compare FLOATING POINT with pytest.approx:
def test_sum():
    assert(0.1 + 0.2) == pytest.approx(0.3)
    # assert(0.1 + 0.2) == 0.3 # this would've failed because of small rounding errors

# you can group tests in a TEST CLASS
# CLASS name should start with Test
# METHODS should start with test_
# note that each test runs within a UNIQUE INSTANCE of the class
# classes are useful to share fixtures and organize tests 
class TestClass:
    check = False
    def test_one(self):
        self.check = True
        assert self.check
    def test_two(self):
        assert self.check == False
    def test_three(self):
        assert hasattr(self,"check")

# FIXTURES
@pytest.fixture
def sample_user():
    return {"name": "Ada", "email": "ada@example.com"}

def test_name(sample_user): # pytest sees the name, calls the fixture
    assert sample_user["name"] == "Ada"

def test_path(tmp_path): # pytest creates a temp path to be used inside the test function 
    print(tmp_path)
    assert tmp_path is not None

# MARK.USEFIXTURES - used to setup something using side effects
# monkeypatch - used to patch attributes and environment variables
@pytest.fixture
def fake_env_vars(monkeypatch):                 # this fixtures applies a side effect to environment variables using monkeypatch
    monkeypatch.setenv("FAKE_ENV", "HereIAm")   # monkeypatch undoes everything at the end of each test to restore the real environment (even if the test raises)

                                          # usefixtures applies a fixture without injecting its return value
@pytest.mark.usefixtures("fake_env_vars") # useful to setup something using side effects (monkeypatch envs, seed db, ...) 
class TestUseFixture:
    def test_one(self):
        assert os.environ["FAKE_ENV"]=="HereIAm"
    def test_two(self):
        assert os.environ["FAKE_ENV"]=="HereIAm"

# MARK.PARAMETRIZE - used to run the same test against different sets of data
@pytest.mark.parametrize("value", ["true", "TRUE", "True", 1]) 
def test_truthy(value):
    assert bool(value) is True

@pytest.mark.parametrize("value,expected", [
    ("true", True),
    ("TRUE", True),
    ("", False),
    (0, False)
    ]) 
def test_truthy_and_falsy(value, expected):
    assert bool(value) is expected

# OTHER MARKS
@pytest.mark.xfail(reason="did it on purpose")
def test_faulty():
    assert True == False

@pytest.mark.skip(reason="not implemented yet")
def test_not_implemented_yet():
    return

@pytest.mark.skipif(sys.platform == "win32", reason="posix-only")
def test_posix():
    assert 1 == True