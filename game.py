from browser import document, timer

canvas = document["game"]
ctx = canvas.getContext("2d")

# Position du carré
x, y = 200, 200

def draw():
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.fillStyle = "blue"
    ctx.fillRect(x, y, 50, 50)

# Déplacement avec la souris
def on_mouse_move(ev):
    global x, y
    rect = canvas.getBoundingClientRect()
    x = ev.clientX - rect.left - 25
    y = ev.clientY - rect.top - 25

# Déplacement avec le doigt (mobile)
def on_touch_move(ev):
    global x, y
    rect = canvas.getBoundingClientRect()
    touch = ev.touches[0]
    x = touch.clientX - rect.left - 25
    y = touch.clientY - rect.top - 25
    ev.preventDefault()  # Empêche le scroll

canvas.bind("mousemove", on_mouse_move)
canvas.bind("touchmove", on_touch_move)

# Boucle du jeu (60 fps)
timer.set_interval(draw, 1000//60)