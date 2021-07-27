import requests
import bs4
import json

root_url = 'https://mantosdofutebol.com.br'
index_url = root_url + '/guia-de-jogos-tv-hoje-ao-vivo'

def get_guia_jogos():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    jogos = []
    canais = []

    # Pega informação do jogo
    for jogoSoap in soup.findAll(class_="inner-post-entry"):
            s = jogoSoap
            for jogo in s.findAll(['h3']):
                jogos.append( jogo.getText() )

    # Pega informação sobre o canal
    for canalSoap in soup.findAll(class_="inner-post-entry"):
            c = canalSoap
            for canal in c.findAll(['span']):
                if canal.getText().find('►') != 0:
                 canais.append( canal.getText() )

    return [list(x) for x in zip(jogos, canais)]
    
print( get_guia_jogos() )