Semestrální prace k předmětu BI-VWM na téma kolaborativní filtrování. Dataset z MovieLens (http://movielens.org).

Instalace pro frontend
---

    cd frontend
    python3 -m venv venv
    ./venv/bin/activate (pripdne chmod +x activate)
    pip install Flask
    pip install Flask-WTF
    
pokud pořád bude hlásit chybu `No module named "flask_wtf"` tak jít do nastavení PyCharmu a ručně nainstalovat Flask WTF
   
   
Spusteni
---

    chmod +x ./run.sh
    ./run.sh
    
nebo

    python3 ./run.py    

Program se spusti v debug modu takže se změny ihned zobrazí (pokud ne tak hard refresh - `SHIFT + R`)