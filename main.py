import random
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('봇이 시작되었습니다.')

@client.event
async def on_message(message):
    if message.content.startswith('?묵찌빠'):
        options = ['**가위** 입니다.', '**바위** 입니다.', '**보** 입니다.']
        random_option = random.choice(options)
        await message.channel.send(embed=discord.Embed(title='묵찌빠', description=random_option))

    if message.content.startswith('?랜덤다이스'):
        players = message.mentions
        if len(players) != 2:
            await message.channel.send('**두 명의 플레이어를 멘션해야 합니다.**')
        else:
            player1 = players[0]
            player2 = players[1]
            random_number1 = random.randint(1, 50)
            random_number2 = random.randint(1, 50)
            if random_number1 > random_number2:
                await message.channel.send(embed=discord.Embed(title='랜덤 다이스', description=f'{player1.mention} : {random_number1}, {player2.mention} : {random_number2}. 승자는 {player1.mention} 님 입니다.'))
            elif random_number1 < random_number2:
                await message.channel.send(embed=discord.Embed(title='랜덤 다이스', description=f'{player1.mention} : {random_number1}, {player2.mention} : {random_number2}. 승자는 {player2.mention} 님 입니다.'))
            else:
                await message.channel.send(embed=discord.Embed(title='랜덤 다이스', description=f'{player1.mention} : {random_number1}, {player2.mention} : {random_number2}. 무승부입니다.'))

client.run('MTEwNjc5Mzc4MTU4OTcwODg2NQ.GwlUii.KxUrXiILIggRsNermFh2wP4l1NBocy9OBi8bNk')
