# Kawaii Hotkeys (✿◠‿◠)

A tiny Python utility that lets you type kaomoji anywhere using custom keyboard shortcuts.

Instead of copying and pasting kaomoji manually, press a keyboard shortcut and the corresponding kaomoji is automatically pasted into the active application.

## Features ヽ(ｏ`皿′ｏ)ﾉ`

* Custom keyboard shortcuts for kawaii emojis
* Works in any application that supports text input
* Uses the clipboard for reliable pasting
* Lightweight and simple

## Hotkeys (づ｡◕‿‿◕｡)づ

| Shortcut           | Kaomoji      |
| ------------------ | ------------ |
| `Ctrl + Shift + 1` | `(✿◠‿◠)`     |
| `Ctrl + Shift + 2` | `(｡♥‿♥｡)`    |
| `Ctrl + Shift + 3` | `(づ｡◕‿‿◕｡)づ` |
| `Ctrl + Shift + 4` | `щ（ﾟДﾟщ）`    |
| `Ctrl + Shift + 5` | `ヽ(ｏ`皿′ｏ)ﾉ`  |
| `Ctrl + Shift + 6` | `★~(◡︿◡✿)`   |
| `Ctrl + Shift + 7` | `(◡﹏◡✿)`     |
| `Ctrl + Shift + 8` | `(T⌓T)`      |

## Requirements ★~(◡︿◡✿)

* Python 3.x
* [`keyboard`](https://pypi.org/project/keyboard/)
* [`pyperclip`](https://pypi.org/project/pyperclip/)

Install the dependencies with:

```bash
pip install keyboard pyperclip
```

## Usage (｡♥‿♥｡)

Run the script:

```bash
python main.py
```

You should see:

```text
Kawaii Hotkeys running! :3
```

The program will keep running in the background and listen for the 
configured hotkeys.

Press `Ctrl + C` in the terminal to stop it.

## Customizing

You can add or change kaomoji by editing the `EMOJIS` dictionary:

```python
EMOJIS = {
    "1": "(✿◠‿◠)",
    "2": "(｡♥‿♥｡)",
    "9": "your kaomoji here",
}
```

The corresponding shortcut will automatically use the new entry.

##  Technologies щ（ﾟДﾟщ）

* Python
* `keyboard`
* `pyperclip`

---

Made for maximum kaomoji efficiency. (づ｡◕‿‿◕｡)づ
