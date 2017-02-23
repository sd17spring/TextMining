from wordCreator import WordCreator
import wikipedia
python = None

python = wikipedia.page('Pythonidae')
pythonLinks = python.links

pythonWordGen = WordCreator(wordList=pythonLinks)
print(pythonWordGen.genWord(150))
