from gensim.models import LdaModel
from gensim.corpora import Dictionary
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import os

'''
Using unsupervised learning techniques, such as topic modeling, to extract the main ideas and concepts from the documents 
and allow the chatbot to understand the context and content of the documents

This code uses the Gensim library to perform topic modeling on the documents. It starts by looping through all files in a specific folder, reading the contents of each file, preprocessing the text by removing stopwords and tokenizing it. 
It then creates a dictionary from the documents and a bag-of-words representation of the documents.
The code then trains a Latent Dirichlet Allocation (LDA) model on the corpus, 
specifying the number of topics (15 in this case) and the dictionary.
Finally, the code extracts the main topics and concepts from the documents by calling the print_topics() method on the LDA model 
and specifying the number of words to include in each topic (10 in this case).
'''


# specify the folder containing the documents
folder_path = './cleaned_docs'

# create a list to store the documents
documents = []

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    # open the file
    with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8', errors='ignore') as file:
        # read the contents of the file
        doc = file.read()
        # preprocess the text
        doc_tokens = simple_preprocess(doc, deacc=True, min_len=2, max_len=15)
        # remove stopwords
        doc_tokens = [token for token in doc_tokens if token not in STOPWORDS]
        # add the preprocessed document to the list
        documents.append(doc_tokens)

# create a dictionary from the documents
dictionary = Dictionary(documents)

# create a bag-of-words representation of the documents
bow_corpus = [dictionary.doc2bow(doc) for doc in documents]

# train a LDA model on the corpus
lda_model = LdaModel(bow_corpus, num_topics=15, id2word=dictionary)

# extract the main topics and concepts from the documents
topics = lda_model.print_topics(num_words=10)

#save model
lda_model.save('models/unsupervised_model')