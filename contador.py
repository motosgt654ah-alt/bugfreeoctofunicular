from datetime import datetime, timedelta

def atualizar_sequencia():
    hoje = datetime.now().date()
    arquivo_dados = "dados_sequencia.txt"
    
    try:
        # Tenta ler o arquivo de dados anterior
        with open(arquivo_dados, "r") as f:
            linha = f.read().strip()
            data_str, dias_str = linha.split(",")
            ultima_data = datetime.strptime(data_str, "%Y-%m-%d").date()
            dias = int(dias_str)
    except FileNotFoundError:
        # Primeira vez criando o arquivo: inicia com os seus 5 dias
        dias = 5
        ultima_data = hoje - timedelta(days=1)

    if hoje == ultima_data:
        print(f"Presença de hoje já registrada! Você continua no {dias}º dia.")
    elif hoje == ultima_data + timedelta(days=1):
        dias += 1
        print(f"Sequência mantida! Agora você está no {dias}º dia seguido!")
        with open(arquivo_dados, "w") as f:
            f.write(f"{hoje},{dias}")
    else:
        # Se passou mais de um dia sem atualizar, reinicia
        dias = 1
        print("Nova sequência iniciada no 1º dia!")
        with open(arquivo_dados, "w") as f:
            f.write(f"{hoje},{dias}")

if __name__ == "__main__":
    atualizar_sequencia()
  
