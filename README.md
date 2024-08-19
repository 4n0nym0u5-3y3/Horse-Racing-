# Horse Racing Animation

This project is a simple horse racing animation created using Python's `turtle` graphics module. The animation features four horses racing on a track, with a finish line and a display announcing the winner.

## Features

- Four animated horses racing towards a finish line.
- Track and starting positions for the horses.
- Winner announcement displaying the name and color of the winning horse.
- Simple and interactive graphics.

## Requirements

- `turtle` module (included with Python's standard library)


2. **Ensure Python is Installed**

   Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Run the Script**

   Navigate to the directory containing the `horse_racing_updated.py` file and run the script using Python:

   ```sh
   python horse_racing_updated.py
   ```

2. **Interact with the Animation**

   - The turtle graphics window will open, displaying the race.
   - The horses will race across the screen, and the winner will be announced once a horse crosses the finish line.

## Code Overview

- **`setup_screen()`**: Initializes the turtle graphics window.
- **`draw_finish_line()`**: Draws the finish line on the track.
- **`draw_track()`**: Draws the track with markers for starting positions.
- **`create_horses()`**: Creates and positions the horses on the track.
- **`move_horse(horse)`**: Moves each horse forward by a random distance.
- **`race(horses)`**: Handles the racing logic and announces the winner.
- **`main()`**: Orchestrates the setup, drawing, and racing.


## Acknowledgements

- [Python Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html) for the turtle graphics library.
- Inspiration and guidance from various Python tutorials and documentation.


Happy racing!
