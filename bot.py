from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá! sou o bot da Evoluto, tudo bem?.')

# Função para o comando /ajuda
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Aqui estão os comandos disponíveis:\n"
        "/start - Iniciar o bot\n"
        "/ajuda - Ver esta mensagem de ajuda\n"
        "/info - Saber mais sobre mim!"
	"/help - Ver esta mensagem de ajuda\n"
    )

# Função para o comando /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Eu sou um bot de exemplo criado para aprender como trabalhar com o Telegram Bot API!"
    )

# Função principal
def main():
    # Substitua "7940172574:AAHjYhEHuNQMiU1fHJyq2BEUBfHCv2trmaE" pelo token do seu bot
    application = Application.builder().token("7940172574:AAHjYhEHuNQMiU1fHJyq2BEUBfHCv2trmaE").build()

    # Adicionar os comandos ao bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("info", info))

    # Inicia o bot
    application.run_polling()

if __name__ == "__main__":
    main()
