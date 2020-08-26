# -*- coding: utf-8 -*-

# Importar bibliotecas
import re
import mysql.connector
from mysql.connector import Error

'''Buscar os tweets armazenados no banco de dados, e armazenar somente os campos com texto preenchido no tweet
 e o nome do usuário, dentro arquivo de texto'''


def pegarDadosTweet(conexao):
    cursor = conexao.cursor()
    try:
        query = "select text, name from " + tabela
        cursor.execute(query)
        tweets = cursor.fetchall()
        print("Total linhas resultado da consulta: ", cursor.rowcount)

        with open('base.txt', 'a') as arquivo:
            for texto, usuario in tweets:
                texto = texto.strip()
                texto = re.sub("\s+", ' ', texto)
                if len(texto) > 0:
                    arquivo.write(texto + '$' + usuario)
                    arquivo.write("\n")

    except Error as e:
        print("Erro ao acessar dados da tabela 'tweets' no banco de dados", e)
    finally:
        if conexao.is_connected():
            conexao.close()
            cursor.close()
            arquivo.close()
            print("conexão com MySQL foi finalizada")


if __name__ == "__main__":
    baseDeDados = "TwitterX"
    tabela = 'tweets'

    conexao = mysql.connector.connect(host='localhost', user='root', passwd='', database=baseDeDados)
    pegarDadosTweet(conexao)
