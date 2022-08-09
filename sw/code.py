import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation


keyboard = KMKKeyboard()


keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
)
keyboard.row_pins = (
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
)
keyboard.diode_orientation = DiodeOrientation.ROW2COL
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

# LAYER_TAP = KC.LT(1, KC.END, prefer_hold=True, tap_interrupted=False, tap_time=2500) # any tap longer than 2500ms will be interpreted as a hold

xxxxx = KC.NO
keyboard.keymap = [[
    #  x10
    #  0    1      2      3          4      5      6      7      8
    xxxxx, xxxxx, xxxxx, KC.PGDOWN, xxxxx, KC.N9, KC.N8, KC.N7, KC.N3,
    # 9    10     11     12         13     14     15     16      17
    KC.N2, KC.N1, KC.F5, xxxxx,     xxxxx, KC.N4, xxxxx, KC.N0, KC.F10,
    # x11
    # 18    19      20     21       22     23     24      25     26
    xxxxx,  KC.DEL, xxxxx, KC.PGUP, xxxxx, KC.F8, KC.EQL, KC.N6, KC.F2,
    # 27   28        29        30     31     32     33     34         35
    KC.F1, KC.NUBS, KC.LCTRL, xxxxx, xxxxx, KC.N5, xxxxx, KC.MINUS, KC.F9,
    # map GRAVE to NUBS to get the international layout
    # x12
    # 36   37       38        39     40       41     42     43    44
    xxxxx, KC.DOWN, KC.RIGHT, xxxxx, KC.LEFT, xxxxx, xxxxx, KC.N, xxxxx,
    # 45   46     47     48     49     50    51       52        53
    xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.B, KC.RALT, KC.SLASH, KC.F12,
    # x13
    # 54   55     56     57     58     59      60        61    62
    xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.DOT, KC.COMMA, KC.M, KC.C,
    # 63   64     65        66     67     68    69     70     71
    KC.X,  KC.Z,  KC.RCTRL, xxxxx, xxxxx, KC.V, xxxxx, xxxxx, KC.ENTER,
    # x117
    # 72   73      74     75     76     77     78     79    80
    xxxxx, KC.SPC, xxxxx, xxxxx, KC.UP, xxxxx, KC.F6, KC.H, KC.F4,
    # 74 is fn --> not sure how to map this
    # 81   82       83     84     85     86    87       88       89
    xxxxx, KC.ESC, xxxxx, xxxxx, xxxxx, KC.G, KC.LALT, KC.QUOTE, KC.F11,
    # x116
    # 90       91     92     93     94     95    96    97    98
    KC.RSHIFT, xxxxx, xxxxx, xxxxx, xxxxx, KC.L, KC.K, KC.J, KC.D,
    # 99  100   101    102      103    104   105    106      107
    KC.S, KC.A, xxxxx, KC.RGUI, xxxxx, KC.F, xxxxx, KC.SCLN, KC.BSLS,
    # x115
    # 108      109    110    111    112    113    114      115   116
    KC.LSHIFT, xxxxx, xxxxx, xxxxx, xxxxx, KC.F7, KC.RBRC, KC.Y, KC.F3,
    # 117    118     119    120    121      122   123    124      125
    KC.CAPS, KC.TAB, xxxxx, xxxxx, KC.LGUI, KC.T, xxxxx, KC.LBRC, KC.BSPC,
    # x114
    # 126  127    128    129    130    131   132   133   134
    xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.O, KC.I, KC.U, KC.E,
    # 135  136   137    138    139    140   141    142   145
    KC.W,  KC.Q, xxxxx, xxxxx, xxxxx, KC.R, xxxxx, KC.P, xxxxx
] ,
# [  #  fn layer
#     #  x10
#     #  0    1      2      3      4      5      6      7      8
#     xxxxx, xxxxx, xxxxx, KC.END, xxxxx, xxxxx, KC.N8, KC.N7, xxxxx,
#     # 9    10     11     12      13     14     15     16      17
#     xxxxx, xxxxx, xxxxx, xxxxx,  xxxxx, xxxxx, xxxxx, KC.PMNS, KC.SLCK,
#     # x11
#     # 18    19      20     21       22     23     24      25     26
#     xxxxx,  KC.INS, xxxxx, KC.HOME, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx,
#     # 27   28        29        30     31     32     33     34         35
#     KC.F1, KC.NUBS, KC.LCTRL, xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.PSCR,
#     # map GRAVE to NUBS to get the international layout
#     # x12
#     # 36   37       38        39     40       41     42     43    44
#     xxxxx, KC.DOWN, KC.RIGHT, xxxxx, KC.LEFT, xxxxx, xxxxx, KC.N, xxxxx,
#     # 45   46     47     48     49     50    51       52        53
#     xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.B, KC.RALT, KC.SLASH, KC.F12,
#     # x13
#     # 54   55     56     57     58     59      60        61    62
#     xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.DOT, KC.COMMA, KC.M, KC.C,
#     # 63   64     65        66     67     68    69     70     71
#     KC.X,  KC.Z,  KC.RCTRL, xxxxx, xxxxx, KC.V, xxxxx, xxxxx, KC.ENTER,
#     # x117
#     # 72   73      74     75     76     77     78     79    80
#     xxxxx, KC.SPC, xxxxx, xxxxx, KC.UP, xxxxx, KC.F6, KC.H, KC.F4,
#     # 74 is fn --> not sure how to map this
#     # 81   82       83     84     85     86    87       88       89
#     xxxxx, KC.ESC, xxxxx, xxxxx, xxxxx, KC.G, KC.LALT, KC.QUOTE, KC.PAUS,
#     # x116
#     # 90       91     92     93     94     95    96    97    98
#     KC.RSHIFT, xxxxx, xxxxx, xxxxx, xxxxx, KC.L, KC.K, KC.J, KC.D,
#     # 99  100   101    102      103    104   105    106      107
#     KC.S, KC.A, xxxxx, KC.RGUI, xxxxx, KC.F, xxxxx, KC.SCLN, KC.BSLS,
#     # x115
#     # 108      109    110    111    112    113    114      115   116
#     KC.LSHIFT, xxxxx, xxxxx, xxxxx, xxxxx, KC.F7, KC.RBRC, KC.Y, KC.F3,
#     # 117    118     119    120    121      122   123    124      125
#     KC.CAPS, KC.TAB, xxxxx, xxxxx, KC.LGUI, KC.T, xxxxx, KC.LBRC, KC.BSPC,
#     # x114
#     # 126  127    128    129    130    131   132   133   134
#     xxxxx, xxxxx, xxxxx, xxxxx, xxxxx, KC.O, KC.I, KC.U, KC.E,
#     # 135  136   137    138    139    140   141    142   145
#     KC.W,  KC.Q, xxxxx, xxxxx, xxxxx, KC.R, xxxxx, KC.P, xxxxx
# ]
]

# keyboard.keymap = [
#     [
# ]
# ]

if __name__ == "__main__":
    keyboard.go()
