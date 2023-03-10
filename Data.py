from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
π·π°π»πΎ {}

ππ΄π»π°πΌπ°π π³π°ππ°π½πΆ π³πΈ {}

πΉπΈπΊπ° ππΈπ³π°πΊ πΏπ΄ππ²π°ππ° π³π΄π½πΆπ°π½ π±πΎπ πΈπ½πΈ, 
1) πΆπ°πππ°π· π±π°π²π° πΏπ΄ππ°π½ πΈπ½πΈ 
2) π±π»πΎπΊπΈπ π±πΎπ π°ππ°π π³π΄π»π°ππ΄ π²π·π°π 

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @kenapatagkazu
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sα΄α΄Κα΄ Ι’α΄Ι΄α΄Κα΄α΄ΙͺΙ΄Ι’ sα΄ssΙͺα΄Ι΄β", callback_data="generate")],
        [InlineKeyboardButton(text="Κα΄α΄α΄β", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sα΄α΄Κα΄ Ι’α΄Ι΄α΄Κα΄α΄ΙͺΙ΄Ι’ sα΄ssΙͺα΄Ι΄", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sα΄α΄Κα΄ Ι’α΄Ι΄α΄Κα΄α΄ΙͺΙ΄Ι’ sα΄ssΙͺα΄Ι΄", callback_data="generate")],
        [InlineKeyboardButton("α΄α΄ΙͺΙ΄α΄α΄Ι΄α΄α΄ ΚΚβ", url="https://t.me/kenapatagkazu")],
        [
            InlineKeyboardButton("Κα΄α΄‘ α΄α΄ α΄sα΄ α΄α΄ββ", callback_data="help"),
            InlineKeyboardButton("α΄Κα΄α΄α΄β", callback_data="about")
        ],
        [InlineKeyboardButton("ΙͺΙ΄κ°α΄ Κα΄α΄ Κα΄ΙͺΙ΄Ι΄Κα΄β", url="https://t.me/kazu_stringbot")],
    ]

    # Help Message
    HELP = """
β¨ **Available Commands** β¨

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
