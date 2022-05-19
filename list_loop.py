import sys
from constant import avengers

# for avenger in avengers:                #   foreach x in avengers
#     print(avenger)

# for i in range(len(avengers)):          #   for 
#     print(avengers[i])

# for i in range(0,len(avengers)):        #   for 0 < i < len(avengers)
#     print(avengers[i])

# for i in range(0,len(avengers),2):      #   even index
#     print(avengers[i])

squares = []

# for i in range(0,10,3):
#     squares.append(i**2)

# print(squares)                          #   [0, 9, 36, 81]

# print(sum(squares))                     #   126
# print(max(squares))                     #   81
# print(min(squares))                     #   0

odd_numbers = [y for y in range(1,8,2)] #   [1, 3, 5, 7]


##################################  EXAMPE ##################################

from1to20 = [number for number in range(0,21,1)]
# print(sys.getsizeof(from1to20))

from1to1M = [number for number in range(0,10000000,1)]
# print(sys.getsizeof(from1to1M))

from1to1M = [number for number in range(1,10000001,1)]
# print(max(from1to1M))
# print(min(from1to1M))
# print(sum(from1to1M))


###############################################################################

from_1_to_3 = from1to20[1:4]            #   1,2,3,4

from_1_to_last = from1to20[1:]          #   1 - inf

from_1_to_last = from1to20[-4:]         #   last 4

from_1_to_last = from1to20[:-4]         #   all - last4

################################################################################

phones = ["Huawei","Apple","Xiaomi","Sonny","Vestel"]

phones_bad_copy = phones

phones_good_copy = phones[:]

phones_bad_copy.append("Oppo")              # phones_bad_copy = ['Huawei', 'Apple', 'Xiaomi', 'Sonny', 'Vestel', 'Oppo'] 
                                            # phones =          ['Huawei', 'Apple', 'Xiaomi', 'Sonny', 'Vestel', 'Oppo'] 

phones_bad_copy.append("General Mobile")    # phones_bad_copy = ['Huawei', 'Apple', 'Xiaomi', 'Sonny', 'Vestel', 'Oppo', 'General Mobile']
                                            # phones =          ['Huawei', 'Apple', 'Xiaomi', 'Sonny', 'Vestel', 'Oppo'] 