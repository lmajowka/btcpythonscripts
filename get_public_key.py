import requests

def get_scriptpubkey(carteira):
    url = f"https://mempool.space/api/address/{carteira}/txs/mempool"
    response = requests.get(url)
    
    if response.status_code == 200:
        transactions = response.json()
        for transaction in transactions:
            for vout in transaction['vout']:
                if vout['scriptpubkey_address'] == carteira:
                    scriptpubkey = vout['scriptpubkey']
                    # Remove os 4 primeiros caracteres
                    return scriptpubkey[4:]
        return "Nenhuma transacao encontrada para a carteira especificada."
    else:
        return f"Erro na requisicao: {response.status_code}"

# Exemplo de uso
carteira = "bc1qlvl0qnk8x2xgtcdsgdzu7a66k7h993cfzg4xfu"
scriptpubkey = get_scriptpubkey(carteira)
print(f"ScriptPubKey: {scriptpubkey[4:]}")
