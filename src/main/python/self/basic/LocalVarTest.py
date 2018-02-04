def func(i):
    print('i inside function is', i)
    i = 2
    print('Local i is', i)
i = 60;
func(i)
print('i outside function is', i)