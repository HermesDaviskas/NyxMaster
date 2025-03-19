#ifndef STATE_TOGGLE_H
#define STATE_TOGGLE_H

#include <Arduino.h>

class StateToggle {
public:
    explicit StateToggle(uint8_t pin);
    void toggle();

private:
    uint8_t _pin;
    bool _lastState; // Store the last known pin state
};

#endif // STATE_TOGGLE_H
