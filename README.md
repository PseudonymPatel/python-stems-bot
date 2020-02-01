# python-stems-bot
Finds a definition and a good sentence (or phrase) for a given word

# Installation/Setup
## Packages needed:
`pip install python-dotenv`  
It also uses `requests` and `os`, which is included.  

## Oxford dictionary stuff
This bot uses Oxford dictionary API, so you will need to get an api id and key  
[Get key here (need to make account)](https://developer.oxforddictionaries.com/)
Keys you will need:
* `api_id` = application ID
* `api_key` = application Key
# Ideas for improvement
* Get the sentences from the sentence part of the API (currently getting 403 error :( ) 
* Create a better interface (possibly a GUI interface?)
* Input a list of words and return a formatted document
