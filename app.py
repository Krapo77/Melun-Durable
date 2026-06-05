import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(layout="wide", page_title="Melun Open Data")

# 1. Charger les données JSON
with open("melun_data.json", "r", encoding="utf-8") as f:
    json_data = f.read()

# 2. Charger le code HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 3. Injecter proprement les données à la fin du script sans casser les filtres
injection_script = f"""
<script>
    const dataFromServer = {json_data};
    initMapWithData(dataFromServer);
</script>
</body>
"""
html_content = html_content.replace("</body>", injection_script)

# 4. Affichage final
components.html(html_content, height=850, scrolling=True)