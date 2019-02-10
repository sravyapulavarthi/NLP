# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:31:17 2018

@author: sravya
"""
import csv
from bs4 import BeautifulSoup
import requests
from person_entity_type import person_func
from other_entity_type import other_func
import re

def get(source):
    page = requests.get(source)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_facts = soup.find('p')
    all_facts_str = (str(all_facts))
    final_data = cleanhtml(all_facts_str)
    return final_data
    

def cleanhtml(all_facts_str):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', all_facts_str)
  return cleantext

if __name__=='__main__':
    mydata = ['entity_sub-type']
    file = open("ran_expected_entity_test.csv")
    entity_file = csv.reader(file)
    next(entity_file)
    web_entry = ""
    str_info = ""
    for each_entity in entity_file:
        str_info = str(get(each_entity[2]))
        if str_info:
            if each_entity[0] == "Person":
                output = person_func(each_entity[2], str_info)
                print(output)  
                mydata.append(output)

            else:
                output = other_func(str_info)
                print(output)
                mydata.append(output)
                
    iterator = 0
    finallist = []
    with open("ran_expected_entity_test.csv", "r") as file:
        entity_sample = csv.reader(file)
        for each_val in entity_sample:
            each_val[4] = mydata[iterator]
            iterator+=1
            finallist.append(each_val)        

    with open("ran_expected_entity-test_output.csv", "w") as op:
        writer = csv.writer(op, lineterminator='\n')
        for val in finallist:
            writer.writerow(val)