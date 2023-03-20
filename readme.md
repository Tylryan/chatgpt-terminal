# ChatGPT from the terminal

# Setup
1. Go to [OpenAI](https://platform.openai.com/).
    - Log in
    - Create an Api Key
2. Create a directory
3. Put a file called `.env` in that directory
    - Open that file an set your parameter = your api key.
    - See my `env` file for as an example.
4. Run `python -m venv .venv`
5. Activate the environment you just setup (You'll have to look it up)
6. `pip install openai python-dotenv`
7. `python main.py`

# Completion.create() parameters
- **model:** You can change these. See [here](https://platform.openai.com/docs/models) for more models you can use.  
- **temperature:** 0 will return the same result every time while 1 will return a different result every time. Anywhere in between has the expected result.  
- **max_tokens:** Determines how long the response can be.  
> For more options, see the [Docs](https://platform.openai.com/docs/api-reference/completions/create)
