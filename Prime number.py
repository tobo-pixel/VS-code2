import matplotlib.pyplot as plt
characters = ["Okonkwo","Okoye","Obiako","Okafo","Obierika"]
with open("things_fall_apart.txt","r",encoding="utf-8") as file:
    text = file.read().lower()
counts = {}
for character in characters:
    counts[character] = text.count(character.lower())
labels = counts.keys()
sizes = counts.values()
plt.figure()
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("Character Occurence in Things Fall Apart")
plt.show()

# number = int(input("Input a number: "))
# if number < 2:
#     print(number,"is not a prime number")
# else:
#     for i in range(2,number):
#         if number % i == 0:
#             print(f"{number} is not a prime number")
#             break
#     else:
#         print(f"{number} is a prime number") 
        
        