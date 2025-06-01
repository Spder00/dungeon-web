from pyscript import Element
from js import document
import random

# 🎲 Wurf-Funktion
def wuerfeln(evt):
    wurf = random.randint(1, 20)
    Element("ausgabe").element.innerText = f"🎲 Du hast eine {wurf} gewürfelt!"

# 💾 Speicher-Funktion (simuliert)
def speichern(evt):
    Element("ausgabe").element.innerText = "💾 Spielstand gespeichert! (Demo)"

# 🧷 Event-Listener verbinden
document.getElementById("btn-wuerfeln").addEventListener("click", wuerfeln)
document.getElementById("btn-speichern").addEventListener("click", speichern)
