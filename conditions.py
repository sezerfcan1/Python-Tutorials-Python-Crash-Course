from constant import avengers

if "Spider-Man" in avengers:
    print("Spider-Man is Avenger")
else:
    print("Spider-Man isn't Avenger")

if "Thanos" in avengers:
    print("Thanos is Avenger")
else:
    print("Thanos isn't Avenger")


if "Ultron" not in avengers:
    print("Ultron isn't Avenger")
else:
    print("Ultron is Avenger")


empty_list = []

if empty_list:
    for item in empty_list:
        print(item)
else:
    print("This list is empty")