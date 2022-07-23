# Telegram UserBot para exibir vídeos e tocar músicas em chamadas de grupos no telegram.

Telegram UserBot para exibir vídeos e tocar músicas em chamadas de grupos no telegram utilizando pytgcalls.

#Este bot é capaz de reproduzir vídeos do Youtube e Lives.

### Requisitos de conta.
- Uma conta do Telegram para usar como bot de música, você não pode usar contas de bot regulares, pois elas não podem participar de bate-papos de voz. Deve ser uma conta de usuário.
- API_ID e API_HASH para essa conta.
- A conta deve ser um administrador do bate-papo, com permissões Gerenciar bate-papos de voz e Excluir mensagens .


## Heroku

#### Gere uma String de Sessão [IMPORTANTE]

Baixe este arquivo [gerar_session_string.py](https://github.com/ErikiCav/ChamadaTelegramShow/blob/main/gerar_session_string.py)

Suba ao heroku clicando no botão abaixo.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Comandos.
Comando | Descrição
:--- | :---
/adicionar [LINK] | Baixa e adiciona um vídeo do Youtube à lista de reprodução.
/adicionar_live [LINK] | Adiciona um link live stream.
/adduser (`Menção`) | Adiciona o usuário marcado à lista de autorizados.
/rmuser (`Menção`) | Remove o usuário marcado da lista de autorizados.
/modo | Dá uma alternativa para trocar entre o modo de som e modo de vídeo.
/listas | Exibe as mídias na fila de reprodução.
/play | Começa a tocar as mídias na fila de reprodução.
/stop | Para a transmissão do bot.

## Note

1. If you want any help you can ask [here](https://t.me/tgvcsupport)

## Créditos.

1. [@MarshalX](https://github.com/MarshalX), para [TGCalls](https://github.com/MarshalX/tgcalls)
2. [pytgcalls](https://github.com/MarshalX), para [pytgcalls](https://pytgcalls.github.io/)
