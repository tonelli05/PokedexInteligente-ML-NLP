# PokedexInteligente-ML-NLP

Este projeto utiliza Machine Learning e Processamento de Linguagem Natural (NLP) para analisar e classificar Pokémon com base em suas descrições biológicas e atributos de performance.

- Escopo de Treinamento vs. Aplicação Real <br>
  Treinamento e Teste: O modelo foi treinado, testado e validado utilizando exclusivamente os dados dos 151 Pokémon da Primeira Geração (Kanto). <br>
  Versatilidade da Aplicação: Apesar do escopo de treino, a aplicação foi desenhada para ser global. Você pode inserir a descrição da Pokédex de qualquer Pokémon de qualquer geração que o algoritmo realizará a previsão do tipo baseando-se nos padrões aprendidos.


- Funcionalidades <br>
  Predição de Tipo (NLP): Um modelo de classificação de texto que analisa a descrição biográfica e identifica o tipo principal do Pokémon. <br>
  Análise de Performance (Clustering): Agrupamento de Pokémon em perfis de combate (Ex: Muralha Física, Atacante de Elite) utilizando o algoritmo K-Means.


- Inteligência Artificial <br>
  Modelo de Texto: LinearSVC treinado com representação TF-IDF (1000 features). <br>
  Acurácia: O modelo atingiu 70,97% de precisão flexível na classificação de tipos. <br>
  Processamento: Utiliza técnicas de Stemming e remoção de Stopwords para focar nas palavras que realmente definem o tipo (ex: "burn", "water", "leaf").


- Notas Importantes sobre a Acurácia <br>
  Distribuição de Tipos: Pokémon dos tipos Gelo, Dragão, Fantasma e Fada apresentam uma taxa de acerto menor. Isso ocorre porque a primeira geração possui pouquíssimos (ou nenhum, no caso de Fada) representantes desses tipos, gerando menos dados para o aprendizado do modelo. <br>
  Pokémon Lendários: Estes podem ser particularmente difíceis de prever. Suas descrições na Pokédex costumam focar em mitos, lendas e feitos heroicos, detalhando pouco as suas características biológicas e poderes elementais, que são a base da nossa análise de texto.


- Agrupamento (Clusters) <br>
  Os Pokémon foram divididos em 5 categorias baseadas em seus status base (HP, Attack, Defense, Special Attack, Special Defense, Speed): <br>
  Atacante de Elite: Alto poder ofensivo. <br> 
  Muralha Física: Defesa extrema. <br>
  Colosso de Vitalidade: Foco em HP alto. <br>
  Equilibrado: Atributos distribuídos de forma homogênea. <br>
  Básico: Status iniciais ou reduzidos.


- Tecnologias Utilizadas <br>
  Linguagem: Python. <br>
  Bibliotecas: Pandas, Scikit-learn (LinearSVC), Plotly Dash, NLTK. <br>
  Representação de Texto: TF-IDF com 1000 features.


- Como Executar <br>
  Instale as dependências: pip install dash pandas scikit-learn nltk requests unidecode; <br>
  Certifique-se de que os arquivos .pkl e o .csv estão na mesma pasta do app.py; <br>
  Execute o comando: python app.py; <br>
  Acesse a rota gerada no seu terminal.
