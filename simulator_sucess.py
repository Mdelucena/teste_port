import pandas as pd

# CSV para XLSX
def converter_csv_para_xlsx(caminho_csv, caminho_xlsx):
    # Carregar o arquivo CSV 
    df = pd.read_csv(caminho_csv)
    
    # Salvar o  XLSX
    df.to_excel(caminho_xlsx, index=False, engine='openpyxl')

    print(f"Arquivo convertido de {caminho_csv} para {caminho_xlsx} com sucesso!")
