import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𝐘𝐄 ||✘𝐔𝐏𝐏𝐄𝐑 •🇾🇪⇩𓄹 ", url=f"https://t.me/UPE3R"), 
                 ],[
                    InlineKeyboardButton(
                        "⎙𝐀𝐖 𝐂𝐎𝐃𝐄 || شروحات برمجيه⎙", url=f"https://t.me/AWCODE3"),
                ],[
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋🜫", url=f"https://t.me/FTTIT"),
                    InlineKeyboardButton(
                        "🕷️َِ .,ᯓََِِ⸁🇨🇵إمـۦـﹻٰ۫ﹻۧﹻــيــﹻٰ۫ﹻــﹻٰ۫ـࢪ.١ ⌯", url=f"https://t.me/ZR_EL"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/AWCODE3"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["علوي انجم","احمد","علوي","مبرمج","TOM","tom"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("UPE3R")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين انجم","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كريستين انجم","كريستين","كرستين","الدكتوره","cristin","كرستينه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مانو انجم","مانو","الممول","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C1_I_I")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𝐘𝐄 ||✘𝐔𝐏𝐏𝐄𝐑 •🇾🇪⇩𓄹", url=f"https://t.me/UPE3R"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/AWCODE3"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/c973727bddf803e028539.jpg",
        caption=f"""**⩹⊷━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𝐘𝐄 ||✘𝐔𝐏𝐏𝐄𝐑 •🇾🇪⇩𓄹", url=f"https://t.me/UPE3R"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐀𝐖 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/AWCODE3"),
                ],

            ]

        ),

    )



    
