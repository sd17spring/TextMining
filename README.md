# Twitter Sentiment Analysis and Visualization
This program allows users to choose two twitter users and are given a graph of the resultant sentiment on a scale of -1 to 1. This scale is based off of [VADER (Valence Aware Dictionary and sEntiment Reasoner)](https://github.com/cjhutto/vaderSentiment) which is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.

## Implementation
Using the Twitter API, the `data_grabber` program took two prompted twitter handles, and gathered 200 tweets for each. This data was stored in two text documents for easy access later. After grabbing the data, the program finished by calling `text_analyzer.main()` with the user names.
### Text analyzer
