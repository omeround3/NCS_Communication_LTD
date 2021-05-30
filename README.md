# NCS_Communication_LTD
A Web Project as part of the Network Communication Course at Afeka College.

- This project was created using the Django framework and Bootstrap.
- Make sure to create a python virtual enviroment and install all the dependencies in `requirements.txt`.

## How to run the project

1. Clone this reposititory to your local computer
2. Install python virtual enviroment using `python3 -m pip install --user virtualenv` on macOS or Linux. On Windows run `py -m pip install --user virtualenv`
3. Create a virtual enviroment using `python3 -m venv env` on macOS or Linux. On Windows run `py -m venv env`
4. Activate the virutal enviroment using `source env/bin/activate` on macOS or Linux. On Windows run `.\env\Scripts\activate`
5. Go into the project directory `cd NCS_Communication_LTD`
6. Install dependendcies using `pip install -r requirements.txt`(this might takes a couple of minutes, don't close the terminal).
7. Run the server using `python manage.py runserver`
8. Open the terminal and you will see a log with the server IP and the port (default is 8080). Open your web browser and go to localhost:8080

## Projects Notes
- The project has been deploy on Digitalocean App Platform which "listens" to the main branch on this repo and builds a new Docker container every time a new commit has been pushed.
- The Digitalocean App Platform provided us with **HTTPS** connection to the website and an **SSL Certificate** signed by cloudflare.
- The Static Files of the web server are being served with Digitalocean CDN, which is an additional componenet of the App Platform.
- **The vulnerabilites have been hard-coded, please see the comments on the python files to understand how we made the website vulnerable to SQL Injections and Stored XSS attacks**

**Website Link** - https://communication-ltd-fz6km.ondigitalocean.app/

## Project Task - Part 1 - Section 5 - Reset Password View
The Reset Password workflow prints the one time **TOKEN** to the terminal.
Make sure to copy it and paste in the website input box to continue the Reset Password workflow.

## Django Admin Credentails
Sign into the Django Admin with `http://<server_ip>:<server_port>/admin` and the next credentials:
- **Username:** afeka
- **Password:** Afeka2021!

## DREAD Document
The DREAD document which is part of a system for risk-assessing computer security threats, has been added to this repo.




