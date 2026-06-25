# About

This toy-project consists of a simple CRUD application made in Python with SQLite as database and Tkinter as GUI. The application stores a catalogue of service providers in Information Technology (IT), where you can read the current catalogue, update or delete an existing entry or add a new one. The persistent storage is implemented as a local `.db` file.

The project was implemented under the concepts of Object-Oriented Programming (OOP) and consisted of an activity for the CSI-22 course of Instituto Tecnológico de Aeronáutica, conducted by Prof. Karla Fook.

# Implementation

The project can be divided in three components: the GUI, the database and the formatter. The database stores all the catalogue and can be retrieved, altered or updated. The GUI can only retrieve data from the database and request an update of it as the user wishes. Between the database and the GUI, there is the formatter, which is applied when there is need for read and validate user input and create a database query from it.

As a differential, when the user is filling the address and insert the Brazilian CEP, all the possible corresponding information is gathered from the Correios API and autocompletes the form. This method is implemented as an side function of the GUI.

# Authors

Arthur de Sousa Vianna and Danilo Carlos da Silva.