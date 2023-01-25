# importing pandas as pd
import pandas as pd

# lists of input-output pairs
inputs = [
    "What is your name?",
    "How old are you?",
    "Where are you from?",
    "What do you like to do?",
    "What is your favorite color?",
]

outputs = [
    "My name is Chatbot.",
    "I am an AI, so I don't have an age.",
    "I am from the internet.",
    "I like to chat with people.",
    "I don't have a favorite color."
]

#  dictionary of lists
dict = {'input_texts': inputs, 'output_texts':outputs}

df = pd.DataFrame(dict)

df.to_json('input-output.json')