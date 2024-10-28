from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string
import nltk
nltk.download('stopwords', quiet=True)

def nuvem_palavras(text):
    """
    Processa um texto em português, removendo pontuações e palavras comuns (stop words).
    Gera e exibe uma nuvem de palavras, destacando visualmente as palavras mais frequentes.
    """
    stop_words = set(stopwords.words('portuguese'))

    # Remove a pontuação do texto e converte os caracteres para minúsculas 
    texto_limpo = ''.join([char.lower() for char in text if char not in string.punctuation])

    # Separa as palavras do texto e remove as stop words
    palavras = [palavra for palavra in texto_limpo.split() if palavra not in stop_words]
    
    # Gerar a nuvem de palavras com as palavras já tratadas
    wordcloud = WordCloud(width=800,
                          height=400,
                          background_color='black',
                          colormap='Purples',
                          max_words=200).generate(' '.join(palavras))

    # Configurar o tamanho da imagem e suavizar a exibição
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

text = str(input('Digite um texto: '))
nuvem_palavras(text)