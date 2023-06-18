list_numbers = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
                {"VI": "S005"}, {"VII": "S005"}, 
                {" V ":"S009"}, {" VIII":"S007"}]

dict_1 = set()
for item in list_numbers:
    for value in item.values():
        dict_1.add(value)
print(dict_1)
