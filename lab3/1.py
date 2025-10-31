'''
# Task 1: 
class MyClass:
    def getString(self):
        self.input_string = input(" ")  

    def printString(self):
        print(self.input_string.upper())  


obj = MyClass()
obj.getString()  
obj.printString()  


# Task 2: 
class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length 
obj_square = Square(9)  
print(f"{obj_square.area()}" )





# Task 3: 


class Rectangle:
    def __init__(self, length, width):
        self.length = length  
        self.width = width    

    def area(self):
        return self.length * self.width  
 
obj_rectangle = Rectangle(5, 10)  
print("Тіктөртбұрыштың аумағы: ",obj_rectangle.area())




# Task 4: 
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
point1 = Point(0, 0)  # Координаттары (0, 0)
point2 = Point(3, 4)  # Координаттары (3, 4)

# Координаттарды көрсету
point1.show()  # Нүктенің координаттарын шығару

# Нүктені жылжыту
point1.move(1, -1)  # Нүктені (1, -1) бойынша жылжыту
point1.show()  # Жылжытылған нүктенің координаттарын көрсету

# Екі нүкте арасындағы қашықтықты есептеу
distance = point1.dist(point2)  # point1 және point2 арасындағы қашықтық
print(f"Қашықтық: {distance}")  # Қашықтықты шығару








# Task 5: 
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
# Есепшот объектісін жасау
account = Account("Айгерім", 1000)  # Баланс 1000 теңге

# Ақша салу
account.deposit(500)
print(f"Баланс: {account.balance} теңге")  # Баланс 1500 теңге болуы керек

# Ақша алу
account.withdraw(2000)  # Баланс жеткіліксіз болған жағдайда
print(f"Баланс: {account.balance} теңге")  # Баланс өзгермейді, себебі ақша жеткіліксіз

# Ақша алу
account.withdraw(1000)  # Баланс 1500 болғанда, 1000 алу
print(f"Баланс: {account.balance} теңге")  # Баланс 500 теңге болуы керек





# Task 6: 
def filter_prime(numbers):
    return list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))

print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]))




# Task 7: унция
def grams_to_ounces(grams):
    return 28.3495231 * grams



# Task 8: 
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)



# Task 9: 
def solve(numheads, numlegs):
    num_rabbits = (numlegs - 2 * numheads) // 2
    num_chickens = numheads - num_rabbits
    return num_chickens, num_rabbits



# Task 10: 
def filter_prime(nums):
    return [num for num in nums if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]


# Task 11: 
import itertools
def string_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]


# Task 12: 
def reverse_words(sentence):
    return ' '.join(reversed(sentence.split()))


# Task 13: 
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Task 14: 
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [0, 0, 7]:
            return True
    return False

# Task 15: 
def sphere_volume(radius):
    return (4 / 3) * math.pi * radius**3

# Task 16: 
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Task 17: 
def is_palindrome(word):
    return word == word[::-1]

# Task 18: 
def histogram(lst):
    for num in lst:
        print('*' * num)

# Task 19: 
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break




movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_above_5_5(movie):
    return movie['imdb'] > 5.5

def filter_above_5_5(movies):
    return list(filter(is_above_5_5, movies))

def get_movies_by_category(category):
    return [movie for movie in movies if movie['category'] == category]

def average_imdb_score(movies):
    return sum([movie['imdb'] for movie in movies]) / len(movies)

def average_imdb_by_category(category):
    category_movies = get_movies_by_category(category)
    return average_imdb_score(category_movies)

'''










