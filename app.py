import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import pickle
import plotly.express as px
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import unidecode
from nltk import tokenize

#baixar recursos necessarios do NLTK
nltk.download('stopwords')

#removendo stopwords
palavras_irrelevantes = nltk.corpus.stopwords.words('english')

#stopwords sem acento
stopwords_sem_acentos = [unidecode.unidecode(palavra) for palavra in palavras_irrelevantes]

#criando tokens de pontuacao
token_pontuacao = tokenize.WordPunctTokenizer()

#simplificando as palavras
stemmer = SnowballStemmer('english')

# 1. FUNCAO DE LIMPEZA (IGUAL AO TREINO)
def limpeza_texto(texto):

    #removendo os acentos e deixando minusculo
    texto_sem_acento = unidecode.unidecode(texto).lower()

    #quebrando em tokens por pontuacao
    palavras_texto = token_pontuacao.tokenize(texto_sem_acento)

    #removendo as stopwords sem acento e pontuacao
    frase_limpa = [palavra for palavra in palavras_texto if palavra not in stopwords_sem_acentos and palavra.isalpha()]

    #simplificando ao radical as palavras
    frase_simplificada = [stemmer.stem(palavra) for palavra in frase_limpa]

    return ' '.join(frase_simplificada)


# 2. CARREGAMENTO DE DADOS E MODELOS
df = pd.read_csv('pokemon_data_final.csv')
with open('modelo_pokemon_svc.pkl', 'rb') as f:
    modelo_svc = pickle.load(f)
with open('tfidf_1000.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# 3. INTERFACE (LAYOUT)
app = dash.Dash(__name__, title="Pokédex ML & Clusters")

app.layout = html.Div([
    html.H1("Pokédex Inteligente: Machine Learning & NLP", style={'textAlign': 'center'}),
    
    html.Div([
        html.H3("🔍 Identificador de Tipo via Descrição"),
        dcc.Textarea(
            id='input-texto', 
            placeholder='Insira a descrição da Pokédex...',
            style={'width': '100%', 'height': 100, 'borderRadius': '5px'}
        ),
        html.Br(),
        html.Button('Analisar Descrição', id='botao-analisar', n_clicks=0, 
                    style={'backgroundColor': '#EE1515', 'color': 'white', 'padding': '10px 20px', 'cursor': 'pointer'}),
    ], style={'padding': '20px', 'backgroundColor': '#f9f9f9', 'borderRadius': '10px'}),

    # Resultado da Previsao
    html.Div(id='container-resultado', style={'marginTop': '20px', 'textAlign': 'center'}),

    html.Hr(),

    # Grafico de Clusters 
    html.Div([
        html.H3("📊 Análise de Performance (Clusters K-Means)"),
        dcc.Graph(id='grafico-clusters')
    ], style={'marginTop': '40px'})

], style={'maxWidth': '1000px', 'margin': '0 auto', 'fontFamily': 'Arial'})

# 4. CALLBACK UNICO
@app.callback(
    [Output('container-resultado', 'children'),
     Output('grafico-clusters', 'figure')],
    Input('botao-analisar', 'n_clicks'),
    State('input-texto', 'value')
)
def processar_tudo(n_clicks, texto_usuario):
    # Grafico de Clusters sempre visivel
    fig = px.scatter(df, x='attack', y='defense', color='cluster_nome',
                     hover_name='nome', title="Distribuição de Status por Cluster")
    fig.update_layout(title_x=0.5)

    if n_clicks == 0 or not texto_usuario:
        return "", fig

    # Logica da IA
    texto_processado = limpeza_texto(texto_usuario)
    vetor = tfidf.transform([texto_processado])
    previsao = modelo_svc.predict(vetor)[0]
    
    # HTML do Resultado
    resultado_html = html.Div([
        html.H2(f"Tipo Identificado: {previsao.upper()}", style={'color': '#EE1515'}),
        html.P(f"Baseado no modelo SVC com 70.97% de acurácia flexível.")
    ], style={'border': '2px solid #EE1515', 'padding': '20px', 'borderRadius': '15px'})

    return resultado_html, fig

if __name__ == '__main__':
    app.run(debug=True)