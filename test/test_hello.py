from Unit_Test import hello

def test_argument():
    assert hello("Swarup") == "hello, Swarup"

def test_defult():
    assert hello() == "hello, world"
    
'''
#Hare are some note for the test file you can create a new file by
mkdir test 3making a test folder, where you can run all the file all at once. 
#then adding the actual file 
code test_unit.py
#then add this line to tell python that it is the test folder. Python treat that folder as the packages. more can be written and can do more.
code test/__init__.py

#then you can run all the file in the folder by this code in terminal. 
pytest test #here test is the filename
'''
    