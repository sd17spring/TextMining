import twitter
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy

def convert_date_to_day_of_year(date_list):
    '''
    This converts dates of tweets to days after Jan 1st 2016. This allows the
    data to be plotted in an easier and more recognizeable fashion.
    '''
    #print(date_list)
    #to avoid 12 if loops, the data was packaged into lists.
    #These lists can be referenced to figure out which day of the year it is
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    day_after_Jan_1st = [] #empty list initialized. Use to store final day values
    #the for loop calculates the day value of each date
    for items in date_list:
        #finds the month, day, and year from the date string
        month = items[0:3]
        day = items[4:6]
        year = items[15:]
        #finds the index of the month within the month_list
        index_of_month = int(month_list.index(month))
        #uses the index of the month to figure out the day value
        day = int(day) + day_list[index_of_month]
        #If the year is 2017, it is at least a year after Jan 1st 2017, so
        #add one years worth of days.
        if year == '2017':
            day = day + 365
        #finally add the day value to the list
        day_after_Jan_1st.append(day)
    return day_after_Jan_1st

def run_sentiment_analysis(list_of_tweets):
    '''
    This function runs sentiment analysis on a list of tweets and returns
    a list of that analysis
    '''
    #initializes an empty list that the sentiment can be put into
    tweet_sentiment_list = []
    #for loop goes through each item in the list of tweets and analyzes it
    for items in list_of_tweets:
        #finds the first item in the list
        tweet = items
        #uses SentimentIntensityAnalyzer to analyze data
        sentiment_analyzer = SentimentIntensityAnalyzer()
        tweet_sentiment = str(sentiment_analyzer.polarity_scores(tweet))
        tweet_sentiment_list.append(tweet_sentiment)
    return tweet_sentiment_list

def make_sentiments_to_float(not_float):
    '''
    After the sentiments come out of the sentiment analyzer they range between 2
    and 4 digits long. To maintain the whole length of the number, 4 places were
    pulled every time and it was stripped down to the actual number and then
    converted to float
    '''
    #strips comma, space, and single quote out
    not_float2 = not_float.strip(', \'')
    if not_float[-1] == '}':
        #takes the bracket out if it exists.
        not_float2 = not_float[:-1]
    #converts to float
    now_float = float(not_float2)
    return now_float

def make_tweet_sentiment_list_plotable(tweet_sentiment_list):
    '''
    This function takes a list of sentiments and takes out the words but leaves
    the numbers. This way the sentiments can be plotted. It returns a list of
    3 lists, each containing the sentiment of either pos, neu, or neg.
    '''
    #initiales empty list for sentiments
    positive_sentiment = []
    negative_sentiment = []
    neutral_sentiment = []
    #The loop calculates the actual number values for each sentiment
    for items in tweet_sentiment_list:
        #parses string based on the title of each section
        neg_index = items.find('neg\':')
        pos_index = items.find('pos\':')
        neu_index = items.find('neu\':')
        #parses strings in relation to titles.
        neutral = items[neu_index + 6: neu_index + 12]
        negative = items[neg_index + 6: neg_index + 12]
        positive = items[pos_index + 6: pos_index + 12]
        #at this point values are separated, but some have extra spaces, etc.
        #after them. To get rid of these and convert to float values,
        #the function above is called.
        neutral2 = make_sentiments_to_float(neutral)
        positive2 = make_sentiments_to_float(positive)
        negative2 = make_sentiments_to_float(negative)
        #adds the float values to the lists
        neutral_sentiment.append(neutral2)
        negative_sentiment.append(negative2)
        positive_sentiment.append(positive2)
    #returns a list of lists. These include positive, negative, and neutral
    #sentiment values
    return([positive_sentiment, negative_sentiment, neutral_sentiment])

def average_sentiments(tweet_data, groups_per_year):
    '''
    In order to make the data less messy, this funtion is used to average the
    tweets negative and positive values. This makes the trends much easier to
    see
    '''
    #finds the number of days for each group
    days_per_group = 365/groups_per_year
    #finds the day and sentiment list
    dates = tweet_data[0]
    sentiments = tweet_data[1]
    #finds the highest day to see how many groups to make
    highest_day = dates[1]
    number_of_groups = int(highest_day/days_per_group)
    #starts a list of groups, with the first starting on day 0
    group_list = [0]
    #initializes a list for the average sentiments
    list_of_average_sentiments = []
    #for loop ssets up a loop of all the groups
    for groups in range(number_of_groups+1):
        previous_group_day = group_list[groups]
        group_list.append(int(previous_group_day+ days_per_group))
    #calls
    positive_average = put_sentiments_into_groups(sentiments, number_of_groups, dates, group_list,  0)
    print(positive_average, "PS")
    negative_average = put_sentiments_into_groups(sentiments, number_of_groups, dates, group_list, 1)
    print(negative_average, "N")
    return([group_list, [positive_average, negative_average]])


