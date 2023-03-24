import openai
import re

# Define OpenAI API key 
openai.api_key = "Your_API_KEY"


def interaction_type(prompt):
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = prompt + '''\n Which type of query is it from the below option in just single word:
    1. Query
    2. Feedback
    3. Complaint
    4. Request'''

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )

    response = completion.choices[0].text
    return response

# For Testing Purpose
# prompt_text = '''Hello my name is Rohit Kumar, I want change my account PIN, Pls tell me the steps to do it.'''
# print(query_type(prompt_text).strip().upper())
