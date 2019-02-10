"""
Created on Sun Jul 15 00:07:54 2018

    order is maintained
    no duplicates present
    string info stored inside a function 
    input 2 or 3 lines for each entity
    modify return c statement and include a list and return the entire list 
    time complexity calculated
    
@author: sravya
"""

import nltk
import csv
import re
import time
from itertools import tee


def comparefn(en, eninfo):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(eninfo)
    nouns_duplicates = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    nouns = unique(nouns_duplicates)
    print(nouns)
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
    print('\n')
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


def stinformation(obj):
    strinfo = ["William Bradley \"Brad\" Pitt (born December 18, 1963) is an American actor and film producer. He has received multiple awards and nominations including an Academy Award as producer under his own company Plan B Entertainment."]
    strinfo.append("Donald John Trump (born June 14, 1946) is the 45th and current President of the United States. Before entering politics, he was a businessman and television personality.")
    strinfo.append("Albert Einstein (14 March 1879 – 18 April 1955) was a German-born theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics). His work is also known for its influence on the philosophy of science. He is best known to the general public for his mass–energy equivalence formula E = mc2, which has been dubbed \"the world\'s most famous equation\" He received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\", a pivotal step in the development of quantum theory.")
    strinfo.append("Gordon James Ramsay Jr. OBE (born 8 November 1966) is a British chef, restaurateur, and television personality. Born in Scotland, Ramsay grew up in Stratford-upon-Avon. His restaurants have been awarded 16 Michelin stars in total.[1][2] His signature restaurant, Restaurant Gordon Ramsay in Chelsea, London, has held three Michelin stars since 2001. First appearing on television in the UK in the late 1990s, by 2004 Ramsay had become one of the best known chefs in British popular culture, and, along with other chefs such as Jamie Oliver, Nigella Lawson, and Delia Smith, he has influenced viewers to become more culinarily adventurous.[3][4]")
    strinfo.append("Christopher Robert Evans[1] (born June 13, 1981)[2] is an American actor. Evans is known for his superhero roles as the Marvel Comics characters Captain America in the Marvel Cinematic Universe and Human Torch in Fantastic Four (2005) and its 2007 sequel.")
    strinfo.append("Steven Allan Spielberg KBE OMRI (born December 18, 1946) is an American filmmaker. He is considered one of the founding pioneers of the New Hollywood era and one of the most popular directors and producers in film history.")
    strinfo.append("Freddie Mercury (born Farrokh Bulsara; 5 September 1946 – 24 November 1991) was a British singer, songwriter and record producer, best known as the lead vocalist of the rock band Queen. He was known for his flamboyant stage persona and four-octave vocal range.[2][3][4] Mercury wrote numerous hits for Queen, including \"Bohemian Rhapsody\", \"Killer Queen\", \"Somebody to Love\", \"Don't Stop Me Now\", \"Crazy Little Thing Called Love\", and \"We Are the Champions\". He led a solo career while performing with Queen, and occasionally served as a producer and guest musician for other artists.")
    strinfo.append("Edgar Allan Poe (/poʊ/; born Edgar Poe; January 19, 1809 – October 7, 1849) was an American writer, editor, and literary critic. Poe is best known for his poetry and short stories, particularly his tales of mystery and the macabre. He is widely regarded as a central figure of Romanticism in the United States and American literature as a whole, and he was one of the country's earliest practitioners of the short story. Poe is generally considered the inventor of the detective fiction genre and is further credited with contributing to the emerging genre of science fiction.[1] He was the first well-known American writer to try to earn a living through writing alone, resulting in a financially difficult life and career.[2]")
    strinfo.append("Jerry Lee Rice (born October 13, 1962) is a former American footballer who played in the National Football League, primarily with the San Francisco 49ers. He is widely considered to be the greatest wide receiver in NFL history,[1][2] and often called the greatest NFL player of all time.[3][4]")
    strinfo.append("Samuel Langhorne Clemens (November 30, 1835 – April 21, 1910),[1] better known by his pen name Mark Twain, was an American writer, humorist, entrepreneur, publisher, and lecturer. Among his novels are The Adventures of Tom Sawyer (1875) and its sequel, the Adventures of Huckleberry Finn (1885),[2] the latter often called The Great American Novel")
    strinfo.append("Leonardo da Vinci was an Italian painter, sculptor, architect, engineer, and scientist. He was one of the greatest minds of the Italian Renaissance, and his influence on painting was enormous to the following generations.")
    strinfo.append("Naina Lal Kidwai (born 1957) is an Indian banker, Chartered Accountant and business executive. She was formerly a Group General Manager and the Country Head of HSBC India.[4][5][6] She is also a former President of the Federation of Indian Chambers of Commerce and Industry (FICCI).")
    return strinfo[obj]
     

        
if __name__=='__main__':
    file = open("person_entity_sample.csv")
    person_entity_sample = csv.reader(file)
    next(person_entity_sample)
    
    profession = open("occupations.csv", "r")
    read = csv.reader(profession)
    mylist = list(read)
    stroccu = [str(i) for i in mylist]
    occupations = [re.sub(r'[^\w]', '', a) for a in stroccu]
    
    mydata = ['Sub-Type']
    iterator = 0    
    total_time = 0
    start_time = time.time()
    for each_entity in person_entity_sample:
        print(each_entity[0])  
        info = stinformation(iterator)
        var = comparefn(each_entity[0], info)
        iterator+=1
        mydata.append(var)
    end_time = time.time() - start_time
    total_time += end_time
    print('\n')
    print(total_time)
    
        
#    0.18376755714416504 for iteration 1
#    0.2089993953704834 for iteration 2
#    0.17241239547729492 for iteration 3
#    0.3204209804534912 for iteration 4
    
    print('\n')
    iterator = 0
    finallist = []
    with open("person_entity_sample.csv", "r") as file:
        new_person_entity_sample = csv.reader(file)
        for each_val in new_person_entity_sample:
            each_val[2] = mydata[iterator]
            iterator+=1
            finallist.append(each_val)
        print(finallist)

    with open("person_entity_output.csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in finallist:
            writer.writerow(val)