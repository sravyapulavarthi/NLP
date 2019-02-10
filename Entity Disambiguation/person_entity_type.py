# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:17:31 2018

@author: sravya
"""

import nltk
import csv
import re
from itertools import tee


def comparefn(en, eninfo, occupations):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(eninfo)
    nouns_duplicates = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    nouns = unique(nouns_duplicates)
    finallist=''
    
    for each_noun in nouns:
        for each_occupation in occupations:
            if each_noun.lower()==each_occupation.lower():
                finallist = finallist + " " + each_occupation
                
    for word1, word2 in pairwise(nouns):
        words_combined = word1 + word2
        for each_occupation in occupations:
            if words_combined.lower()==each_occupation.lower():
                finallist = finallist + " " + each_occupation
    return finallist



def unique(obj):
  output = []
  for x in obj:
    if x not in output:
      output.append(x)
  return output


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


        
def person_func(person_entity, person_entity_info):

    profession = open("occupations.csv", "r")
    read = csv.reader(profession)
    mylist = list(read)
    stroccu = [str(i) for i in mylist]
    occupations = [re.sub(r'[^\w]', '', a) for a in stroccu]
    
    var = comparefn(person_entity, person_entity_info, occupations)
    return var