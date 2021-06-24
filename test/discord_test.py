# -*- coding: utf-8 -*-

import discord
from discord import message
from discord import channel
import sys

from discord import guild

with open('token.txt', 'r') as f:
    data = f.readline()
TOKEN = data

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

    channel = discord.utils.get(guild.text_channels, name='debug')
    await channel.send('ログインしたよ！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    
    if message.content == '/hello':
        await message.channel.send('ハロー！')

    # quitでbotの停止（id指定ではなくロールで判断したい）
    if message.content == '/quit':
        if 'admin' in [users_lole.name for users_lole in message.author.roles]:
            await message.channel.send('バイバイ！また遊んでね')
            await client.logout()
            await sys.exit()
        else:
            await message.channel.send('君は僕を止めることができない。。。')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)