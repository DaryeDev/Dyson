#No modificar.
from discord.ext import commands

bot = commands.Bot(command_prefix="d.")


class nombreModulo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
#Fin de no modificable.

        if message.author.id != 741962880097845340: # Si el mensaje no viene de Dyson en sí:

# Caso 1: Si quieres que Dyson responda algo al ver que un mensaje tiene las palabras que le has indicado (ojo, lo tiene que encontrar todo junto).
            if message.content.lower().find("algo"): # Si en el mensaje se encuentra "algo", tenga mayus o no:
                await message.channel.send("Respuesta") # Dyson responde con "Respuesta".


# Caso 2: Si quieres que Dyson responda algo al ver que un mensaje termina por las palabras que le indiques.
            if message.content.lower().endswith("algo"): # Si el mensaje termina por "algo", tenga mayus o no:
                await message.channel.send("Respuesta") # Dyson responde con "Respuesta".


# Caso 3: Si quieres que Dyson responda algo al ver que un mensaje empieza por las palabras que le indiques.
            if message.content.lower().startswith("algo"): # Si el mensaje empieza por "algo", tenga mayus o no:
                await message.channel.send("Respuesta") # Dyson responde con "Respuesta".


#Si se quisiese poner más, solo hay que copiar el bloque deseado (desde "if message.content..." hasta el final del bloque de codigo).



def setup(bot):
    bot.add_cog(nombreModulo(bot))