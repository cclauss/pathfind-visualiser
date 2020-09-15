import pygame

# Custom module imports
import board
import algorithms
from buttons import Button

# COLOURS
BUTTON1 = (0, 0, 0)  # Black
BUTTON2 = (255, 255, 255)  # White
BUTTON3 = (162, 162, 162)  # Silver
BG_LINE = (255, 255, 255)  # White
BG = (50, 50, 50)   # dark gray
BG2 = (100, 100, 100)  # white
OUTLINE_COLOUR = (0, 0, 0)  # black
TEXT_COLOUR = (0, 0, 0)  # Black

# FONTS
pygame.font.init()
title_font = pygame.font.SysFont("arial", 40, bold=True)
button_font = pygame.font.SysFont("arial", 30)
small_font = pygame.font.SysFont("arial", 20, bold=True)
tiny_font = pygame.font.SysFont("arial", 15)
tiny_bold_font = pygame.font.SysFont("arial", 15, bold=True)


# Extra Draw UI Functions -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def outline_rect(window, size, x, y, width, height):
    outline_colour = OUTLINE_COLOUR

    extra_size = size // 200

    pygame.draw.rect(window, outline_colour, (x - extra_size,
                                              y - extra_size,
                                              width + extra_size * 2,
                                              height + extra_size * 2
                                              ))


