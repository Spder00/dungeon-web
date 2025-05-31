players = []

zauber_liste = [
    {"name": "Magische Geschosse", "beschreibung": "3x 1W4+1 Schaden"},
    {"name": "Heilendes Wort", "beschreibung": "1W4+Mod Heilung"},
    {"name": "Schild", "beschreibung": "+5 RK für 1 Runde"},
]

räume = [
    "Ein modriger Raum mit Spinnweben.",
    "Eine zerfallene Bibliothek.",
    "Ein runder Saal mit Kristall.",
    "Ein überwucherter Altar.",
    "Ein kalter Kerker mit Gittern."
]

def log(text):
    document.getElementById("log").innerHTML += f"<p>{text}</p>"

def update_list():
    pl = sorted(players, key=lambda x: x['ini'], reverse=True)
    ul = document.getElementById("player-list")
    ul.innerHTML = ""
    for p in pl:
        ul.innerHTML += f"<li>{p['name']} – Ini: {p['ini']} – TP: {p['tp']}</li>"
    save_data()

def add_player():
    name = document.getElementById("name").value
    ini = document.getElementById("ini").value
    tp = document.getElementById("tp").value
    if name and ini and tp:
        players.append({"name": name, "ini": int(ini), "tp": int(tp)})
        update_list()
        document.getElementById("name").value = ""
        document.getElementById("ini").value = ""
        document.getElementById("tp").value = ""

def random_spell():
    z = random.choice(zauber_liste)
    log(f"✨ <b>{z['name']}</b>: {z['beschreibung']}")

def random_room():
    raum = random.choice(räume)
    log(f"📜 Dungeonraum: {raum}")

def roll_die():
    augenzahlen = [4, 6, 8, 10, 12, 20, 100]
    erg = [f"W{w} = {random.randint(1, w)}" for w in augenzahlen]
    log("🎲 " + " | ".join(erg))

def save_data():
    # Spieler in localStorage speichern
    window.localStorage.setItem("spielerdaten", json.dumps(players))

def load_data():
    global players
    data = window.localStorage.getItem("spielerdaten")
    if data:
        players = json.loads(data)
        update_list()

def clear_data():
    window.localStorage.removeItem("spielerdaten")
    players.clear()
    update_list()
    log("🗑️ Gespeicherte Daten gelöscht.")

# Lade beim Start
load_data()
