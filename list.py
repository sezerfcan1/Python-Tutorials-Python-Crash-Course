from constant import avengers

avengers[1].lower()                 # "ant-man"
avengers[-1].upper()                # "HAWKEYE"

######################################################################################

avengers.append("Iron-Man")         # ['Spider-Man', 'Ant-Man', 'Scarlet Witch', 'Vision', 'Hawkeye', 'Iron-Man']
avengers.insert(2,"Thor")           # ['Spider-Man', 'Ant-Man', 'Thor', 'Scarlet Witch', 'Vision', 'Hawkeye', 'Iron-Man']
del avengers[3]                     # ['Spider-Man', 'Ant-Man', 'Thor', 'Vision', 'Hawkeye', 'Iron-Man']

popped_avengers = avengers.pop()    #   avengers =  ['Spider-Man', 'Ant-Man', 'Thor', 'Vision', 'Hawkeye']
                                    #   popped_avengers = "Iron-Man"

popped_avengers = avengers.pop(3)   #   avengers =  ['Spider-Man', 'Ant-Man', 'Thor', 'Hawkeye']
                                    #   popped_avengers = "Vision"

avengers.remove("Ant-Man")          #   avengers =  ['Spider-Man', 'Thor', 'Hawkeye']

#######################################################################################

avengers.sort()                     #   ['Spider-Man', 'Thor', 'Hawkeye'] -> ['Hawkeye', 'Spider-Man', 'Thor']
avengers.sort(reverse=True)         #   ['Hawkeye', 'Spider-Man', 'Thor'] -> ['Thor', 'Spider-Man', 'Hawkeye']

sorted_avengers = sorted(avengers, reverse=True)  #   sorted_avengers = ['Thor', 'Spider-Man', 'Hawkeye']

sorted_avengers.reverse()           #   ['Thor', 'Spider-Man', 'Hawkeye'] -> ['Hawkeye', 'Spider-Man', 'Thor']

########################################################################################


len(avengers)                       #   3

# print(avengers[3])                  # list index out of range


