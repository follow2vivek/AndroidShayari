from rivescript import RiveScript

def get_reply(cmd):
    bot = RiveScript()
    bot.load_directory("./brain")
    bot.sort_replies()
    while True:
        reply = bot.reply("Alisha",cmd)
        return reply