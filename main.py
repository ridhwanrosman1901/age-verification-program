def positive_num(num):
    if num < 18:
        raise ValueError("18+ Adults only")
    else:
        return num

num = int(input("Enter your age: "))

try:
    positive_num(num)
    print('Allowed to enter')
except ValueError as e:
    print(e)