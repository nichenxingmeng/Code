a = str(input().strip())
b = str(input().strip())
if '.' in a and '.' in b:
    temp__a = a[a.index('.')+1:]
    temp__b = b[b.index('.')+1:]
    len_ = max(len(temp__b), len(temp__a))
    while len(temp__b) < len_:
        temp__b += '0'
    while len(temp__a) < len_:
        temp__a += '0'
    temp__ = str(int(temp__a)+int(temp__b))
    while len(temp__) < len_:
        temp__ = '0'+temp__
    if temp__[:len(temp__)-len_] != '':
        temp_ = int(temp__[:len(temp__)-len_])
        temp__ = temp__[len(temp__)-len_:]
        temp_a = a[:a.index('.')]
        temp_b = b[:b.index('.')]
        temp_ += int(temp_a)+int(temp_b)
        temp_ = str(temp_)
        print(temp_+'.'+temp__)
    else:
        temp__ = temp__[len(temp__)-len_:]
        temp_a = a[:a.index('.')]
        temp_b = b[:b.index('.')]
        temp_ = int(temp_a)+int(temp_b)
        temp_ = str(temp_)
        print(temp_+'.'+temp__)

elif '.' in a and '.' not in b:
    temp__a = a[a.index('.')+1:]
    temp_a = a[:a.index('.')]
    temp_ = int(temp_a)+int(b)
    print(str(temp_)+'.'+temp__a)

elif '.' in b and '.' not in a:
    temp__b = b[b.index('.')+1:]
    temp_b = b[:b.index('.')]
    temp_ = int(temp_b)+int(a)
    print(str(temp_)+'.'+temp__b)

else:
    print(int(a)+int(b))
