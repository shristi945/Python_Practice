
import nltk
nltk.download('all')
string = input().strip()
words = string.split()
# print(words)
tagged = nltk.pos_tag(words)
