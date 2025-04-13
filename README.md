<img src="https://vlegalwaymayo.atu.ie/pluginfile.php/1/core_admin/logo/0x200/1741260610/ATU-Logo-Initial-English-RGB-White.png" width=20% height=20%>



# WSAA_assignments

author: Monika Dabrowska

This repository is for solutions to the assignmemts  for the Web Services and Applications in the Higher Diploma in Data Analytics course from [ATU](https://www.atu.ie/) in the summer semester of 2024/25.

Below I will explain my approach to solving the assigned task and reference the sources I researched for solving these problems: 


## Table of contents:
* [Assignments](#assignments)
    * [Assignment 02 - *carddraw.py*](#assignment-02---carddrawpy)
    * [Assignment 03 - *cso.py*](#assignment-03---csopy)
    * [Assignment 04 - *github.py*](#assignment-04---githubpy)
  

## Get Started

To begin with *.py files you need Python installed on your machine. To do that, you can use the following: 

**Anaconda** \
[Download](https://www.anaconda.com/download) \
The easiest way to install Python and the necessary packages for this course.

**Visual Studio Code** \
[Download](https://code.visualstudio.com) \
The editor we will use to create Python scripts and Jupyter notebooks. 

**Git** \
[Download](https://git-scm.com) \
The software we will use to track our progress.

---

## Assignments:

### [Assignment 02 - *carddraw.py*](https://github.com/mondbr/WSAA_assignments/blob/main/assignment2-carddraw.py)

   *Write a program that "deals" (prints out) 5 cards first you need to shuffle [https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1] get the deck_id, with the deck_id you can get the cards [https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2]  This example gets two cards From there you need to print the value and the sui of each card. Save the file as assignment2-carddraw.py (or as a notebook)*


The code I wrote interacts with the Deck of Cards API to shuffle a deck and draw 5 cards. It sends a request to shuffle the deck, retrieves the deck ID, then sends another request to draw 5 cards. The drawn cards are displayed with their value and suit.

The program is called: 

   ```
   $ assignment2-carddraw.py
   ```

The output (randomly) is:


   ```
   the status code is 200
   Deck shuffled, deck id is qb9y9m023v8d
   You drew:
   8 of HEARTS
   3 of DIAMONDS
   6 of HEARTS
   4 of CLUBS
   KING of DIAMONDS
   ```

The code 200 indicates that the request was successful, and the server has returned the requested data. 

---

### [Assignment 03 - *cso.py*](https://github.com/mondbr/WSAA_assignments/blob/main/assignment03-cso.py)

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".

   *Upload this program to the same repository you used for the first assignment. Save this assignment as "assignment03-cso.py". This program should not be a long one. I don't need you to reformat or analyse the data in any way. It should be about 10ish lines long (I have not counted). You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.*

The program is called: 
   
   ```
   $ assignment03-cso.py
   ```

This code retrieves a dataset from the Central Statistics Office (CSO) API related to the "exchequer account (historical series)" and stores it as a JSON file. 
I started with uploading necessary libraries: `requests` to handle the HTTP request and `json` library to work with JSON data. 
Then I used GET request to connect to the CSO API URL to retrieve the dataset. After that I extracted the JSON data from the API response using `response.json()`.
Next, I printed the status code of the response to confirm whether the request was successful. Then I saved the received dataset into a file named "cso.json" using `json.dump()` in write mode ('w').

---

### [Assignment 04 - *github.py*](https://github.com/mondbr/WSAA_assignments/blob/main/assignment03-cso.py)


   *Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name. The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).I do not need to see your keys (see lab2) Handup: Push the program as assignment04-github.py to assignments repository. Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.*


The program is called: 

   ```
   $ assignment04-github.py
   ```


The output is:

   ```
   $ the status code is 200
   Monika
   Monika
   ...
   Monika

   {'commit': Commit(sha="5843f6de49b5c7c0ccc15adf752f14f98ad0e8a7"), 'content': ContentFile(path="andrew.txt")}
   ```

This program connects to a GitHub repository using the PyGithub library and updates a file by replacing all occurrences of the text "Andrew" with my name "Monika." It retrieves the file from the repository, modifies its content, and then commits and pushes the changes back to the repository using the GitHub API. Authorization is handled via an API key stored in a config file. The config.py file is saved in .gitignore file, therefore is not commited and pushed to my public Git repository as it contains sensitive information.

I started with importing `PyGithub` to interact with GitHub and `requests` to download the file. Then I retrieved the GitHub API key from a config.py file, ensuring it was stored securely by adding it to .gitignore. Next, I authenticated with GitHub by creating a Github object using the API key. I accessed the repository by calling the `get_repo()` method with my repository username and name. Next, I fetched the file andrew.txt from the repository using the `get_contents()`. Afterward, I downloaded the content from the file by getting its download URL and sending a GET request. Once I had the content, I replaced all occurrences of the word "Andrew" with "Monika" using `replace()`. Finally, I pushed the updated content back to the repository by `update_file()`. I printed the status code from the file download and the response from the commit to verify the changes were successful.



## About me

My name is Monika Dabrowska and I am an [ATU](https://www.atu.ie/) student of Higher Diploma in Data Analytics course in Summer 2024/25.


---

## Technologies

* Visual Studio Code Version: 1.99.2
* Cmder version v1.7.14

---

## Installing Dependencies

To set up this project and install all required dependencies, follow these steps:

1. Clone the repository to your local machine:
   ```
   $ git clone https://github.com/mondbr/WSAA_assignments
   ```
2. Navigate into the project directory

3. Install the required Python packages using pip and the requirements.txt file:
   ```
   $ pip install -r requirements.txt
   ```
This will install all the dependencies listed in the requirements.txt file, allows to run the programs. 



## References:

* WSAA module by Andrew Beatty in Higher Diploma in Data Analytics course
* [stackoverflow.com](https://stackoverflow.com/questions/66576064/api-json-result-to-file)
* [geeksforgeeks.org](https://www.geeksforgeeks.org/python-string-replace/)

----
END















