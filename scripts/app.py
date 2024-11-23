import streamlit as st
st.sidebar.title('Nuvem de Palavras ☁️')
st.sidebar.markdown('Este projeto gera uma nuvem de palavras a partir de um texto, destacando visualmente as palavras mais frequentes. Utiliza técnicas de pré-processamento de linguagem natural (**NLP**) para limpar o texto, removendo pontuações e palavras comuns (**stopwords**).\n\nLink do repositório GitHub: https://github.com/ryanrodr/wordcloud')

tab1, tab2 = st.tabs(['wordcloud', 'sentiment-analysis'])

with tab1:
    st.header('Gerador de Nuvem de Palavras')
    st.write('Em produção...')
with tab2:
    st.header("Análise de Sentimento")
    st.write('Em produção...')