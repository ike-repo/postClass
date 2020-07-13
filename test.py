# counting the passengers for number of cars needed
# def cars_needed(n):
#    if n <= 5:
# 	    return 1
#    elif n % 5 != 0:
# 	    return n // 5 + 1
#    else:
# 	    return int(n / 5)

# print(cars_needed(20))
##############################
#counting the letters in a word and compare
# def XO(txt):
#     x_count = 0
#     o_count = 0 
#     new_txt = txt.lower()  
#     for i in range(len(new_txt)):
#         if new_txt[i] == 'x':
#             x_count += 1
#         elif new_txt[i] == 'o':
#             o_count += 1
#     if x_count == o_count:
#         print(o_count)
#         print(x_count)
#         return True
#     else:
#         return False
# print(XO('oxOoxXOx'))
##############################
# def grocery(**kwargs):
#     for key, value in kwargs.items():
#         print(f"Item type is {key} and the name is {value}")

# grocery(fruit = 'melon', bread = 'artisan', \
#     vegetable = 'cucumber')

# def team_names(*teams) :
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)

# team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')

print([i for i in 'beri gel berber' if i != 'e'])