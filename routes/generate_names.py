from flask import Blueprint, render_template
import random

generate_names = Blueprint('generate_names', __name__)


@generate_names.route('/generate/names/orc')
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


@generate_names.route('/generate/names/elf')
def generate_elf_names(n=10):
    prefixes = ["Al", "Eld", "Fa", "Gla", "La", "Mel", "Nim", "Or", "Syl", "Thal",
            "Vand", "El", "Lir", "Ril", "Ael", "Faer", "Ith", "Ryn", "Tal", "Vor"]

    middles = ["ar", "en", "il", "or", "an", "el", "is", "as", "in", "or",
            "al", "en", "el", "ir", "il", "ra", "on", "or", "ir", "an"]

    suffixes = ["ion", "iel", "ar", "an", "on", "el", "as", "is", "us", "or",
                "or", "ae", "ir", "il", "en", "is", "an", "ar", "il", "ith"]
    
    elf_names = []
    for _ in range(n):
        name_length = random.randint(1, 3)

        name_parts = [random.choice(prefixes)]
        if name_length > 1:
            name_parts.append(random.choice(middles))
        if name_length > 2:
            name_parts.append(random.choice(suffixes))
        elf_names.append(''.join(name_parts))
    return elf_names

#entre outras coisas, nomes de vilas, cidades, castelos, tavernas (estabelecimentos no geral)
#gerar nomes para outras raças, humanos, halflings, anões,  
