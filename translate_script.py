#                                                #
# Author: Bruno Gomes  -  31/05/2023             #
# www.github.com/pobruno                         #
# Bruno Gomes                                    #
#                                                #
# Script para traduzir os arquivos JSON do jogo  #
##################################################

import json
import regex as re
from googletrans import Translator

# Array com os caminhos dos arquivos JSON
json_paths = [
    "./pt-BR/Achievements.json",
    "./pt-BR/Events.json"
    #"./pt-BR/Items.json",
    #"./pt-BR/Perks.json",
    #"./pt-BR/Quotes.json"
    #"./pt-BR/Tutorial.json"
]

# Tamanho máximo de caracteres para cada lote de tradução
batch_size = 1000

# Função para filtrar e modelar os caracteres indesejados e remover comandos de formatação
def filter_text(text):
    # Remove comandos de formatação HTML e outros comandos específicos
    text = text.replace("\n", "a1b1c1").replace(
        "\"", "a2b2c2").replace("[char0]", "a01b01c00").replace("[char1]", "a01b01c01").replace("[char2]", "a01b01c02").replace("[char3]", "").replace("[char4]", "a01b01c04").replace("[char4]", "a01b01c04")
    return text

# Função para traduzir um lote de textos
def translate_batch(texts, dest_language):
    translator = Translator()

    # Traduz o lote de textos, ignorando textos que excedem o limite de caracteres
    translations = []
    for text in texts:
        try:
            translation = translator.translate(text, dest=dest_language)
            translations.append(translation.text)
        except AttributeError:
            translations.append(text)

    # Retorna os textos traduzidos
    return translations

# Percorre os arquivos JSON
for json_path in json_paths:
    # Carrega o arquivo JSON
    with open(json_path, "r", encoding="utf-8") as json_file:
        json_content = json.load(json_file)

    # Cria uma lista para armazenar os textos a serem traduzidos
    texts_to_translate = []

    # Percorre os objetos e adiciona os textos à lista
    for row in json_content["rows"]:
        text = row["text"]
        filtered_text = filter_text(text)
        texts_to_translate.append(filtered_text)

    # Divide a lista de textos em lotes menores
    batches = [texts_to_translate[i:i+batch_size]
               for i in range(0, len(texts_to_translate), batch_size)]

    # Percorre cada lote e realiza a tradução
    for batch in batches:
        translated_batch = translate_batch(batch, "pt")

        # Atualiza os textos traduzidos no JSON
        for i, translation in enumerate(translated_batch):
            json_content["rows"][i]["text"] = translation

    # Salva o arquivo JSON traduzido
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)

# Fim de tradução






##################################
# Modelos de traduçoes 

##################################
# Test V2 translate
# from translate import Translator
#import json
#
## Carregue o arquivo JSON
#json_path = "./pt-BR/Achievements.json"
#with open(json_path, "r", encoding="utf-8") as json_file:
#    json_content = json.load(json_file)
#
## Crie uma instância do tradutor
#translator = Translator(to_lang="pt")
#
## Percorra os objetos e traduza o campo "text"
#for row in json_content["rows"]:
#    translated = translator.translate(row["text"])
#    row["text"] = translated
#
## Salve o arquivo JSON traduzido
#with open(json_path, "w", encoding="utf-8") as json_file:
#    json.dump(json_content, json_file, ensure_ascii=False, indent=4)
##################################


##################################
# Test v1 Google Translate
#import json
#from googletrans import Translator
#
## Carregue o arquivo JSON
#json_path = "./pt-BR/Achievements.json"
#
#with open(json_path, "r", encoding="utf-8") as json_file:
#    json_content = json.load(json_file)
#
## Crie uma instância do tradutor do Google
#translator = Translator(service_urls=["translate.google.com"])
#
## Percorra os objetos e traduza o campo "text"
#for row in json_content["rows"]:
#    translated = translator.translate(row["text"], dest="pt")
#    row["text"] = translated.text
#
## Salve o arquivo JSON traduzido
#with open(json_path, "w", encoding="utf-8") as json_file:
#    json.dump(json_content, json_file, ensure_ascii=False, indent=4)
#
##################################

