# inclusive 1, exclusive 4
for item in range(1, 4):
    print(item, end=" ")

# step 5
print()
for item in range(1, 100, 5):
    print(item, end=" ")

print()
for item in list(range(1, 10)):
    print(item, end=" ")

print()
test_str = 'This is a test String'
for item in test_str:
    print(item, end=" ")

print()
test_list = ['a_lala', 'b_lala', 'c_lala']
for item in test_list:
    print(item, end=" ")

print()
test_tuple = ('a_haha', 'b_haha', 'c_haha')
for item in test_tuple:
    print(item, end=" ")

print()
test_dictionary = {
    'a': 'a_heihei',
    'b': 'b_heihei',
    'c': 'c_heihei'
}
for item_key, item_value in test_dictionary.items():
    print(item_key, ":", item_value, end=" ")