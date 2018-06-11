udacity-item-catalog
=============

Description
-------------
A web application that provides a list of items within a variety of categories as well as providing a user registration and authentication system. Registered users will have the ability to create, edit and delete their own items.

Test-driving the app with vagrant
-------------
(Using $repo to refer to the path of the repository)

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
