# TRINIT_INFINITELOOP_DEV04
                           INfinder
                           
                           
Steps to run the application:
1) Download/Clone the repo
2) Open cmd with the path of the repo
3) Run the command "python app.py" 
4) Copy the sever link and run on the browser

Introduction:
The problem statement is to develop an application that takes the email id as input and displays the URL to the respective LinkedIn account as output on the screen. 
Once our web application is opened, to enter the email id “Get started” button should be clicked. This navigates to another page where the email id should be entered with proper syntax. If in case you have entered a wrong email id then there comes a popup validation saying “You have entered a Wrong mail id”. Once the correct email id is entered, it should be submitted. On submission, it displays the LinkedIn Profile Link associated with the entered email id. 




Tech Stack Used:
•	Html
•	 Css
•	Bootstrap (Framework)
•	JavaScript
•	Flask


Libraries Used:
•	Requests
•	Html5lib
•	beautifulsoup4


Proposed Method :
The intuition behind our solution is Web Scraping.
On the basis of our observation, when a full name which has a LinkedIn account is searched in the Google, the first link that appears in the search results is LinkedIn account link. When this page is inspected, the LinkedIn URL is found. With this       taken as the base idea, we proceeded.
We used BeautifulSoup library. It is a Python package for parsing HTML and XML documents. 
Now, once the email id is entered, the name is extracted from it. As the LinkedIn    URL is being searched “LinkedIn” keyword is added to the URL to be searched in      the Google for more accuracy. The HTML page of the search results in passed to the BeautifulSoup library. This searches through the HTML page for the href link which would be the required LinkedIn URL.


Work Done and Result:
The landing page consists of the basic UI and the user can proceed to the next page by clicking on get started
Another page is displayed with a text box to enter the email id
When submitted, it displays the URL of respective email id that can be 
copied simply by clicking on the text.   



Conclusion:
We have implemented the above approach for our problem statement and tested the solution with various Email Ids Considering all different types of edge cases. Our Solution works well with all the Email Ids given by us.


Vedio demostration Link:

https://drive.google.com/drive/folders/1BWJ5dLS3pBn9MwRT7nJ_H8Z3QFjSQ2ly?usp=sharing
Video Demonstartion DEV04-TEAM INFINITELOOP - Google ドライブ


