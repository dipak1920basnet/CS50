# from cs50 import get_int
# changes = [25,10,5,1]

# def main():
#     while True:
#         get_changes = get_int("Change owed: ")
#         if get_changes < 0:
#             continue
#         else:
#             new = change_owed(get_changes)
#             print(new)
#             break
# def change_owed(x):
#     count_change = 0
#     while x != 0:
#         for i in changes:
#             if x == i:
#                 count_change += 1
#         else:
#             for j in changes:
#                 if j > x:
#                     x = j-x
#                     count_change += 1
#     return count_change
# if __name__=="__main__":
#     main()


changes_list = {'quarters' : 25,
                'dimes'    : 10,
                'nickles'  : 5,
                'pennies'  : 1}

# for i in changes_list.values():
#     print(i)

