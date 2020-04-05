iZETTLE DATA SCIENCE CHALLENGE README
=====================================

This file aims to describe all the elements of the solution to iZettle's Data Science Challenge
submitted by Srdjan Santic. The solution includes the following files:

* iZettle-Srdjan_Santic.ipynb
* app.py
* requirements.txt
* Dockerfile
* README.md


iZettle-Srdjan_Santic.ipynb
---------------------------

This file is a Jupyter notebook with the complete solution to the the challenge. In order to work with the
notebook, the data files are required. They are not provided as a part of the solution, due to the size,
and were originally provided by iZettle. The cells in the notebook are meant to be run in consecutive order. They provide the
exploratory data analysis, the feature engineering, the modeling and accuracy metrics, and export of the models as pickle files.


app.py
------

This file provides a minimum Flask server, and serves the models exported from the notebook through an API endpoint.
To run the server, use the following command at the terminal:

$ python app.py

The server listens on port 5000 by default, but this can be changed by modifying the file.

It's important to note that the pickled models **are not** provided with the solution, and thus the Jupyter notebook
has to be run first.


requirements.txt
----------------

This file lists all the dependencies needed to run the project. They can be installed by running:

$ pip install -r requirements.txt


Dockerfile
----------

This file is used to build a Docker image which contains the pickled models, as well as the Flask-based web server. Not that
in this case the Jupyter notebook has to be run first in order to export the models. The image is built by running:

$ docker build .
