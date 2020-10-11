# ALPHABOT.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.author.name == "Extreme":
    #    await message.channel.send("shut up retard")

    await client.process_commands(message)

@client.command()
async def source(ctx):
    await ctx.send("THE SOURCE CODE FOR THE MOST ALPHA BOT DISCORD: https://github.com/zainaraza43/ALPHA-BOT")

@client.command(aliases=['streamtitle'])
async def title(ctx):
    responses = ["MAJESTIC PRECISION CALCULATE AND TAKES OVER !!! BOOM !!!!",
                 "MACHO MONSTER CONSTRUCT DESTRUCT INCOMING PLAYER !! HUGE !!!",
                 "SLICE OF BREAD . HAMMER . ORANGE !!! internet plate !!! LET GO !!!!",
                 "calmness and winner . right here . TURBO GENETIC MASTERMIND !!!",
                 "T1 .. ODDS AGAINST HE .. BUT DONT CARE HE MUSCLE FREAK POWER THROUGH PUNISHER !!!!",
                 "INSANELY ATHLETIC ! TALL LIKE TREE !! MOLLY WOP ALL COME FRONT !",
                 "RIDICULOUS !!! THIS GUY !! HOW !! IT MAKE NOT SENSE !! i wish like he lol ",
                 "ABSOLUTELY INVINCIBLE WORLD WONDER T1 ! HE NOT THE SAME !!!!",
                 "UNSTOPPABLE BEAST OF MAN 6'5 POWER HOUSE MACHINE !! DIFFERENT BUILT !!",
                 "SIZE 17 SHOE WALLOP ENEMY ! NOT CLOSE !!!! me good :D !",
                 "WINNER IS ALWAYS WIN !! WIN ALL TIME FOR WINNER . won !",
                 "UNDEFEAT T1 TODDLERS DO AGAIN !! IT EASY !!!",
                 "DOMINATING SKYROCKET THROUGH DIAMOND ELO ! BUILT FREAKY ! ! ",
                 "DIAMOND I GO ! PLOW OVER SMALL GET OUT !!! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "COCONUT ! GASP ITS T1 PLEASE DONT HURT ME !!! OVERPOWER MAN DESTROY ALL !!!!!",
                 "INSANE MEMBRANE DOMINATION 6'5 OUTSTANDING !!! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "HOW CANTS HERE HAHAH TURBO YELLOW AROUND TOWN !!! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "MONSTER MAN HUGE ! OH WOW HE DO ARE LOL !! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "UNDISPUTED BESTS PLAYER ALIVE ! NOT 1 CLOSE EVEN !! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "SNAPPY POP TTTTURBO BOOST TO DIAMONDS! i freak lol ! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "LEGENDARY LARGE FANTASTIC ! ALL EQUAL ME ! toaster oven !!! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "DOMINATING WAYS TO DIAMOND ! BEAST AND BONKERS !!! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "FOCUS SPICE INSPIRATIONAL DEMOLISH CLASSIC ! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "GENETIC ANOMALY BULLY TOP PLAYER IN WAY !! MOVE !! UNRANKED TO CHALLENGER TOP LANE !!!"]
    await ctx.send(f'{random.choice(responses)}')


client.run(TOKEN)
