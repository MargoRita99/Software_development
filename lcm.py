import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def find_lcm(numbers):
    lcm_ab = lcm(numbers[0], numbers[1])
    return lcm(lcm_ab, numbers[2])


def play_lcm():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):
        numbers = [random.randint(1, 50) for _ in range(3)]
        correct_answer = find_lcm(numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_lcm()