import keyboard
import pyperclip
EMOJIS = {
    "1": "(✿◠‿◠)",
    "2": "(｡♥‿♥｡)",
    "3": "(づ｡◕‿‿◕｡)づ",
    "4": "щ（ﾟДﾟщ）",
    "5": "ヽ(ｏ`皿′ｏ)ﾉ",
    "6": "★~(◡︿◡✿)",
    "7": "(◡﹏◡✿)",
    "8": "(T⌓T)"
}

def write_emoji(emoji):

    #pyperclip.copy(emoji)
    #keyboard.press_and_release("ctrl+v")
    #keyboard.press_and_release(emoji)
    keyboard.write(emoji)
    
def main():
    for key, emoji in EMOJIS.items():
        keyboard.add_hotkey(
            f"ctrl+shift+{key}",
            write_emoji,
            args=(emoji,)
        )

    print("Kawaii Hotkeys running! :3")
    keyboard.wait()

if __name__ == "__main__":
    main()