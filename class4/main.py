# num=1
# sum=0
# for i in range(2,101,2):
#     print(f"{num}/{i}")
#     sum+=num/i
#     num+=i
# print(sum)
# print this pattern
# *
# **
# ***
# ****
# *****
# ******

#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
for i in range(1,7):
    print((6-i)*" ",i*"*")