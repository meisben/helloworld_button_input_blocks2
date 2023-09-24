# If button A is pressed set the state variable to 0 
def on_button_pressed_a():
    global state
    state = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

# If button B is pressed set the state variable to 1
def on_button_pressed_b():
    global state
    state = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

# If button B has been pressed, then show a sad face. Otherwise show a happy face
def on_forever():
    if state == 1:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)

# Start the program, then run the forever loop
state = 0
basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)