class script(object):
    START_TXT = """๐๐ฒ๐น๐น๐ผ {}!
๐ ๐ ๐ป๐ฎ๐บ๐ฒ ๐ถ๐ <a href=https://t.me/{}>{}</a>, ๐ ๐ฐ๐ฎ๐ป ๐ฝ๐ฟ๐ผ๐๐ถ๐ฑ๐ฒ ๐บ๐ผ๐๐ถ๐ฒ๐, ๐๐๐๐ ๐๐ฒ๐ป๐ฑ ๐บ๐ผ๐๐ถ๐ฒ ๐ป๐ฎ๐บ๐ฒ ๐ฏ๐ฒ๐น๐ผ๐ ๐๐ป"""
    HELP_TXT = """๐๐ฒ๐, {}
๐๐ฒ๐ฟ๐ฒ ๐ถ๐ ๐๐ต๐ฒ ๐ต๐ฒ๐น๐ฝ ๐ณ๐ผ๐ฟ ๐บ๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐."""
    ABOUT_TXT = """โฏ My Name: {}
โฏ Creator: <a href=https://t.me/VasuXD>แด แด๊ฑแดโขโ</a>
โฏ Library: Pyrogram
โฏ Language: Python 3
โฏ DataBase: MONGO DB 
โฏ Bot Server: Heroku
โฏ Build Status: v1.0.6 [ Beta ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Special Thanksโค to Eva Maria project. 
- Source - Private, Maintained By <a href=https://t.me/VasuXD>แด แด๊ฑแดโขโ</a>
- Bot Owner - @JordanGill

<b>DEVELOPER:</b>
- <a href=https://t.me/VasuXD>แด แด๊ฑแดโขโ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/VasuXD)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of bot

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ Total Files: <code>{}</code>
โ Total Users: <code>{}</code>
โ Total Chats: <code>{}</code>
โ Used Storage: <code>{}</code> MiB
โ Free Storage: <code>{}</code> MiB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
