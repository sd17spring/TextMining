# TextMining - EPL Twitter Sentiment Analysis


## Project Overview

This projects uses Twitter and Wikipedia as the data source for collecting the Tweets of all of the [English Premier League Players](https://twitter.com/BBCSport/lists/premier-league-players/members?lang=en), starting from 13 August, 2016 (First Day of Season) to 18 Feb, 2017. <br>
A [Sentiment analysis(NLTK)](http://www.nltk.org/howto/sentiment.html) of Tweets was conducted to find out if there exists any relationship between the current league standing and the result of the sentiment analysis of each club. <br>
> *<i>"Twitter is a Waste of Time"</i>, Sir Alex Ferguson, the Legendary Former Manchester United Manager*

Let's find out whether Sir Alex Ferguson was right or not!

## Key Components / Implementation Details

##### Two Main Components of Text_Mining.py
  * ##### Pickling Data from Twitter and Wikipedia <br>
    Data collected from these sources as pickles are :
    1. <u>*Twitter User Instances*</u> of members of <i>Premier League Twitter List</i>
    2. <u>*Twitter Status Instances*</u> from the Collected User Instances
    3. <u>*Tweet Texts*</u> from the Collected Status Instances
    4. <u>Current Clubs</u> of players from Wikipedia (BeautifulSoup)

  * ##### Sentiment Analysis of Tweets
    1. Sentimental Analysis(NLTK) with all Tweet Texts of an Individual Player
    2. Summation of the individual NLTK results to analyze individual Club Sentiment
    3. Displays EPL Clubs sorted by values of NLTK Sentiments.
       (compound, negative, neutral, positive)

##### Data Structures Used :
1. List is used to store User and Status Instances.
2. Dictionary using the names of the player as *keys* is implemented to store the followings as *values*:
    * Texts
    * Current Clubs
    * List of Individual NLTK Sentiments
    * List of Club NLTK Sentiments <br>

Lists were used because the Twitter Package returned most values in list of instances.<br>
Dictionaries are very useful with this project because all players and clubs have unique names that qualifies as keys. Searching(hashing) through a big set of data is way more efficient when implemented with a dictionary.


##### Design Choices :
1. I chose to take a SUM of all Sentiment Analysis results instead of taking an average of the values because I believe that frequency of Twitter usage does effect the overall result.
2. Although saving only the names of the Twitter instances of the players to different function is definetely more efficient considering memory usage, I chose to save all the instances of players in case I need to modify the codes later since these instances allow access to more diverse set of data.


## Results:

#### Here are some examples.

##### Tweet Texts Example(Player: Loris Karius)
```
['Gettin ready for another session  training LaManga Spain LK1 ', 'Back to winning ways  Well done everyone Great atmosphere at Anfield today  WeAreLiverpool LIVTOT YNWA  ', 'Ready for tomorrows game under the Anfield lights  LIVSOU EFLCup YNWA LK1  ', 'Next FA Cup round unlocked  Congrats  for scoring the winner  PLYLIV YNWA CleanSheet LK1  ', 'Rollin into the weekend Big game on Sunday MUNLIV  LK1 LFC ', 'Happy birthday bro  Stay the way you are  smile friends lfc LK1 EC23 ', 'Happy 30th birthday   Have a good one felizaniversario YNWA LFC', 'Not the result we were after but great to see so many young players on the pitch  LIVPLY YNWA LK1  ', 'Little stroll through the city  LK1 ', 'Such an important win in the last game of the year Wish everyone a Happy New Year  WeAreLiverpool LIVMCI  ', 'Good job boys  41 home win and back on the 2nd place Now full focus on the last match of the year against City  YNWA LIVSTK ', 'All preparations done  Christmas can come  How do you spend your holidays  xmas LK1 ', 'Very important derby win for us tonight But my thoughts are with the victims in my homeland Germany  Berlin ', 'Auf gehts   ich drcke euch die Daumen  Mainz05 M05FCB Bundesliga', 'Nice afternoon out there  sun enjoy LK1 ', 'Training preparation inprogress BOULIV YNWA LK1  ', 'YES boys  Were into the semi finals Congrats to  for becoming  s youngest goal scorer ever  LIVLEE EFLCup YNWA', 'Get well soon Coutinho I hope its not too bad  YNWA LFC', 'Important win  Glad we were rewarded for our efforts Thanks for your visit boys  CleanSheet YNWA  ', 'I had great fun visiting the schools tournament at Liverpool academy last week  LFC Liverpool LK1  ', 'Good performance but unlucky not to take all three points On to the next one  CleanSheet SOULIV YNWA  ', 'Fresh new haircut  perfectly in time for the return of the  at the weekend  Liverpool LK1 ', 'Its international break but the hard work continues training LFC LK1  ', 'Happy birthday    I wish you all the best and hope you enjoy your day my friend YNWA seeyousoon ', 'Spending a day off in Germany  InternationalBreak Home Fashion LK1 graceworldclo  ', 'Great weekend for us  Lets continue like this after the international break  stayfocused YNWA LK1  ', 'Tabletoppers  Amazing win and great performance from the team We are Liverpool  LIVWAT YNWA LFC  ', 'Focus on your goals amp dont look in any direction but ahead  YNWA LFC LK1  ', 'This is just unfair  Youre a fighter   Im sure youll come back stronger once again We believe in you  YNWA ', 'Nice afternoon in the city  relax walk Liverpool LK1  ', 'Crazy first half but in the end a welldeserved win for us Great performance lads  CRYLIV YNWA LFC  ', 'Off we go next stop London  Important away game tomorrow  CPFCLIV Boys YNWA LFC  ', ' days until were back in action   LK1  ', 'Congrats to your comeback   welcomeback LIVTOT ', 'Well done boys were in the next round  Good night from Anfield  LIVTOT EFLCup YNWA LFC  ', 'Chin up bro   Im sure youll come back even stronger than before  allthebest comebacksoon ', 'Yesss  Home win and now were tied at the top of the  table  LIVWBA LFC YNWA  ', 'First clean sheet in the    Amazing to play in front of all you Reds  LFCvMUFC YNWA  ', 'Im more than excited for tomorrows clash at Anfield  Lets make it a special night  YNWA LFCvMUFC  ', 'Its WorldDogDay so I took Hugo for an extralong walk mansbestfriend dog LK1 Liverpool ', 'Theres always a reason to smile   even though theres no  this weekend  WorldSmileDay LK1 LFC ', 'This one is very nicely done Keep it up  goodjob drawing art portrait LK1 LFC thekopartstudio ', 'Difficult game today but a very important victory  Thanks to our travelling fans SWAvLFC YNWA LK1  ', ' LK1 relax Liverpool UK ', 'Back home from the training ground now its time for fifa17  LK1 LFC YNWA  ', 'Listening to good music is the best way to find focus on matchday  LK1 ready perfectweekend  ', '51 home win  Not a bad start to my  career Massive team performance LFCvHCFC YNWA  ', 'Working at full throttle in todays training  Were back at Anfield on Saturday  LFCvHCFC YNWA LK1  ', 'An indescribable feeling to be back  Clean sheet  Next round  Successful comeback  WelcomeBackEmre ', 'Matchday  Its time for some League Cup action at Derby Were ready  lets go for it  YNWA DCFCvLFC  ', 'Great team effort today boys  Back to Liverpool with three points  CFCvLFC bigwin YNWA ', 'Big game tonight Weve been working hard during the week now its time to make it count  CFCvLFC YNWA  ', 'Whos that on the cover of Magazine  Check out the stories inside  LK1 fashion football inspiration ', 'Its interesting being linked with a person youve never heard of before Please stop inventing stories and let us do our work  annoying', 'Enjoying a nice day off after Saturdays great game at Anfield priceless LK1 LFC  ', 'Great to be back in the squad   it was simply amazing to experience the support of the fans at Anfield today   YNWA LFCvLCFC ', 'Dont let your dreams just be dreams  PremierLeague LK1 FindFocus ZNE  ', 'My very first time at the Anfield  Cant wait to play there in front of the fans  LFC LK1  ', 'Hugo and I had a nice lunch today  Now off to the training ground  WorkHard LK1 Liverpool  ', 'Finally back in full training action  GreatFeeling LK1 LFC  ', 'Im excited to see what next week brings  Wish you all a nice Sunday  LK1 Liverpool ', 'RT   Theres nothing Im scared of on why hes ready for the   ', 'RT  Plenty of positivity right now for this man   gives an injury update  ', 'Recovering from a successful surgery  Wires are removed from now on things can only move upwards LK1  ', 'Amazing to be back catching some balls Would be easier to use the second hand as well  training focus  ', 'Short rest at Melwood Ill use the international break to continue the hard work for my comeback   LK1  ', 'Yesssss that goal definitely comes at the right time Well done James  Keep on going guys  THFCvLFC ', 'Getting better day by day Ill slowly return to training routine once the wires have been removed next week ', 'Welldeserved 50 win at Burton and a good performance by the team  Cant wait to be back on the pitch with the lads  BAFCvLFC ', 'SundayFunday with my bros Gold silver and bronze medal for us LiverpoolONE Liverpool LK1  ', 'Good to be back in training with the   I hope I can wear those gloves soon again  LK1 Melwood  ', 'Well any good comeback needs countless gym hours first LFC DontStop HardWork training  ', '43 away win against Arsenal  What a way to start the season  Well done boys  YNWA ARSLIV  ', 'What a performance  Im  proud of the lads Turned that game around     ARSLIV AFCvLFC ', 'Come on boys   Great goal Adam ARSLIV AFCvLFC', 'Yesss such an important goal Nice one Coutinho  ARSLIV AFCvLFC ', 'Come on reds Lets go  ARSLIV AFCvLFC ', 'Finally  starts for us Cant wait for the kickoff Come on Liverpool YNWA AFCvLFC  ']
```

##### Individual Sentiment Analysis example
```
{Loris Karius: [36.216300000000004, 2.003, 56.47400000000002, 19.526000000000007] }
{Lamine Koné: [33.57890000000002, 3.53, 87.76100000000002, 25.706999999999994] }
{Antonio Valencia: [14.804799999999998, 1.4779999999999998, 64.40599999999999, 8.116000000000001] }

```
##### Team Sentiment Analysis Results
```
  {'AFC Bournemouth': [17.781400000000005, 2.816, 38.730999999999995, 12.453999999999999],
  'West Ham United': [31.2421, 1.962, 83.33300000000001, 19.704],
  'Southampton': [160.524, 13.452999999999998, 372.30600000000004, 115.245],
  'Chelsea': [226.45769999999993, 14.091000000000001, 438.946, 150.96599999999998],
  'Everton': [99.8178, 10.213000000000001, 337.52699999999993, 75.25899999999999],
  'Arsenal': [320.34680000000003, 26.116, 872.086, 221.801],
  'Watford': [31.428300000000004, 2.967, 188.93699999999998, 25.095],
  'Leicester City': [81.4855, 4.873, 173.072, 59.057],
  'Tottenham Hotspur': [272.8685999999999, 11.057, 591.123, 178.82],
  'Manchester City': [105.24719999999998, 10.818, 296.73699999999997, 67.44699999999999],
  'Stoke City': [286.24909999999994, 26.766, 576.4929999999999, 204.73900000000003],
  'Burnley': [6.3087, 1.303, 16.861, 4.836],
  'Middlesbrough': [74.9784, 3.988, 185.50300000000001, 53.51000000000001],
  'Sunderland': [98.71300000000002, 10.615, 254.84300000000007, 67.538],
  'Swansea City': [70.8638, 7.290000000000001, 179.22000000000003, 50.489999999999995],
  'Hull City': [7.638599999999999, 1.499, 21.9, 5.6],
  'West Bromwich Albion': [12.290799999999999, 0.902, 21.218, 7.880000000000001],
  'Liverpool': [190.58339999999998, 12.847999999999999, 370.33799999999997, 119.81200000000001],
  'Manchester United': [390.6162000000001, 32.54599999999999, 888.55, 271.906],
  'Crystal Palace': [181.08800000000002, 15.683000000000002, 426.36, 126.955]}
```
##### Comparison Table

No. |League Standing | Compound | Negative | Neutral | Positive
---  | -------------  | -------- | ------- | ---------| --------
1|Chelsea |Man.United|Man.United|Man.United|Man.United
2|Man.City | Arsenal  | Stoke City  |Arsenal  | Arsenal
3|Tottenham | Stoke City | Arsenal   | Tottenham | Stoke City
4|Arsenal | Tottenham| Crystal Palace  | Stoke City  |  Tottenham
5|Liverpool|Chelsea| Chelsea  | Chelsea   | Chelsea
6|Man.United|Liverpool| Southampton | Crystal Palace  | Crystal Palace
7|Everton |Crystal Palace| Liverpool  | Southampton  | Liverpool
8|West Brom| Southampton | Tottenham  | Liverpool | Southampton
9|Stoke City|Man.City| Man.City  | Everton | Everton
10|West Ham|Everton | Sunderland | Man.City | Sunderland
11|Southampton| Sunderland  | Everton  | Sunderland  | Man.City
12|Burnley| Leicester| Swansea City  | Watford  | Leicester
13|Watford | Middlesbrough | Leicester  | Middlesbrough  | Middlesbrough
14|Bournemouth| Swansea City | Middlesbrough | Swansea City | Swansea City
15|Swansea City| Watford | Watford   | Leicester  | Watford
16|Middlesbrough |West Ham| Bournemouth  | West Ham |West Ham
17|Leicester |Bournemouth| West Ham | Bournemouth | Bournemouth
18|Hull City| West Brom  | Hull City  | Hull City | West Brom
19|Crystal Palace| Hull City | Burnley   | West Brom  | Hull City
20|Sunderland| Burnley  | West Brom  | Burnley | Burnley


Looking at the comparison table, we notice a few interesting trends.

1. We observe that while there are some slight differences between different types of sentiments (compound, negative, neutral, positive), the pattern stays reasonably similar for these sentiments. This probably results from taking the sum of all individual values without considering the average.
2. We observe that the most frequently sentiment-wise top ranked club is Manchester United, but it's only ranked at #6 in the current league standing. While the dominant sentiment ranking for Manchester United might indicate that the ManU Players are the most active Twitters, it might also indicate that Sir Alex Ferguson was indeed right.
3. We observe that Chelsea, the top ranking team in current league standings, ranks only #5 for all the sentiment analysis. This might also indicate that Sir Alex Ferguson was indeed right
4. However, more carefully structured analysis needs to be conducted in order to acquire statistically trustworthy data. These trends are just for fun at the moment!


### Reflection

What went well with this project was that I successfully completed the anaylsis that I planned at the beginning of this project. Also the initial outline of the functions turned out to be quite accurate and useful, although I had to add some extra functions that I had not thought at the planning stage.<br>
What didn't go well is that it was difficult to create reasonable doctest strings for functions that deal with a collection of big data. Dealing with the pickled data made the unit testing process even more difficult. I ended up not writing any doctests because I didn't feel the necessity of making any after I was done with the project. I probably should've created docstrings incrementally as I worked on the project.<br>
What I learned from doing this project is that there are so many cool packages and APIs out there for python and that reading package documentations really help a lot when actually implementing the idea down with codes. Overall, this project taught me the joy of text mining!
