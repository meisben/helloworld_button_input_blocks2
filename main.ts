// If button A is pressed set the state variable to 0
input.onButtonPressed(Button.A, function () {
    state = 0
})
// If button B is pressed set the state variable to 1
input.onButtonPressed(Button.B, function () {
    state = 1
})
let state = 0
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    if (state == 1) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
