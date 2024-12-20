import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "29869097"))
API_HASH = getenv("API_HASH", "b011037acfaf24f5dd4b5dda104c55fe")
BOT_TOKEN = getenv("BOT_TOKEN", "6508386922:AAGSbwF2YK5X6zzbt_vfWf7ojR88jwD7Mx0")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kingbrukh:kingkhan@kingbruh.ra3pjgm.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 500))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002028213552"))
OWNER_ID = int(getenv("OWNER_ID", 1814052601))
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Hamza4900/Sportive",
)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/askkoleji")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/konnusanlar")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "AgFjGt4AFPZyAeH_agLhLR7CgOiPViN5mqsbto7ex1-JvLSpIwTwcMIRIBeNb22P7U12eBfPWqsW-lZvwcwzshXR8aNoVQ32gvdK_XeNvhlcEM5znspF-p555aek99P663A7asRuFFsFSr3f1gL4ONVPUOEUWz9cGb6RMMOp1Zo4A6TF2BZmPV4MV3fOF7SItsMdr99thLMVPJryvgHGVuw_wG09kbBObKrKcD842ZDYGe7Ji6q54pNFzx8LObFj9xLXjtSGs-ut0mq7gFk7CcPAvdkYRMC4oHEVeDvdlnZyr9J_83YeskrrjMjShGwsD8k83DGcShUcz0Jucqh7Nvd2s4QTlwAAAAHL7cygAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)



HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)
# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/5933c1352e77e43c7af52.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
