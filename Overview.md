# -*- coding: utf-8 -*-
# MovementTracker #

###Overview of the project structure

The MovementTracker Application is made up of a number of modules:

* Login (Not yet started)
* Movement Summary (Not yet started)
* User Administration (Not yet started)
* Configuration (Not yet started)
* Movement Diagnostics (Not yet started)
* User Editing (Not yet started)
* Contacts (Not yet started)
* Cake Diagram (Not yet started)
* Network Diagram (Not yet started)
* Texting (Not yet started)
* Emailing (Not yet started)

The application uses the MVC methodology and built in kivy operates off the following structure:

###Module Naming
Each module is named in the following format:  

xxxxxxxxx_model.py - Containing the model  

xxxxxxxxx_vc.py - Containing the view and the controller  

In the vc file, the view is built using the kivy language (kv) and is loaded into the builder as a string. This follows standard operating practices for kivy applications.

The only exception to this rule is main.py and main.kv  

The string is separated out into a separate file for clarity and these files create the base template upon which the rest of the application is built.  

After the builder string, the controller logic follows.  

This will enable reuse of code in the future if platforms beyond kivy are required.  

###Other Modules

Alongside this are two backend modules:  

* mt_objects.py  
* db_connection.py  

mt_objects.py contains classes which are required by the model.  

db_connection.py contains all database calls (functions) to create / modify / delete data. These functions will return lists of mt_objects
