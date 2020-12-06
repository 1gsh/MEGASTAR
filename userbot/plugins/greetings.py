import random

from ..utils import admin_cmd, edit_or_reply
from . import catmemes


@bot.on(admin_cmd(pattern=f"gn$", outgoing=True))
async def night(night):
    txt = random.choice(catmemes.GDNIGHT)
    await edit_or_reply(night, txt)


@bot.on(admin_cmd(pattern=f"gm$", outgoing=True))
async def morning(morning):
    txt = random.choice(catmemes.GDMORNING)
    await edit_or_reply(morning, txt)


@bot.on(admin_cmd(pattern=f"gnoon$", outgoing=True))
async def noon(noon):
    txt = random.choice(catmemes.GDNOON)
    await edit_or_reply(noon, txt)


@bot.on(admin_cmd(pattern="gnt$"))
async def gn(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


@bot.on(admin_cmd(pattern="gmg$"))
async def gm(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


# by  @Halto_Tha
@bot.on(admin_cmd(pattern=r"lmoon$"))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕",
    )


@bot.on(admin_cmd(pattern=r"city$"))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁
🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                        👬     🌴/            l  🚔    \🌲
      🌲/   🚖     l        \
          🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲""",
    )


# @PhycoNinja13b 's Part begin from here

@bot.on(admin_cmd(pattern=r"hi ?(.*)"))
async def hi(event):
    giveVar = event.text
    lub = giveVar[4:5]
    if not lub:
        lub = "🌺"
    await edit_or_reply(
        event,
        f"{lub}✨✨{lub}✨{lub}{lub}{lub}\n{lub}✨✨{lub}✨✨{lub}✨\n{lub}{lub}{lub}{lub}✨✨{lub}✨\n{lub}✨✨{lub}✨✨{lub}✨\n{lub}✨✨{lub}✨{lub}{lub}{lub}\n☁☁☁☁☁☁☁☁",
    )



@bot.on(admin_cmd(pattern=r"cheer$"))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@bot.on(admin_cmd(pattern=r"getwell$"))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@bot.on(admin_cmd(pattern=r"luck$"))
async def luck(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@bot.on(admin_cmd(pattern=r"sprinkle$"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )
