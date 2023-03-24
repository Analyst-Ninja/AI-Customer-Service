import openai

# Define OpenAI API key 
openai.api_key = "YOUR_API_KEY"

def interaction_type(prompt):
        
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = prompt + '''\n Which query type is it from the options given below in one word:
    1. Query
    2. Feedback
    3. Request
    4. Interaction'''

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text

    return response.strip().upper()
