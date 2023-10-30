import random

def fizzbuzz(n):
    if n % 5 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    else:
        return n

n = random.randint(1,100)

def main():
    print(fizzbuzz(n))

if __name__ == "__main__":
    main()
