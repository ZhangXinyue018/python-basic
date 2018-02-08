def save_to_file(file_dir, counter, student_a, student_b):
    if len(student_a) and len(student_b):
        file_a = open(file_dir + r'student_a_' + str(counter) + '.txt', mode='w')
        file_b = open(file_dir + r'student_b_' + str(counter) + '.txt', mode='w')
        file_a.writelines(student_a)
        file_b.writelines(student_b)
        file_a.close()
        file_b.close()


dir_str = r'/Users/zhangxinyue/Documents/pycharm/project_content/python-basic/resource/'
file_original = open(dir_str + r'conversation.txt')

student_a = []
student_b = []
counter = 0
for each_line in file_original:
    if not each_line.startswith('======'):
        (role, line_spoken) = each_line.split(':', 1)
        if role == 'student_a':
            student_a.append(line_spoken)
        else:
            student_b.append(line_spoken)
    else:
        save_to_file(dir_str, counter, student_a, student_b)
        student_a.clear()
        student_b.clear()
        counter += 1
save_to_file(dir_str, counter, student_a, student_b)

file_original.close()

