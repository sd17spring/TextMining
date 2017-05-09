import data_finder

class Auto_Tweeter:
    def __init__ (self):
        self.start()


    def start(self):
        print ('What is the handle of the person you want to mimic?')
        user_handle = input()

        print ('Have you collected Data? (y/n)')
        collect_data = input()
        if collect_data == 'n':
            statuses = data_finder.data_finder(user_handle)

        print (statuses)
#import user_handle.py

if __name__ == '__main__':
    tweeter = Auto_Tweeter()
