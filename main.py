# coding: utf-8

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
kivy.require("1.9.2")
Window.clearcolor = get_color_from_hex("#ff6c0e")
import sys
from get_set.instrucao import Instrucoes as cmd_lines
from control.mobile import Server


#sudo apt-get install xclip xsel

class Pesquisar(FloatLayout):

    def cmd_line(self):
        if self.ids.consultar.text != '':
            cmd = self.ids.consultar.text
            Server().connecting(cmd)
            self.ids.retornos.text = cmd_lines.resultado
            acesso = str(cmd_lines.cmd)
            self.ids.status_campo_vazio.text = "conectado " + acesso
        else:
            self.ids.status_campo_vazio.text = "Campo Vazio!"

    def voltar(self):

        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(ControleInicial())


class ControleInicial(BoxLayout):

    def pesquisar(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Pesquisar())

    def sair(self):
        sys.exit(0)




class TelaInicial(FloatLayout):
    def endereco(self):
        conf = self.ids.entrada.text


        if conf != '1':
            self.ids.status.text = "erro"

        else:

            janela.root_window.remove_widget(janela.root)
            janela.root_window.add_widget(ControleInicial())


class ControleApp(App):
    pass

janela = ControleApp()


if (janela.root):
    janela.root_window.remove_widget(janela.root)
    janela.root = None
    janela = None



janela.run()
