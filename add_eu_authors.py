import json

authors = [
    {
        "id": "karl-popper",
        "name": "Karl Popper",
        "nationality": "Austríaco-Britânico",
        "birth": 1902,
        "death": 1994,
        "continent": "Europa",
        "shortDescription": "Karl Popper propôs o falsificacionismo como critério de demarcação entre ciência e não-ciência, argumentando que o conhecimento científico progride por meio de refutações.",
        "longDescription": "Karl Popper foi um dos mais importantes filósofos da ciência do século XX. Sua principal contribuição, detalhada em 'A Lógica da Pesquisa Científica' (1934), foi a rejeição do método indutivo e a proposição do falsificacionismo. Para Popper, uma teoria só é científica se puder ser submetida a testes rigorosos que tentem falseá-la. A ciência não avança por meio da confirmação de verdades definitivas, mas através da eliminação de erros (conjecturas e refutações). Ele também foi um forte defensor da 'sociedade aberta' e um crítico do historicismo, influenciando não apenas a filosofia da ciência, mas também a filosofia política e social.",
        "books": [
            {"title": "A Lógica da Pesquisa Científica", "year": 1934},
            {"title": "Conjecturas e Refutações", "year": 1963},
            {"title": "A Sociedade Aberta e Seus Inimigos", "year": 1945}
        ],
        "image": "/static/imagens/karl-popper.jpeg",
        "flag": "🇦🇹",
        "countryIso": "040"
    },
    {
        "id": "gaston-bachelard",
        "name": "Gaston Bachelard",
        "nationality": "Francês",
        "birth": 1884,
        "death": 1962,
        "continent": "Europa",
        "shortDescription": "Gaston Bachelard desenvolveu a epistemologia histórica, destacando conceitos como 'obstáculo epistemológico' e 'ruptura epistemológica' no desenvolvimento científico.",
        "longDescription": "Gaston Bachelard foi um filósofo e epistemólogo francês cuja obra teve um impacto profundo na filosofia e na história da ciência. Ele argumentou que o progresso científico não é um acúmulo contínuo de conhecimento, mas ocorre por meio de 'rupturas epistemológicas' (ruptures épistémologiques), nas quais a ciência deve romper com o senso comum e com as intuições sensíveis. Ele também introduziu o conceito de 'obstáculo epistemológico' (obstacle épistémologique), que são noções preconcebidas e hábitos de pensamento que impedem a formulação de novas teorias e o avanço do conhecimento. Além de seu trabalho em epistemologia da ciência, Bachelard também é conhecido por seus estudos pioneiros sobre a poética e a imaginação, abordando os elementos (fogo, água, ar, terra).",
        "books": [
            {"title": "A Formação do Espírito Científico", "year": 1938},
            {"title": "O Novo Espírito Científico", "year": 1934},
            {"title": "A Poética do Espaço", "year": 1957}
        ],
        "image": "/static/imagens/gaston-bachelard.jpeg",
        "flag": "🇫🇷",
        "countryIso": "250"
    },
    {
        "id": "paul-feyerabend",
        "name": "Paul Feyerabend",
        "nationality": "Austríaco",
        "birth": 1924,
        "death": 1994,
        "continent": "Europa",
        "shortDescription": "Paul Feyerabend ficou famoso por seu 'anarquismo epistemológico', argumentando que não existe um único 'método científico' que conduza ao progresso.",
        "longDescription": "Paul Feyerabend foi um controverso filósofo da ciência austríaco que propôs uma visão radical conhecida como 'anarquismo epistemológico'. Em sua obra mais famosa, 'Contra o Método' (1975), Feyerabend argumentou que não existem regras metodológicas universais e imutáveis na ciência; ao contrário, ele afirmou que 'tudo vale' (anything goes) na busca pelo conhecimento. Para ele, o progresso científico, como nas revoluções introduzidas por Galileu, muitas vezes ocorre justamente porque os cientistas ignoram ou violam regras metodológicas consagradas. Ele criticou o status privilegiado e hegemônico dado à ciência moderna nas sociedades contemporâneas, defendendo a proliferação de teorias alternativas e valorizando outras formas de saber e tradições.",
        "books": [
            {"title": "Contra o Método", "year": 1975},
            {"title": "A Ciência em uma Sociedade Livre", "year": 1978},
            {"title": "Adeus à Razão", "year": 1987}
        ],
        "image": "/static/imagens/paul-feyerabend.jpeg",
        "flag": "🇦🇹",
        "countryIso": "040"
    },
    {
        "id": "imre-lakatos",
        "name": "Imre Lakatos",
        "nationality": "Húngaro-Britânico",
        "birth": 1922,
        "death": 1974,
        "continent": "Europa",
        "shortDescription": "Imre Lakatos propôs a metodologia dos 'Programas de Pesquisa Científica' como uma forma de reconciliar a visão falsificacionista de Popper com a perspectiva dos paradigmas de Kuhn.",
        "longDescription": "Imre Lakatos foi um influente filósofo da matemática e da ciência húngaro que construiu grande parte de sua carreira na London School of Economics, no Reino Unido. Ele procurou oferecer uma síntese e uma superação dos debates entre Karl Popper e Thomas Kuhn. A solução de Lakatos foi o conceito de 'Programas de Pesquisa Científica' (Scientific Research Programmes). Segundo essa teoria, a ciência se desenvolve não em torno de teorias isoladas que podem ser refutadas instantaneamente, mas através de amplos programas de pesquisa. Esses programas possuem um 'núcleo duro' (hard core) de suposições fundamentais que são protegidas de falsificação por um 'cinturão protetor' (protective belt) de hipóteses auxiliares. O progresso ocorre quando um programa é 'progressivo' (leva à descoberta de fatos novos) em oposição a ser 'degenerativo'.",
        "books": [
            {"title": "A Metodologia dos Programas de Pesquisa Científica", "year": 1978},
            {"title": "Provas e Refutações", "year": 1976}
        ],
        "image": "/static/imagens/imre-lakatos.jpeg",
        "flag": "🇭🇺",
        "countryIso": "348"
    },
    {
        "id": "bruno-latour",
        "name": "Bruno Latour",
        "nationality": "Francês",
        "birth": 1947,
        "death": 2022,
        "continent": "Europa",
        "shortDescription": "Bruno Latour foi pioneiro dos Estudos de Ciência e Tecnologia (STS) e co-desenvolvedor da Teoria Ator-Rede (ANT), enfatizando as redes sociotécnicas.",
        "longDescription": "Bruno Latour foi um sociólogo, antropólogo e filósofo da ciência francês cujo trabalho revolucionou os Estudos de Ciência, Tecnologia e Sociedade (STS). Ele é um dos fundadores da Teoria Ator-Rede (Actor-Network Theory - ANT), que propõe que a produção científica (e a sociedade como um todo) deve ser entendida através da rede de conexões entre atores humanos e 'não-humanos' (instrumentos, micróbios, textos, instituições), tratando-os de forma simétrica. Em livros como 'Vida de Laboratório' (escrito com Steve Woolgar) e 'Ciência em Ação', Latour estudou os cientistas na prática (a ciência enquanto está sendo feita), desmistificando a visão abstrata e idealizada do método científico. Ele demonstrou como o 'fatos' científicos são construídos (mas não arbitrariamente inventados) a partir de intensas negociações e estabilização de redes de atores.",
        "books": [
            {"title": "Vida de Laboratório: A Construção dos Fatos Científicos", "year": 1979},
            {"title": "Ciência em Ação", "year": 1987},
            {"title": "Jamais Fomos Modernos", "year": 1991}
        ],
        "image": "/static/imagens/bruno-latour.jpeg",
        "flag": "🇫🇷",
        "countryIso": "250"
    }
]

with open('app/data/info.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Append only if not already present
existing_ids = {a["id"] for a in data}
for a in authors:
    if a["id"] not in existing_ids:
        data.append(a)

with open('app/data/info.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

