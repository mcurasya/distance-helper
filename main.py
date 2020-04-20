import telebot
import config
from PIL import Image
import os
import shutil
bot = telebot.TeleBot(config.TOKEN)


i_s = {}

@bot.message_handler(content_types=["photo"])
def getpics(message):
    global i_s
    identity = message.from_user.id
    if identity not in i_s:
        print(f"new user: {message.from_user.username}!")
        i_s[identity] = 0
    print(f"getting photo {i_s[identity]} from user {message.from_user.username} with id {identity}")
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    if not os.path.exists(f"user_{identity}"):
        os.mkdir(f"user_{identity}")
    with open(f"user_{identity}/image_{identity}_{i_s[identity]}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
        i_s[identity]+=1

@bot.message_handler(commands=["stop"])
def handle_stop(message):
    print("sending pdf")
    global i_s
    identity = message.from_user.id
    length = i_s[identity]
    del i_s[identity]
    images = []
    if length == 0:
        bot.reply_to(message, "sorry, you didnt provide any files")
        return
    im0 = Image.open(f"user_{identity}/image_{identity}_0.jpg")
    for i in range(1, length):
        image = Image.open(f"user_{identity}/image_{identity}_{i}.jpg")
        im = image.convert("RGB")
        images.append(im)
    if not os.path.exists('results'):
        os.mkdir('results')
    im0.save(f"results/file_{identity}.pdf", save_all=True, append_images=images)
    doc = open(f"results/file_{identity}.pdf", "rb")
    bot.send_document(message.chat.id, doc)
    doc.close()
    shutil.rmtree(f"user_{identity}")
    os.remove(f"results/file_{identity}.pdf")


@bot.message_handler(commands=["start"])
def handle_start(message):
    print("new user")
    global i_s
    identity = message.from_user.id
    i_s[identity] = 0
    if os.path.exists(f"user_{identity}"):
        shutil.rmtree(f"user_{identity}")
    bot.send_message(message.chat.id, "hello, send me images then write /stop to get a pdf")



print("start polling")
while True:
    bot.polling(none_stop=True)