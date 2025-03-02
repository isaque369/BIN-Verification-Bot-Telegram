
# **Documentação do Bot de Verificação de BIN - Telegram**

## **Visão Geral**

O Bot de Verificação de BIN é um bot do Telegram desenvolvido em Python que permite aos usuários verificar informações detalhadas sobre os números de BIN (Bank Identification Number) de cartões bancários. O bot usa múltiplas APIs para verificar dados sobre os BINs, como o banco emissor, bandeira do cartão, tipo de cartão e país de emissão. Este bot é ideal para verificar BINs de cartões emitidos no Brasil.

## **Funcionalidades**

- **Verificação de BIN**: O bot permite que os usuários verifiquem o número do BIN para obter informações detalhadas sobre o cartão.
- **APIs Utilizadas**: O bot utiliza as APIs de verificação de BIN do **BinCheck** e **IIN Lookup** para obter dados sobre o BIN.
- **Respostas Detalhadas**: O bot fornece informações como:
  - Banco emissor do cartão
  - Bandeira do cartão
  - Tipo de cartão
  - País de emissão

## **Comandos**

### **/verificarbin [NÚMERO]**

- **Descrição**: Comando utilizado para verificar as informações de um BIN (Número de Identificação Bancária).
- **Argumento**: O comando requer que o usuário forneça o número do BIN (um número de 6 a 8 dígitos).
- **Exemplo de Uso**:
  - `/verificarbin 489406`

### **Formato de Resposta**

A resposta do bot será no seguinte formato:

```
🔍 Resultados para o BIN [NÚMERO]:

🏦 BIN: [NÚMERO]
🏢 Banco Emissor: [Nome do Banco]
💳 Bandeira: [Bandeira do Cartão]
🏷️ Tipo de Cartão: [Tipo do Cartão]
🌍 País de Emissão: [País]
Método: [Nome da API Utilizada]
```

Exemplo:

```
🔍 Resultados para o BIN 489406:

🏦 BIN: 489406
🏢 Banco Emissor: Banco do Brasil
💳 Bandeira: VISA
🏷️ Tipo de Cartão: Débito
🌍 País de Emissão: Brasil
Método: BinCheck
```

### **Mensagens de Erro**

1. **Erro de Formato do Comando**:
   - Mensagem: `Uso incorreto do comando. Utilize: /verificarbin [NÚMERO]`
   - Causa: O usuário não forneceu um número de BIN válido ou forneceu o comando de forma incorreta.
   
2. **Número BIN Inválido**:
   - Mensagem: `Número BIN inválido. Certifique-se de que possui entre 6 e 8 dígitos numéricos.`
   - Causa: O número fornecido pelo usuário não está no formato correto (não é numérico ou não tem entre 6 e 8 dígitos).

3. **Erro ao Acessar a API**:
   - Mensagem: `Erro ao tentar acessar a API. Tente novamente mais tarde.`
   - Causa: O bot não conseguiu acessar a API para realizar a verificação, possivelmente devido a problemas de rede ou problemas com as APIs externas.

## **Tecnologias Utilizadas**

- **Python**: A linguagem de programação utilizada para desenvolver o bot.
- **Python-telegram-bot**: Biblioteca para interagir com a API do Telegram e criar o bot.
- **Requests**: Biblioteca para realizar requisições HTTP às APIs externas.
- **RegEx**: Usado para validar o formato do BIN informado pelo usuário.
- **APIs**:
  - **BinCheck API**: Para verificação de BINs, fornecendo dados como banco emissor, bandeira, tipo e país.
  - **IIN Lookup API**: Outra fonte de dados para verificação de BINs.

## **Configuração e Execução**

### **Requisitos**

- **Python 3.x**: Certifique-se de ter o Python 3 instalado no seu sistema.
- **Bibliotecas Python**: Você precisará instalar as bibliotecas necessárias para rodar o bot:
  ```bash
  pip install python-telegram-bot requests
  ```

### **Passos para Executar**

1. **Obter as Chaves de API**:
   - Cadastre-se nas plataformas **BinCheck** e **IIN Lookup** para obter as chaves de API necessárias.
   - Substitua as chaves `YOUR_API_KEY` no código pelo token fornecido por essas APIs.

2. **Configurar o Token do Telegram**:
   - Substitua o valor da variável `TELEGRAM_TOKEN` no código pelo token gerado ao criar o bot no [BotFather](https://core.telegram.org/bots#botfather).

3. **Rodar o Código**:
   - Execute o script Python para iniciar o bot:
     ```bash
     python bot.py
     ```

4. **Interagir com o Bot**:
   - No Telegram, busque pelo nome do bot e envie o comando `/verificarbin [NÚMERO]` para começar a verificar os BINs.

### **Exemplo de Execução**

#### **Passo 1**: O usuário envia o comando `/verificarbin 489406`.

#### **Passo 2**: O bot responde com as informações detalhadas sobre o BIN.

```
🔍 Resultados para o BIN 489406:

🏦 BIN: 489406
🏢 Banco Emissor: Banco do Brasil
💳 Bandeira: VISA
🏷️ Tipo de Cartão: Débito
🌍 País de Emissão: Brasil
Método: BinCheck
```

#### **Passo 3**: Caso o número de BIN não seja válido, o bot irá responder com um erro.

```
Número BIN inválido. Certifique-se de que possui entre 6 e 8 dígitos numéricos.
```

## **Personalização**

- **Adicionar Mais APIs**: Se desejar, você pode adicionar mais APIs de verificação de BIN ao código, seguindo o padrão de integração utilizado para o **BinCheck** e **IIN Lookup**.
- **Melhorias nas Respostas**: Você pode personalizar as mensagens de resposta ou formatar os dados de maneira diferente para melhorar a experiência do usuário.

## **Licença**

Este projeto está licenciado sob a licença MIT.
