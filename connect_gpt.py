import argparse
from datetime import datetime

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

#language variable
#use history(assistant) variable

#receive sentence
def speak_to_gpt(utterance):

    print(f"Received {utterance}")

    system_content1 = "You are about to have a conversation with a patient who is troubled by certain symptoms. Ask for details about the symptoms and how they came about."
    system_content2 = "Avoid private questions like personal information."
    user_content = utterance

    messages=[
        {"role": "system", "content": system_content1},
        {"role": "system", "content": system_content2},
        {"role": "user", "content": user_content}
    ]

    response = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    pol_msg = response.choices[0].message.content
    response = pol_msg

    print(f"Send: {response}")

    log_str = f" {datetime.now().timestamp():f} "
    return response
            

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run a chatGpt system')
    speak_to_gpt("My chest hurts.")

