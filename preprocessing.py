import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

'''
This code will loop through all files in a specific folder, it will read the contents of each file, 
remove any special characters and numbers, convert the text to lowercase, tokenize the text, 
removes stop words and stem the remaining words, join the stemmed words back into a single string, 
and add the cleaned document to a list.

The code uses the NLTK library for stopwords and stemmer, so make sure to have nltk installed 
and download the stopwords before running the code. Here, the stopwords have been downloaded in English. 
Please note that this is just an example and you may need to run nltk.download() function for other languages or corpora as well.
It's also worth noting that, there are other libraries like spaCy, NLTK, and gensim that offer stopwords in many languages. 
You can use any of them, depending on your preference or the specific requirements of your project.
Also, added 'utf-8' encoding to the opening file statement, as some documents may contain unicode characters.
'''
# download stopwords if not already done
# nltk.download('stopwords')

# specify the folder containing the documents
folder_path = './training_docs'

# initialize a list to store the cleaned documents
cleaned_docs = []

# initialize NLTK's stemmer and stopwords list
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    # open the file
    with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8', errors='ignore') as file:
        # read the contents of the file
        doc = file.read()
        # remove any special characters and numbers
        doc = re.sub(r'[^a-zA-Z\s]', '', doc)
        # convert the text to lowercase
        doc = doc.lower()
        # tokenize the text
        doc_tokens = doc.split()
        # remove stop words and stem the remaining words
        doc_tokens = [stemmer.stem(word) for word in doc_tokens if word not in stop_words]
        # join the stemmed words back into a single string
        doc = ' '.join(doc_tokens)
        # add the cleaned document to the list
        cleaned_docs.append(doc)

'''
This code first checks if the "cleaned_docs" folder exists, if not it creates it. 
It then iterates over the cleaned documents, creates a file name for each document, and writes the document to the file.
'''
# create the "cleaned_docs" folder if it doesn't exist
if not os.path.exists("cleaned_docs"):
    os.makedirs("cleaned_docs")

# iterate over the cleaned documents
for i, doc in enumerate(cleaned_docs):
    # create a file name for the document
    file_name = "cleaned_docs/doc_{}.txt".format(i)
    # write the document to the file
    with open(file_name, "w") as file:
        file.write(doc)
