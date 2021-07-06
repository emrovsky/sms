from discord.ext import commands
from twilio.rest import Client
import discord

bot = commands.Bot(command_prefix='!')

@bot.command()
async def mesajgonder(ctx, arg , arg2):
    account_sid = ('gir')
    auth_token = ('gir')
    client = Client(account_sid, auth_token)


    message = client.messages \
                    .create(
                         body=arg2,
                         from_='+13189333284',
                         to=arg
                     
                     )
    print(message.sid)
    await ctx.send("Mesajınız gönderildi!")
    


bot.run('Njk4ODk5Mjk1MTE3NTA4NjM5.XpMisA.R2X7sFd4Uia-2f0K_6tO9mmKK1A')