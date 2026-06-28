# About

This toy-project consists of a simple CRUD application made in Python with SQLite as database and Tkinter as GUI. The application stores a catalogue of service providers in Information Technology (IT), where you can read the current catalogue, update or delete an existing entry or add a new one. The persistent storage is implemented as a local `.db` file.

The project was implemented under the concepts of Object-Oriented Programming (OOP) and consisted of an activity for the CSI-22 course of Instituto Tecnológico de Aeronáutica (ITA), conducted by Prof. Karla Fook.

# Instructions

The projected was tested in Python 3.12.3 and 3.13.12. Please make sure to have one of these versions installed in your machine. 

Clone the repository in a desired directory with `git clone` and run in `pip install -r requirements.txt` to install the project dependencies. It is recommended to create a Python virtual environment. Then, simply run `python app.py` to start the program.

# Implementation

The project was made under the concepts of OOP and was implemented using the Model-View-Controller (MVC) design pattern (more info: [MVC - Glossary - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Glossary/MVC)). The view component consists of the GUI, implemented with Tkinter, which can only display the graphical interface and cannot directly access data from the database and declare business logic. The model consists of the data storage, implemented as a SQLite database, and the formatter, which format the user input to correspondingly read or modify the database. The controller component constitutes the interface between the GUI and the model, manipulating the model as the user interacts with the GUI.

As a differential, when the user completes the CEP address, it is gathered from the ViaCEP API ([ViaCEP](https://viacep.com.br/)) all the possible address information, autocompleting the forms. Thus, the program handles API exceptions the proper way.

# Authors

- Arthur de Sousa Vianna: Database and Controller
- Danilo Carlos da Silva: GUI and Integration