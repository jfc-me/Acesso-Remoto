# coding: utf-8
import socket
from get_set.instrucao import Instrucoes as retornos
from arquivos.transferir_arquivo import Transferir



class Server():

    def connecting(self, cmd_line):
        power_plug = socket.socket()
        power_plug.bind(("localhost", 8081))
        power_plug.listen(1)
        conn, addr = power_plug.accept()

        retornos.cmd = addr
        if 'cp' in cmd_line:
            Transferir().transferencias(conn, cmd_line)
        elif 'tela' in cmd_line:
            Transferir().transferirImagem(conn, cmd_line)
        else:
            conn.send(cmd_line.encode())
            retornos.resultado = conn.recv(1024).decode('utf-8')
            conn.send('sair'.encode())

