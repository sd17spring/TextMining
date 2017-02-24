from wordCreator import WordCreator
import wikipedia
python = None

python = wikipedia.page('Pythonidae')
pythonContent = python.content

pythonWordGen = WordCreator(words=pythonContent)
print(pythonWordGen.genWord(150))
