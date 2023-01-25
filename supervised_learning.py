from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, LSTM, Dense
from keras.models import Sequential
import pandas as pd

'''
Using the supervised learning technique (neural network) to train the chatbot.

This code uses the Keras library to create a neural network model with an Embedding layer, an LSTM layer, and a Dense layer. 
The Embedding layer is used to convert the input sequences into a dense representation, the LSTM layer is used to process the sequence, 
and the Dense layer is used to make the final prediction.
The code starts by creating a tokenizer that is fit on the input-output pairs and then converts the input-output pairs to sequences. 
The sequences are then padded to ensure equal length.
The code then creates the neural network model, compiles it and trains it on the input-output pairs. 
The model is trained for 100 epochs.

You can also experiment with other supervised learning algorithms such as decision trees, Random Forest, Gradient Boosting, etc, 
depending on your needs and the nature of your data.
'''

# reading the JSON file
input_output_pairs = pd.read_json('input-output.json')

# defining variables
input_texts = input_output_pairs.loc[:,"input_texts"]
output_texts = input_output_pairs.loc[:,"output_texts"]
vocab_size = 10000

# create tokenizer
tokenizer = Tokenizer()
# fit the tokenizer on the input-output pairs
tokenizer.fit_on_texts(input_texts)

# convert the input-output pairs to sequences
input_sequences = tokenizer.texts_to_sequences(input_texts)
output_sequences = tokenizer.texts_to_sequences(output_texts)

# pad the sequences to ensure equal length
max_input_len = max([len(s) for s in input_sequences])
max_output_len = max([len(s) for s in output_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_input_len)
output_sequences = pad_sequences(output_sequences, maxlen=max_output_len)

# create the neural network model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=128, input_length=max_input_len))
model.add(LSTM(units=128))
model.add(Dense(units=vocab_size, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# train the model on the input-output pairs
model.fit(input_sequences, output_sequences, epochs=100)

#save model
model.save('models/supervised_model.h5')
model.save_weights('models/supervised_model_weights.h5')

'''
Loading weights of saved model
model2 = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])
model2.load_weights('models/my_model_weights.h5')
'''