import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url} \n")
except Exception as e:
    print(f"Error fetching content: {e} \n")
#print(soup.prettify())

''' ---------------------------------------------------------'''
#QUESTION 3
#<h1> tag 
a_array= soup.find_all('h1')
h1_count = 0 
for element in a_array:
    if (element.name == 'h1'): #tag comparision 
        h1_count+=1
print("Number of <h1> tags are: " + str(h1_count)+'\n')

#<h2> tag 
a_array= soup.find_all('h2')
h2_count = 0 
for element in a_array:
    if (element.name == 'h2'): #tag comparision 
        h2_count+=1
print("Number of <h2> tags are: " + str(h2_count)+'\n')

#<h3> tag 
a_array= soup.find_all('h3')
h3_count = 0 
for element in a_array:
    if (element.name == 'h3'): #tag comparision 
        h3_count+=1
print("Number of <h3> tags are: " + str(h3_count)+'\n')

#<h4> tag 
a_array= soup.find_all('h4')
h4_count = 0 
for element in a_array:
    if (element.name == 'h4'): #tag comparision 
        h4_count+=1
print("Number of <h4> tags are: " + str(h4_count)+'\n')

#<h5> tag 
a_array= soup.find_all('h5')
h5_count = 0 
for element in a_array:
    if (element.name == 'h5'): #tag comparision 
        h5_count+=1
print("Number of <h5> tags are: " + str(h5_count)+'\n')

#<h6> tag 
a_array= soup.find_all('h6')
h6_count = 0 
for element in a_array:
    if (element.name == 'h6'): #tag comparision 
        h6_count+=1
print("Number of <h6> tags are: " + str(h6_count)+'\n')

#<a> tag 
a_array= soup.find_all('a')
a_count = 0 
for element in a_array:
    if (element.name == 'a'): #tag comparision 
        a_count+=1
print("Number of <a> tags are: " + str(a_count)+'\n')

#<p> tag 
a_array= soup.find_all('p')
p_count = 0 
for element in a_array:
    if (element.name == 'p'): #tag comparision 
        p_count+=1
print("Number of <p> tags are: " + str(p_count)+'\n')

'''------------------------------------------------------------------------'''
#QUESTION 5
web_text= soup.get_text()
web_text = web_text.split()
web_text = [word.lower() for word in web_text]
freq_list = {}
for word in web_text:
    if (word in freq_list):
        freq_list[word] += 1
    else:
        freq_list[word] = 1
sorted_freq = dict(sorted(freq_list.items(), key = lambda item: item[1], reverse=True)[:5])
print("Top 5 most frequently occurning words:")
for word, count in sorted_freq.items():
    print(f' {word}:{count}')



'''----------------------------------------------------------------------'''
#QUESTION 7 
import matplotlib.pyplot as plt
headings = h1_count+ h2_count+h3_count+h4_count+h5_count+h6_count
links = a_count
paragraphs = p_count

labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Put your Group# Here')
plt.ylabel('Count')
plt.show()