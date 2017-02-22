# TextMining - EPL Twitter Sentiment Analysis


### Project Overview :

This projects uses Twitter as the data source for collecting the Tweets of all [English Premier League Players](https://twitter.com/BBCSport/lists/premier-league-players/members?lang=en) starting from the first day of the season(13 August, 2016) to 16 Feb, 2017. [Sentiment analysis(NLTK)](http://www.nltk.org/howto/sentiment.html) of Tweets was conducted to find out if there exists any relationship between the league standing and the result of the sentiment analysis of each club. Let's figure out whether Sir Alex Ferguson, the legendary ManU manager who said <i>"Twitter is a waste of time"</i> was indeed right or not!

### Implementation [~2-3 paragraphs]  


Teams -> Players (dictionary)
ex) {ManU : "@Paul Pogba"}


Players -> \tweets\player_name.txt (contains all tweets, pickled)

for each player, for each line -> player_tweets.append(text)
ex) paul_pogba.append.text(blahblahbalh)


Team -> (dict) analysis result[compound, neg, neu, pos]
ex){ManU : [compound, neg, neu, pos], ManCity: [compound, neg, neu, pos]}

total sum of all these values. Sort by each category and see if there is any relationship.


Describe your implementation at a system architecture level. You should NOT walk through your code line by line, or explain every function (we can get that from your docstrings). Instead, talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.

Results [~2-3 paragraphs + figures/examples]

### Present what you accomplished:

If you did some text analysis, what interesting things did you find? Graphs or other visualizations may be very useful here for showing your results.
If you created a program that does something interesting (e.g. a Markov text synthesizer), be sure to provide a few interesting examples of the program’s output.
### Reflection [~1 paragraph]

From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?
