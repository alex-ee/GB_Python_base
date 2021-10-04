st = input('Введите фразу: ')

i = 1
for s in st.split():
    print(i, s[:10])
    i += 1