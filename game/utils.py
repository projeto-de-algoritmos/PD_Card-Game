import pyxel 

WIDTH = 256
HEIGHT = 256

def knapsack(table ,weight, weights, values, n):

    for i in range(n + 1):
        for weight in range(weight + 1):
            if i == 0 or weight == 0:
                table[i][weight] = 0
            elif weights[i-1] <= weight:
                table[i][weight] = max(values[i-1]
                          + table[i-1][weight-weights[i-1]], 
                              table[i-1][weight])
            else:
                table[i][weight] = table[i-1][weight]
 
    return table[n][weight]

def solution_knapsack(table, weights, ati, atj):
    ans = []

    while ati != 0 and atj != 0:
        if table[ati][atj] != table[ati-1][atj]:
            ans.append(ati-1)
            atj = atj-weights[ati-1]

        ati -= 1

    return ans

def show_table(table, weight, n):
    for i in range(0,n+1):
        for j in range(0,weight+1):
            print(table[i][j], end=" | ")
        print("\n")

def align_text(x, str):
    """
        Centraliza o texto
    """
    n = len(str)
    return (x - (n * pyxel.FONT_WIDTH) / 2)

def col_mouse_bt(mx, my, btx, bty, btw, bth):
    """
        Verifica o clique no botão
    """
    if (btx+(btw/2) > mx > btx-(btw/2)) and (bty+(bth/2) > my > bty-(bth/2)-4):
        return True

def hl_text(x, y, str, color, subcolor):
    pyxel.text(x+1, y+1, str, subcolor)
    pyxel.text(x+1, y,   str, subcolor)
    pyxel.text(x+1, y-1, str, subcolor)
    pyxel.text(x,   y+1, str, subcolor)
    pyxel.text(x,   y-1, str, subcolor)
    pyxel.text(x-1, y+1, str, subcolor)
    pyxel.text(x-1, y,   str, subcolor)
    pyxel.text(x-1, y-1, str, subcolor)

    pyxel.text(x, y, str, color)

def shadow_text(x, y, str, color, subcolor):
    pyxel.text(x+1, y, str, subcolor)
    pyxel.text(x, y+1, str, subcolor)
    pyxel.text(x+1, y+1, str, subcolor)

    pyxel.text(x, y, str, color)

