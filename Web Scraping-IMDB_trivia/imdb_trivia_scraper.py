import csv
from bs4 import BeautifulSoup
import requests
import re


def cleanhtml(all_facts_str):
    line = re.sub('[!,@#$]', '', all_facts_str)
    cleantext = BeautifulSoup(line, "lxml").text
    return cleantext

if __name__=='__main__':
    movie_title = ""
    file = open("movies.csv", "r")
    movies = csv.reader(file)
    movie_list = list(movies)
    movie_title = [str(i[1]) for i in movie_list]
#    movie_title = [re.sub(r'[^\w]', '', a) for a in movie_details]
#    print(movie_title)
    movie_name = [str(i[2]) for i in movie_list]
#    print(movie_name)
    
    for (each_name, each_title) in zip(movie_name, movie_title):
        f = open(each_name + ".txt", 'w')
        page = requests.get("https://www.imdb.com/title/" + each_title + "/trivia")
        soup = BeautifulSoup(page.content, 'html.parser')
        all_facts = soup.find_all('div', attrs={'class': 'sodatext'})
#            print(all_facts)
        print("\n")
        all_facts_str = (str(all_facts))
        final_data = cleanhtml(all_facts_str)
        print(final_data + "\n")
        f.write(final_data + "\n")
        f.close()