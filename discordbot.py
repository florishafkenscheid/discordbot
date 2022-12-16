import hikari
import lightbulb
import random
from datetime import datetime

bot = lightbulb.BotApp(
    token='ENTER TOKEN HERE',
    intents=hikari.Intents.ALL_UNPRIVILEGED
    | hikari.Intents.MESSAGE_CONTENT,
)

now = datetime.now()

@bot.listen(hikari.GuildMessageCreateEvent)
async def PATAT(event):
    if event.is_bot or not event.message.content:
        return
        
    if "wat" in event.message.content.lower():
        random_number = random.randint(1, 1000)
        if random_number == 1000:
            await event.message.respond("Keukenschildpad 🐢", reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'Keukenschildpad {event.member} {now}\n')
        elif 989 < random_number < 1000:
            await event.message.respond("Vinger in je gat", reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()    
                f.write(f'Vinger in je gat {event.member} {now}\n')
        elif 0 < random_number < 334:
            await event.message.respond("PATAT!", reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'PATAT! {event.member} {now}\n')
        elif 333 < random_number < 667:
            await event.message.respond("patat", reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'patat {event.member} {now}\n')
        elif 666 < random_number < 990:
            await event.message.respond("PATAT!11!!!!1!!111!!!11!!!!1!!!1!!!!!", reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'Patat!11!!11!! {event.member} {now}\n')

    if "moeder" in event.content.lower():
        random_number_moeder = random.randint(1, 69)
        if random_number_moeder == 69:
            mena = '767097794711519283'
            mena2 = '776055422481072159'
            await event.message.respond(f'<@{mena}>, <@{mena2}>', reply=True, user_mentions=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'Moeder {event.member} {now}\n')

    if "dan mij" in event.content.lower():
        await event.message.respond('HET IS DAN IK!!', reply=True, mentions_reply=True)
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'Dan ik {event.member} {now}\n')

    if "wanneer" in event.content.lower():
        if event.author_id == 405733173423767559:
            await event.message.respond('Wanneer je vader terug komt', reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now() 
                f.write(f'Milo vader {now}\n')

    if " pull " in event.content.lower():
        random_pull = random.randint(1, 3)
        if event.author_id == 444758306997796888:
            await event.message.respond('Wanneer pull je bitches?', reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'Tom pull {now}\n')
        elif event.author_id == 459998819527032842:
            await event.message.respond('Wanneer pull je bitches?', reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now()
                f.write(f'Siebe pull {now}\n')
        elif random_pull == 3:
            await event.message.respond('Wanneer pull je bitches?', reply=True, mentions_reply=True)
            with open("funnies.txt", "a") as f:
                now = datetime.now() 
                f.write(f'1/3 Pull {event.member} {now}\n')

    if "siebe" in event.content.lower():
        await event.message.respond('belg.. :(')
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'belg siebe {event.member} {now}\n')

    if "ferre" in event.content.lower():
        await event.message.respond('belg.. :(')
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'belg ferre {event.member} {now}\n')

    if " ide " in event.content.lower():
        await event.message.respond('belg.. :(')
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'belg ide {event.member} {now}\n')

    if "12" in event.content.lower():
        await event.message.respond('cock')
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'12 cock {event.member} {now}\n')

    if event.author_id == 459998819527032842:
        await event.message.respond('bek houden belg')
        with open("funnies.txt", "a") as f:
            now = datetime.now()
            f.write(f'siebe bek {now}\n')

if __name__ == "__main__":
    with open("funnies.txt", "a") as f:
        f.write(f'\nNew session started {now}\n')
        f.close()
        bot.run()
