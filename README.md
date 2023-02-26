# EnderecoMAC-Regex-Classificacao

Algoritmo responsável por:

* Encontrar o padrão do Endeço MAC utilizando Expressão Regular(REGEX)

* Classificar esse endereço por fabricante.

Trabalho da Disciplina de Compiladores 
 
Créditos Arquivo (mac-vendors-export.csv): https://maclookup.app/downloads/csv-database

Tutorial VENV: https://flask.palletsprojects.com/en/1.1.x/installation/

Rodar o Requirements: pip install -r requirements.txt

# Signifucado da expressão `(?:(?:[A-F0-9]{2}[:|-]){5})[A-F0-9]{2}`

    * (?: agrupa todas as expressões em um grupo sem realizar a captura. 
    * [A-F0-9]{2}[:|-]{5} captura cinco vezes sucessivamente, todos caracteres na faixa hexadecimal(0 a 9 e A a F) duas vezes,
    concatenado com o símbolo `:` ou `-`.
    * [A-F0-9]{2} captura todos caracteres na faixa hexadecimal(0 a 9 e A a F) duas vezes.
