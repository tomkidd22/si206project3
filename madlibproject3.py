# coding: utf-8
#-*- coding: utf-8 -*-
# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  
#
# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")
import nltk 
import random
from nltk import word_tokenize,sent_tokenize
from nltk.book import *
from nltk import bigrams

debug = False #True
tokens = text2[0:150]
theString = ""
for w in tokens:
	theString+=w+" "

print (theString)

# tokens = nltk.word_tokenize(para)
# print("TOKENS")
# print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		pass
		#print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","RB":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))






# import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
# import random
# from nltk.book import *
# from nltk import bigrams
# from nltk import word_tokenize,sent_tokenize
# fname = text2 # need a file with this name in directory

# f = open(fname)
# para = f.read()

# tokens = nltk.word_tokenize(para)
# print("TOKENS")
# print(tokens)
# tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

print("\n\nEND*******")
