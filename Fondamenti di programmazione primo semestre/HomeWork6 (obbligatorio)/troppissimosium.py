import images
import time
start_img = "./data/input_03.png"
position = [1, 20]
commands = "S S E E E E E N N N N N E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E E N N N N N N N N N N N N N N N N N N E N N N N N N N N E E E E E S S E S S E S E S S S SE SE SE SE SE SE SE SE SE NE NE NE SE NE SE NE NE NE NE NE N NE NE NE N N N N E E E E S S S S S S S S S S S S S S S W N E SW NW E S SE W E E SE SE NE W E S S E SE N SW W SE N SE S NE NE W S NE S E NW S NE N E E E NE S SE W W E S W SE E N NE S SW E SW W NW E SE N NE S S SW S SW N NW NE E N N NE SW S SE E NW NE NE NW S SE W SW SE W SE E S W N N S SW SW SW S NE E E N N S SE N NW W E NE NE S W SW N E W S W NW S S NE S E S NW SE N W SE S SE NE S N SW W SW S NE W N SW NE SE NW W S W SW SW E SE SE S NE W S W W SE NE S NW NE E S E SW S NW SE SE S N W NE NE N W W NW E W NW SE S S S S NW W SW N W S N NE N NW S S NW E SW E E N W NW W S W E W W SE SE NE SW W SW SW SE N NE N W W S N SE SE S S S SE W SE SE SW N SW NE W SW E NW SE SW SW SW SE NW SE S W NE W SW S E W W N S E S SW E N NW SW S E S W E S SE N SE E SW E SE S SW SW SE E SW NW S W SW N SE SW S E E E N SE SE N S S NE N SW SW E S W E E S NW NW E W SW SE W NE SE E NE S E N W NW W SE S NE W SW N S NW NW NW SE NE W SW NW S SW NW SW SW SW S E S NE SW W S W E E S N S N E S W SE NW W S NW S NW SE W S NE SE E NE SE SE SE S SE SE N E NE NE S SW N NW N S N SW SE S S SE W E E NE E S NW N E W W S N N E SE W S E S S E S SE S S E N E NW N W N N SE S SW S NE S W SE W NW SW E NW SW SE NW SW W NE NW NE NW N NW S NE NE S S NE E N NW N W S W SW W W E S S E SW S W NE SW N S S S S SW SE S W E SE W NE S E S W W S W S NE N W N S S E W W SE SW S SE E SW S S SW NW E NE S S NW E SW S N NW NE W W E E S NE S NE S SE N N S S NW N NW SW E S SE S NE E NE SE NW S W SW SE NE NW S SE N NW SW E SE N SE S SE W N E W S S W SW N NW SW SE SE E N SW S NW NE N SW S SW NW S E E S N W E E NW E W S N S SE SE E NW W S NE S NW SE N W S E NW SW N S W E S SW SE E E NE NW S SW S SW S W SE SW NW E SW NW E NE NE NE N E NE N W S S SE S S NE N E SE W N E S S NW S NE NE SE N W S NW NE W SW N S NE W E S S S W SW N S W N W W SW NE NW S N SE N E NW N SE S E N SE N S N SW E N SE N NE E N E E NE SW NW N NE S NE NE NE SE SE E W W N SW N N S S E E S N S E E W N S NW W S S SE S N SW S W SW NE S SW SE SW S SE N SW S NW S W W E S E S S NE S S N S NE S SE NW SE S SW S S NW NW S E NW S SE SE SE SE NW N SW NE E S N NE S NW W S W W S N S S NW NW S S NW SW S E SE SW S SW NW N NW SW S"
out_img = "./output/output_end_03.png"


def draw_pixel(img, x, y, colore):
    L, A = len(img[0]), len(img)
    if 0 <= x < L and 0 <= y < A:
        x = int(round(x))
        y = int(round(y))
        img[y][x] = colore


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img, commands, snakelen, nextmove, all_positions = images.load(start_img), commands.split(), 1, 0, [position]
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    while nextmove < len(commands) and position not in all_positions[-snakelen:-1] and position != (0, 255, 0): 
        #time.sleep(0.1)
        input()
        images.save(img, out_img)
        command = commands[nextmove]
        draw_pixel(img, all_positions[-snakelen][0], all_positions[-snakelen][1], (128, 128, 128))
        position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        if position[0] < 0:
            position[0] = len(img[0]) - 1
        elif position[0] >= len(img[0]):
            position[0] = 0
        if position[1] < 0:
            position[1] = len(img) - 1
        elif position[1] >= len(img):
            position[1] = 0
        if img[position[1]][position[0]] == (255, 128, 0):
            snakelen += 1
        draw_pixel(img, position[0], position[1], (0, 255, 0))
        all_positions.append(position)
        nextmove += 1
        #command = commands[nextmove]
        #position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]

    if img[all_positions[-1][1]][all_positions[-1][0]] == (255, 0, 0):
        all_positions.remove(all_positions[-1])
    nextmove = len(all_positions) - snakelen
    #images.save(img, out_img)
    return snakelen

generate_snake(start_img, position, commands, out_img)