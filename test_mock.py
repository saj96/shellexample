#unit test 3 question 1 
from random import randint
from unittest.mock import Mock
from unittest.mock import patch

# def get_random_number():
#     return randint(1, 10)
# def add_number_with_random_number(a, get_random_number):
#     return a + get_random_number()

# #test
# def test_add_number_with_random_number():
# # Arrange
#     mock_get_random_number = Mock()
#     mock_get_random_number.return_value = 10
#     expected = 15 
# # Act
#     actual = add_number_with_random_number(5, mock_get_random_number)
# # Assert
#     assert expected == actual

#question 2
# def get_random_number(randint):
#     return randint(1, 10)
# def test_get_random_number():
# # Arrange
#     expected = 5
#     mock_get_random_number = Mock()
#     mock_get_random_number.return_value = 5
# # Act
#     actual = get_random_number(mock_get_random_number)
# # Assert
#     assert expected == actual

#question 3
def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f'Thank you, your name is {name} and your age is {age}')

@patch("builtins.input", side_effect = ['John', 18])
@patch("builtins.print")
def test_get_user_details(mock_print, mock_input):
    get_user_details()
    #assert
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
    mock_print.assert_called_with("Thank you, your name is John and your age is 18") # Passes
    
    
    