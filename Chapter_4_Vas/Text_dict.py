def create_dict(text):
    a = set(text)
    b = [text._count(i) for i in a]
    c = {}
    c.update(zip(list(a),b))

    return c


if __name__ == "__main__":
    text = input()
    print(create_dict(text))