import random
import math


def function_A(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(no1, no2, ope):
    questions = f"{no1} {ope} {no2}"
    if ope == '+':
        answer = no1 + no2    # Addition
    elif ope == '-':
        answer = no1 - no2    # Subtraction
    else:
        answer = no1 * no2    # Multiplication
    return questions, answer

def math_quiz():
    score = 0
    total_q = 3     # we need integer

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_q):
        no1 = function_A(1, 10);
        no2 = function_A(1, 5);
        operator = function_B()

        problem, answer = function_C(no1, no2, operator)
        print(f"\nQuestion: {problem}")
        try:
           useranswer = int(input("Your answer: "))

        except ValueError:
            print('Not Valid Input : ')
            continue

        if useranswer == answer:
            print("Correct! \nCongratulation!!! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. \nThe correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_q}")

if __name__ == "__main__":
    math_quiz()