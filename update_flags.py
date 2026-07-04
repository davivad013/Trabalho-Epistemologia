import json
flags = {
    'Canadense': '🇨🇦',
    'Estadunidense': '🇺🇸',
    'Argentino': '🇦🇷',
    'Fijiana': '🇫🇯',
    'Nigeriano': '🇳🇬',
    'Senegalês': '🇸🇳',
    'Neerlandês (Especialista na Cultura Maori)': '🇳🇱',
    'Indiano': '🇮🇳',
    'Burquinense (Burkina Faso)': '🇧🇫',
    'Salomônico': '🇸🇧',
    'Neozelandesa': '🇳🇿',
    'Boliviana': '🇧🇴',
    'Chinês': '🇨🇳',
    'Estadunidense (Pesquisadora nas Ilhas Salomão)': '🇺🇸'
}
with open("app/data/info.json", "r") as f:
    data = json.load(f)
for a in data:
    if a.get('nationality') in flags:
        a['flag'] = flags[a['nationality']]
with open("app/data/info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
