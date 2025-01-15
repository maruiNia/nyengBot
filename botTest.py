import discord
from discord.ext import commands
import random

class Nyeng :
    def __init__(self, token) :
        self.intents = discord.Intents.default()
        self.intents.message_content = True  # 메시지 내용에 접근하려면 이 설정이 필요합니다.

        self.bot = commands.Bot(command_prefix="!", intents=self.intents)

        self.nyengList = ["느엥", "흐엥", "후아앙", "희엥", "우앙", "엘리자빠스와요!", "홋!홋!홋", "느이엥", "느에엥엥"]

        @self.bot.event
        async def on_ready():
            print("아카네리제에요오으엥")

        @self.bot.command()
        async def hello(ctx):
            await ctx.send("느에엥")

        @self.bot.event
        async def on_message(message):
            if "안녕" in message.content:
                await message.channel.send('뿌에에으에엥')
            
            if message.author != self.bot.user:
                ranListNum = random.randint(0, len(self.nyengList)-1)
                await message.channel.send(self.nyengList[ranListNum])
            
            await self.bot.process_commands(message)

        self.bot.run(token)
        #허재원 테스트
