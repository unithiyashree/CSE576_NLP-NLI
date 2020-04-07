import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import urllib
import sys
import os
import zipfile
import json

glove_vectors_file = "C:\\Users\\sudha\\Desktop\\NLP Assignment\\glove.6B.50d.txt"
glove_wordmap={}

with open(glove_vectors_file, "r",errors='ignore') as glove:
    for line in glove:
        name, vector = tuple(line.split(" ", 1))
        glove_wordmap[name] = np.fromstring(vector, sep=" ")


def sentence2sequence(sentence):
    tokens = sentence.lower().split(" ")
    rows = []
    rows1=[]
    words = []
    #Greedy search for tokens
    for token in tokens:
        i = len(token)
        while len(token) > 0 and i > 0:
            word = token[:i]
            if word in glove_wordmap:
                rows.append(glove_wordmap[word])
                words.append(word)
                token =""
            else:
                i = i-1
    rows1=[item for sublist in rows for item in sublist]
    rows1+=[0]*(750-len(rows1))
    return rows1, words,len(rows1)

def score_setup(row):
    convert_dict = {
      'entailment': 0,
      'neutral': 1,
      'contradiction': 2
    }
    score = np.zeros((3,))
    for x in row['annotator_labels']:
        if x in convert_dict: score[convert_dict[x]] += 1
    return score / (1.0*np.sum(score))

def parse_input_data(fileName):
	premise = []
	hypothesis = []
	output_label = []
	scores = []
	with open( fileName, "r") as inputData:
        data = json.loads(inputData)
		# data = [inputData.split(',')]
		print data
		# for row in data:
		# 	premise.append(sentence2sequence(row['sentence1'].lower())[0])
  #           hypothesis.append(sentence2sequence(row['sentence2'].lower())[0])
  #           output_label.append(sentence2sequence(row['gold_label'].lower())[0])
  #           scores.append(score_setup(row))
  #       hyp_sentences = np.stack(hyp_sentences)
  #       evi_sentences = np.stack(evi_sentences)
  #       scores=np.stack(scores)
    return (hyp_sentences, evi_sentences), scores
