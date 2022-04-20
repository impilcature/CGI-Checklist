The original working implementation and framework from which this code as based is within the unfactored module as app2.py.

app2.py runs and has the ability to interface with an api that uses jsonify to use json strings and objects to interact with
the database through the api.  Once the application was refactored i could never get the api portion to function like it
origianlly did so I left that in.  I added an abilty to upload files to the refactored portion and was successful in uloading
however more work needs to be done in order to organize the files and integrate them into the checklist properly.

running flaskapi.py starts the program and creates the local database (not completely implemented as the database setup did
not get accomplished in the refactor).