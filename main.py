import pytest

@pytest.mark.login
def test_m1():
    a=2
    b=3
    assert a+1==b,"test failed"
    assert a==b,"test failed"

def test_m2():
   name="selenium"
   assert name.upper()=="SELENIUM"

@pytest.mark.login
def test_m3():
   assert 10 == 10

@pytest.mark.login
def test_m4():
   print("nikhil")

def test_login():
   assert "admin" == "admin12"

@pytest.mark.login
def test_login_fb():
   assert "admin" == "ADMIN"