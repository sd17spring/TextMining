import wikipedia

def presidents_to_texts():
    presidents = ['George Washington', 'John Adams', 'Thomas Jefferson',
    'James Madison', 'James Monroe', 'John Quincy Adams', 'Andrew Jackson',
    'Martin Van Buren', 'William Henry Harrison', 'John Tyler',
    'James K. Polk', 'Zachary Taylor', 'Millard Fillmore', 'Franklin Pierce',
    'James Buchanan', 'Abraham Lincoln', 'Andrew Johnson', 'Ulysses S. Grant',
    'Rutherford B. Hayes', 'James A. Garfield', 'Chester Arthur',
    'Grover Cleveland', 'Benjamin Harrison', 'William McKinley',
    'Theodore Roosevelt', 'William Howard Taft', 'Woodrow Wilson',
    'Warren G. Harding', 'Calvin Coolidge', 'Herbert Hoover',
    'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower',
    'John F. Kennedy', 'Lyndon B. Johnson', 'Richard Nixon', 'Gerald Ford',
    'Jimmy Carter', 'Ronald Reagan', 'George H. W. Bush', 'Bill Clinton',
    'George W. Bush', 'Barack Obama', 'Donald Trump'
    ]
    for name in presidents:
        page = wikipedia.page(name)
        # text = page.summary
        text = page.content
        with open(name + '.txt', 'w') as f:
            f.write(text)

# def format_filename(president_name):
    # return '/tmp/president_data/' + '_'.join(president_name.lower().split(' '))(
    #      + '.txt')

if __name__ == '__main__':
    presidents_to_texts()
