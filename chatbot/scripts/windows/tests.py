import aiml
import os

# from click._compat import raw_input
#
# kernel = aiml.Kernel()
#
# # if os.path.isfile("bot_brain.brn"):
# #     kernel.bootstrap(brainFile="bot_brain.brn")
# # else:
# # kernel.bootstrap(brainFile="bot_brain.brn", learnFiles="startup.xml", commands="load aiml b")
# kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
# # kernel.saveBrain("bot_brain.brn")
# # kernel.respond("load aiml b")
# # kernel now ready for use
# while True:
#     print(kernel.respond(raw_input("Enter your message >> ")))
# from programy.clients.embed.datafile import EmbeddedDataFileBot

from programy.clients.embed.configfile import EmbeddedConfigFileBot

# files = {'aiml': ['bots/super/aiml']}
config_file = "../../config/windows/config.yaml"
my_bot = EmbeddedConfigFileBot(config_file)
# my_bot = EmbeddedDataFileBot(files, defaults=True)
client_context = my_bot.create_client_context("testuser")
response = my_bot.process_question(client_context, "帮助")
print("Response '%s'" % response)
# print("Response = %s" % my_bot.ask_question("订单号"))
