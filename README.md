Semestrální prace k předmětu BI-VWM na téma kolaborativní filtrování. Dataset z MovieLens (http://movielens.org).

Instalace pro frontend
---

    cd frontend
    python3 -m venv venv
    ./venv/bin/activate (pripdne chmod +x activate)
    pip install Flask
    
Spusteni
---

    chmod +x ./run.sh
    ./run.sh
    
nebo

    python3 ./run.py    

Program se spusti v debug modu takže se změny ihned zobrazí (pokud ne tak hard refresh - `SHIFT + R`)