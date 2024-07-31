#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
from typing import Optional, List, Dict, Any


BASE_URL = "https://mempool.space/api"


def get_scriptpubkey(wallet: str) -> str:
    while True:
        try:
            url = f'https://blockchain.info/q/pubkeyaddr/{wallet}'
            response = requests.get(url)
            if response.status_code == 200:
                chave = response.text
                return chave 
                   
            print('Não encontrada, tentando novamente em 5 segundos...')
            time.sleep(5)

        except:
            time.sleep(5)

if __name__ == "__main__":
    print("Exemplo de Endereço: bc1qlqlch88awgah90y8890rtaqdf867las9kk9q2h")

    wallet: str = input("\nInforme o endereço da carteira: ")

    scriptpubkey: str = get_scriptpubkey(wallet)
    print(f"\n{scriptpubkey}")
