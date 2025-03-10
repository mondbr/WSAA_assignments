# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository
# You will need authorisation to do this

# Author: Monika Dabrowska
# I was referring to the lab05.03-githubbymodule.py file to write this program


# to use this installed package PyGithub
# -- pip install PyGithub

# import necessary libraries
from github import Github
import requests

# import the api key from the config file
from config import config as cfg

# get the api key from the config file
# this is saved in the config file that is not pushed to github
# .gitignore file is used to ignore the config file
apikey = cfg["mygithubkey"]

# create an instance of the Github class
g = Github(apikey)

# get the repository from the github
# it will only need username and repository name
repo = g.get_repo("mondbr/WSAA_assignments")

# get the file from the repository
# the file is called andrew.txt
file_info = repo.get_contents("andrew.txt")

# get the download url of the file
url_of_file = file_info.download_url

# get the content of the file
response = requests.get(url_of_file)

# Simple print of the status code
print(f'the status code is {response.status_code}')


content_of_file = response.text

# replace all the instances of the text "Andrew" with "Monika"
# https://www.geeksforgeeks.org/python-string-replace/

new_content = content_of_file.replace("Andrew", "Monika")
print (new_content)

# update the file with the new content
# the commit message is "updated by program"
# SHA(Secure Hash Algorithm) value of the file in the GitHub repository
git_hub_response=repo.update_file(file_info.path,"updated by program assignment04",new_content,file_info.sha)
print (git_hub_response)


