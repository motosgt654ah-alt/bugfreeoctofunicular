import calendar
from datetime import datetime

FERIADOS = ["01/01", "21/04", "01/05", "07/09", "12/10", "02/11", "15/11", "25/12"]

def obter_status_dia(ano, mes, dia, fez_commit=False):
    agora = datetime.now()
    data_str = f"{dia:02d}/{mes:02d}"
    
    if data_str in FERIADOS:
        return "Feriado (Dourado)"
        
    if fez_commit:
        if ano == agora.year and mes == agora.month:
            return "Ativo (Verde Neon)"
        else:
            return "Concluído (Verde Claro)"
            
    return "Inativo (Vermelho)"

def processar_historico():
    agora = datetime.now()
    ano_atual = agora.year
    mes_atual = agora.month
    
    print(f"--- Processando Streak até 2040 (Data atual: {agora.strftime('%d/%m/%Y')}) ---")
    
    for ano in range(2026, 2041):
        if ano < ano_atual:
            inicio_mes, fim_mes = 1, 12
        elif ano == ano_atual:
            inicio_mes, fim_mes = 1, mes_atual
        else:
            inicio_mes, fim_mes = 1, 12
            
        for mes in range(inicio_mes, fim_mes + 1):
            _, total_dias = calendar.monthrange(ano, mes)
            nome_mes = calendar.month_name[mes].capitalize()
            print(f"Mês: {nome_mes}/{ano} - Total de dias: {total_dias}")

if __name__ == '__main__':
    processar_historico()
