# Reflection for text-mining project
## Noah Rivkin



Overview:

For my textmining project I am making a markov chain generator. The user finds a text online, and either downloads it or gives the program the url. The text is then used by the program to generate a markov chain, with a prefix length of 2.



Implementation:

The user first gives the program a text, using the get_text
function. the get_text fuction has perameters of (file_name, [url]). If the file already exists the program accesses the locally stored file. If it does not exist the program gets the text from the internet and pickles it. The function returns the text.

The text in used as one of the parameters in the function markovchain(seed1, seed2, length, text). The seed parameters provide a start for the markov chain, and the length parameter defines the length of the markov chain.

markovchain calls get_suffix_dict, which generates a dictionary of suffixes and their frequencies. The function is memoized to improve running speed if it is called a large number of times. A suffix is selected randomly, weighted by the frequency they occur.

Results:

My program generated a number of interesting results. A few particularly amusing ones from War and Peace, by Tolstoy, are included below.

it was something, something in passing: 
“What did you come from? Who are ‘they’? What do you shout so? You’ll frighten them!” said Nicholas. 
 
“Uncle, forgive me, darling.... Mamma, what 
does it matter to you?” 
 
“Here. What lightning!” they called 
the count went with Sónya and her late father, whom 
Malvíntseva had evidently had no 
military appointment in the 
reception room if he thought again quite clearly. “But not love which it is in this life and knows how to 
refer only to keep 
him any longer began 
to demonstrate the defects of the heroic exploit of his

Reflection:

My program works, but it is not particularly efficient. Given more time, I think I could make it run better. I messed around with the prefix length some, and found that longer prefixes led to more coherent results.