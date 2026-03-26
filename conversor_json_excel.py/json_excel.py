import json
import pandas as pd
import os

def carregar_json():
    caminho = os.path.join(os.path.dirname(__file__), "dados.json")

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo 'dados.json' não encontrado.")
        return None

def escolher_campos(dados):
    print("\nCampos disponíveis:")
    for chave in dados[0].keys():
        print(f"- {chave}")

    campos = input("\nDigite os campos desejados (separados por vírgula): ")
    return [c.strip() for c in campos.split(",")]

def exportar_excel(dados, campos):
    df = pd.DataFrame(dados)

    try:
        df = df[campos]
    except KeyError:
        print("Erro: algum campo digitado não existe.")
        return

    nome_arquivo = "resultado.xlsx"
    df.to_excel(nome_arquivo, index=False)

    print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")

def main():
    dados = carregar_json()

    if not dados:
        return

    if not isinstance(dados, list):
        print("O JSON precisa ser uma lista de objetos.")
        return

    campos = escolher_campos(dados)
    exportar_excel(dados, campos)

if __name__ == "__main__":
    main()