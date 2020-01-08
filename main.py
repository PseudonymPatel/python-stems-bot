import requests
from dotenv import load_dotenv  # to load from env file
import os  # to import variables

load_dotenv()  # load enviroment variables that have keys.

language = "en-us"
urlBase = "https://od-api.oxforddictionaries.com/api/v2/"


def main():
    while True:
        wordStuff()


def wordStuff():
    print("Word to define:", end=" ")
    usrInput = input()
    if usrInput == "exit":
        exit()
    # print(f"Getting definition for: {usrInput}")
    definitionUrl = urlBase + "entries/" + language + "/" + \
        usrInput.lower() + "?fields=definitions,examples"
    request = requests.get(definitionUrl, headers={
                           "app_id": os.environ["api_id"], "app_key": os.environ["api_key"]})
    parsedJson = request.json()
    # print("Results:")
    # print("code {}\n".format(request.status_code))
    # print("text \n" + request.text) # this is the pretty one
    # print("json \n" + json.dumps(request.json()))
    if request.status_code == 200:
        # print("success!")
        # TODO actually print the right stuff. need to get just some json strings
        definitionArray = (
            parsedJson["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])
        if len(definitionArray) > 1:
            print(bcolors.WARNING + "more than one defintion, copy-paste only one" + bcolors.ENDC)
            for i in range(len(definitionArray) - 1):
                print(str(i) + ": " + bcolors.OKGREEN + usrInput + bcolors.ENDC + ": " + definitionArray[i]["definitions"][0])
                try:
                    print(" \t\"" + definitionArray[i]["examples"][0]["text"] + "\"")
                except KeyError:
                    print(bcolors.FAIL + "There is no sentence available for this definition :(" + bcolors.ENDC)

        else:
            print(bcolors.OKGREEN + f"{usrInput}" + bcolors.ENDC + f": {definitionArray[0]['definitions'][0]}")
            try:
                print("\t\"" + definitionArray[0]["examples"][0]["text"] + "\"")
            except KeyError:
                print(bcolors.FAIL + "There is no sentence available :(" + bcolors.ENDC)


# colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    main()
