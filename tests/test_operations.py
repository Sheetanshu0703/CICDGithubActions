from src.math_operations import add,subtract,multiply,divide,power

def test_add():
    assert add(1,2) == 3
    assert add(4,2) == 6
    
def test_subtract():
    assert subtract(1,2) == -1
    assert subtract(4,2) == 2
    
def test_multiply():
    assert multiply(1,2) == 2
    assert multiply(4,2) == 8
    
def test_divide():
    assert divide(1,2) == 0.5
    assert divide(4,2) == 2
    
def test_power():
    assert power(1,2) == 1
    assert power(4,2) == 16
    
    