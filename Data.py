from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝙷𝙰𝙻𝙾 {}

𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝙳𝙰𝚃𝙰𝙽𝙶 𝙳𝙸 {}

𝙹𝙸𝙺𝙰 𝚃𝙸𝙳𝙰𝙺 𝙿𝙴𝚁𝙲𝙰𝚈𝙰 𝙳𝙴𝙽𝙶𝙰𝙽 𝙱𝙾𝚃 𝙸𝙽𝙸, 
1) 𝙶𝙰𝚄𝚂𝙰𝙷 𝙱𝙰𝙲𝙰 𝙿𝙴𝚂𝙰𝙽 𝙸𝙽𝙸 
2) 𝙱𝙻𝙾𝙺𝙸𝚁 𝙱𝙾𝚃 𝙰𝚃𝙰𝚄 𝙳𝙴𝙻𝙰𝚃𝙴 𝙲𝙷𝙰𝚃 

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @kenapatagkazu
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ​", url="https://t.me/kenapatagkazu")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/kazu_stringbot")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @karstring_bot

Group Support : [Gabung](https://t.me/kazusupportgrp)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @kenapatagkazu
    """
