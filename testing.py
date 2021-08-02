# def add_two_numbers(a, b):
#     return a + b 

# def test_adds_two_numbers():
#     # Assemble
#     a = 7
#     b = 12
#     expected = 19
#     # Act
#     result = add_two_numbers(a, b)
#     # Assert
#     assert result == expected

# test_adds_two_numbers()
# def test2_adds_two_numbers():
#     # Assemble
#     a = 7
#     b = -12
#     expected = -5
#     # Act
#     result = add_two_numbers(a, b)
#     # Assert
#     assert result == expected

# test2_adds_two_numbers()

# def test3_adds_two_numbers():
#     # Assemble
#     a = 7.3
#     b = 12.7
#     expected = 20
#     # Act
#     result = add_two_numbers(a, b)
#     # Assert
#     assert result == expected

# test3_adds_two_numbers()
# def test4_adds_two_numbers():
#     # Assemble
#     a = 7
#     b = 'simon'
#     expected = '7simon'
#     # Act
#     result = add_two_numbers(a, b)
#     # Assert
#     assert result == expected
# test4_adds_two_numbers()



# #UNIT 2 DEPENDENCY INJECTIONS - MOCKS AND STUBS
# import random
# def get_random_number():
#     return random.randint(1, 10)

# def add_number_with_random_number(a, random):#i put random so i can plug in which ever test or actual
#     return a + random()

# def test_number_random():
#     #given
#     a = 10
#     b = 5
#     expected = 15
#     def mock_function():
#         return 5
#     #when
#     result = add_number_with_random_number(10, mock_function)
#     print(result)
#     #then
#     assert result == expected
    
# test_number_random()
# print(add_number_with_random_number(5, get_random_number))

#unit test 2 question 3
# from random import randint
# def get_random_number():
#     return randint(1, 10)

# def add_two_random_numbers(random, random2):
#     return random() + random2()


# def test_number_random():
#     #given
#     def mock2():
#         return 10
#     expected = 15
#     def mock_function():
#         return 5
#     #when
#     result = add_two_random_numbers(mock2, mock_function)
#     print(result)
#     #then
#     assert result == expected

# test_number_random()
# print(add_two_random_numbers(get_random_number, get_random_number))

#question 4 
from random import randint

def get_random_number():
    return randint(1, 10)

def test_randint():
    #given
    expected = 5 
    def mock_rand():
        return 



