def draw_instructions(window, size):
    # Background
    bg_colour = BG2
    x = size // 20
    y = size // 10
    width = size // 2
    height = size * 17 // 40

    outline_rect(window, size, x, y, width, height)

    pygame.draw.rect(window, bg_colour, (x,
                                         y,
                                         width,
                                         height
                                         ))

    # DEFINE LABELS
    instructions_label = small_font.render("Instructions", 1, TEXT_COLOUR)

    line1 = tiny_font.render(
        "1. Look over the controls and key on the right.", 1, TEXT_COLOUR)

    line2 = tiny_font.render(
        "2. Choose which pathfinding algorithm you would like to", 1, TEXT_COLOUR)
    line3 = tiny_font.render(
        "     visualise down below. This will open another window.", 1, TEXT_COLOUR)

    line4 = tiny_font.render(
        "3. Choose a start and end point. This can be done by left", 1, TEXT_COLOUR)
    line5 = tiny_font.render(
        "      clicking any 2 nodes. Reset any node with a right click.", 1, TEXT_COLOUR)

    line6 = tiny_font.render(
        "4. Any further left clicks will change empty nodes into", 1, TEXT_COLOUR)
    line7 = tiny_font.render(
        "      barriers, which cannot be traversed.", 1, TEXT_COLOUR)

    line8 = tiny_font.render(
        "5. To visualise the pathfinding algorithm, press the spacebar.", 1, TEXT_COLOUR)
    line9 = tiny_font.render(
        "      Once it has finished, you can clear the board with the c", 1, TEXT_COLOUR)
    line10 = tiny_font.render(
        "      key, or just move the end or start points and run again.", 1, TEXT_COLOUR)
    line11 = tiny_font.render(
        "      Hit the esc key to return to the main menu.", 1, TEXT_COLOUR)

    # LABEL PLACEMENT
    window.blit(instructions_label, (x + size // 80, y + size // 80))

    window.blit(line1, (x + size // 80, y + size * 5 // 80))

    window.blit(line2, (x + size // 80, y + size * 8 // 80))
    window.blit(line3, (x + size // 80, y + size * 10 // 80))

    window.blit(line4, (x + size // 80, y + size * 13 // 80))
    window.blit(line5, (x + size // 80, y + size * 15 // 80))

    window.blit(line6, (x + size // 80, y + size * 18 // 80))
    window.blit(line7, (x + size // 80, y + size * 20 // 80))

    window.blit(line8, (x + size // 80, y + size * 23 // 80))
    window.blit(line9, (x + size // 80, y + size * 25 // 80))
    window.blit(line10, (x + size // 80, y + size * 27 // 80))
    window.blit(line11, (x + size // 80, y + size * 29 // 80))


def draw_key(window, size):
    # Background
    bg_colour = BG2

    x = size * 37 // 60
    y = size * 6 // 60
    width = size * 7 // 20
    height = size * 4 // 20

    outline_rect(window, size, x, y, width, height)

    pygame.draw.rect(window, bg_colour, (x,
                                         y,
                                         width,
                                         height
                                         ))

    # DEFINE LABELS
    key_label = small_font.render("Key", 1, TEXT_COLOUR)
    start_label = tiny_font.render("Start node", 1, TEXT_COLOUR)
    end_label = tiny_font.render("End node", 1, TEXT_COLOUR)
    barrier_label = tiny_font.render("Untraversable", 1, TEXT_COLOUR)
    open_label = tiny_font.render("Traversable", 1, TEXT_COLOUR)
    closed_label = tiny_font.render("Already traversed", 1, TEXT_COLOUR)
    path_label = tiny_font.render("Ideal path", 1, TEXT_COLOUR)
    # LABEL PLACEMENT
    # key
    window.blit(key_label, (x + size // 80, y + size // 80))
    # start
    window.blit(start_label, (x + size * 3 // 80, y + size * 4 // 80))
    # end
    window.blit(end_label, (x + size * 16 // 80, y + size * 4 // 80))
    # barrier
    window.blit(barrier_label, (x + size * 3 // 80, y + size * 8 // 80))
    # path
    window.blit(path_label, (x + size * 16 // 80, y + size * 8 // 80))
    # open
    window.blit(open_label, (x + size * 3 // 80, y + size * 12 // 80))
    # closed
    window.blit(closed_label, (x + size * 16 // 80, y + size * 12 // 80))

    # SQUARES
    # start
    pygame.draw.rect(window, board.START, (x + size // 80,
                                           y + size * 4 // 80,
                                           size // 50,
                                           size // 50
                                           ))
    # end
    pygame.draw.rect(window, board.END, (x + size * 14 // 80,
                                         y + size * 4 // 80,
                                         size // 50,
                                         size // 50
                                         ))
    # barrier
    pygame.draw.rect(window, board.BARRIER, (x + size // 80,
                                             y + size * 8 // 80,
                                             size // 50,
                                             size // 50
                                             ))
    # path
    pygame.draw.rect(window, board.PATH, (x + size * 14 // 80,
                                          y + size * 8 // 80,
                                          size // 50,
                                          size // 50
                                          ))
    # open
    pygame.draw.rect(window, board.OPEN, (x + size // 80,
                                          y + size * 12 // 80,
                                          size // 50,
                                          size // 50
                                          ))
    # closed
    pygame.draw.rect(window, board.CLOSED, (x + size * 14 // 80,
                                            y + size * 12 // 80,
                                            size // 50,
                                            size // 50
                                            ))


def draw_controls(window, size):
    # Background
    bg_colour = BG2

    x = size * 37 // 60
    y = size * 21 // 60
    width = size * 7 // 20
    height = size * 7 // 40

    outline_rect(window, size, x, y, width, height)

    pygame.draw.rect(window, bg_colour, (x,
                                         y,
                                         width,
                                         height
                                         ))
    # DEFINE LABELS
    controls_label = small_font.render("Controls", 1, TEXT_COLOUR)

    left1_label = tiny_bold_font.render("Left click:", 1, TEXT_COLOUR)
    left2_label = tiny_font.render("Change node", 1, TEXT_COLOUR)

    right1_label = tiny_bold_font.render("Right click:", 1, TEXT_COLOUR)
    right2_label = tiny_font.render("Reset node", 1, TEXT_COLOUR)

    c1_label = tiny_bold_font.render("C:", 1, TEXT_COLOUR)
    c2_label = tiny_font.render("Reset all nodes", 1, TEXT_COLOUR)

    space1_label = tiny_bold_font.render("Spacebar:", 1, TEXT_COLOUR)
    space2_label = tiny_font.render("Start algorithm", 1, TEXT_COLOUR)

    escape1_label = tiny_bold_font.render("Escape:", 1, TEXT_COLOUR)
    escape2_label = tiny_font.render("Return to menu", 1, TEXT_COLOUR)
    # LABEL PLACEMENT
    # title
    window.blit(controls_label, (x + size // 80, y + size // 80))
    # left click
    window.blit(left1_label, (x + size // 80, y + size * 4 // 80))
    window.blit(left2_label, (x + size * 10 // 80, y + size * 4 // 80))
    # right click
    window.blit(right1_label, (x + size // 80, y + size * 6 // 80))
    window.blit(right2_label, (x + size * 10 // 80, y + size * 6 // 80))
    # c
    window.blit(c1_label, (x + size // 80, y + size * 8 // 80))
    window.blit(c2_label, (x + size * 10 // 80, y + size * 8 // 80))
    # spacebar
    window.blit(space1_label, (x + size // 80, y + size * 10 // 80))
    window.blit(space2_label, (x + size * 10 // 80, y + size * 10 // 80))
    # escape
    window.blit(escape1_label, (x + size // 80, y + size * 12 // 80))
    window.blit(escape2_label, (x + size * 10 // 80, y + size * 12 // 80))


# Main Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def options_menu(window, size, rows):
    pass

def run_algorithms(window, size, rows, algorithm):

    grid = board.make_grid(rows, size)

    start = None
    end = None

    run = True
    # Keeps track of whether algorithm has been started, so user input can be disabled for its duration
    started = False

    while run:
        board.draw_board(window, grid, rows, size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            # If algorithm has started, does not allow the user to change nodes
            if started:
                continue

            # Changing nodes
            if pygame.mouse.get_pressed()[0]:  # left click
                pos = pygame.mouse.get_pos()
                row, col = board.get_clicked_position(pos, rows, size)
                node = grid[row][col]
                if not start and node != end and not node.is_hard_barrier:
                    start = node
                    start.make_start()
                elif not end and node != start and not node.is_hard_barrier:
                    end = node
                    end.make_end()
                elif node != end and node != start and not node.is_hard_barrier:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # right click
                pos = pygame.mouse.get_pos()
                row, col = board.get_clicked_position(pos, rows, size)
                node = grid[row][col]
                if not node.is_hard_barrier:
                    node.reset()

                    # Reset start and end if they are deleted
                    if node == start:
                        start = None
                    if node == end:
                        end = None

            if event.type == pygame.KEYDOWN:
                # Pressing c resets all nodes
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = board.make_grid(rows, size)

            # Starts the chosen algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end and not started:
                    # Prevents user from starting the search again while a search is underway
                    started = True
                    # Add neighbours to each node, not including barriers
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    # Which algorithm to use:
                    # Lambda function allows function with these perimeters to be called over and over without having to assign another function
                    # specifically to that
                    if algorithm == "a*":
                        algorithms.a_star_algorithm(lambda: board.draw_board(window, grid,
                                                                             rows, size), grid, start, end)

                    if algorithm == "breadth first":
                        algorithms.breadth_first_search(lambda: board.draw_board(window, grid,
                                                                                 rows, size), grid, start, end)

                    if algorithm == "depth first":
                        algorithms.depth_first_search(lambda: board.draw_board(window, grid,
                                                                               rows, size), grid, start, end)

                    if algorithm == "dijkstra's":
                        algorithms.dijkstras(lambda: board.draw_board(window, grid,
                                                                      rows, size), grid, start, end)

                    if algorithm == "best-first":
                        algorithms.best_first(lambda: board.draw_board(window, grid,
                                                                       rows, size), grid, start, end)

                    # Reset started variable so that user can again give commands
                    started = False


def main(window, size, rows):
    # Variable to check if the left mouse button has been pressed
    clicked = False

    # Will contain all the buttons, so they can be looped through in a for loop
    buttons = []

    # DEFINE LABELS
    # Title
    choose_label = title_font.render(
        "Algorithms:", 1, TEXT_COLOUR)
    # How to use
    usage_label = title_font.render("How to use:", 1, TEXT_COLOUR)

    # DEFINE BUTTONS
    # A* pathfinding algorithm
    a_star_button = Button(BUTTON1,
                           BUTTON2,
                           size // 20,
                           size * 25 // 40,
                           size * 7 // 16,
                           size // 15,
                           lambda: run_algorithms(window, size, rows, "a*"),
                           text='A* algorithm',
                           )
    buttons.append(a_star_button)
    # Breadth first search algorithm
    breadth_first_button = Button(BUTTON1,
                                  BUTTON2,
                                  size // 20,
                                  size * 28 // 40,
                                  size * 7 // 16,
                                  size // 15,
                                  lambda: run_algorithms(
                                      window, size, rows, "breadth first"),
                                  text='Breadth first search',
                                  )
    buttons.append(breadth_first_button)
    # Depth first search algorithm
    depth_first_button = Button(BUTTON1,
                                BUTTON2,
                                size // 20,
                                size * 31 // 40,
                                size * 7 // 16,
                                size // 15,
                                lambda: run_algorithms(
                                    window, size, rows, "depth first"),
                                text='Depth first search',
                                )
    buttons.append(depth_first_button)
    # Dijkstra's shortest path algorithm
    dijkstra_button = Button(BUTTON1,
                             BUTTON2,
                             size // 20,
                             size * 34 // 40,
                             size * 7 // 16,
                             size // 15,
                             lambda: run_algorithms(
                                 window, size, rows, "dijkstra's"),
                             text="Dijkstra's algorithm",
                             )
    buttons.append(dijkstra_button)
    # Greedy best-first search algorithm
    best_first_button = Button(BUTTON1,
                               BUTTON2,
                               size // 20,
                               size * 37 // 40,
                               size * 7 // 16,
                               size // 15,
                               lambda: run_algorithms(
                                   window, size, rows, "best-first"),
                               text="Greedy best-first search",
                               )
    buttons.append(best_first_button)

    run = True
    while run:
        window.fill(BG)

        draw_instructions(window, size)
        draw_key(window, size)
        draw_controls(window, size)

        # Labels
        window.blit(choose_label, (size // 20,
                                   size * 22 // 40
                                   ))
        window.blit(usage_label, (size // 20, size // 40))

        # Buttons
        xpos, ypos = pygame.mouse.get_pos()
        for button in buttons:
            button.draw(window, button_font, xpos, ypos)

            if button.is_selected(xpos, ypos):
                if clicked:
                    button.on_clicked()
        # Reset clicked value
        clicked = False

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                clicked = True

        pygame.display.update()


if __name__ == "__main__":
    # Pygame Window
    # Window will always be a square so size used instead of width and height
    SIZE = 800
    ROWS = 50

    WIN = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("Pathfinding Algorithms Visualiser")

    main(WIN, SIZE, ROWS)
