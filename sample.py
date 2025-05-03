# begin sample.py
# This file is to show how we can use the functions defined in exercise.py
# 이 파일은 exercise.py에 정의된 함수를 어떻게 사용할 수 있는지 보여주기 위한 것입니다.
# This file is not to be evaluated.
# 이 파일은 평가되지 않습니다.

import random


# Import the module containing the functions
# 학생이 작성한 exercise.py 모듈을 import
import exercise

# Set the random seed
# (유사) 난수 발생기를 초기화
random.seed()


def main():
    # Tests with random numbers
    # 무작위 숫자로 시험
    for _ in range(5):  # Run 5 random tests
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        # Skip division by zero in random tests for now
        # 0으로 나누는 예는 일단 건너뜁시다
        if b == 0:
            continue

        print(f"Testing with random numbers: a = {a}, b = {b}")

        # Addition
        # 덧셈
        result = exercise.add(a, b)
        print(f"  add({a}, {b}) = {result}")

        # Subtraction
        # 뺄셈
        result = exercise.sub(a, b)
        print(f"  sub({a}, {b}) = {result}")

        # Multiplication
        # 곱셈
        result = exercise.mul(a, b)
        print(f"  mul({a}, {b}) = {result}")

        # Division
        # 나눗셈
        result = exercise.div(a, b)
        print(f"  div({a}, {b}) = {result}")

        print("-----")

    # Divide by zero
    # 0으로 나누기
    result = exercise.div(a, 0)
    print(f"  div({a}, {0}) = {result}")


if __name__ == "__main__":
    # Lines below are executed only when this file is run directly
    # 이 파일이 직접 실행될 때만 아래의 코드가 실행됩니다.
    # When this file is imported, the lines below are not executed.
    # 이 파일이 import될 때는 아래의 코드가 실행되지 않습니다.
    main()

# end sample.py
