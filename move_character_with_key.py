from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_SIZE = 100
FRAME_COUNT = 8
DRAW_WIDTH = 100
DRAW_HEIGHT = 100

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                pressed_keys.add(SDLK_RIGHT)
            elif event.key == SDLK_LEFT:
                pressed_keys.add(SDLK_LEFT)
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_UP, SDLK_DOWN):
                pressed_keys.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_keys.discard(event.key)

def update():
    global x, y
    if SDLK_RIGHT in pressed_keys:
        x += 10
    elif SDLK_LEFT in pressed_keys:
        x -= 10
    if SDLK_UP in pressed_keys:
        y += 10
    elif SDLK_DOWN in pressed_keys:
        y -= 10


def draw():
    clear_canvas()
    background.draw(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    character.clip_draw(frame * FRAME_SIZE, 100, FRAME_SIZE, FRAME_SIZE, x, y, DRAW_WIDTH, DRAW_HEIGHT)
    update_canvas()


pressed_keys = set()
running = True
x = CANVAS_WIDTH / 2
y = CANVAS_HEIGHT / 2
frame = 0

# fill here
while running:
    handle_events()
    if not running:
        break
    update()
    draw()
    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()

