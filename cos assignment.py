cube = lambda x:x**3
print(cube(3))

temperatures = [0,10,20,30,40]
converter = list(map(lambda x:(x*9/5)+32 , temperatures))
print(converter)

characters = ["dog","cat","lion","tiger"]
sorted_characters = sorted(characters, key = lambda x:x[-1])
print(sorted_characters)

words = ["data","science","ai","python"]
sorted_words = list(filter(lambda x: len(x) > 4, words))
print(sorted_words)