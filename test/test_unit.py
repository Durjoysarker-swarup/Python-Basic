'''
from Unit_Test import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 sqared was not 4")
    if square(3) != 9:
        print("3 sqared was not 9")

if __name__ == "__main__":
    main()
    


#assert
from Unit_Test import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except:
        print("2 sqared was not 4")
    try:
        assert square(3) == 9
    except:
        print("3 sqared was not 9")
    try:
        assert square(-2) == 4
    except:
        print("-2 sqared was not 4")
    try:
        assert square(-3) == 9
    except:
        print("-3 sqared was not 9")
    try:
        assert square(0) == 0
    except:
        print("0 sqared was not zero")

if __name__ == "__main__":
    main()
 


#pytest
from Unit_Test import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


#To find more clue
from Unit_Test import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
'''

from Unit_Test import hello

def test_argument():
    assert hello("Swarup") == "hello, Swarup"

def test_defult():
    assert hello() == "hello, world"