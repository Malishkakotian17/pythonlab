my_list = [5,3,8,9,1]
new_element = 4
my_list.append(new_element)
print("after adding",my_list)
my_list.sort()
print("after sorting",my_list)
my_list.reverse()
print("after reverse",my_list)
element_to_remove = 8
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print("after eleminating",my_list)
else:
    print("no elements")