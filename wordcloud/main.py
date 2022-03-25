# O prgrama cria uma nuvem de palavras conforme arquivoo inserido.
# autor: Edson Sales<sales_eds@hotmail.com
#-----------------------------------------------------------------------------
import readline
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

arquivo = open('data/texto_1.txt', 'r') #Importa o arquivo de texto
texto = arquivo.readline()
arquivo.close()

figura = np.array(Image.open('img/index.jpeg')) #Importa a imagem para máscara
   
STOPWORDS = ['a','as','o','os','na','nas','no','nos','só','se','todos',
            'ou','ao','em', 'que', 'quem','qual','da','das','do','dos',
            'de','por','pra','para','pelo','pela','e','é','mim','me','tem',
            'sobre',
            'esse','essa','este','isso','isto','esta','esses','essas','nesta',
            'desta','desde',
            'um','uns','umas','uma','mas','mais','aqui','ali','então',
            'senhores',
            'eu','tu','nós','ele', 'eles','hoje','onde','porque','pois',
            'foi','ser','está','será','assim','com','como','sem','boa',
            'meu','meus','minha','teu','sua','seu','nossa','acho','deu'
            ]
wc = WordCloud(stopwords=STOPWORDS,
                background_color="white",
                max_font_size=256,
                random_state=42,
                width=400, height=400,
                mask=figura)

wc.generate(texto)
plt.figure( figsize=(80,40) ) #ajustar tamanho imagem
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()

