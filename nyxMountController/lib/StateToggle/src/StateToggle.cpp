#include "StateToggle.h"

StateToggle::StateToggle(uint8_t pin) : _pin(pin), _lastState(LOW) {
    pinMode(_pin, OUTPUT);
    digitalWrite(_pin, _lastState); // Ensure pin starts at LOW
}

void StateToggle::toggle() {
    _lastState = !_lastState;  // Flip the stored state
    digitalWrite(_pin, _lastState);

    if (Serial) {
        Serial.printf("Pin %d: %d\n", _pin, _lastState);
    }
}