def put_sentiments_into_groups(sentiments, number_of_groups, dates, group_list, int):
    #initializes a list to store all the values per group in
    sentiment_averages = [0]*(number_of_groups+1)
    print(sentiment_averages)
    date_index = 0
    #for negative values
    items_in_each_group = [0]*(number_of_groups+1)
    for current_tweet in sentiments[int]:
        group_not_found = True
        date_index = date_index + 1
        group_list_index = 0
        while group_not_found:
            if dates[date_index-1] <= group_list[group_list_index]:
                sentiment_averages[group_list_index-1] += current_tweet
                group_not_found = False
            group_list_index +=1
        items_in_each_group[group_list_index-2] += 1
    print(items_in_each_group)
    print(sentiment_averages)
    for index in range(len(sentiment_averages)):
        if items_in_each_group[index] != 0:
            print(items_in_each_group[index])
            averaged_value = float(sentiment_averages[index])/float(items_in_each_group[index])
            sentiment_averages[index] = averaged_value
            print(averaged_value)
    sentiment_averages
    return sentiment_averages

def plot_tweet(dates, tweet_sentiment_list):
    '''
    This function plots the data in a scatter plot. The data is plotted in
    the form of positive - negative score for each tweet. This gives a
    holistic score for each tweet.
    '''
    #list of trumps standing over times
    political_standing_date = [191, 196, 201, 206, 211, 216, 221, 226, 231, 236, 241, 246, 251, 256, 261, 266]
    political_standing = [42.5, 41.5, 43, 46.5, 46, 43.5, 42.5, 40.5, 43.5, 42.5, 44, 43, 42.5, 46, 45, 45.5]
    for number in range(len(political_standing)):
        political_standing[number] = political_standing[number]/60-.65
    positive_minus_negative_list = []
    #splits the list of sentiments up into positive and negative
    positivity_list = tweet_sentiment_list[0]
    negativity_list = tweet_sentiment_list[1]
    #the for loop makes a list of the positive values minus the negative values
    for items in range(len(tweet_sentiment_list[0])):
        positive_minus_negative_value = positivity_list[items]- negativity_list[items]
        positive_minus_negative_list.append(positive_minus_negative_value)
    #makes a scatter plot with dates on the x axis and the positive minus
    #the negative on the y. It also adds labels and axes.
    plt.plot(dates[11:len(dates)-8], positive_minus_negative_list[11:len(dates)-8], label = 'Positivity')
    plt.plot(political_standing_date, political_standing, color ='r', label = 'Political Standing')
    #plt.scatter(dates, tweet_sentiment_list[1], label = 'Negativity', color = 'r')
    plt.title('Average Tweet Sentiment vs. Political Standing')
    plt.xlabel('Date')
    plt.ylabel('Positivity-Negativity')
    plt.legend()
    plt.show()


def access_twitter_files ():
    '''
    This is the main function. It loads the tweets from a file so they can be
    edited without accessing twitter again. It then parses out the tweets and
    date from the other information. The data is then put through the
    other functions in the file, which analyze the data and graph it.
    '''
    #This opens the file that the other atom file created when it pulled the
    #tweets from twitter
    files = open("trump_tweets.txt", 'rb')
    tweets = pickle.load(files)
    files.close

    #this is the contents of the file which contains all the tweets, dates, etc.
    tweets = str(tweets)
    #boolean is used for while loop. When there are no more tweets it stops.
    is_another_Tweet = True
    list_of_tweets = []
    list_of_dates = []
    #while loop goes through parsing out dates and tweets from the file
    while is_another_Tweet:
        #finds the index of text and status to see where the text starts and
        #ends respectively
        tweet_index = tweets.find('Text')
        status_index = tweets.find('), Status')
        #finds the index of date to see where the date starts
        date_index = tweets.find('Created=')
        #if the index of "text" or "status" is -1 then there are no more tweets
        #and it stops the while loops.
        if tweet_index == -1 or status_index == -1:
            is_another_Tweet = False
        #finds the date and year from the string by using the "date" index
        date = tweets[date_index + 12: tweet_index - 13]
        year = tweets[date_index + 34: tweet_index - 2]
        #adds the year to the end of date. It is parsed out later
        date = date + year
        #adds the specific date to the list of dates
        list_of_dates.append(date)
        #finds the current tweet by parsing using the "text" and "status" index
        current_tweet = tweets[tweet_index+6: status_index-1]
        #takes the entire string of data that it took from the file and doesn't
        #include the tweet that was just read. This allows it to find the next
        #tweet on the next iteration
        tweets = tweets[status_index+1:]
        #adds the date and tweet to the list of all the tweets.
        list_of_tweets.append((current_tweet))
    #print(list_of_tweets)
    #this accesses the function which converts the dates to days after Jan 1st
    day_of_year = convert_date_to_day_of_year(list_of_dates)
    #this runs the sentiment analysis on the tweets.
    tweet_sentiment_lists = run_sentiment_analysis(list_of_tweets)
    #this cleans up the data so it becomes plotable
    plotable_tweet_sentiment = make_tweet_sentiment_list_plotable(tweet_sentiment_lists)
    #averages the data based on the groups_per_year variable. This makes the data less wild
    groups_per_year = 24
    average_plotable_sentiment = average_sentiments([day_of_year, plotable_tweet_sentiment], groups_per_year)
    average_dates = average_plotable_sentiment[0]
    print("AV",average_plotable_sentiment[1])
    print("AV@", average_dates)
    #print(plotable_tweet_sentiment)
    #this plots the data
    #plot_tweet(day_of_year, plotable_tweet_sentiment)
    plot_tweet(average_dates[1:], average_plotable_sentiment[1])


if __name__ == "__main__":
    access_twitter_files()
