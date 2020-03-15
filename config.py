# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
#define_modmap({
#    Key.CAPSLOCK: Key.LEFT_CTRL
#})
#
# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile(r'Emacs'), {
    Key.RIGHT_CTRL: Key.ESC,
})

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
define_multipurpose_modmap(
    # Enter is enter when pressed and released. Control when held down.
#    {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}

    # Capslock is escape when pressed and released. Control when held down.
    {Key.CAPSLOCK: [Key.CAPSLOCK, Key.LEFT_CTRL]}
    # To use this example, you can't remap capslock with define_modmap.
)


# Keybindings for Firefox/Chrome
#define_keymap(re.compile("Firefox|Google-chrome"), {
#    # Ctrl+Alt+j/k to switch next/previous tab
#    K("C-M-j"): K("C-TAB"),
#    K("C-M-k"): K("C-Shift-TAB"),
#    # Type C-j to focus to the content
#    K("C-j"): K("C-f6"),
#    # very naive "Edit in editor" feature (just an example)
#    K("C-o"): [K("C-a"), K("C-c"), launch(["gedit"]), sleep(0.5), K("C-v")]
#}, "Firefox and Chrome")
#
# Keybindings for Zeal https://github.com/zealdocs/zeal/
define_keymap(re.compile("Zeal"), {
    # Ctrl+s to focus search area
    K("C-s"): K("C-k"),
}, "Zeal")

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt","terminator","chromium-browser","Google-chrome"), {
    # Cursor
    K("C-s"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-e"): with_mark(K("up")),
    K("C-d"): with_mark(K("down")),

    # delete
    K("C-w"): with_mark(K("backspace")),

    # jump 
    ##  Forward/Backward word
    K("C-dot"): with_mark(K("C-a")),
    K("C-comma"): with_mark(K("C-s")),
    K("C-a"): with_mark(K("C-left")),
    K("C-g"): with_mark(K("C-right")),

    K("C-y"): [K("up"),K("up"),K("up"),K("up"),K("up"), set_mark(False)],
    K("C-b"): [K("down"),K("down"),K("down"),K("down"),K("down"), set_mark(False)],

    ## Beginning/End of line
    K("C-p"): with_mark(K("home")),
    K("C-semicolon"): with_mark(K("end")),

    # Beginning/End of file
    K("C-h"): [K("C-Shift-left"), set_mark(False)],
    
    K("C-t"): [K("C-n"), set_mark(False)],
    K("C-n"): [K("C-Shift-right"), set_mark(False)],

    # delete 
    K("C-r"): [K("delete"), set_mark(False)],

    # delete to line end
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],

    # delete to line begin
    K("C-Shift-u"): [K("Shift-home"), K("C-x"), set_mark(False)],

    # choose to line begin 
    K("C-u"): [K("Shift-home"), set_mark(False)],

    # choose to line end
    K("C-o"): [K("Shift-end"), set_mark(False)],

    # choose to up line 
    K("C-i"): [K("Shift-up"), set_mark(False)],

    # addition
    K("C-k"): [K("Shift-down"), set_mark(False)],
    K("C-m"): [K("Shift-down"), K("Shift-down"), K("Shift-down"), K("Shift-down"), K("Shift-down"), set_mark(False)],
    K("C-slash"): [K("Shift-up"), K("Shift-up"), K("Shift-up"), K("Shift-up"), K("Shift-up"), set_mark(False)],

    K("C-j"): [K("Shift-left"), set_mark(False)],
    K("C-l"): [K("Shift-right"), set_mark(False)],

    K("C-q"): [K("C-F4"), set_mark(False)],

}, "Emacs-like keys")

