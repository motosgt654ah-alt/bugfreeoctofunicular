import calendar
from datetime import datetime
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

FERIADOS = ["01/01", "21/04", "01/05", "07/09", "12/10", "02/11", "15/11", "25/12"]

class ContadorApp(App):
    def build(self):
        # Container de rolagem
        self.scroll = ScrollView()
        self.layout_principal = BoxLayout(orientation='vertical', size_hint_y=None)
        self.layout_principal.bind(minimum_height=self.layout_principal.setter('height'))
        
        self.scroll.add_widget(self.layout_principal)
        
        # Gera os meses até o mês atual
        self.carregar_historico_ate_mes_atual()
        
        # Rola automaticamente para o mês atual assim que a tela abre
        Clock.schedule_once(self.focar_mes_atual, 0.1)
        
        return self.scroll

    def focar_mes_atual(self, dt):
        # Força o ScrollView a ir direto para o final da lista (mês corrente)
        self.scroll.scroll_y = 0

    def obter_cor_do_dia(self, ano, mes, dia, fez_commit):
        agora = datetime.now()
        data_str = f"{dia:02d}/{mes:02d}"
        
        if data_str in FERIADOS:
            return "#FFD700"  # Dourado para feriados
            
        if fez_commit:
            if ano == agora.year and mes == agora.month:
                return "#00FF66"  # Verde Neon para o mês atual
            else:
                return "#7CE38B"  # Verde Claro para meses anteriores
                
        return "#FF3344"  # Vermelho para inatividade

    def carregar_historico_ate_mes_atual(self):
        agora = datetime.now()
        ano_atual = agora.year
        mes_atual = agora.month  # Outubro
        
        # Renderiza a lista de meses até o mês atual
        for mes in range(1, mes_atual + 1):
            _, total_dias = calendar.monthrange(ano_atual, mes)
            
            # Cria um bloco para o mês
            mes_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=60)
            
            # Nome do mês para referência visual
            nome_mes = calendar.month_name[mes]
            lbl_mes = Label(text=f"{nome_mes} {ano_atual}", size_hint_y_max=20)
            mes_layout.add_widget(lbl_mes)
            
            dias_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            dias_layout.bind(minimum_width=dias_layout.setter('width'))
            
            for dia in range(1, total_dias + 1):
                fez_commit = False  # Substitua pela sua checagem real de commits
                cor = self.obter_cor_do_dia(ano_atual, mes, dia, fez_commit)
                
                # Cria um rótulo simples simulando o quadradinho do dia
                dia_lbl = Label(text=str(dia), size_hint_x=None, width=30)
                dias_layout.add_widget(dia_lbl)
                
            mes_layout.add_widget(dias_layout)
            self.layout_principal.add_widget(mes_layout)

if __name__ == '__main__':
    ContadorApp().run()
    
