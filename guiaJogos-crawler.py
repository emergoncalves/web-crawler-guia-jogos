# coding: utf-8

import requests
import bs4
import json

root_url = 'https://mantosdofutebol.com.br'
index_url = root_url + '/guia-de-jogos-tv-hoje-ao-vivo'

def get_guia_jogos():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    jogos = []
    file = open('guia.txt', 'w')

    for jogoSoap in soup.findAll(class_="inner-post-entry"):
            s = jogoSoap
            for jogo in s.findAll(['h3', 'p']):
                jogos.append( jogo.getText() )
                file.write( jogo.getText() + '\n' )
    file.close()
    #delete os primeiros elementos
    del(jogos[0:4])
    
    #deleta os três últimos
    jogos.pop()
    jogos.pop()
    jogos.pop()
    
    #Envia para um arquivo json
    out_file = open("guia-jogos.json", "w") 
    json.dump(jogos, out_file, indent = 6) 
    out_file.close()
    return jogos
    
print( get_guia_jogos() )
