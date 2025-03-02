import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import re

TELEGRAM_TOKEN = 'TELEGRAM_TOKEN'

def verificar_bin_bincheck(numero: str):
    url = f"https://bincheck.io/api/v1/lookup/{numero}"
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'  # Substitua por sua chave da API do BinCheck
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            dados = response.json()
            if 'error' not in dados:
                banco = dados.get('bank', {}).get('name', 'Desconhecido')
                bandeira = dados.get('scheme', 'Desconhecido')
                tipo = dados.get('type', 'Desconhecido')
                pais = dados.get('country', {}).get('name', 'Brasil')
                resultado = f"""
                🏦 BIN: {numero}
                🏢 Banco Emissor: {banco}
                💳 Bandeira: {bandeira}
                🏷️ Tipo de Cartão: {tipo}
                🌍 País de Emissão: {pais}
                """
                return resultado, "BinCheck"
            else:
                return None, "BinCheck"
        else:
            return None, "BinCheck"
    except Exception as e:
        return None, "BinCheck"

def verificar_bin_iin_lookup(numero: str):
    url = f"https://www.ii-n.com/api/v1/lookup/{numero}"
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'  # Substitua por sua chave da API do IIN Lookup
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            dados = response.json()
            banco = dados.get('bank', {}).get('name', 'Desconhecido')
            bandeira = dados.get('scheme', 'Desconhecido')
            tipo = dados.get('type', 'Desconhecido')
            pais = dados.get('country', {}).get('name', 'Brasil')
            resultado = f"""
            🏦 BIN: {numero}
            🏢 Banco Emissor: {banco}
            💳 Bandeira: {bandeira}
            🏷️ Tipo de Cartão: {tipo}
            🌍 País de Emissão: {pais}
            """
            return resultado, "IIN Lookup"
        else:
            return None, "IIN Lookup"
    except Exception as e:
        return None, "IIN Lookup"

def validar_bin(numero: str) -> bool:
    return bool(re.match(r'^\d{6,8}$', numero))

async def verificarbin(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        await update.message.reply_text('Uso incorreto do comando. Utilize: /verificarbin [NÚMERO]')
        return

    numero_bin = context.args[0]
    if not validar_bin(numero_bin):
        await update.message.reply_text('Número BIN inválido. Certifique-se de que possui entre 6 e 8 dígitos numéricos.')
        return

    resultado_bincheck, metodo_bincheck = verificar_bin_bincheck(numero_bin)
    resultado_iin_lookup, metodo_iin_lookup = verificar_bin_iin_lookup(numero_bin)

    resposta = f"🔍 Resultados para o BIN {numero_bin}:\n\n"
    if resultado_bincheck:
        resposta += f"{resultado_bincheck}\nMétodo: {metodo_bincheck}\n\n"
    if resultado_iin_lookup:
        resposta += f"{resultado_iin_lookup}\nMétodo: {metodo_iin_lookup}\n\n"

    await update.message.reply_text(resposta)

def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("verificarbin", verificarbin))
    application.run_polling()

if __name__ == '__main__':
    main()