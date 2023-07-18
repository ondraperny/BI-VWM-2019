# Python 3 program for collaborative filtering.

This program implements a recommendation system based on collaborative filtering using the Spearman correlation coefficient. The dataset used is a smaller version of the [MovieLens](http://movielens.org) dataset, containing 100,000 records.

The backend is written in Python and has a webpage GUI frontend created with Flask (a Python web framework).

Installations for frontend
---

    cd frontend
    python3 -m venv venv
    ./venv/bin/activate (alternatively: chmod +x activate)
    pip install Flask
    pip install Flask-WTF
    
In case of error: `No module named "flask_wtf"` install "Flask WTF" through IDE (or other means).
   
Run program
---

    chmod +x ./run.sh
    ./run.sh
    
or

    python3 ./run.py    

The program will run in debug mode.

Web GUI:
---
Choosing User and recommend parameters:
![GUI](data/admin_module.JPG)

Result recommendation for that User:
![GUI](data/recommend_result.JPG)
