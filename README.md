# Mini Project 4: Text Mining
## Software Design Spring 2017
### Gracey Wilson

### Project Overview

I chose to analyze the script of Shakespeare's Romeo and Juliet. Specifically, I was curious how often characters spoke on the comparative metric of gender. My goal for the project was to develop some numbers and perhaps a graphic or two comparing how often male vs. female characters speak in the play. From a software design perspective, I also wanted to practice structuring a program on my own without any guiding scaffolding, and being able to justify the choices I made as the process moved forward. To gain access to the text and work with it repetitively, I saved a local copy of the play from the Project Gutenberg website using Python's pickle module.

### Implementation

As mentioned in the project overview, I used Python's pickle module to gain a local copy of the text from the Project Gutenberg website. I chose for the return values of most functions to be in the form of dictionaries that map the way each character is referred to in the text (their abbreviated character name) to their gender and the number of times they speak. The main actions of the program are counting the number of characters who speak in the script by gender, counting the number of times each of those characters speaks, and finding the average number of times gendered character speaks.

I tried to make most functions as general as possible in the hopes that the program could be used on other text files, especially plays. For instance, I included a text file as an input argument for all the functions I could. However, there are still parts of the program that are very specific to the text I chose to work with. For instance, when I came across a few character names that consist of two words rather than one, I hard-coded the program to recognize them. If I were to use this program with another text file, I would need to consider in what format those characters are referred to and perhaps do some specific hard coding to handle any outliers in that specific case.

### Results

On the most basic level, when comparing the average number of times all male characters speak to the average number of times all female characters speak, the female characters actually speak more than the male characters. However, it's worth noting that there are only 4 female characters, one of whom is Juliet, while there are 23 male characters, several of whom are servants with less than 5 lines, which likely skewed the averages.

In order to get more useful but perhaps also more subjective data, we can compare characters individually based on the size of their role in the play (i.e. Romeo vs. Juliet, the patriarchal figures vs. the matriarchal figures, etc.). Below is a bar graph showing a few of these comparisons:


![alt text](https://github.com/graceyw/TextMining/blob/master/Maincharacters_bargraph.png "")


Because there are only 4 female characters, we actually run out of characters of equal standing to compare; many characters such as Benvolio (shown above), Tybalt, the Prince and many others do not have female counterparts. What's especially interesting is that when the play was written, all the characters would have likely been played by men anyway.

From this kind of data we cannot necessarily draw strong conclusions on whether male characters in the play generally speak more than female characters. However, assuming male and female characters speak on average for similar lengths of time (more about testing that assumption in the following section), we *can* say that at any given time in the play, it is substantially more likely for a male character to be speaking than a female character.

### Reflection

Overall, I feel I was successful in making progress on my learning goals during this project. I practiced tackling a project without any given scaffolding, managed to answer my questions using the limited skills I have in Python, and strengthened the scope of those skills along the way. In future projects I aim to practice thinking out the whole script and what each function will do before beginning to write. I believe this will help me foresee issues and design better programs before I get in too deep.

If I were to continue this project, I would be interested in tracking how many words each character says rather than just how many times they speak because some of the characters might speak less than 20 times, but often give a 20-line soliloquy, while others might only say a line or two. If instead or in addition I wanted to optimize the work I did during this iteration of the project, I would also be interested in trying out a weighting system for each character (i.e. main characters' voices carry more weight in the overall average than supporting characters) in order to get more relevant results than simply an average of all the times the characters speak.

In conclusion, I enjoyed working on this project and am looking forward to continued learnings - both about 16th century literature, and about software design!
