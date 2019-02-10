# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:42:04 2018

@author: sravy
"""

import nltk

def compfn(eninfo):
    is_verb = lambda pos: pos[:2] == 'VB'
    tokenized = nltk.word_tokenize(eninfo)
    verb = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    list_verb = list(verb)
    try:
        my_var = substring(eninfo, list_verb[0], list_verb[1])        
    except IndexError:
        my_var = 'null'
    return my_var

def substring(value, begin, end):
    pos_begin = value.find(begin)
    if pos_begin == -1:
        return "None"
    pos_end = value.rfind(end)
    if pos_end == -1: 
        return "None"
    adjusted_pos_begin = pos_begin + len(begin)
    if adjusted_pos_begin >= pos_end:
        return "None"
    return value[adjusted_pos_begin:pos_end]    
    
def other_func(entityinfo):
        var = compfn(entityinfo)
        return var