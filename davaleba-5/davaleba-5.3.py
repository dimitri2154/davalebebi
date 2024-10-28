my_llist = [43, '22', 12, 66, 210, ["hi"]]

if 210 in my_llist:
    index_210 = my_llist.index(210)
    print("Index of 210 is:", index_210)
else:
    print("210 is not in the list")

my_llist[-1].append("hello")
print("List after adding 'hello':", my_llist)

del my_llist[2]
print("List after deleting index 2:", my_llist)

my_llist_2 = my_llist.copy()
my_llist_2.clear()
print("my_llist:", my_llist)
print("my_llist_2:", my_llist_2)
