import pandas as pd
from googletrans import Translator

# Carregando o arquivo XLS
file_path = "./pt-BR/Events.xlsx"
df = pd.read_excel(file_path)

# Criando uma instância do tradutor
translator = Translator(service_urls=['translate.google.com'])

# Função para traduzir o texto
def translate_text(text):
    translation = translator.translate(text, src='en', dest='pt')
    return translation.text


# Traduzindo os valores da coluna "en-US" e inserindo na coluna "pt-BR"
df['pt-BR'] = df['en-US'].apply(translate_text)

# Salvando o arquivo XLS traduzido
output_file_path = "./pt-BR/Events_translated.xlsx"
df.to_excel(output_file_path, index=False)

