# spartan_project
Web Application (REST-API) Sparta-Trainee Management System

Your task is to build a web application to manage the trainee records in sparta.<br> 
Please check requirements as follows:<br>
1-  The users can communicate with the app using REST APIs.<br>
2-  The system should automatically save the spartan data in a JSON file (data.json) after each user action (i.e. API call)<br>
3-  Each spartan should have the following data:<br>
    - spartan_id: Spartan ID (int)<br>
    - first_name: First name (string: minimum 2 Characters)<br>
    - last_name: Last Name (string: minimum 2 Characters)<br>
    - birth_year: Birth Year (int between 1900 and 2004)<br>
    - birth_month: Birth Month (int between 1 and 12)<br>
    - birth_day: Birth Day (int between 1 and 31)<br>
    - course: Course (string)<br>
    - stream: Stream (string)<br>

4-  The system should use Object-Oriented to manage the spartan data.<br>
5-  Object variables should be dealt with using getters and setters only.<br>
6-  Organise your code to have main.py that would have all te routes and spartan.py for the Spartan class<br>
7-  You can test the spartan class by using a main code in the same file, the code should not be executed when this file is called by the main.py<br>

The following functionalities (and routes are expected to be implemented)<br>

1-  method: GET, route: /
  This is the landing page (Home page) and should return a welcome message along with a simple tutorial clarifying how APIs can be used

2-  method: POST, route: /spartan/add
  This API should allow the user to add new spartan to the system by passing a JSON object.

3-  method: GET, route: /spartan/<spartan_id>
  Get certain employee using the spartan_id. An error message should be returned if the spartan_id doesn't exist in the system. The data should be returned as string

4-  method: POST, route: /spartan/remove?id=sparta_id
  This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string

5-  method: GET, route: /spartan
  This API should return the spartan list as one JSON object.


Working Methodology:<br>
1-  Start by creating a new git repository (spartan_project)<br>
2-  Create a new pycharm project and link it to the repository that you created.<br>
3-  Use commit after each step from now on<br>
4-  Start by creating all the routes (at this stage they will only be returning strings to show that they are working)<br>
5-  Create the Class and test (locally) that you can create an object from the class<br>
6-  Create a file called management.py and use it to add all the functions that will manage the spartans<br>
7-  Use Postman to test your code: create new collection and create a new request for each API that you are testing<br>
