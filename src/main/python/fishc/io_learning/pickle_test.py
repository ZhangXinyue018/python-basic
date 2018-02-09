# pickle是文件存放及读取模块
import pickle

my_list = [123, 413.4, 'hahaha', range(2)]
pickle_file = open(r'/Users/zhangxinyue/Documents/pycharm/project_content/python-basic/'
                   r'resource/pickle_test.txt', mode='wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open(r'/Users/zhangxinyue/Documents/pycharm/project_content/python-basic/'
                   r'resource/pickle_test.txt', mode='rb')
my_list2 = pickle.load(pickle_file)
pickle_file.close()
print(my_list2)