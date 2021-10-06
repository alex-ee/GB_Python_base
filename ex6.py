def ucase_f(s_txt):
    m = s_txt.split()
    z = ''
    for e in m:
        z += int_func(e) + ' '
        
    return z

def int_func(s_word):
    return s_word[:1].upper() + s_word[1:]

print(int_func('asdasdasd'))

print(ucase_f('asdasdasd asdasd asddgsdg sdjg fdjkghjk jkdfk jdf'))