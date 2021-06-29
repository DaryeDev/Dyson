from discord.ext import commands


class respuestas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # message.content = message.content.lower().replace('', '')

        if message.author.id != 741962880097845340:
            if len(
                    message.content) == 1:  # Si el mensaje es de una letra, te responde con un gif de la letra en cuestion: a o f, por el momento
                if message.content.lower().endswith("a"):
                    print("a")
                    await message.channel.send("<a:A_:710519875730407537>")
                elif message.content.lower().endswith("f"):
                    print("f")
                    await message.channel.send("<a:fbutton:742060918761848963>")

                # Si el mensaje empieza por f y esta seguido por un espacio, para ser verdadero en el caso de "F por algo" o "F en el chat", manda un emoticono animado de una f
            if message.content.lower().find("f por") != -1:
                await message.channel.send("<a:fbutton:742060918761848963>")

            if message.content.lower().find("f en") != -1:
                await message.channel.send("<a:fbutton:742060918761848963>")

            if message.content.lower().find("uwu") != -1:
                await message.channel.send(
                    "<a:ugu:742464560262283355><a:ugu:742464560262283355><a:ugu:742464560262283355>")
                await message.channel.send(
                    "<a:ugu:742464560262283355><a:ugu:742464560262283355><a:ugu:742464560262283355>")
                await message.channel.send(
                    "<a:ugu:742464560262283355><a:ugu:742464560262283355><a:ugu:742464560262283355>")

            if message.content.lower().find("tiktok") != -1:
                await message.channel.send("<a:tik1:742468353104543855> <a:tik2:742468352676462592>")
                await message.channel.send("<a:tik3:742468353385562243> <a:tik4:742468352999424170>")

            if message.content.lower().find("owo") != -1:
                await message.channel.send("<a:whatsdis:742468350961123338>")

            if message.content.lower().find("pito") != -1:
                await message.channel.send("MMM PITO")

            if message.content.lower().find("no u") != -1:
                await message.channel.send("no u")

            if message.content.lower().find("patas") != -1:
                await message.channel.send("MMM PATAS")

            if message.content.lower().find("somebody") != -1:
                await message.channel.send("once told me")

            if message.content.lower().find("the world") != -1:
                await message.channel.send("is gonna roll me")

        # await bot.process_commands(discord.message)


def setup(bot):
    bot.add_cog(respuestas(bot))
