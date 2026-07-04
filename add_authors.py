import json
import os

with open("app/data/info.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add new authors
new_authors = [
    {
        "id": "nelson-goodman",
        "name": "Nelson Goodman",
        "nationality": "Estadunidense",
        "birth": 1906,
        "death": 1998,
        "continent": "América do Norte",
        "shortDescription": "Nelson Goodman contribuiu para a epistemologia da ciência ao reformular o problema da indução por meio do famoso paradoxo do \"grue\". Sua obra mostrou que a confirmação científica depende não apenas das evidências, mas também das categorias conceituais e da linguagem utilizada para descrever o mundo.",
        "longDescription": "Nelson Goodman foi um filósofo norte-americano cuja obra exerceu grande influência sobre a epistemologia, a lógica, a filosofia da linguagem e a filosofia da ciência. Sua principal contribuição para a epistemologia da ciência consiste na reformulação do chamado problema da indução, originalmente apresentado por David Hume. Em sua obra, Goodman mostrou que a dificuldade da indução não está apenas em justificar inferências do passado para o futuro, mas também em determinar quais regularidades observadas podem ser legitimamente projetadas. Para ilustrar esse problema, formulou o famoso paradoxo do \"grue\" (\"verdul\"), mostrando que diferentes hipóteses podem ser igualmente compatíveis com as evidências disponíveis, mas conduzir a previsões incompatíveis. Essa análise revelou que a aceitação de hipóteses científicas depende das práticas conceituais, da linguagem utilizada e da história de confirmação das teorias. Goodman também defendeu que diferentes sistemas simbólicos podem construir maneiras distintas, porém igualmente legítimas, de descrever a realidade. Sua filosofia contribuiu para ampliar o debate epistemológico sobre a natureza da objetividade científica, os critérios de confirmação e o papel da linguagem na construção do conhecimento.",
        "books": [
            {"title": "Fact, Fiction, and Forecast", "year": 1955},
            {"title": "Languages of Art", "year": 1968},
            {"title": "Ways of Worldmaking", "year": 1978}
        ],
        "image": "/static/imagens/nelson-goodman.jpeg",
        "flag": "🇺🇸",
        "countryIso": "840"
    },
    {
        "id": "theophile-obenga",
        "name": "Théophile Obenga",
        "nationality": "Congolês (República do Congo)",
        "birth": 1936,
        "death": None,
        "continent": "África",
        "shortDescription": "Théophile Obenga é um historiador e linguista congolês que, seguindo Cheikh Anta Diop, aplicou o método da linguística histórica comparada para demonstrar os vínculos entre o Egito Antigo e a África negra. Sua obra reforçou a exigência de rigor metodológico na produção de uma história científica africana.",
        "longDescription": "Théophile Obenga é um historiador, linguista e egiptólogo congolês, discípulo direto de Cheikh Anta Diop e um de seus principais continuadores intelectuais. A partir do encontro com Diop no colóquio da UNESCO de 1974, dedicado ao povoamento do Egito Antigo, Obenga desenvolveu uma linha própria de pesquisa concentrada na linguística histórica comparada, buscando demonstrar parentescos genéticos entre a língua egípcia antiga e diversas línguas negro-africanas, como o wolof. Sua principal contribuição metodológica foi criticar o método de comparação em massa proposto pelo linguista Joseph Greenberg, por considerá-lo incapaz de comprovar parentescos genéticos reais entre línguas, e propor em seu lugar o rigor da linguística histórica clássica, que exige a demonstração de correspondências regulares e sistemáticas entre os idiomas comparados. Com base nesse método, Obenga formulou a hipótese de uma família linguística \"negro-egípcia\", situando o egípcio antigo dentro do conjunto das línguas africanas. Na epistemologia da ciência, sua contribuição central foi exigir que a reivindicação da africanidade do Egito Antigo fosse sustentada por métodos científicos rigorosos e verificáveis, e não apenas por argumentos políticos ou identitários. Obenga defendia, assim, uma ciência histórica africana que dialogasse em pé de igualdade com a comunidade acadêmica internacional, submetendo suas hipóteses aos mesmos critérios de prova exigidos de qualquer disciplina científica.",
        "books": [
            {"title": "L'Afrique dans l'Antiquité: Égypte pharaonique, Afrique noire", "year": 1973},
            {"title": "Ancient Egypt and Black Africa: A Student's Handbook for the Study of Ancient Egypt in Philosophy, Linguistics and Gender Relations", "year": 1992},
            {"title": "African Philosophy: The Pharaonic Period, 2780–330 BC", "year": 1990}
        ],
        "image": "/static/imagens/théophile-obenga.jpeg",
        "flag": "🇨🇬",
        "countryIso": "178"
    },
    {
        "id": "mogobe-ramose",
        "name": "Mogobe Ramose",
        "nationality": "Sul-africano",
        "birth": 1945,
        "death": None,
        "continent": "África",
        "shortDescription": "Mogobe Ramose é um filósofo sul-africano que desenvolveu a filosofia do Ubuntu como alternativa epistemológica ao paradigma ocidental de conhecimento. Sua obra denuncia o \"epistemicídio\" colonial e defende a libertação das concepções africanas de realidade, verdade e justiça.",
        "longDescription": "Mogobe Bernard Ramose é um filósofo sul-africano, um dos principais responsáveis pela internacionalização da filosofia africana, em especial da filosofia do Ubuntu. Exilado da África do Sul durante o regime do apartheid, doutorou-se na Bélgica e lecionou em diversos países africanos e europeus antes de retornar ao seu país em 1996. Sua obra desenvolve o conceito de Ubuntu — a ideia de humanidade partilhada, presente em diversas línguas bantu — como base de uma filosofia africana original de conhecimento, ética, direito e política. Ramose argumenta que a filosofia ocidental, desde Aristóteles até o Iluminismo, construiu-se sobre uma definição excludente de racionalidade que serviu para justificar a escravidão e a colonização dos povos africanos. Para ele, esse processo constituiu um verdadeiro \"epistemicídio\": a destruição sistemática de formas africanas de conhecer o mundo, substituídas à força pelo paradigma epistemológico europeu. Sua principal contribuição para a epistemologia da ciência é a defesa de uma \"libertação epistemológica\" da África: a necessidade de romper com a dominação do paradigma europeu de conhecimento, verdade e realidade, para que possa emergir um universo de discurso comum, autêntico e plural, capaz de reconhecer o Ubuntu e outras cosmovisões africanas como fontes legítimas de racionalidade e saber.",
        "books": [
            {"title": "African Philosophy Through Ubuntu", "year": 1999},
            {"title": "Hegel's Twilight: Liber Amicorum Discipulorumque Pro Heinz Kimmerle (org.)", "year": 2013},
            {"title": "Contrasts and Contests About Philosophy", "year": 2016}
        ],
        "image": "/static/imagens/mogobe-ramose.jpeg",
        "flag": "🇿🇦",
        "countryIso": "710"
    },
    {
        "id": "kwasi-wiredu",
        "name": "Kwasi Wiredu",
        "nationality": "Ganês",
        "birth": 1931,
        "death": 2022,
        "continent": "África",
        "shortDescription": "Kwasi Wiredu foi um filósofo ganês que desenvolveu o conceito de \"descolonização conceitual\", mostrando que muitas noções tidas como universais na ciência e na filosofia ocidentais são, na verdade, particularidades culturais. Sua obra defende uma investigação filosófica mais atenta à diversidade linguística e conceitual das culturas africanas.",
        "longDescription": "Kwasi Wiredu foi um filósofo ganês, formado na tradição analítica em Oxford, frequentemente considerado o mais influente filósofo africano de sua geração. Sua obra é conhecida sobretudo pelo conceito de \"descolonização conceitual\", apresentado em 1980 durante um encontro de especialistas da UNESCO em Nairóbi. Segundo Wiredu, muitos conceitos e categorias tidos como universais na filosofia ocidental — como certas noções de verdade, ser ou pessoa — são, na verdade, particularidades da língua e da cultura europeias, e simplesmente não se sustentam quando traduzidos para línguas africanas, como o akan. A partir dessa constatação, Wiredu propôs que os filósofos africanos examinassem criticamente os conceitos herdados do colonialismo, distinguindo o que neles é genuinamente universal daquilo que é apenas uma imposição etnocêntrica disfarçada de universalidade. Ao mesmo tempo, defendia que os recursos das línguas e do pensamento africanos tradicionais deveriam ser tratados como ideias filosóficas legítimas, e não como meras curiosidades antropológicas, podendo inclusive contribuir para resolver problemas da própria filosofia ocidental. Sua contribuição central para a epistemologia da ciência foi mostrar que a busca por conhecimento e por critérios de verdade não é neutra do ponto de vista linguístico e cultural: conceitos científicos e filosóficos apresentados como universais devem ser postos à prova em diferentes esquemas conceituais, o que exige uma ciência mais consciente de seus próprios pressupostos culturais e mais aberta à pluralidade de racionalidades humanas.",
        "books": [
            {"title": "Philosophy and an African Culture", "year": 1980},
            {"title": "Cultural Universals and Particulars: An African Perspective", "year": 1996},
            {"title": "A Companion to African Philosophy (org.)", "year": 2004}
        ],
        "image": "/static/imagens/kwasi-wiredu.jpeg",
        "flag": "🇬🇭",
        "countryIso": "288"
    },
    {
        "id": "paulin-jidenu-hountondji",
        "name": "Paulin Jidenu Hountondji",
        "nationality": "Beninense",
        "birth": 1942,
        "death": 2024,
        "continent": "África",
        "shortDescription": "Paulin Hountondji foi um filósofo beninense conhecido por sua crítica à \"etnofilosofia\" e por defender que a filosofia africana deveria seguir padrões universais de rigor e argumentação. Sua obra também investigou as condições desiguais da produção científica entre África e os centros de pesquisa do Norte global.",
        "longDescription": "Paulin Jidenu Hountondji foi um filósofo, político e acadêmico beninense, formado na École Normale Supérieure de Paris sob influência de Louis Althusser e Jacques Derrida. É considerado um dos fundadores da filosofia africana contemporânea, principalmente por sua crítica contundente à chamada \"etnofilosofia\" — corrente que, segundo ele, confundia descrições antropológicas das visões de mundo coletivas de povos africanos com filosofia propriamente dita, atribuindo a comunidades inteiras, e não a indivíduos identificáveis, teses filosóficas sistemáticas. Para Hountondji, a filosofia é, por definição, um exercício individual, crítico e argumentativo, do qual um autor assume publicamente a responsabilidade; por isso, ele defendia que a filosofia africana deveria adotar padrões universais de racionalidade, rigor lógico e método científico, em vez de se apoiar apenas na valorização romântica de uma suposta \"sabedoria coletiva\" ou \"filosofia implícita\" dos povos africanos. Em obras posteriores, sua posição se tornou mais matizada, admitindo maior diálogo entre o pensamento tradicional africano e o método filosófico rigoroso. Sua principal contribuição para a epistemologia da ciência foi analisar as condições institucionais e materiais da produção científica na África, mostrando como o continente frequentemente ocupava um papel de mero fornecedor de dados brutos para teorias elaboradas em centros de pesquisa do Norte global. Hountondji defendia a construção de comunidades científicas africanas autônomas, capazes de gerar teoria própria e não apenas coletar informação para ser processada no exterior.",
        "books": [
            {"title": "Sur la \"philosophie africaine\": critique de l'ethnophilosophie / African Philosophy: Myth and Reality", "year": 1983},
            {"title": "The Struggle for Meaning: Reflections on Philosophy, Culture and Democracy in Africa", "year": 2002},
            {"title": "Endogenous Knowledge: Research Trails (org.)", "year": 1997}
        ],
        "image": "/static/imagens/paulin-jidenu-hountondji.jpeg",
        "flag": "🇧🇯",
        "countryIso": "204"
    },
    {
        "id": "henry-odera-oruka",
        "name": "Henry Odera Oruka",
        "nationality": "Queniano",
        "birth": 1944,
        "death": 1995,
        "continent": "África",
        "shortDescription": "Henry Odera Oruka foi um filósofo queniano criador do Projeto de Filosofia dos Sábios, que identificou, por meio de entrevistas de campo, indivíduos capazes de exercer pensamento crítico e racional dentro da tradição oral africana. Sua obra ampliou os critérios do que se reconhece como produção filosófica e científica legítima.",
        "longDescription": "Henry Odera Oruka foi um filósofo queniano, professor da Universidade de Nairóbi e fundador do departamento de Filosofia dessa instituição, separado do departamento de Religião após anos de disputa acadêmica. É mundialmente conhecido por ter criado o \"Projeto de Filosofia dos Sábios\" (Sage Philosophy Project), iniciado na década de 1970, que consistia em entrevistar sistematicamente anciãos e pensadores tradicionais de comunidades queniana, registrando e analisando filosoficamente suas reflexões sobre temas como conhecimento, moralidade, natureza e comunidade. Odera Oruka distinguia entre a \"sabedoria popular\" (folk sage), que reproduz de forma consensual as crenças e valores aceitos por uma comunidade, e a \"sagacidade filosófica\" (philosophic sagacity), praticada por indivíduos que, mesmo sem formação acadêmica ou escrita, submetem essas mesmas crenças a um exame crítico, racional e argumentativo. Com essa distinção, buscava demonstrar empiricamente que o pensamento crítico e sistemático não era um privilégio da tradição escrita ocidental, mas também podia ser encontrado, por meio da oralidade, em indivíduos específicos dentro das sociedades africanas tradicionais. Sua principal contribuição para a epistemologia da ciência foi fornecer uma metodologia empírica de campo — a entrevista filosófica documentada — capaz de identificar racionalidade crítica em contextos orais, ampliando a própria definição do que conta como atividade filosófica e científica legítima e contestando a ideia de que o conhecimento rigoroso dependeria necessariamente da escrita ou das instituições acadêmicas ocidentais.",
        "books": [
            {"title": "Sage Philosophy: Indigenous Thinkers and Modern Debate on African Philosophy", "year": 1990},
            {"title": "Punishment and Terrorism in Africa", "year": 1976},
            {"title": "Trends in Contemporary African Philosophy (org.)", "year": 1990}
        ],
        "image": "/static/imagens/henry-odera-oruka.jpeg",
        "flag": "🇰🇪",
        "countryIso": "404"
    }
]

# We also need to map existing ones to countryIso so they can appear in the new map.
iso_map = {
    "ian-hacking": "124", # Canada
    "thomas-kuhn": "840", # USA
    "larry-laudan": "840",
    "bimal-krishna-matilal": "356", # India
    "sundar-sarukkai": "356",
    "mou-zongsan": "156", # China
    "jitendra-nath-mohanty": "356",
    "karen-ann-watson-gegeo": "090", # Solomon Islands
    "david-welchman-gegeo": "090", # Solomon Islands
    "cresantia-frances-koya": "242", # Fiji
    "linda-tuhiwai-smith": "554", # New Zealand
    "toon-van-meijl": "554", # NZ (research focus) or 528 (Netherlands). Actually if he's mapped to a country for the map, the user says "autores desse país". Let's put Netherlands (528) as nationality is Neerlandês.
    "oscar-varsavsky": "032", # Argentina
    "walter-mignolo": "032", # Argentina
    "silvia-rivera-cusicanqui": "068", # Bolivia
    "rolando-garcia": "032", # Argentina
    "cheikh-anta-diop": "686", # Senegal
    "joseph-ki-zerbo": "854", # Burkina Faso
    "muyiwa-falaiye": "566", # Nigeria
    "bas-van-fraassen": "528", # Netherlands
}

existing_ids = {a["id"] for a in data}

for author in new_authors:
    if author["id"] not in existing_ids:
        data.append(author)

for author in data:
    if "countryIso" not in author and author["id"] in iso_map:
        author["countryIso"] = iso_map[author["id"]]
    if "image" in author and not author["image"].startswith("/static/"):
        author["image"] = author["image"].replace("images/", "/static/imagens/")

with open("app/data/info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Updated info.json")
