from Analysis import *
import matplotlib.pyplot as plt

def scat_plot(a,b,s):
    '''
    Takes two lists, a and b and creates a scatterplot of both these lists
    overlaid on the same scatterplot.
    s = String. Either 'pos' for positivity analysis or 'neg' for negativity analysis
    '''
    x = range(len(a))
    y = range(len(b))
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(x, sorted(a), s=10, c='r', marker="s", label='Trump')
    ax1.scatter(y, sorted(b), s=10, c='b', marker="o", label='Obama')

    if(s == 'pos'):
        ax1.scatter(y, [0.11585 for i in range(len(b))], s=10, c='black', marker="o", label='Mean Obama')
        ax1.scatter(x, [0.09122 for i in range(len(a))], s=10, c='y', marker="o", label='Mean Trump')
        ax1.set_xlabel("Tweet No.")
        ax1.set_ylabel("Positivity Score")
        ax1.set_title("Positivity Analysis")
        plt.legend(loc='upper left')
        plt.show()
    if(s=='neg'):
        ax1.scatter(y, [0.10901 for i in range(len(b))], s=10, c='black', marker="o", label='Mean Obama')
        ax1.scatter(x, [0.08868 for i in range(len(a))], s=10, c='y', marker="o", label='Mean Trump')
        ax1.set_xlabel("Tweet No.")
        ax1.set_ylabel("Negativity Score")
        ax1.set_title("Negativity Analysis")
        plt.legend(loc='upper left')
        plt.show()

def create_list(d, key):
    '''
    Creates a list of values extracted from the list of dictionaries d, taking the
    value from the same key in each dictionary.
    '''
    array = []
    for i in d:
        array.append(i[key])
    return array

def main():
    trump = open_file('sentiments_trump.pickle')
    obama = open_file('sentiments_obama.pickle')

    trumppos = create_list(trump, 'pos')
    obamapos = create_list(obama, 'pos')

    scat_plot(trumppos, obamapos, 'pos')

    trumpneg = create_list(trump, 'neg')
    obamaneg = create_list(obama, 'neg')

    scat_plot(trumpneg, obamaneg, 'neg')

if __name__ == '__main__':
    main()
