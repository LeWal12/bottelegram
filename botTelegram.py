from telegram.ext import Updater, CommandHandler

def welcome(update, context):
	message = 'Ola, ' + update.message.from_user.first_name + '!'
	print(message)
	context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def main():
	token = '793256335:AAGDOlaPbGeCOastdaWtuufhIlvrHZjg32s' #test bot
	updater = Updater(token=token, use_context=True)

	updater.dispatcher.add_handler(CommandHandler('start', welcome))

	updater.start_polling()
	print('testando bot' + str(updater))
	updater.idle()

if __name__ == '__main__':
	main()

