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
        self.scroll = ScrollView()
        self.layout_principal = BoxLayout(orientation='vertical', size_hint_y=None)
        self.layout_principal.bind(minimum_height=self.layout_principal.setter('height'))
        
        self.scroll.add_widget(self.layout_principal)
        self.carregar_historico_ate_2040()
        Clock.schedule_once(self.focar_mes_atual, 0.1)
        
        return self.scroll

    def focar_mes_atual(self, dt):
        self.scroll.scroll_y = 0

    def obter_cor_do_dia(self, ano, mes, dia, fez_commit=False):
        agora = datetime.now()
        data_str = f"{dia:02d}/{mes:02d}"
        
        if data_str in FERIADOS:
            return "#FFD700"
            
        if fez_commit:
            if ano == agora.year and mes == agora.month:
                return "#00FF66"
            else:
                return "#7CE38B"
                
        return "#FF3344"

    def carregar_historico_ate_2040(self):
        agora = datetime.now()
        ano_atual = agora.year
        mes_atual = agora.month
        
        for ano in range(2026, 2041):
            if ano < ano_atual:
                inicio_mes, fim_mes = 1, 12
            elif ano == ano_atual:
                inicio_mes, fim_mes = 1, mes_atual
            else:
                inicio_mes, fim_mes = 1, 12
            
            for mes in range(inicio_mes, fim_mes + 1):
                _, total_dias = calendar.monthrange(ano, mes)
                
                bloco_mes = BoxLayout(orientation='vertical', size_hint_y=None, height=70)
                
                nome_mes = calendar.month_name[mes].capitalize()
                lbl_mes = Label(text=f"{nome_mes} / {ano}", size_hint_y_max=25, bold=True)
                bloco_mes.add_widget(lbl_mes)
                
                dias_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                
                for dia in range(1, total_dias + 1):
                    fez_commit = False
                    cor = self.obter_cor_do_dia(ano, mes, dia, fez_commit)
                    
                    dia_lbl = Label(text="■", size_hint_x=None, width=25, color=cor)
                    dias_layout.add_widget(dia_lbl)
                    
                bloco_mes.add_widget(dias_layout)
                self.layout_principal.add_widget(bloco_mes)

if __name__ == '__main__':
    ContadorApp().run()
