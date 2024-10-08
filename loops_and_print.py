def enumerate_list(list):
    list2=[]
    list3=[]
    for item in list:
        if item != "":
            list2.append(item)
    for i, items in enumerate(list2):
        list3.append(f"{i}. {items}")
    return list3

print(enumerate_list(["Red", "Green", "", "White", "Black"]))


def enumerate_backwards(strings):
    list1=[]
    list2=[]
    for str1 in strings:
        if str1 != "":
            list1.append(str1)
    for index, str2 in enumerate(list1):
        list2.append(f"{index}. {str2[::-1]}")
    return list2

print(enumerate_backwards(["Red", "Green", "", "White", "Black"]))

