import os
import random

from actor import Actor
from artifact import Artifact
from cast import Cast

from director import Director

from keyboard_service import KeyboardService
from video_service import VideoService

from color import Color
from point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "\\messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    score = 0
    # create the banner
    banner = Actor()
    banner.set_text(score)
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(585)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    robot.set_score(0)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()
    
    count = 1
    for n in range(DEFAULT_ARTIFACTS):
      
        

        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x,y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        y2= random.randint(5,15)
        velocity = Point(0,y2)
    
        selector = random.randint(0,1) 
        if selector == 0:
            text = 'G'
            gem = Artifact()
            gem.set_text(text)
            gem.set_font_size(FONT_SIZE)
            gem.set_color(color)
            gem.set_position(position)
            gem.set_score(100)
            gem.set_velocity(velocity)
            cast.add_actor("artifacts", gem)
        if selector == 1:
            rock = Artifact()
            text = 'R'
            rock.set_text(text)
            rock.set_font_size(FONT_SIZE)
            rock.set_color(color)
            rock.set_position(position)
            rock.set_score(-75)
            rock.set_velocity(velocity)
    
            cast.add_actor("artifacts", rock)
        count += 1
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()