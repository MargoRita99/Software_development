import random

RULES = "Find the smallest common multiple of given numbers."

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def find_lcm(numbers):
    lcm_ab = lcm(numbers[0], numbers[1])
    return lcm(lcm_ab, numbers[2])

def get_question():
    numbers = [random.randint(1, 50) for _ in range(3)]
    correct_answer = find_lcm(numbers)
    question = " ".join(map(str, numbers))

    return question, correct_answer