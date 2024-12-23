def textdict(text):
    text = list(text)
    c = {}
    for let in text:
        newtext = text[:text.index(let)] + text[text.index(let)+1:]
        c.update({let: newtext})
    return c


if __name__ == "__main__":

    text = input()
    print(textdict(text))