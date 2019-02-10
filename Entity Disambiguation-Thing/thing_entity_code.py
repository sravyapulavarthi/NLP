# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:09:35 2018

    returns substring found inbetween two verbs
    output as desired
    low time complexity 

@author: sravya
"""

import nltk
import csv
import time



def compfn(eninfo):
    is_verb = lambda pos: pos[:2] == 'VB'
    tokenized = nltk.word_tokenize(eninfo)
    verb = [word for (word, pos) in nltk.pos_tag(tokenized) if is_verb(pos)]
    list_verb = list(verb)
    print(list_verb)
    print("\n")
    return substring(eninfo, list_verb[0], list_verb[1])        
        


def substring(value, begin, end):
    # Find and validate before-part.
    pos_begin = value.find(begin)
    if pos_begin == -1:
        return "None"
    # Find and validate after part.
    pos_end = value.rfind(end)
    if pos_end == -1: 
        return "None"
    # Return middle part.
    adjusted_pos_begin = pos_begin + len(begin)
    if adjusted_pos_begin >= pos_end:
        return "None"
    return value[adjusted_pos_begin:pos_end]    
    


def entityinfo(obj):
    strinfo = ["Moon Knight (Marc Spector) is a fictional superhero appearing in American comic books published by Marvel Comics."]
    strinfo.append("Marvel's The Defenders, or simply The Defenders, is an American web television miniseries created by Douglas Petrie and Marco Ramirez for Netflix, based on the Marvel Comics characters Daredevil, Jessica Jones, Luke Cage, and Iron Fist, who form the eponymous superhero team.")
    strinfo.append("Magneto is a fictional character appearing in American comic books published by Marvel Comics, commonly in association with the X-Men.")
    strinfo.append("Spider-Man is a fictional superhero appearing in American comic books published by Marvel Comics.")
    strinfo.append("Rick Grimes is a fictional character and the protagonist in the comic book series The Walking Dead and the television series of the same name portrayed by Andrew Lincoln. Created by writer Robert Kirkman and artist Tony Moore, the character made his debut in The Walking Dead #1 in 2003.")
    strinfo.append("The Justice League is a team of fictional superheroes appearing in American comic books published by DC Comics.")
    return strinfo[obj]



if __name__=='__main__':
    file = open("thing_entity_sample.csv")
    reader = csv.reader(file)
    next(reader)
    
    mydata = ['Sub-Type']
    iterator = 0
    total_time = 0
    start_time = time.time()
    for line in reader:
        print(line[0])
        var = compfn(entityinfo(iterator))
        iterator+=1
        mydata.append(var)
    end_time = time.time() - start_time
    total_time += end_time
    print(total_time)
    print('\n')
    
    iterator = 0
    finallist = []
    with open("thing_entity_sample.csv", "r") as file:
        thing_entity_sample = csv.reader(file)
        for temp_iterator in thing_entity_sample:
            temp_iterator[2] = mydata[iterator]
            iterator+=1
            finallist.append(temp_iterator)
        print(finallist)

    with open("thing_entity_output.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for iterator in finallist:
            writer.writerow(iterator)