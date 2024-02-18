import os
import datetime
import webbrowser
from interface import data_user

data_convertida = int(data_user)



def verificar_adicao_arquivo(pasta):
    arquivos = []
    agora = datetime.datetime.now()
    limite_tempo = agora - datetime.timedelta(hours=data_convertida)

    for pasta_atual, subpastas, arquivos_atual in os.walk(pasta):
        for arquivo in arquivos_atual:
            caminho_completo = os.path.join(pasta_atual, arquivo)
            ultima_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(caminho_completo))

            if ultima_modificacao > limite_tempo:
                arquivos.append((ultima_modificacao,arquivo, os.path.basename(pasta_atual),))

    return arquivos

def criar_relatorio(arquivos_adicionados, relatorio_path):
        if arquivos_adicionados and relatorio_path is not None:
           with open(relatorio_path, 'w') as arquivo_relatorio:
            arquivo_relatorio.write(f"ARQUIVOS ADICIONADS NAS ÚLTIMAS {data_user} HORAS\n\n")
            for ultima_modificacao, arquivo, pasta_arquivo in arquivos_adicionados:
                    data_hora_formatada = ultima_modificacao.strftime("%d-%m-%Y / %H:%M:%S")
                    arquivo_relatorio.write(f"\nDATA/HORA {data_hora_formatada}\nNOME DA PASTA = {pasta_arquivo}\nNOME DO ARQUIVO = {arquivo} \n----------------------------------------------\n")
        else: 
            with open(relatorio_path, 'w') as arquivo_relatorio:
             arquivo_relatorio.write(f"NENHUM ARQUIVO ADICONADO NAS ÚLTIMAS {data_user} HORAS!\n\n")           

def main():
    pastas = [r'C:\Users\marco\OneDrive\Documentos\Nova pasta']  # Adicione as suas pastas aqui
    relatorio_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Relatório de Notas.txt')
    

    arquivos_adicionados = []

    for pasta in pastas:
        arquivos_adicionados.extend(verificar_adicao_arquivo(pasta))

    if arquivos_adicionados:
        criar_relatorio(arquivos_adicionados, relatorio_path)
        print(f"Relatório criado em {relatorio_path}")

        # Abrir o relatório no navegador padrão
        webbrowser.open('file://' + os.path.realpath(relatorio_path))
    else:
        criar_relatorio(arquivos_adicionados, relatorio_path)
        print(f"Relatório criado em {relatorio_path}")

        # Abrir o relatório no navegador padrão
        webbrowser.open('file://' + os.path.realpath(relatorio_path))

if __name__ == "__main__":
    main()