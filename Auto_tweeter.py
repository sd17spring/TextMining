import data_finder


print ('What is the handle of the person you want to mimic?')
user_handle = input()

print ('Have you collected Data? (y/n)')
collect_data = input()
if collect_data == 'n':
    data_finder.data_finder(user_handle)


#import user_handle.py
