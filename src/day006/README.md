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
