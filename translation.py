from info import Info

class Translation(object):
    START_TEXT = """
Hello {}, I' am small media or file to `telegra.ph` link uploader bot.

Made with love ❤️ by @FayasNoushad from India 🇮🇳. Contact <a href='https://telegram.me/FayasChat'>support group</a> for discussion.
"""
    HELP_USER = """
<b><u>Help and Informations</u></b>

- Just give me a media under 5MB.
- Then I will download it.
- I will then upload it to the `Telegra.ph` link.

Made with love ❤️ by @FayasNoushad from India 🇮🇳. Contact <a href='https://telegram.me/FayasChat'>support group</a> for discussion.
"""
    ABOUT_TEXT = f"""
<b><u>Informations About Me</u></b>

- Name : <a href='https://telegram.me/{Info.BOT_USERNAME}'>{Info.BOT_NAME}</a>
- Channel : <a href='http://telegram.me/FayasNoushad'>Fayas</a>
- Support : <a href='http://telegram.me/FayasChat'> Fayas Chat</a>
- Projects : <a href='http://telegram.me/FNPROJECTS'>Fayas Projects</a>
- Language : <a href='https://www.python.org/'>Python3</a>
- Framework : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
- Server : <a href='https://{Info.SERVER_DOMAIN}/'>{Info.SERVER}</a>
- Credits : <a href='https://github.com/FayasNoushad/Image-Editor#credits'>Click Here</a>
- Source : <a href='https://github.com/FayasNoushad/Telegraph-Uploader-Bot'>Click Here</a>
"""
    DOWNLOAD_TEXT = "<code>Downloading to My Server ...</code>"
    UPLOADING_TEXT = "<code>Downloading Completed. Now I'am Uploading to telegra.ph Link ...</code>"
    SOMETHING_WRONG = "Something Wrong! Click help button for more... Contact <a href='https://telegram.me/FayasChat'>support group</a>."
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
