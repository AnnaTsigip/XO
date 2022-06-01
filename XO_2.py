import random
import tkinter as tk

root = tk.Tk()
root.title('Крестики-нолики')
root.geometry("300x400")

game_over = False


def get_game_over():
    global game_over
    if (btn1['text'] == btn2['text'] == btn3['text']) and btn2['text'] != '':
        btn1['fg'] = 'red'
        btn2['fg'] = 'red'
        btn3['fg'] = 'red'
        game_over = True
    elif (btn4['text'] == btn5['text'] == btn6['text']) and btn5['text'] != '':
        btn4['fg'] = 'red'
        btn5['fg'] = 'red'
        btn6['fg'] = 'red'
        game_over = True
    elif (btn7['text'] == btn8['text'] == btn9['text']) and btn8['text'] != '':
        btn7['fg'] = 'red'
        btn8['fg'] = 'red'
        btn9['fg'] = 'red'
        game_over = True
    elif (btn1['text'] == btn5['text'] == btn9['text']) and btn5['text'] != '':
        btn1['fg'] = 'red'
        btn5['fg'] = 'red'
        btn9['fg'] = 'red'
        game_over = True
    elif (btn7['text'] == btn5['text'] == btn3['text']) and btn5['text'] != '':
        btn7['fg'] = 'red'
        btn3['fg'] = 'red'
        btn5['fg'] = 'red'
        game_over = True
    elif (btn1['text'] == btn4['text'] == btn7['text']) and btn7['text'] != '':
        btn1['fg'] = 'red'
        btn4['fg'] = 'red'
        btn7['fg'] = 'red'
        game_over = True
    elif (btn2['text'] == btn5['text'] == btn8['text']) and btn5['text'] != '':
        btn2['fg'] = 'red'
        btn5['fg'] = 'red'
        btn8['fg'] = 'red'
        game_over = True
    elif (btn3['text'] == btn6['text'] == btn9['text']) and btn9['text'] != '':
        btn3['fg'] = 'red'
        btn6['fg'] = 'red'
        btn9['fg'] = 'red'
        game_over = True
    elif btn1['text'] != '' and btn2['text'] != '' and btn3['text'] != '' and btn4['text'] != '' and btn5['text'] != '' and btn6['text'] != '' and btn7['text'] != '' and btn8['text'] != '' and btn9['text'] != '':
        game_over=True
    return game_over


def get_move_ai():
    global game_over
    new_random = True
    while new_random:
        button = random.randint(1, 9)
        if button == 1:
            if btn1['text'] == '':
                btn1['text'] = '0'
                new_random = False
        elif button == 2:
            if btn2['text'] == '':
                btn2['text'] = '0'
                new_random = False
        elif button == 3:
            if btn3['text'] == '':
                btn3['text'] = '0'
                new_random = False
        elif button == 4:
            if btn4['text'] == '':
                btn4['text'] = '0'
                new_random = False
        elif button == 5:
            if btn5['text'] == '':
                btn5['text'] = '0'
                new_random = False
        elif button == 6:
            if btn6['text'] == '':
                btn6['text'] = '0'
                new_random = False
        elif button == 7:
            if btn7['text'] == '':
                btn7['text'] = '0'
                new_random = False
        elif button == 8:
            if btn8['text'] == '':
                btn8['text'] = '0'
                new_random = False
        elif button == 9:
            if btn9['text'] == '':
                btn9['text'] = '0'
                new_random = False
    game_over = get_game_over()


def btn1_click():
    global game_over
    if not game_over:
        if btn1['text'] == '':
            btn1['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn2_click():
    global game_over
    if not game_over:
        if btn2['text'] == '':
            btn2['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn3_click():
    global game_over
    if not game_over:
        if btn3['text'] == '':
            btn3['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn4_click():
    global game_over
    if not game_over:
        if btn4['text'] == '':
            btn4['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn5_click():
    global game_over
    if not game_over:
        if btn5['text'] == '':
            btn5['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn6_click():
    global game_over
    if not game_over:
        if btn6['text'] == '':
            btn6['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn7_click():
    global game_over
    if not game_over:
        if btn7['text'] == '':
            btn7['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn8_click():
    global game_over
    if not game_over:
        if btn8['text'] == '':
            btn8['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn9_click():
    global game_over
    if not game_over:
        if btn9['text'] == '':
            btn9['text'] = 'X'
        game_over = get_game_over()
        if not game_over:
            get_move_ai()


def btn0_click():
    global game_over
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''
    game_over = False


btn1 = tk.Button(text='', command=btn1_click, fg='black')
btn2 = tk.Button(text='', command=btn2_click, fg='black')
btn3 = tk.Button(text='', command=btn3_click, fg='black')
btn4 = tk.Button(text='', command=btn4_click, fg='black')
btn5 = tk.Button(text='', command=btn5_click, fg='black')
btn6 = tk.Button(text='', command=btn6_click, fg='black')
btn7 = tk.Button(text='', command=btn7_click, fg='black')
btn8 = tk.Button(text='', command=btn8_click, fg='black')
btn9 = tk.Button(text='', command=btn9_click, fg='black')
btn0 = tk.Button(text='Начать с начала', command=btn0_click, fg='black')

btn1.pack()
btn1.place(x=0, y=0, height=100, width=100)
btn2.pack()
btn2.place(x=100, y=0, height=100, width=100)
btn3.pack()
btn3.place(x=200, y=0, height=100, width=100)
btn4.pack()
btn4.place(x=0, y=100, height=100, width=100)
btn5.pack()
btn5.place(x=100, y=100, height=100, width=100)
btn6.pack()
btn6.place(x=200, y=100, height=100, width=100)
btn7.pack()
btn7.place(x=0, y=200, height=100, width=100)
btn8.pack()
btn8.place(x=100, y=200, height=100, width=100)
btn9.pack()
btn9.place(x=200, y=200, height=100, width=100)
btn0.pack()
btn0.place(x=100, y=340, height=50, width=100)

root.mainloop()