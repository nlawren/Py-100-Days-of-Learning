# DAY 6 - While loops and functions

## Description

* Functions
* How to use
* using functions in a module
* Using the following website [reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
* Using the range(n) function in a for loop to mimic other languages for loop functions

```python
 for hurdle in range(6):
    jump()
```

## Task 6.3 Hurdles using a while loop

Reeborg code:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
```

## Task 6.4 More Hurdles and While loops

Hurdles race 3
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position and number of hurdles changes each time this world is reloaded.
What you need to know

* The functions move() and turn_left().
* The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
* How to use a while loop and an if statement.

Your program should also be valid for worlds Hurdles 1 and Hurdles 2.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()
```

## Task 6.5 Hurdles and Loops with variable heights

Hurdles race 4
Reeborg has entered a hurdle race. Make him run the course, following the path shown.

The position, the height and the number of hurdles changes each time this world is reloaded.

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    wall_height = 1
    turn_left()
    move()
    while wall_on_right():
        wall_height += 1
        move()
    turn_right()
    move()
    turn_right()
    for descend in range(wall_height):
        move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()
```
