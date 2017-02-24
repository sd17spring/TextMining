# TextMining
This is the base repo for the text mining and analysis project for Software Design at Olin College.
## by Margaret Rosner
### Project Overview 
I combined two books, Robinson Crusoe and Herland, and used a Markov Chain to generate random sentences/quotes from the words of the combined texts. I wanted to see what the product of the two books would generate and I hoped to create some interesting sentences. In completing this project I hoped to learn how to think through a project on my own because up to this point there has been a lot of scaffolding and I wanted to focus on how to think through a project. 

### Implementation 
  I implemented my program by downloading the two texts that I had chosen to focus on and then quickly stripped the combination of the two texts of all punctuation and converted every letter in the string of words to lowercase and made sure that everything was separated by a space. I then chose to use the enumerate function because it would give me an index for every word in the combined text and I used enumerate to go through the text and create a dictionary that took in each unique word as a key and stored the word that immediately followed it in the text as a value. By using enumerate I was able to easily add the next indexed word into the value section of the dictionary. 
	After I had created a dictionary of all the words in the text, I then created a function that would generate a sentence of a specific length. In this function I randomly chose a starting key which I then used to randomly choose a word from the value of the key. I then added that value to a string and made that word my new key. Once I had reached a string of my desired length I return the string in quotation marks.
### Results 
  I chose to use a Markov Chain to create sentence from a combination of the books Herland and Robinson Crusoe because both books were written in the early 18th century and document men on a journey. The interesting piece about these two texts is that the journeys of these men take place in very different contexts. Robinson Crusoe is stranded on an island and the book focuses on his struggle to conquer his environment. On the other hand, Herland tells the story of a group of men who journey into the unknown in an attempt to find an undiscovered all female society and later are imprisoned by the women until they learn more about the world. Herland focuses on the themes of love and the definition of femininity. 
	I thought that because these two books both are about men on journeys, but with very different themes, the sentences generated randomly would be interesting and weird. See a smattering below.
  
"in cold like this in time as i found for."

“great forests looked round me no effort applied myself a quarter of my head for he called my strength the.”
“creatures were armed we being murdered and all good things.”
"I made snares to son i inquired if burglars try to believe."
"so that they were decimated by the wall and begged lazily."
"to take much better import some merchants for the guns of bread i that price was by this savage that which i."
"approach seemed to mere nature should happen that went in further into the person but this line i must have a matter."
"cautiously and wisdom justice of cats were if i did not at my condition i sat down immediately driven by."
"remedy for as follows three killed one word i could come that and that if founded on the country seat which i was ashore but did not so that in less a habitation."
"as it to lie down and loaded my pistols with my story at it to me governor what became but the knees and pointing to us if i asked him what he meant."
"to sleep had a pitch of labor too with me for home in the way to this retreat i slept all that part i hastened to their darts or deliverance which."
### 



