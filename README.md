Item Catalog
=============

Description
-------------
A web application that provides a list of items within a variety of categories as well as providing a user registration and authentication system. Registered users will have the ability to create, edit and delete their own items.

Technical Skills
-----------------
1. python
2. HTML
3. CSS
4. OAuth
5. Flask Framework

Test-driving the app with vagrant
-------------

1. Install Vagrant and VirtualBox
2. Clone this repository
3. Create a directory. This can be used to hold instance specific config, overriding the testing config variables.
4. Download your Oauth client secret json file.
5. Launch the Vagrant VM with the command `vagrant up`.
6. Use the command `vagrant ssh` to ssh into the VM.
7. In the VM, run the command `python database_setup.py` to create the database.
8. In `/vagrant/`and run `python finalproject.py` to start the server.
9. In your browser, navigate to [http://localhost:5000](http://localhost:5000).
10. Sign in with Google to experience full functionality. Note that the first user you sign in with will be considered the owner of all the items and tags created by `database_setup.py`. Sign out and sign in with a second user to verify that users cannot change other users' items or tags.

Using Google Login
---------------------
To get the Google login working there are a few additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Item-Catalog'
7. Authorized JavaScript origins = 'http://localhost:5000'
8. Authorized redirect URIs = 'http://localhost:5000/login' && 'http://localhost:5000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in item-catalog directory that you cloned from here
14. Run application using `python finalproject.py`

Expected functionality
-----------------------
1. Users can login / logout with FB or Google Plus sign in.
2. Users cannot Get or Post New, Edit, or Delete pages without being signed in.
3. Users cannot Get or Post Edit or Delete items without being the original creators of the item.
4. Logged in users can create new items.
