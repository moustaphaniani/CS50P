def main():
    emoji_in = input('Input a phrase with emoji: ')
    print(convert(emoji_in))

def convert(emoji):
    emoticon = emoji.replace(':)', '🙂').replace(':(', '🙁')
    return emoticon

main()
