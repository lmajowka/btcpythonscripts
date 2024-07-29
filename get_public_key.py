#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from typing import Optional, List, Dict, Any


BASE_URL = "https://mempool.space/api"


def get_scriptpubkey(wallet: str) -> str:
    """
    Procura a chave pública de uma carteira.

    Args:
        wallet (str): O endereço da carteira Bitcoin.

    Returns:
        str: O scriptpubkey ou uma mensagem de erro.
    """
    
    if not wallet:
        return "Endereço de carteira inválido!"

    url: str = f"{BASE_URL}/address/{wallet}/txs/mempool"

    try:
        response: requests.Response = requests.get(url)
        response.raise_for_status()
        
        transactions: List[Dict[str, Any]] = response.json()
        
        if len(transactions) == 0:
            return "Nenhuma transação encontrada para a carteira especificada."

        scriptpubkey: Optional[str] = transactions[0]['vin'][0]['witness'][1]

        if scriptpubkey:
            return f"[+] CHAVE PÚBLICA: {scriptpubkey}\n"
        return "Nenhuma transação encontrada para a carteira especificada."
    except requests.RequestException as e:
        return f"Erro na requisição: {str(e)}"
    except ValueError:
        return "Erro ao processar a resposta JSON."


if __name__ == "__main__":
    print("Exemplo de Endereço: bc1qlqlch88awgah90y8890rtaqdf867las9kk9q2h")

    wallet: str = input("\nInforme o endereço da carteira: ")

    scriptpubkey: str = get_scriptpubkey(wallet)
    print(f"\n{scriptpubkey}")
