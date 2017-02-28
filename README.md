# TextMining

This is the base repo for the text mining and analysis project for Software Design at Olin College.

## Project Write-Up

### Part l: Project Overview

I used data from gutenburg.com for this project. From there, I took books from the front page that have the word adventure in the title. I hoped to analyze these books by comparing the language used in them to see if they shared any common themes, and wanted to see how many times they actually talked about adventure. To do so, I parsed the text using the nltk package and created a histogram of the number of times each word was used. Lastly, I found which words were unique to each and how many times ‘adventure’ appeared in each.

### Part ll: Implementation

The major components of the code for this project were the text preparation, the text analysis, and the data analysis. For the text preparation, I first had to cut off the text at the beginning and end of the book that was added by project gutenberg. The rest of the text preparation was done mainly with nltk, which broke the single string into a list of strings for each individual word or punctuation.  Then, I had to get rid of extraneous punctuation and cut off punctuation that found its way into the strings that were supposed to just be words.

For the text analysis, I took the list of words for each book and made a histogram with the number of times that each word appeared. Then I sorted the histogram by its values so that it was organized from most common to least common words. After that, I took the histograms from both books and created two new lists of the top 15 words in each list that don’t appear in the other book. The point of this was to find the most common unique words in each book to give a general feel of the unique theme of the book. For data analysis, I found the percent of the words in each book that were unique from the other because I was curious how similar each book was to the other.

The toughest design decision that I made for this project was figuring out which source to use for my text. I originally wanted to use twitter, but ended up running into a ton of problems with the secret keys that made it impossible to download the data. In the end, I decided to switch to using data from the gutenberg project because it was easier to access and easier to save. This allowed me to focus more of my efforts on the implementation of the project.

### Part lll: Results

The books that I chose for this project were Alice’s Adventures in Wonderland and The Adventures of Tom Sawyer. I chose them because they both were both children’s books about adventure, but had a male and a female main character. I was curious how both books were similar and different in themes and how much actual ‘adventure’ was in them, and if that could be correlated to the gender of their main characters.

From the list of 15 most common unique words, I found that the most common in Tom Sawyer (that weren’t misspellings of contractions) were: boys, reckon, village, town, cave, and men. For Alice in Wonderland, they were: tea, cook, pool, gloves and soldiers. I found it interesting that in the book with the male protagonist, some of the most common words were directly about men or more ‘manly’ things, but in the book with the female protagonist, the words were related to cooking or feminine things (except soldiers). Additionally, I found that the word adventure was used 14 times in Tom Sawyer, but none in Alice, implying that the authors may have only viewed Tom’s adventures as true adventures, and not Alice’s.

### Part lV: Reflection

This project was not my strongest this semester. A big struggle was that I was very sick during the entire time that it was assigned to when it was due, and thus got very behind with work. Due to that, I was not able to spend as much time experimenting with different methods of text analysis as I had hoped to be able to. To improve the project, I would do something with sentiment analysis around the instances of the word adventure, and possibly analyze more books to see if the trends I found occur again.
