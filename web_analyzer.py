import requests
from bs4 import BeautifulSoup
url = input("Enter a URL in the correct format: ")

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")



keyword = input("Enter the keyword that you would like to search for in the webpage: ")
keyword_count = (soup.get_text().lower().count(keyword))

print("The number of", keyword + " found in your website is : ", keyword_count)


max_word_count = 0 
longest_paragraph = ""
for para in soup.find_all("p"):
    para_text = para.get_text().strip()

    if not para_text :
        continue 

    para_words = [word for word in para_text.split()]
    para_word_count = len(para_words)

    if para_word_count < 5 :
        continue 

    if para_word_count > max_word_count: 
        longest_paragraph = para_text 
        max_word_count = para_word_count

    
 
print("The longest paragraph is {} words and it contains: {}".format(max_word_count, longest_paragraph))
    
    

