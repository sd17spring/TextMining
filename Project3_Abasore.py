
import requests
import string


"""
Project Plans: to sort the requencies of words for each book by Jane Austen. Then, adjust with ratio for size of book. 
Compare her most frequent words from the beginng,middle, and end of her career. 
"""


def adjust_factor(max, freq):
	"""
	take frequency and max frequency as an input and makes an adjustment ratio and stores it in a new dictionary
	"""
	output = {}
	for w , v in freq.items():
		output[w] = v/max[0]
	return output

def skip_first(text):
	for line in text:
		line = line.replace('-',' ')
		line = line.replace('_',' ')
		if line.startswith('*** START'):
			break

def clean_up_and_sort(filename, skip):
	"""
	removes the header from a text file and cleans out all the /n and like characters.

	"""
	#using the string method of startwith to find the end of the header
	fin = open(filename)
	hist = {}
	if skip:
		skip_first(fin)
	
	for line in fin:
		#this is the basic function that makes the histogram
		line = line.replace('-',' ')
		line = line.replace('_',' ')
		to_take_off = string.punctuation + string.whitespace
		for word in line.split():
 			#this divides each word up at the spaces, you can put anything you want to split at, a helpful one would be the \n new line
			word = word.strip(to_take_off)#strip only takes it off the end
			word = word.lower() #makes it lower case
			hist[word] = hist.get(word, 0) + 1 #this is a simple way to count the frequencies. get has default to what you se it equal to (this case 0) unless it already has a value. no matter what though, it gets a +
	return hist
		

def count_freq(hist, number = 10 ):
	"""
	countes the frequency of each word and stores it in a dictionary with the word as the key and the frequency as the
	value. A second dicionary is make the stores the word as the key and teh ratio as the value.
	and ratio as the second value.
	"""
	output = []
	for w, v in hist.items():
		output.append((v, w)) #Here I am just making a list of all the pairs in the dictioanry, this will keep it so every word is only done once
		output.sort() #this updates the current value of output to be in order
		output.reverse() #this makes it so you get the highest number first
	new = adjust_factor(output[0], hist)
	adj_output = []
	for nw, nv in new.items():
		adj_output.append((nv,nw))
		adj_output.sort()
		adj_output.reverse()
	return adj_output

def process_text(filename, name):
	"""
	Use lower branch functions to calculated the adjected frequencies of words.
	Returns, a list of the top 10 words in the book.
	Input: the book variable name to process.

	"""
	normal_freq = clean_up_and_sort(filename, skip=True) #sends the file to opening function witch processes it and send each line to be processe
	#count_freq also actually and calls the adjustment function to adjust for size
	adjusted = count_freq(normal_freq)
	textfile.write('\n')
	textfile.write(name)
	textfile.write('\n')
	for i in range(5):
		textfile.write('\n')
		for w in adjusted[i]:
			output = ''
			output += str(w)
			output += '\n'
			textfile.write(output)



textfile = open("Jane_Austen_freq.odt", "w")
process_text('sense.txt', 'Sense and Sensibility-Start-1811')
textfile.write('\n')
process_text('northabby.txt', 'Northwestern Abby-Start-1811')
textfile.write('\n')
process_text('love_and_friendship.txt', 'Love and Friendship-Start-1811')
textfile.write('\n')
process_text('Pride.txt', 'Pride and Prejudice-1811-1814')
textfile.write('\n')
process_text('park.txt', 'Mansfield Park-1811-1814')
textfile.write('\n')
process_text('persuasion.txt', 'Persuasion-1814-Death')
textfile.write('\n')
process_text('Susan.txt', 'Lady Susan-1814-Death')
textfile.write('\n')
process_text('Emma.txt', 'Emma-1814-Death')
textfile.close()


