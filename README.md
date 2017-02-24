# Wiki Game Algorithm

## Project Overview
I used Wikipedia as a source and used word frequency analysis to analyze and do work with the wikipedia data.  I hoped to create a simple algorithm for searching for articles on wikipedia through clicking links from article to article (The Wiki Game).  I hoped to create a method that wouldn't take as long as searching for the perfect route but also would be significantly better than just searching for random links.

## Implementation
My project had two major parts:  *Pulling information from Wikipedia*, and using that information to *determine the next article to pull*.

#### Pulling Information from Wikipedia
In order to pull the information from Wikipedia, I first needed to create code that downloads the html of the Wikipedia article.  The suggested way to do this was to import the Wikipedia library, which provides the markdown text for wikipedia articles.  However, with markdown I can't retrieve the correct linking information.  Thus I had to use urllib in order to get the bytes version of the html document.  From there I used *BeautifulSoup*, a library for html parsing.  This allowed me to quickly grab all the text or find links in only paragraphs / lists so as to not get the links to the settings and information items in wikipedia.  In order to specify the limitations for link grabbing I had to use some confusing and lengthy regular expressions.

#### Determine next article to pull
Once the article information was all stored on my computer along with the complete html file for future use if I ever ran over the same article again, it was time to find the link to click next / article to travel to.  To start this process I needed some way to rank which links are more important than others.  To do this, I decided that a good standard for whether a link is good or not is based on the number of times the text that represents the hyperlink (in the current article) appears in the target article.  Using the word frequency of the target document, the algorithm picks the shortest link with the highest score, this ensures it gets to bigger articles (bigger articles tend to have shorter words and smaller articles tend to have much longer titles).  Lastly some measures are taken to filter the chosen links and words.  For example, non-nouns are filtered out using the nltk package, and the algorithm doesn't circle back on its self.

## Results
The results of this program is surprisingly good for the amount of time alotted for the project.  I am pretty happy with the results.  When trying to find any pretty general topics or object with a large wikipedia page, the algorithm can very effectively find links from one thing to another in 4-6 links on average.  There are many successes of this algorithm, most notably the ability to not blow up wikipedia in order to determine the exactly fastest route.  It is more a benchmark to try to beat as a human than an optimization.

Some of the downfalls of the algorithm and program is that it can very easily become caught on specific topics, schools and political positions in particular.  Additionally many pages that one might think would link to one another, in fact don't.  For example, Darthmouth and numerous other colleges do not have links to college (in general).  There are probably numerous ways to make the search algorithm better, most likely with machine learning.  I plan to possibly do that for the 5th Mini Project, however for now, I think this is a good stopping point for this project.


Examples of program at work:
--
Enter Start Title (Capitolize): Swagger
Enter End Title (Capitolize): Electronic Dance Music
len: 81663  /  107072
0	Swagger

Searched Word: album	2
1	Swagger Gun album

Searched Word: music	147
2	1994 in music

Searched Word: dance	80
3	Mary Janes Last Dance

Searched Word: music	147
Retrieving from Files
4	Music video

5	Electronic dance music

Finished!
Found Electronic Dance Music!!
--

Enter Start Title (Capitolize): Pear
Enter End Title (Capitolize): Grape
len: 58313  /  58313
Retrieving from Files
0	Pear

Searched Word: juice	21
1	Juice

Searched Word: grape	86
2	Grape

Finished!
Found Grape!!
--

Enter Start Title (Capitolize): Quantum Mechanics
Enter End Title (Capitolize): Philosophy
len: 91193  /  163832
philosophies was already deleted
0	Quantum mechanics

Searched Word: philosophy	190
1	Stanford Encyclopedia of Philosophy

Retrieving from Files
2	Philosophy

Finished!
Found Philosophy!!
--

Enter Start Title (Capitolize): Michigan
Enter End Title (Capitolize): Discrete Mathematics
len: 36422  /  57373
Retrieving from Files
0	Michigan

Searched Word: research	9
1	Research and development

Searched Word: computer	16
Retrieving from Files
2	Computer science

3	Discrete mathematics

Finished!
Found Discrete Mathematics!!
--

Enter Start Title (Capitolize): Great Red Spot
Enter End Title (Capitolize): Cardistry
len: 11823  /  17878
0	Great Red Spot

Searched Word: book	2
1	BookJupiter

Finished!
Couldn't find anymore links in BookJupiter
--


## Reflection
This project originally started as just a project to grab the first link of a wikipedia article and continue to do that.  This quickly evolved into a wikigame player.  I am quite proud of this project and feel that a lot went well.  I learned a lot through the process of making this.

Some things I would change is that my code is mostly pretty dense and not split into multiple functions.  I definitely need to work on this "design" portion of my software design.  Additionally, there are still many of places for improvement in the project and I would very much like to try to come up with better heuristics for determining good links to click than just the word frequency of the target article.