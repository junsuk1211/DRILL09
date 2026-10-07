from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here
    global x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x+10
            elif event.key == SDLK_LEFT:
                x = x -10
            elif event.key == SDLK_ESCAPE:
                running = False

running = True
x = CANVAS_WIDTH // 2
frame = 0

# fill here
while running:
    clear_canvas()
    background.draw(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    character.clip_draw(frame*100,100,100,100,x,90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()

