import calendar
from datetime import datetime

# Lista de feriados nacionais fixos (DD/MM)
FERIADOS = ["01/01", "21/04", "01/05", "07/09", "12/10", "02/11", "15/11", "25/12"]

def obter_cor_do_dia(ano, mes, dia, fez_commit):
    """
    Define a cor do quadradinho de acordo com as regras:
    - Feriado: Amarelo/Dourado (#FFD700)
    - Mês Atual com commit: Verde Neon (#00FF66)
    - Mês Passado com commit: Verde Claro (#7CE38B)
    - Sem commit (Inatividade): Vermelho (#FF3344)
    """
    data_atual = datetime.now()
    data_dia = datetime(ano, mes, dia)
    data_str = data_dia.strftime("%d/%m")
    
    # 1. Verifica se é feriado
    if data_str in FERIADOS:
        return "#FFD700"
        
    # 2. Verifica se houve commits/trabalho
    if fez_commit:
        # Se for o mês e ano atuais, usa Verde Neon; senão, Verde Claro
        if ano == data_atual.year and mes == data_atual.month:
            return "#00FF66"
        else:
            return "#7CE38B"
            
    # 3. Dias sem trabalho (inatividade)
    return "#FF3344"

def gerar_grade_anual(ano_desejado=None):
    """
    Gera a matriz de dias respeitando a quantidade real de dias de cada mês
    e a virada automática do ano atual se nenhum ano for informado.
    """
    if ano_desejado is None:
        ano_desejado = datetime.now().year
        
    calendario_ano = {}
    
    for mes in range(1, 13):
        # calendar.monthrange retorna (dia_da_semana_inicio, total_de_dias_no_mes)
        _, total_dias = calendar.monthrange(ano_desejado, mes)
        
        dias_mes = []
        for dia in range(1, total_dias + 1):
            # Aqui você conecta com a checagem real dos seus commits do GitHub
            fez_commit = False  # Exemplo padrão, substitua pela sua verificação de commits
            
            cor = obter_cor_do_dia(ano_desejado, mes, dia, fez_commit)
            dias_mes.append({"dia": dia, "cor": cor})
            
        calendario_ano[mes] = dias_mes
        
    return calendario_ano
    
