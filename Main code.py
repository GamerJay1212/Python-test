import urwid
def select_option(Placeholder1):
    print("This is placeholder text!")

def exit_handler(key):
    if key == 'q':
        raise urwid.ExitMainLoop()

def main():
    menu_items = [
        urwid.Button("Print Guide.txt")
    ]
