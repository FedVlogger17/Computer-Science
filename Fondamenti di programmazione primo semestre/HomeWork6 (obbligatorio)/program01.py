#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Siete stati appena ingaggiati in una software house di videogiochi e
dovete renderizzare su immagine il giochino dello snake salvando
l'immagine finale del percorso dello snake e restituendo la lunghezza
dello snake.
Si implementi la funzione generate_snake che prende in ingresso un
percorso di un file immagine, che e' l'immagine di partenza
"start_img" che puo' contenere pixel di background neri, pixel di
ostacolo per lo snake di colore rosso e infine del cibo di colore
arancione. Lo snake deve essere disegnato di verde. Inoltre bisogna
disegnare in grigio la scia che lo snake lascia sul proprio
cammino. La funzione inoltre prende in ingresso una posizione iniziale
dello snake, "position" come una lista di due interi X e Y. I comandi
del giocatore su come muovere lo snake nel videogioco sono disponibili
in una stringa "commands".  La funzione deve salvare l'immagine finale
del cammino dello snake al percorso "out_img", che e' passato come
ultimo argomento di ingresso alla funzione. Inoltre la funzione deve
restituire la lunghezza dello snake al termine del gioco.

Ciascun comando in "commands" corrisponde ad un segno cardinale ed e
seguito da uno spazio. I segni cardinali possibli sono:

| NW | N | NE |
| W  |   | E  |
| SW | S | SE |

che corrispondono a movimenti dello snake di un pixel come:

| alto-sinistra  | alto  | alto-destra  |
| sinistra       |       | destra       |
| basso-sinistra | basso | basso-destra |

Lo snake si muove in base ai comandi passati e nel caso in cui
mangia del cibo si allunga di un pixel.

Lo snake puo' passare da parte a parte dell'immagine sia in
orizzontale che in verticale. Il gioco termina quando sono finiti i
comandi oppure lo snake muore. Lo snake muore quando:
- colpisce un ostacolo
- colpisce se stesso quindi non puo' passare sopra se stesso
- si incrocia in diagonale in qualsiasi modo. Ad esempio, un percorso
  1->2->3-4 come quello sotto a sinistra non e' lecito mentre quello a
  destra sotto va bene.

  NOT OK - diagonal cross        OK - not a diagonal cross
       | 4 | 2 |                    | 1 | 2 |
       | 1 | 3 |                    | 4 | 3 |

Ad esempio considerando il caso di test data/input_00.json
lo snake parte da "position": [12, 13] e riceve i comandi
 "commands": "S W S W W W S W W N N W N N N N N W N" 
genera l'immagine in visibile in data/expected_end_00.png
e restituisce 5 in quanto lo snake e' lungo 5 pixels alla
fine del gioco.

NOTA: analizzate le immagini per avere i valori esatti dei colore da usare.

NOTA: non importate o usate altre librerie
'''


import images


def check_diagonal_cross(all_positions, position, nextmove, command, moveset, img):
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    print(f"current command: {command}")
    if img[all_positions[-1][1] + diagonals[command][0]][all_positions[-1][0]] == (0, 255, 0) and img[all_positions[-1][1]][all_positions[-1][0] + diagonals[command][1]] == (0, 255, 0):
        img[position[1]][position[0]] = (0, 255, 0)
        return False
    return True


def check_bordeless(position, img):
    checked = 0
    if position[0] < 0:
        position[0] = len(img[0]) - 1
        checked = 1
    elif position[0] >= len(img[0]):
        position[0] = 0
        checked = 1
    if position[1] < 0:
        position[1] = len(img) - 1
        checked = 1
    elif position[1] >= len(img):
        position[1] = 0
        checked = 1
    return position, checked


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
    img, commands, snakelen, nextmove, all_positions = images.load(start_img), commands.split(), 1, 0, [position]
    moveset = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1)}
    diagonals = {'NE': (-1, 1), 'NW': (-1, -1), 'SE': (-1, 1), 'SW': (-1, -1)}
    img[position[1]][position[0]] = (128, 128, 128)
    command = commands[nextmove]
    position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
    nextmove += 1
    all_positions.append(position)
    while nextmove < len(commands):
        #time.sleep(0.2)
        #input()
        if img[position[1]][position[0]] == (0, 255, 0) or img[position[1]][position[0]] == (255, 0, 0):
            break
        command = commands[nextmove]
        if command in diagonals.keys() and supercheck == 0:
            if not check_diagonal_cross(all_positions, position, nextmove, command, moveset, img):
                break
        img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (128, 128, 128)
        img[position[1]][position[0]] = (0, 255, 0)
        position = [position[0] + moveset[command][0], position[1] + moveset[command][1]]
        position, supercheck = check_bordeless(position, img)
        print(position)
        supercheck = check_bordeless(position, img)
        if img[position[1]][position[0]] == (255, 128, 0):
            snakelen += 1
        all_positions.append(position)
        images.save(img, out_img)
        nextmove += 1
    if img[position[1]][position[0]] == (0, 0, 0):
    #    img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (128, 128, 128)
        img[position[1]][position[0]] = (0, 255, 0)
        img[all_positions[-snakelen - 1][1]][all_positions[-snakelen - 1][0]] = (128, 128, 128)
    images.save(img, out_img)
    return snakelen