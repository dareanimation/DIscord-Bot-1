import discord # インストールした discord.py
import time
import datetime
from time import sleep
import threading

client = discord.Client() # 接続に使用するオブジェクト
client_id = '477364767200247812'


# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print("ログインしました")
    #print(client.get_channel("552329640036007936"))



@client.event
async def on_message(message):
    #msg = message.author.mention
    #mesau = message.author
    if message.channel.id == '539821439767937036':
        await client.add_reaction(message,'👌')
        

    else:
        if message.channel.id != '528442984476311564':
            if "giegwiotheuioywsoi" in message.content:
                pass
            else:
                pass
                #print("なにかメッセージがあったゾ")
                #await client.delete_message(message)

    jj = datetime.datetime.now()
    jh = '{0:%H}'.format(jj)+":"+'{0:%M} '.format(jj)

    if jh == "13:30":
        print("一時半やで")

    if message.content.startswith('!clean'):
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1: # 1発言以下でdelete_messagesするとエラーになる
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, 'ログの全削除が完了しました')

    if message.channel.id == '553981332217397268':
        print("private channel")
        if message.attachments:
            print("Go image")
            await client.add_reaction(message, ':GG:556998169800605720')

    if message.channel.id == '546270171375861761':
        print("private channel")
        if message.attachments:
            print("Go image")
            await client.add_reaction(message, ':nice_kill:557020321040039936')

    

    
        


# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）

client.run("NDc3MzY0NzY3MjAwMjQ3ODEy.D2DDlA.3UNfMlOFGiRDRmh_JEUYATiddcs")