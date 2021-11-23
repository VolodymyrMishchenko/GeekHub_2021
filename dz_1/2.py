color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
result = [elem for elem in color_list_1 if elem not in color_list_2]
print(result)