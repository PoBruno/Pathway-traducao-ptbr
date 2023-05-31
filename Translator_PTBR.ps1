
# Description: This script will translate a string from English to Portuguese (Brazilian)


# Function to translate a string from English to Portuguese (Brazilian)

# Requires: 
Install-Module -Name GoogleCloudTranslate

# Instale o módulo 'GoogleCloudTranslate' se ainda não estiver instalado
Install-Module -Name GoogleCloudTranslate

# Defina sua chave de API do Google Translate
$apiKey = "SUA_CHAVE_DE_API"

# Carregue o arquivo JSON
$jsonPath = "Caminho_para_o_arquivo_achievements.json"
$jsonContent = Get-Content -Raw -Path $jsonPath | ConvertFrom-Json

# Importe o módulo 'GoogleCloudTranslate' e crie um cliente
Import-Module GoogleCloudTranslate
$client = New-GcTranslateClient -ApiKey $apiKey

# Percorra os objetos e traduza o campo "text"
foreach ($row in $jsonContent.rows) {
    $translatedText = $client.TranslateText($row.text, "pt")
    $row.text = $translatedText.TranslatedText
}

# Salve o arquivo JSON traduzido
$jsonContent | ConvertTo-Json -Depth 100 | Set-Content -Path $jsonPath


import json
from googletrans import Translator

# Carregue o arquivo JSON
json_path = "./pt-BR/Achievements.json"

with open(json_path, "r", encoding="utf-8") as json_file:
    json_content = json.load(json_file)

# Crie uma instância do tradutor do Google
translator = Translator(service_urls=["translate.google.com"])

# Percorra os objetos e traduza o campo "text"
for row in json_content["rows"]:
    translated = translator.translate(row["text"], dest="pt")
    row["text"] = translated.text

# Salve o arquivo JSON traduzido
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(json_content, json_file, ensure_ascii=False, indent=4)









