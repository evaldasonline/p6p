from asciimatics.screen import Screen

def fonas(screen):
    for x in range(3,60):
        for y in range(3,20):
            screen.print_at(' ', x,y,bg=4)
            screen.refresh()

Screen.wrapper(fonas)
