a = input()
b = input()
if len(a) != len(b):
    print(1)
else:
    if a == b:
        print(2)
    else:
        if a.lower() == b.lower():
            print(3)
        else:
            print(4)
