from constant import avengers

avengers_tuple = tuple(avengers)                                    # ('Spider-Man', 'Ant-Man', 'Scarlet Witch', 'Vision', 'Hawkeye')

# avengers_tuple[2] = "Iron-Man"        'tuple' object does not support item assignment

avengers_temp_list = [avengers_tuple[2], avengers_tuple[3]]         # ['Scarlet Witch', 'Vision']

avengers_temp_tuple = (avengers_temp_list,"Black Panter")           # (['Scarlet Witch', 'Vision'], 'Black Panter')
