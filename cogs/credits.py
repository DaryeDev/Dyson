import discord
from discord.ext import commands
import yaml
import asyncio
import os

class credits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        base_dir = "config"
        creditsName = "credits.yml"
        creditsFile = str(os.path.join(base_dir, creditsName))
        try:
            with open(creditsFile, "r") as f:
                self.users = json.load(f)
        except:
            os.mkdir(creditsFile)
            with open(creditsFile, "r") as f:
                self.users = json.load(f)

        self.bot.loop.create_task(self.save_users())

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(self.creditsFile, "w") as f:
                yaml.dump(self.users, f)
            await asyncio.sleep(5)

    def lvl_up(self, author_id):
        currentXP = self.users[author_id]["xp"]
        currentLVL = self.users[author_id]["lvl"]

        if currentXP >= round((4*(currentLVL**3))/5):
            self.users[author_id]['lvl'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            author_id = str(message.author.id)
            if not author_id in self.users:
                self.users[author_id] = {}
                self.users[author_id]['lvl'] = 1
                self.users[author_id]['xp'] = 0

            self.users[author_id]['xp'] += 1

            if self.lvl_up(author_id):
                await message.channel.send(f"¡{message.author.mention} acaba de subir al nivel {self.users[author_id]['lvl']}!")

    @commands.command()
    async def lvl(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send(f"{member} no ha hablado aún... ¡Anímale a que mande algún mensaje!")
        else:
            embed = discord.Embed(color=member.color)
            embed.set_author(name=f"Nivel de {member}:", icon_url=member.avatar_url)
            embed.add_field(name="Lvl", value = self.users[member_id]["lvl"])
            embed.add_field(name="XP", value=self.users[member_id]["xp"])
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(credits(bot))