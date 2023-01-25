from keras.models import load_model
from gensim import models
from get_input import get_input_text
'''
use the outputs of both models to generate a set of candidate responses, 
and then use a voting system to select the final response.
This code generates candidate responses using both the supervised and unsupervised models, 
and then combines them into a single list. 
It then uses a voting function to select the final response by counting the number of votes for each candidate response, 
and returning the candidate response with the most votes.
You can adjust the voting function based on your specific requirements, for example, you can assign different weights to the votes coming from each model, 
or you can use other voting systems such as weighted voting or majority voting.
'''
supervised_model = load_model('models/supervised_model.h5')
unsupervised_model = models.ldamodel.LdaModel.load('models/unsupervised_model')
input_text = get_input_text()

# generate candidate responses using the supervised model
candidate_responses_supervised = supervised_model.predict(input_text)

# generate candidate responses using the unsupervised model
candidate_responses_unsupervised = unsupervised_model.predict(input_text)

# combine the candidate responses from both models
candidate_responses = candidate_responses_supervised + candidate_responses_unsupervised

# define a voting function to select the final response
def vote(candidate_responses):
    # count the number of votes for each candidate response
    votes = {}
    for response in candidate_responses:
        if response in votes:
            votes[response] += 1
        else:
            votes[response] = 1
    # return the candidate response with the most votes
    return max(votes, key=votes.get)

# generate the final response
final_response = vote(candidate_responses)

print(final_response)
