def snakelist(H, W):

    lis = [[0 for i in range(W)] for j in range(H)]
    switcher = 1
    Hmax, Wmax = H - 1, W - 1
    Hmin, Wmin = 0, 0
    t, p = 0, 0

    for k in range(H*W):
        if switcher > 0:
            if t == Wmax and p != Hmax:
                lis[p][t] = k
                p += 1
            elif t == Wmax and p == Hmax:
                switcher = -1
                Wmax -= 1
                Hmax -= 1
                lis[p][t] = k
                t -= 1
            else:
                lis[p][t] = k
                t += 1
        else:
            if t == Wmin and p != Hmin:
                lis[p][t] = k
                p -= 1
            elif t == Wmin and p == Hmin:
                Hmin += 1
                Wmin += 1
                t, p = Wmin, Hmin
                switcher = 1
                lis[p][t] = k
                if Wmax > 1:
                    t += 1
                else:
                    p += 1
            else:
                lis[p][t] = k
                t -= 1
    return lis


if __name__ == "__main__":

    H = int(input("Height: "))
    W = int(input("Width: "))

    lis = snakelist(H,W)
    for i in range(H):
        for j in range(W):
            print(lis[i][j], end='\t')
        print('\n')
