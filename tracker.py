import random

COLORS = {
    "reset": "\033[0m",
    "pink": "\033[95m",
    "cyan": "\033[96m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "bold": "\033[1m"
}

def color(text, c):
    return COLORS.get(c, COLORS["reset"]) + text + COLORS["reset"]


def anime_get_emoji(mood):
    anime_emojis = {
        "happy": "(＾▽＾)",
        "sad": "(︶︹︺)",
        "angry": "(╬ Ò﹏Ó)",
        "excited": "☆*:.｡.o(≧▽≦)o.｡.:*☆",
        "tired": "(-＿-)",
        "confused": "(◎_◎;)",
        "calm": "(˘ω˘)",
        "romantic": "(♡˙︶˙♡)",
        "shy": "(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)",
        "determined": "(•̀ᴗ•́)و ̑̑"
    }
    # mood = mood.lower()

    return anime_emojis.get(mood, "(・・ ) ?  I don't know that mood yet!")

def get_anime_quote(mood):
    quotes = {
        "happy": [
            "“Whatever you lose, you'll find it again. But what you throw away you’ll never get back.” — Kenshin",
            "“If it’s to protect our family, be it the family we were born with or the one we create, I’ll fight!” — Naruto"
        ],
        "sad": [
            "“It's okay to feel sad. Crying cleans the heart.” — Luffy",
            "“People’s lives don’t end when they die. It ends when they lose faith.” — Itachi"
        ],
        "angry": [
            "“If you don’t take risks, you can’t create a future!” — Luffy",
            "“A lesson without pain is meaningless.” — Fullmetal Alchemist"
        ],
        "excited": [
            "“I’m fired up!” — Natsu",
            "“Power comes in response to a need, not a desire.” — Goku"
        ],
        "tired": [
            "“Sometimes you must hurt in order to know.” — Pain",
            "“Take a break. Even heroes rest.”"
        ],
        "confused": [
            "“Whatever you do, enjoy it to the fullest.” — Gojo",
            "“You don’t need a reason to be kind.” — Mob"
        ],
        "calm": [
            "“In this world, there is no such thing as coincidence.” — Yuuko",
            "“A calm heart can overcome any storm.”"
        ],
        "romantic": [
            "“You’re my reason to smile.” — Unknown Anime Hero",
            "“No matter how far apart we are, our hearts will always be connected.” — Tohru"
        ],
        "shy": [
            "“You… you make my heart race.” — An anime protagonist probably",
            "“It’s embarrassing… but I like being with you.”"
        ],
        "determined": [
            "“I will become stronger… no matter what.”",
            "“When you give up, that’s when the game is over.” — Coach Anzai"
        ]
    }

    if mood in quotes:
        return random.choice(quotes[mood])
    return "'I don't recognize that feeling yet... but I believe in you!'"
    
def main():
    print(color("Welcome to the Anime Emoji Mood Tracker", "pink"))
    print(color("Type 'quit' to stop. \n", "cyan"))

    while True:
        mood = input(color("How are you feeling right now? ", "yellow")).lower()

        if mood.lower() == "quit":
            print(color("\nThanks for using the Mood Tracker! (＾▽＾)ノ", "green"))
            break

        emoji = anime_get_emoji(mood)
        quote = get_anime_quote(mood)

        print(color(f"Your anime mood is: {emoji}\n", "bold"))
        print(color(f"Anime wisdom:\n{quote}\n", "blue"))

main()