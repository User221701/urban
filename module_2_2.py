first = int(input())
second = int(input())
third = int(input())
if first == second:
    if second == third:
        print(3)
    else:
        print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
