import discord
import random
import requests
from discord.ext import commands
from bot_logic import gen_pass
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def cześć(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))


@bot.command()
async def jaktam(ctx):
    await ctx.send(f'Dziękuję, że pytasz, ale jestem tylko programem komputerowym, więc nie mam uczuć ani emocji.')

@bot.command()
async def kostka(ctx):
    a = random.randint(1,6)
    await ctx.send(f'Wylosowałeś ' + str(a))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def pa(ctx):
    await ctx.send(f'Papa')

@bot.command()
async def proekologia(ctx):
    x = random.randint(1, 11)
    if x == 1:
        await ctx.send('Recykling: Rozpocznij od segregacji odpadów w swoim domu. Naucz się, jakie materiały można recyklingować i przestrzegaj zasad właściwego segregowania śmieci.')
    if x == 2:
        await ctx.send('Oszczędzanie energii: Zainwestuj w energooszczędne urządzenia, takie jak żarówki LED, termosy, czy izolowane okna. Unikaj marnotrawienia energii poprzez wyłączanie nieużywanych urządzeń.')
    if x == 3:
        await ctx.send('Zdrowa żywność: Wybieraj lokalne i sezonowe produkty spożywcze, które mają mniejszy wpływ na środowisko. Redukcja spożycia mięsa i jedzenie mniej przetworzonej żywności również może pomóc.')
    if x == 4:
        await ctx.send('Transport: Wybieraj środki transportu o mniejszym wpływie na środowisko, takie jak rower, komunikację publiczną, czy samochody elektryczne. Możesz również zastanowić się nad carsharingiem lub carpoolingiem.')
    if x == 5:
        await ctx.send('Minimalizacja odpadów: Staraj się unikać produktów jednorazowego użytku, takie jak plastikowe opakowania i słomki. Rozważ używanie wielokrotnego użycia przed jednorazowymi alternatywami.')
    if x == 6:
        await ctx.send('Upcykling: Przemyśl, jakie przedmioty można wykorzystać ponownie lub przekształcić w coś innego zamiast wyrzucać je na śmietnik.')
    if x == 7:
        await ctx.send('Edukacja: Czytaj, ucz się i rozmawiaj na temat problemów ekologicznych. Możesz dołączyć do organizacji proekologicznych, uczestniczyć w warsztatach, czy wziąć udział w kampaniach edukacyjnych.')
    if x == 8:
        await ctx.send('Zero waste: Jeśli jesteś naprawdę zaangażowany w minimalizację odpadów, zainteresuj się ruchem "zero waste". To podejście polega na maksymalnym ograniczeniu wytwarzania śmieci poprzez recykling, kompostowanie, ponowne wykorzystanie i unikanie jednorazowych produktów.')
    if x == 9:
        await ctx.send('Woda: Oszczędzaj wodę, zamykając kran podczas mycia zębów i instalując oszczędzające wodę urządzenia w swoim domu.')
    if x == 10:
        await ctx.send('Inspiracja: Poszukaj innych osób, które żyją proekologicznie, na przykład w mediach społecznościowych lub blogach. Mogą one dostarczyć ci wielu inspirujących pomysłów i wskazówek.')
    if x == 11:
        await ctx.send('Wyrzucanie śmieci do odpowiednich pojemników zależy od lokalnych przepisów i systemów gospodarki odpadami. Ogólnie rzecz biorąc, plastik, papier, karton, szkło i metal powinny być wrzucane do odpowiednich pojemników na surowce wtórne. Odpady organiczne, takie jak resztki jedzenia i trawa, powinny trafiać do osobnego pojemnika. Elektronikę, zużyte baterie, oraz niebezpieczne substancje należy oddać w specjalistycznych punktach zbierania. Pamiętaj, aby przestrzegać miejscowych wytycznych dotyczących segregacji odpadów, aby pomóc w ochronie środowiska.')







bot.run("MTE2MjA1NTg0MjYwMjk1NDc4Mg.G2mpFF.6Y65jgG4juFZfNt1MFtLqKq2bn28R2Dls2t-e4") 