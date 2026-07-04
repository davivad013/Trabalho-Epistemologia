import json
import os
import urllib.request
import urllib.parse
import re

json_path = "/home/al.carlos.pereira/Documentos/Trabalho-Epistemologia/app/data/info.json"
images_dir = "/home/al.carlos.pereira/Documentos/Trabalho-Epistemologia/app/static/imagens"

# Load JSON
with open(json_path, "r", encoding="utf-8") as f:
    authors = json.load(f)

# Get images
images = os.listdir(images_dir)

def search_wikipedia(name):
    # Try Portuguese wikipedia first
    url = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(name)}&utf8=&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data['query']['search']:
                title = data['query']['search'][0]['title']
                return f"https://pt.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
    except Exception as e:
        pass
    
    # Try English wikipedia
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(name)}&utf8=&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data['query']['search']:
                title = data['query']['search'][0]['title']
                return f"https://en.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
    except:
        pass
    return None

for author in authors:
    # 1. Match image
    # Generate expected filename: e.g. "Ian Hacking" -> "ian-hacking"
    expected_base = author["name"].lower().replace(" ", "-").replace("'", "").replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    for img in images:
        if img.startswith(expected_base):
            author["image"] = f"/static/imagens/{img}"
            break
            
    # 2. Wikipedia Reference
    wiki_url = search_wikipedia(author["name"])
    if wiki_url:
        author["reference"] = wiki_url

# If Bas van Fraassen is missing, let's add him (since he's in the updated PDF)
bas_found = any("Fraassen" in a["name"] for a in authors)
if not bas_found:
    bas = {
        "id": "bas-van-fraassen",
        "name": "Bas van Fraassen",
        "nationality": "Holandês (carreira acadêmica nos Estados Unidos)",
        "birth": 1941,
        "death": None,
        "continent": "América do Norte",
        "shortDescription": "Bas van Fraassen é um dos principais filósofos da ciência contemporânea e formulador do empirismo construtivo. Sua teoria defende que o objetivo da ciência é construir teorias empiricamente adequadas, sem exigir que elas sejam consideradas literalmente verdadeiras em relação às entidades não observáveis.",
        "longDescription": "Bas van Fraassen é um filósofo da ciência contemporâneo conhecido por desenvolver o empirismo construtivo, uma das principais correntes da epistemologia científica nas últimas décadas. Em oposição ao realismo científico, van Fraassen argumenta que o objetivo da ciência não é descobrir a verdade sobre entidades não observáveis, mas produzir teorias empiricamente adequadas, isto é, capazes de explicar corretamente os fenômenos observáveis. Segundo essa perspectiva, aceitar uma teoria científica significa reconhecer sua capacidade explicativa e preditiva em relação às observações, sem assumir necessariamente que todas as entidades postuladas pela teoria realmente existam. Essa posição procura preservar o sucesso da ciência sem comprometer-se com uma interpretação metafísica das teorias científicas. Sua filosofia influenciou profundamente os debates contemporâneos sobre realismo científico, explicação, observação, modelos científicos e racionalidade. O empirismo construtivo tornou-se uma das alternativas mais importantes ao realismo científico durante o final do século XX e permanece amplamente discutido na epistemologia da ciência.",
        "books": [
            {"title": "The Scientific Image", "year": 1980},
            {"title": "Laws and Symmetry", "year": 1989},
            {"title": "Scientific Representation: Paradoxes of Perspective", "year": 2008}
        ],
        "flag": "🇳🇱"
    }
    # Match image for Bas
    for img in images:
        if img.startswith("bas-van-fraassen"):
            bas["image"] = f"/static/imagens/{img}"
            break
    
    wiki_url = search_wikipedia("Bas van Fraassen")
    if wiki_url:
        bas["reference"] = wiki_url

    authors.append(bas)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(authors, f, ensure_ascii=False, indent=2)

print("JSON updated successfully!")
