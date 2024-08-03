from flask import Flask
import math
import random

app = Flask(__name__)

@app.route('/orc_names')
def generate_orc_names(n=10):
    prefixes = ["Gor", "Mug", "Zog", "Thrug", "Krag", "Brak", "Drak", "Rok", "Grim", "Urg",
                "Thok", "Blarg", "Vrak", "Snag", "Dro", "Krug", "Gruk", "Lok", "Grash", "Mor"]

    middles = ["dum", "lok", "gar", "mok", "gor", "zug", "zag", "rok", "brog", "zug",
            "tar", "nok", "bur", "lug", "krak", "mog", "drek", "rug", "grok", "dak"]

    suffixes = ["nar", "rak", "gash", "thar", "dush", "gor", "grash", "mur", "gul", "zak",
                "burz", "nak", "thok", "drag", "shar", "mog", "brak", "lor", "rog", "drok"]
    
    orc_names = []
    for _ in range(n):
        name_length = random.randint(1, 3)
        name_parts = [random.choice(prefixes)]
        if name_length > 1:
            name_parts.append(random.choice(middles))
        if name_length > 2:
            name_parts.append(random.choice(suffixes))
        orc_names.append(''.join(name_parts))
    return orc_names


def generate_orc_name():
    prefix = random.choice(prefixes)
    middle = random.choice(middles)
    suffix = random.choice(suffixes)
    return prefix + middle + suffix

if __name__ == '__main__':
    app.run(debug=True)