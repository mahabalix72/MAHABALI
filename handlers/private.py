import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bae74190b4bbcfa058415.jpg",
        caption=f"""** 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = 💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔](https://t.me/BROKENLONDAZ)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨ 💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔 💜](https://t.me/BROKENLONDAZ)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝐂𝐇𝐀𝐓𝐓𝐈𝐍𝐆 ❤️🎸](https://t.me/Flarting_chatting)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨  𝐆𝐑𝐎𝐔𝐏 🎧](https://t.me/Flarting_chatting)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = 💔𓊈 𝐁𝐑𝐎𝐊𝐄𝐍 𓊉💔](https://t.me/BROKENLONDAZ)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/Flarting_chatting")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bae74190b4bbcfa058415.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Cʟɪᴄᴋ Mᴇ Tᴏ Gᴇᴛ Rᴇᴘᴏ 💞", url=f"https://t.me/Flarting_chatting")
                ]
            ]
        ),
    )
