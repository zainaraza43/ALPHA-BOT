# ALPHABOT.py
import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import random
from riotwatcher import LolWatcher, ApiError
from twitchAPI.twitch import Twitch

load_dotenv()

# Discord Stuff
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!')

# Riot Stuff
riot_key = os.getenv('RIOT_TOKEN')
watcher = LolWatcher(riot_key)

# Twitch Stuff
twitch_key = os.getenv('TWITCH_TOKEN')
secret_key = os.getenv('TWITCH_SECRET_TOKEN')

twitch = Twitch(twitch_key, secret_key)
twitch.authenticate_app([])

# Tyler1 League information
my_region = 'na1'

TOP_ACCOUNT = watcher.summoner.by_name(my_region, 'HULKSMASH1337')
JG_ACCOUNT = watcher.summoner.by_name(my_region, 'BUZZLIGHTYEAR99')
ADC_ACCOUNT = watcher.summoner.by_name(my_region, 'S8 IS SO FUN')

TOP_MATCHES = watcher.match.matchlist_by_account(my_region, TOP_ACCOUNT['accountId'])
JG_MATCHES = watcher.match.matchlist_by_account(my_region, JG_ACCOUNT['accountId'])
ADC_MATCHES = watcher.match.matchlist_by_account(my_region, ADC_ACCOUNT['accountId'])


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == "! scatter":
        await message.channel.send("shut up ape")

    league_activity_channel = client.get_channel(765830438563348510)
    # await league_activity_channel.send('testing')

    await client.process_commands(message)


@client.command(aliases=['src'])
async def source(ctx):
    await ctx.send("THE SOURCE CODE FOR THE MOST ALPHA DISCORD BOT! WIN !!: https://github.com/zainaraza43/ALPHA-BOT")


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
                 "GENETIC ANOMALY BULLY TOP PLAYER IN WAY !! MOVE !! UNRANKED TO CHALLENGER TOP LANE !!!",
                 "CLOBBERING TIME !! MOVE IT OR DOWN GO !!! IMMACULATE MACHO !"]
    await ctx.send(f'{random.choice(responses)}')


@client.command()
async def meme(ctx):
    responses = [
        "https://cdn.discordapp.com/attachments/421865297285480460/764683875284418574/eyes.png",
        "https://tenor.com/view/tyler1-loltyler1-screaming-dead-wtf-gif-17500255",
        "https://cdn.discordapp.com/attachments/421865297285480460/764684769312636958/pz1uVcP_d.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764684904759558174/unknown.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764684996790976532/rerrrr.PNG",
        "https://cdn.discordapp.com/attachments/421865297285480460/764684985931661312/fadsfff.PNG",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685091003695144/unknown.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685209337200670/unknown.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685291117477898/unknown.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685347643719730/unknown.png",
        "https://tenor.com/view/tyler-booty-tyler1-t1-alpha-gif-14526618",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685540955783198/2afb06a434ccef228c227e556bc7e28e96f7f009.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685609021079582/DcMuMMEWAAAuwwC.png",
        "https://media.discordapp.net/attachments/421865297285480460/764685946154254427/323538814021201.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764685992137326602/D6yEXwZWkAEl97F.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686030879850526/w953wj3wdbi11.png",
        "http://community.tacticsoft.net/uploads/db9473/original/3X/d/1/d17c9e5edbff313af8a9ee4442cec18f0b50a0ea.gif",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686163767197696/unknown.png",
        "https://tenor.com/view/tyler1-food-drop-have-some-oops-food-spill-gif-14542838",
        "https://tenor.com/view/tyler1-funny-meme-sad-tyler1meme-gif-18519966",
        "https://tenor.com/view/tyler1-funny-meme-sad-tyler1meme-gif-18519966",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686444035178537/unknown.png",
        "https://tenor.com/view/league-of-legends-tyler1backflip-fail-gif-14420932",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686534585745408/unknown.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686559345115166/vny6krrv5to51.png",
        "https://cdn.discordapp.com/attachments/421865297285480460/764686909263314974/18KxlZ0.png"
    ]
    await ctx.send(f'{random.choice(responses)}')


def series_to_string(series):
    line = ""
    for ch in series:
        if ch == 'W':
            line += ":white_check_mark: / "
        elif ch == 'L':
            line += ":x: / "
        else:
            line += ":black_large_square: / "
    line = line[:len(line) - 2]
    return line


@client.command(aliases=['Rank'])
async def rank(ctx):

    TOP_ACCOUNT_STATS = watcher.league.by_summoner(my_region, TOP_ACCOUNT['id'])
    JG_ACCOUNT_STATS = watcher.league.by_summoner(my_region, JG_ACCOUNT['id'])
    ADC_ACCOUNT_STATS = watcher.league.by_summoner(my_region, ADC_ACCOUNT['id'])

    accounts = [TOP_ACCOUNT_STATS, JG_ACCOUNT_STATS, ADC_ACCOUNT_STATS]

    for account in accounts:
        if account[0]["leaguePoints"] == 100:
            await ctx.send(
                f'{account[0]["summonerName"]} is {account[0]["tier"]} {account[0]["rank"]} {account[0]["leaguePoints"]} LP. PROMOTION SERIES: ({series_to_string(account[0]["miniSeries"]["progress"])})')
        else:
            await ctx.send(
                f'{account[0]["summonerName"]} is {account[0]["tier"]} {account[0]["rank"]} {account[0]["leaguePoints"]} LP.')


@client.command()
async def live(ctx):
    twitchChannel = twitch.search_channels("loltyler1", 1, "", False)['data'][0]
    is_live = twitchChannel['is_live']
    if is_live:
        await ctx.send(
            f'{twitchChannel["display_name"]} is live with \"{twitchChannel["title"]}\" since {twitchChannel["started_at"]} at '
            f'https://www.twitch.tv/{twitchChannel["display_name"]}')
    else:
        await ctx.send(f'{twitchChannel["display_name"]}\'s dorm was tragically on fire and is not live.')


async def update_activity():
    all_matches = [TOP_MATCHES, JG_MATCHES, ADC_MATCHES]
    while not client.is_closed():
        await asyncio.sleep(1)
        for match in all_matches:
            print(match['matches'][0]['champion'])


client.loop.create_task(update_activity())
client.run(TOKEN)