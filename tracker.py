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

    mood = mood.lower()

    return anime_emojis.get(mood, "(・・ ) ?  I don't know that mood yet!")
    
def main():
    print("Anime Emoji Mood Tracker")
    print("Type 'quit' to stop. \n")

    while True:
        mood = input("How are you feeling? ")

        if mood.lower() == "quit":
            print("\nThanks for using the Mood Tracker! (＾▽＾)ノ")
            break

        emoji = anime_get_emoji(mood)
        print(f"Your anime mood is: {emoji}\n")

main()