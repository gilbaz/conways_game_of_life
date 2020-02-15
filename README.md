# conways_game_of_life

Here is a quick implementation of Conway's Game of Life

(I made this in 2 hours just for fun, feel free to continue dev on it!)

Wiki:

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

High-level Intro to Conway's Game of Life:

https://www.youtube.com/watch?v=Aq51GfPmD54

Idea:
* The game is a zero-player game, meaning that its evolution is determined by its initial state. 
* One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 
* It is Turing complete and can simulate a universal constructor or any other Turing machine.

Rules:

At each step in time, the following transitions occur:
* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Conway's Criteria:

* There should be no explosive growth.
* There should exist small initial patterns with chaotic, unpredictable outcomes.
* There should be potential for von Neumann universal constructors.
* The rules should be as simple as possible, whilst adhering to the above constraints

Play-list showcasing some interesting "life-forms":

https://www.youtube.com/playlist?list=PL_DEGJtvl7wtPc-ZyTq_jh0ptRjnYGaWZ

Conway himself:

https://www.youtube.com/watch?v=R9Plq-D1gEk

REQUIRES:
* Python 3.5 + 
* numpy
* matplotlib

