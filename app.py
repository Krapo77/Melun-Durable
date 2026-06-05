import streamlit as st
import streamlit.components.v1 as components
import json

# Configuration de la page Streamlit
st.set_page_config(layout="wide", page_title="Melun Open Data")

# 1. Charger les données du fichier JSON
with open("melun_data.json", "r", encoding="utf-8") as f:
    json_data = f.read()

# 2. Charger le code de ton fichier index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. Injection propre des données en remplaçant l'appel fetch d'origine
old_fetch = "fetch('melun_data.json').then(r => r.json()).then(data => {"
new_injection = f"const data = {json_data};\n(() => {{"

if old_fetch in html_content:
    html_content = html_content.replace(old_fetch, new_injection)
else:
    # Si le format diffère légèrement, on force la variable au début du script
    html_content = html_content.replace("<script>", f"<script>\nconst data = {json_data};")

# 4. Affichage de la carte (Ajustement de la hauteur pour correspondre à ton écran)
components.html(html_content, height=850, scrolling=True)