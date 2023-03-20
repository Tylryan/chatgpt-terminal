
from dotenv import load_dotenv
import openai
import os
# For more information on how to use the api
# https://platform.openai.com/docs/api-reference/completions

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    question = get_question()
    answer   = get_answer(question)
    print(answer)

    return

def get_question():
    question = input("What would you like to know: ")
    return question

def get_answer(question):
    response = openai.Completion.create(
            # For more models:
            # https://platform.openai.com/docs/models
            model  = "text-davinci-003",
            prompt = question,
            temperature = 0.6,
            # You only have a limited amount!
            # Set this to a low number for it to
            # last longer
            max_tokens = 100

            )
    return response["choices"][0].text

if __name__ == "__main__":
    main()
