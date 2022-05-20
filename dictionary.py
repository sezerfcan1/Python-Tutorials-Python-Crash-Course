from constant import alien_0,data

# print(alien_0)
# print(alien_0["color"])
# print(alien_0["puan"])

alien_0["x_coordinate"] = 0
alien_0["y_coordinate"] = 25

del alien_0["x_coordinate"]

# print(alien_0)

human_0 = {
    "name":"James",
    "age":29,
}

human_1 = {
    "name":"Mary",
    "age":24
}

human_0["friend"] = human_1

temp = human_0["friend"]
temp["name"] = "Jennifer"

# human_0 = {'name': 'James', 'age': 29, 'friend': {'name': 'Jennifer', 'age': 24}}
# human_0 = {'name': 'Jennifer', 'age': 24}


# for item in data:
#     for key,value in item.items():
#         print(f"Key:{key} : Value:{value}")

# for item in data:
#     if "0003" in item.values():
#         print(f"Exist")
#     else:
#         print(f"Not Exist")

avenger_0 = {
    "name":"Iron-Man",
    "value": 90,
}
avenger_1 = {
    "name":"Ant-Man",
    "value": 50,
}
avenger_2 = {
    "name":"Spider-Man",
    "value": 60,
}
avenger_3 = {
    "name":"Thor",
    "value": 90,
}
avenger_4 = {
    "name":"Thanos",
    "value": 120,
}

avengers_dic = [avenger_0,avenger_1,avenger_2,avenger_3,avenger_4]
