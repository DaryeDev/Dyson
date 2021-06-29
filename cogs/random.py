import random as rnd
from discord.ext import commands


class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['8', '🎱'])
    async def ocho(self, ctx, *, question=None):

        if question is None:
            msg = 'Pregúntame algo xdd.'
            await ctx.channel.send(msg)
            return

        answerList = ["En mi opinión, sí",
                      "Es cierto",
                      "Es decididamente así",
                      "Probablemente",
                      "Buen pronóstico",
                      "Todo apunta a que sí",
                      "Sin duda",
                      "Sí",
                      "Sí - definitivamente",
                      "Debes confiar en ello",
                      "Respuesta vaga, vuelve a intentarlo",
                      "Pregunta en otro momento",
                      "Será mejor que no te lo diga ahora",
                      "No puedo predecirlo ahora",
                      "Concéntrate y vuelve a preguntar",
                      "Puede ser",
                      "No cuentes con ello",
                      "Mi respuesta es no",
                      "Mis fuentes me dicen que no",
                      "Las perspectivas no son buenas",
                      "Muy dudoso"]
        randomNumber = rnd.randint(0, len(answerList) - 1)
        msg = f'{answerList[randomNumber]}'
        # Say message
        await ctx.channel.send(msg)

    @commands.command(pass_context=True, aliases=['dice', '🎲'])
    async def dado(self, ctx, *, caras=None):

        if caras is None:
            randomNumber = rnd.randint(1, 6)
            msg = f'¡Ha salido {str(randomNumber)}!'
            # Say message
            await ctx.channel.send(msg)
        else:
            randomNumber = rnd.randint(1, int(caras))
            msg = f'¡Ha salido {str(randomNumber)}!'
            # Say message
            await ctx.channel.send(msg)

    @commands.command(pass_context=True, aliases=['choose', 'pick'])
    async def elige(self, ctx, *args):
        print(args)
        msgList = ["En mi opinión, %decision% es mejor opción.",
                   "Si yo fuese tú, elegiría %decision%.",
                   "Gana %decision%, lo siento a los demás.",
                   "Hm... %decision%, apuesto por ello",
                   "%decision% parece ser la mejor opción en este caso",
                   "Todo apunta a que %decision% es a por lo que deberías decidirte",
                   "Sin duda, %decision% gana.",
                   "%decision%, sin duda alguna.",
                   "Definitivamente elijo %decision%",
                   "Es difícil elegir... Pero en mi opinión %decision% gana esta vez.",
                   "Uf... parece una difícil decisión, pero me inclino más hacia %decision%",
                   "%decision%. Definitivamente",
                   "%decision%, de una.",
                   "%decision%, obviamente.",
                   "Elijo pito, jaja momento joto. Nah, pero fuera de coñas elijo %decision% xdddd",
                   "Elijo pito, jaja momento collado. Nah, pero fuera de coñas elijo %decision% xdddd",
                   "Si.",
                   "No.",
                   "Si le estás preguntando algo así a un bot de Discord, no se que coño haces con tu vida... Pero elijo %decision% xd",
                   "Yo iría a por %decision% de cabeza.",
                   "pito"]
        randnum = rnd.randint(0, len(args) - 1)
        msgTemplate = rnd.randint(0, len(msgList) - 1)
        msg = msgList[msgTemplate].replace("%decision%", args[randnum])
        await ctx.channel.send(msg)


def setup(bot):
    bot.add_cog(random(bot))
