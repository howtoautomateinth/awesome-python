# Generator Python

Type of function, allowing us to generate a sequence of values over time

> yield statement instead of a return statement

while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.

## Key point

- resume their execution and state around the last point of value
- waits until the value is called for, no compute an entire series of values
  - no need to do a giant list anymore
  - save our memory

## Mechanism

using next() to go throught next value
