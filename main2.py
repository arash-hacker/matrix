from math import cos, sin
import string
import sys
import pyglet
from pyglet import shapes
from datetime import datetime
import random
import string
from pyglet import shapes
w = 600
font_size = 10
window = pyglet.window.Window(w, w)
batch = pyglet.graphics.Batch()
fps_display = pyglet.window.FPSDisplay(window=window)
verticals = []
colors = []
canvas = {}
shuffling = False
alphabet = 0
letters_hiragana = "ㇰㇱㇲㇳㇴㇵㇶㇷㇸㇹㇺㇻㇼㇽㇾㇿ㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩㈪㈫㈬㈭㈮㈯㈰㈱㈲㈳㈴㈵㈶㈷㈸㈹㈺㈻㈼㈽㈾㈿㉀㉁㉂㉃㊀㊁㊂㊃㊄㊅㊆㊇㊈㊉㊊㊋㊌㊍㊎㊏㊐㊑㊒㊓㊔㊕㊖㊗㊘㊙㊚㊛㊜㊝㊞㊟㊠㊡㊢㊣㊤㊥㊦㊧㊨㊩㊪㊫㊬㊭㊮㊯㊰㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿㋀㋁㋂㋃㋄㋅㋆㋇㋈㋉㋊㋋㋐㋑㋒㋓㋔㋕㋖㋗㋘㋙㋚㋛㋜㋝㋞㋟㋠㋡㋢㋣㋤㋥㋦㋧㋨㋩㋪㋫㋬㋭㋮㋯㋰㋱㋲㋳㋴㋵㋶㋷㋸㋹㋺㋻㋼㋽㋾㌀㌁㌂㌃㌄㌅㌆㌇㌈㌉㌊㌋㌌㌍㌎㌏㌐㌑㌒㌓㌔㌕㌖㌗㌘㌙㌚㌛㌜㌝㌞㌟㌠㌡㌢㌣㌤㌥㌦㌧㌨㌩㌪㌫㌬㌭㌮㌯㌰㌱㌲㌳㌴㌵㌶㌷㌸㌹㌺㌻㌼㌽㌾㌿㍀㍁㍂㍃㍄㍅㍆㍇㍈㍉㍊㍋㍌㍍㍎㍏㍐㍑㍒㍓㍔㍕㍖㍗㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㍢㍣㍤㍥㍦㍧㍨㍩㍪㍫㍬㍭㍮㍯㍰㍱㍲㍳㍴㍵㍶㍻㍼㍽㍾㍿"
letters_katakana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ"
letters_persian = "ضصثقفغعهخحمنتالبیسشظطزرذدو.گکچج.ضصثقفغعهخحمنتالبیسشظطزرذدو.گکچج."
letters_hindi = "कखगघङचछजझञटठडढणतथदधनपफबभमक़ख़ग़ज़ड़ढ़फ़यरलळवहशषसऱऴअआइईउऊऋॠऌॡएऐओऔॐऍऑऎऒ"
letters_hebrew = "א‎בּ‎ב‎גּ‎ג‎דּ‎ד‎ה‎ו‎ז‎ח‎ט‎י‎כּ‎כ‎ךּ‎ך‎ל‎מ‎ם‎נ‎ן‎ס‎ע‎פּ‎פ‎ףּ‎פֵּה ף‎פֵה צ‎ץ‎ק‎ר‎שׁ‎שׂ‎תּ‎ת"
letters_emoji = "😀😃😄😁😆😅😂🤣😊😇🙂😍😌😉🙃😘😗😙😚😛😝😜😋🤑🤗🤓😎😒😏😞😟😕😖😣🙁😫😩😤😠😑😐😶😯😦😧😮"
letters_binary = "1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"

letters_en = string.ascii_lowercase
all_letters = [
    letters_binary,
    letters_en,
    letters_hiragana,
    letters_katakana,
    letters_persian,
    letters_hindi,
    letters_hebrew,
    letters_emoji,
]


def rotate(str):
    result = []
    result.append(str[-1])
    for x in str[0:-1]:
        result.append(x)
    return result


def generate_strings(length, sp=5):
    global all_letters, alphabet
    return ''.join(random.choice(all_letters[alphabet]) for i in range(length))+(" "*sp)


def make():
    global verticals, canvas, colors
    verticals = []
    colors = []
    canvas = {}
    for _ in range(1+w//font_size):
        l = (w//font_size)
        n = int((l//10)*random.random())
        verticals.append(generate_strings(l-n, n))
        colors.append([None]*l)

    for v in range(len(verticals)):
        for _ in range(int((w//font_size)*random.random())):
            verticals[v] = rotate(verticals[v])

    for v in range(len(verticals)):
        for c in range(len(verticals[v])):
            index = v*len(verticals)+c
            colors[v][c] = (0,
                            55 + int(200*random.random()),
                            0,
                            int(255*random.random()))
            if(verticals[v][c] == " "):
                colors[v][c] = (
                    255,
                    255,
                    255,
                    255)

            canvas[index] = pyglet.text.Label(
                verticals[v][c], font_name='Times New Roman', font_size=font_size, x=v*font_size, y=w-c*font_size,
                anchor_x="left", anchor_y='center', batch=batch,
                color=colors[v][c])


def draw():
    global canvas, all_letters, alphabet
    for v in range(len(verticals)):
        for c in range(len(verticals[v])):
            index = v*len(verticals)+c
            canvas[index].text = random.choice(
                all_letters[alphabet]) if shuffling == True and verticals[v][c] != " " else verticals[v][c]
            canvas[index].color = colors[v][c]
            canvas[index].draw()


def reset():
    global canvas
    for v in range(len(verticals)):
        for c in range(len(verticals[v])):
            index = v*len(verticals)+c
            canvas[index].text = ""
            canvas[index].color = colors[v][c]
            canvas[index].draw()


def shift():
    for v in range(len(colors)):
        colors[v] = rotate(colors[v])
    global canvas, all_letters, alphabet
    for v in range(0, len(verticals)):
        if(random.random() > 0.9):
            for c in range(len(verticals[v])):
                index = v*len(verticals)+c
                canvas[index].color = colors[v][c]
                canvas[index].draw()


make()
draw()


def update(dt):
    shift()


pyglet.clock.schedule_interval(update, 1/60)


@window.event
def on_key_press(symbol, modifiers):
    global shuffling, alphabet, all_letters, window
    if symbol == pyglet.window.key.Q:
        window.close()
    if symbol == pyglet.window.key.R:
        print("Refresh")
        reset()
        make()
    if symbol == pyglet.window.key.S:
        print("Shuffling:", shuffling)
        shuffling = not shuffling
    if symbol == pyglet.window.key.A:
        alphabet = (alphabet+1) % len(all_letters)
        print("alphabet:", alphabet)
        reset()
        make()


@window.event
def on_draw():
    window.clear()
    batch.draw()
    fps_display.draw()


pyglet.app.run()
