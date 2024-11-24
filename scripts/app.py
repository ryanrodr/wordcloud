import streamlit as st
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string
import nltk
nltk.download('stopwords', quiet=True)

def nuvem_palavras(text, colormap):
    stop_words = set(stopwords.words('portuguese'))

    # Remove a pontuação do texto e converte os caracteres para minúsculas 
    texto_limpo = ''.join([char.lower() for char in text if char not in string.punctuation])

    # Separa as palavras do texto e remove as stop words
    palavras = [palavra for palavra in texto_limpo.split() if palavra not in stop_words]
    
    # Gerar a nuvem de palavras com as palavras já tratadas
    wordcloud = WordCloud(width=800,
                          height=400,
                          background_color='black',
                          colormap=colormap,
                          max_words=max_words).generate(' '.join(palavras))

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)  # Exibe o gráfico no Streamlit

# Configuração da interface Streamlit
st.sidebar.title('Nuvem de Palavras ☁️')
st.sidebar.markdown('Este projeto gera uma nuvem de palavras a partir de um texto, destacando visualmente as palavras mais frequentes. Utiliza técnicas de pré-processamento de linguagem natural (**NLP**) para limpar o texto, removendo pontuações e palavras comuns (**stopwords**).\n\nLink do repositório GitHub: https://github.com/ryanrodr/wordcloud')

tab1, tab2 = st.tabs(['wordcloud', 'sentiment-analysis'])

with tab1:
    st.header('Gerador de Nuvem de Palavras')
    
    # Adiciona uma caixa de texto para entrada do usuário
    user_input = st.text_area("Insira o texto para gerar uma nuvem de palavras:")
    
    colormap = st.selectbox("Escolha o colormap:", 
    ['Blues', 'Purples', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'])
    
    max_words = st.slider("Número máximo de palavras na nuvem:", min_value=50, max_value=500, value=200, step=50)

    if st.button("Gerar Nuvem"):
        if user_input.strip():  # Verifica se o texto não está vazio
            nuvem_palavras(user_input, colormap)
        else:
            st.warning("Insira algum texto para gerar a nuvem de palavras")

with tab2:
    st.header("Análise de Sentimento")
    st.write('Em produção...')
