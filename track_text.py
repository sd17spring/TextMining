"""
Extends the markovify Python module (https://github.com/jsvine/markovify) in order to filter text
for common things we don't want in track titles.
"""

import markovify
import re


# Extends NewlineText because that works best for the format of our data
class TrackText(markovify.NewlineText):

    def word_split(self, sentence):
        """
        Splits a string of words, and removes parts that are unwanted
        """
        removed_words = ['feat.', 'remastered', 'remix', 'edit']  # These are common words that we don't want
        punctuation = '&()\"[]:'  # Used to remove random punctuation from track titles

        words = re.split(self.word_split_pattern, sentence)
        filtered_words = [word for word in words if word not in removed_words]  # remove filter words
        # Remove filtered puncutation
        filtered_text = [''.join([char for char in word if char not in punctuation]) for word in filtered_words]
        return filtered_text

    def make_fixed_length(self, sentence_length, **kwargs):
        """
        Makes a sentence of a fixed number of words by combining multiple Markov chains.
        """
        out_sentence = ''
        cur_len = 0 # The current length of the track name
        while cur_len < sentence_length:
            sentence = self.make_sentence(**kwargs)
            out_sentence += sentence + ' '
            cur_len = len(out_sentence.split())
        if len(out_sentence.split()) > sentence_length:
            out_sentence = ' '.join(out_sentence.split()[:sentence_length])
        return out_sentence
