from math import hypot

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_SIZE = 100
FRAME_COUNT = 8
DRAW_WIDTH = 100
DRAW_HEIGHT = 100
MOVE_SPEED = 200.0
ANIMATION_FPS = {"IDLE": 6.0, "MOVE": 12.0}

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

def update(dt):
    global x, y, facing, state, frame, animation_elapsed
    dx = int(SDLK_RIGHT in pressed_keys) - int(SDLK_LEFT in pressed_keys)
    dy = int(SDLK_UP in pressed_keys) - int(SDLK_DOWN in pressed_keys)
    if dx > 0:
        facing = "RIGHT"
    elif dx < 0:
        facing = "LEFT"
    previous_position = (x, y)
    length = hypot(dx, dy)
    if length:
        dx /= length
        dy /= length
    x += dx * MOVE_SPEED * dt
    y += dy * MOVE_SPEED * dt
    x = max(DRAW_WIDTH / 2, min(x, CANVAS_WIDTH - DRAW_WIDTH / 2))
    y = max(DRAW_HEIGHT / 2, min(y, CANVAS_HEIGHT - DRAW_HEIGHT / 2))
    state = "MOVE" if (x, y) != previous_position else "IDLE"
    animation_elapsed += dt
    frame_interval = 1.0 / ANIMATION_FPS[state]
    while animation_elapsed >= frame_interval:
        animation_elapsed -= frame_interval
        frame = (frame + 1) % FRAME_COUNT


def draw():
    clear_canvas()
    background.draw(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT)
    row_y = 100 if facing == "RIGHT" else 0
    if state == "IDLE":
        row_y += 200
    character.clip_draw(frame * FRAME_SIZE, row_y, FRAME_SIZE, FRAME_SIZE, x, y, DRAW_WIDTH, DRAW_HEIGHT)
    update_canvas()


pressed_keys = set()
running = True
x = CANVAS_WIDTH / 2
y = CANVAS_HEIGHT / 2
facing = "RIGHT"
state = "IDLE"
frame = 0
animation_elapsed = 0.0

last_time = get_time()
while running:
    current_time = get_time()
    dt = current_time - last_time
    last_time = current_time
    handle_events()
    if not running:
        break
    update(dt)
    draw()
    delay(0.05)

close_canvas()

