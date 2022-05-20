from constant import avengers

current_index = 0

while current_index < 5:
    temp_avenger = input("Enter a avenger.")
    if temp_avenger not in avengers:
        avengers.append(temp_avenger)
    current_index += 1
print(avengers)