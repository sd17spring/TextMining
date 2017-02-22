# Spotify Text Mining: Random Song Name Generation

**NOTE:** the Project Writeup for this project is located in the repo, in writeup.md.

This Python script generates random song names of a particular genre by using Markov chains.
Requires: Spotipy, numpy, matplotlib

Usage: `python3 spotify_scrape.py "Genre Name"`

Optional arguments:

`--fixed`: Generates song titles with lengths distributed according to the length distribution of the genre.
`--graph`: Creats a histogram of song title lengths for the genre.
