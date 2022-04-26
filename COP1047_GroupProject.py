# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:23:04 2022

@author: iambi
@author: Gio
@author: Krister
"""


def menu():  #By iambi
    print("[1] Paper Rock Scissors")    #By Krister
    print("[2] Tic Tac Toe")            #By Krister
    print("[3] Snake")                  #By Gio
    print("[4] Pong")                   #By Gio
    print("[0] Exit the program. Or not, I have chocolate.")


# Or if you don't put the game code below, put it here with def option():

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        # do option 1 stuff
        print("Rock Paper Scissors Game")
        # imports
        import random
        import math


        def game_on():
            player = input("Please enter your move: 'r' for rock, 'p' for paper, 's' for scissors\n")
            player = player.lower()

            comp = random.choice(['r', 'p', 's'])

            if player == comp:
                return (0, player, comp)

            if winner(player, comp):
                return (1, player, comp)

            return (-1, player, comp)


        def winner(human_player, comp_player):
            if (human_player == 'r' and comp_player == 's') or (human_player == 's' and comp_player == 'p') or (
                    human_player == 'p' and comp_player == 'r'):
                return True
            return False


        def most_wins_of(w):
            human_player_wins = 0
            comp_player_wins = 0
            wins_needed = math.ceil(w / 2)
            while human_player_wins < wins_needed and comp_player_wins < wins_needed:
                score, player, comp = game_on()

                if score == 0:
                    print("You and the computer have tied the game.  We both choose {}. \n".format(player))

                elif score == 1:
                    human_player_wins += 1
                    print("You beat me! you picked {} and the computer picked {}\n".format(player, comp))

                else:
                    comp_player_wins += 1
                    print("You lost, HA! You picked {} and the computer picked {}\n".format(player, comp))

            if human_player_wins > comp_player_wins:
                print("You have won {} games! Give me another chance to beat you!".format(w))

            else:
                print("I finally Conquered you! You have lost {} games,  Sorry but not sorry".format(w))


        if __name__ == '__main__':
            most_wins_of(3)
        # This is where I will have to put the code for game 1.
    elif option == 2:
        # do option 2 stuff
        print("Tic Tac Toe Game")
        board = [

            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]

        ]

        # true x otherwise o
        player = True
        turns = 0


        def show_board(board):
            for row in board:
                for slot in row:
                    print(f"{slot} ", end="")
                print()


        show_board(board)


        def end_game(player_input):
            if player_input == "q":
                print("I hope you had a blast playing Tic-Tac-Toe.  See you soon.")
                return True
            else:
                return False


        def check_player_input(player_input):
            if not isitanumber(player_input):
                return False
            player_input = int(player_input)
            if not bounds(player_input):
                return False
            return True


        def isitanumber(player_input):
            if not player_input.isnumeric():
                print("This is not a numeric number")
                return False
            else:
                return True


        def bounds(player_input):
            if player_input > 9 or player_input < 1:
                print("This number is out of bounds")
                return False
            else:
                return True


        def istaken(coords, board):
            row = coords[0]
            col = coords[1]
            if board[row][col] != "-":
                print("This position is already taken")
                return True
            else:
                return False


        def coordinates(player_input):
            row = int(player_input / 3)
            col = player_input
            if col > 2: col = int(col % 3)
            return (row, col)


        def add_to_board(coords, board, active_player):
            row = coords[0]
            col = coords[1]
            board[row][col] = active_player


        def current_player(player):
            if player:
                return "x"
            else:
                return "o"


        def iswin(player, board):
            if check_row(player, board):
                return True
            if check_col(player, board):
                return True
            if check_diag(player, board):
                return True
            return False


        def check_row(player, board):
            for row in board:
                complete_row = True
                for slot in row:
                    if slot != player:
                        complete_row = False
                        break
                if complete_row:
                    return True
            return False


        def check_col(player, board):
            for col in range(3):
                complete_col = True
                for row in range(3):
                    if board[row][col] != player:
                        complete_col = False
                        break
                if complete_col:
                    return True
            return False


        def check_diag(player, board):
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            else:
                return False


        while turns < 9:
            active_player = current_player(player)
            show_board(board)
            player_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
            if end_game(player_input):
                break
            if not check_player_input(player_input):
                print("Please try once more")
                continue
            player_input = int(player_input) - 1
            coords = coordinates(player_input)
            if istaken(coords, board):
                print("Please try again.")
                continue
            add_to_board(coords, board, active_player)
            if iswin(active_player, board):
                print(f"{active_player.upper()} won!!")
                break

            turns += 1
            if turns == 9:
                print("Tie !!")
            player = not player

    elif option == 3:
    #MADE BY GIO
        import pygame, sys, random
        from pygame.math import Vector2


        class SNAKE:

            def __init__(self):
                self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
                self.direction = Vector2(0, 0)
                self.new_block = False

                self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
                self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
                self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
                self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

                self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
                self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
                self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
                self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

                self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
                self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

                self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
                self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
                self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
                self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
                self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

            def draw_snake(self):
                self.update_head_graphics()
                self.update_tail_graphics()

                for index, block in enumerate(self.body):
                    x_pos = int(block.x * cell_size)
                    y_pos = int(block.y * cell_size)
                    block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

                    if index == 0:
                        screen.blit(self.head, block_rect)

                    elif index == len(self.body) - 1:
                        screen.blit(self.tail, block_rect)
                    else:
                        previous_block = self.body[index + 1] - block
                        next_block = self.body[index - 1] - block
                        if previous_block.x == next_block.x:
                            screen.blit(self.body_vertical, block_rect)
                        elif previous_block.y == next_block.y:
                            screen.blit(self.body_horizontal, block_rect)
                        else:
                            if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                                screen.blit(self.body_tl, block_rect)
                            elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                                screen.blit(self.body_bl, block_rect)
                            elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                                screen.blit(self.body_tr, block_rect)
                            elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                                screen.blit(self.body_br, block_rect)

            def update_head_graphics(self):
                head_relation = self.body[1] - self.body[0]
                if head_relation == Vector2(1, 0):
                    self.head = self.head_left
                elif head_relation == Vector2(-1, 0):
                    self.head = self.head_right
                elif head_relation == Vector2(0, 1):
                    self.head = self.head_up
                elif head_relation == Vector2(0, -1):
                    self.head = self.head_down

            def update_tail_graphics(self):
                tail_relation = self.body[-2] - self.body[-1]
                if tail_relation == Vector2(1, 0):
                    self.tail = self.tail_left
                elif tail_relation == Vector2(-1, 0):
                    self.tail = self.tail_right
                elif tail_relation == Vector2(0, 1):
                    self.tail = self.tail_up
                elif tail_relation == Vector2(0, -1):
                    self.tail = self.tail_down

            def move_snake(self):
                if self.new_block == True:
                    body_copy = self.body[:]
                    body_copy.insert(0, body_copy[0] + self.direction)
                    self.body = body_copy[:]
                    self.new_block = False
                else:
                    body_copy = self.body[:-1]
                    body_copy.insert(0, body_copy[0] + self.direction)
                    self.body = body_copy[:]

            def add_block(self):
                self.new_block = True

            def play_crunch_sound(self):
                self.crunch_sound.play()

            def reset(self):
                self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
                self.direction = Vector2(0, 0)


        class FRUIT:
            def __init__(self):
                self.randomize()

            def draw_fruit(self):
                fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
                screen.blit(apple, fruit_rect)

            def randomize(self):
                self.x = random.randint(0, cell_number - 1)
                self.y = random.randint(0, cell_number - 1)
                self.pos = Vector2(self.x, self.y)


        class MAIN:
            def __init__(self):
                self.snake = SNAKE()
                self.fruit = FRUIT()

            def update(self):
                self.snake.move_snake()
                self.check_collison()
                self.check_fail()

            def draw_elements(self):
                self.draw_grass()
                self.fruit.draw_fruit()
                self.snake.draw_snake()
                self.draw_score()

            def check_collison(self):
                if self.fruit.pos == self.snake.body[0]:
                    self.fruit.randomize()
                    self.snake.add_block()
                    self.snake.play_crunch_sound()

                for block in self.snake.body[1:]:
                    if block == self.fruit.pos:
                        self.fruit.randomize()

            def check_fail(self):
                if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
                    self.game_over()

                for block in self.snake.body[1:]:
                    if block == self.snake.body[0]:
                        self.game_over()

            def game_over(self):
                self.snake.reset()

            def draw_grass(self):
                grass_color = (167, 209, 61)
                for row in range(cell_number):
                    if row % 2 == 0:
                        for col in range(cell_number):
                            if col % 2 == 0:
                                grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                                pygame.draw.rect(screen, grass_color, grass_rect)

                    else:
                        for col in range(cell_number):
                            if col % 2 != 0:
                                grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                                pygame.draw.rect(screen, grass_color, grass_rect)

            def draw_score(self):
                score_text = str(len(self.snake.body) - 3)
                score_surface = game_font.render(score_text, True, (56, 74, 12))
                score_x = int(cell_size * cell_number - 60)
                score_y = int(cell_size * cell_number - 40)
                score_rect = score_surface.get_rect(center=(score_x, score_y))
                apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
                bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                                      apple_rect.height)

                pygame.draw.rect(screen, (167, 209, 61), bg_rect)
                screen.blit(score_surface, score_rect)
                screen.blit(apple, apple_rect)
                pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        cell_size = 40
        cell_number = 20
        screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
        clock = pygame.time.Clock()
        apple = pygame.image.load('Graphics/apple.png').convert_alpha()
        game_font = pygame.font.Font('Graphics/PoetsenOne-Regular.ttf', 25)

        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)

        main_game = MAIN()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y != 1:
                            main_game.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y != -1:
                            main_game.snake.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x != 1:
                            main_game.snake.direction = Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x != -1:
                            main_game.snake.direction = Vector2(1, 0)

            screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)

    elif option == 4:
    #MADE BY GIO
        import pygame
        pygame.init()

        WIDTH, HEIGHT = 700, 500
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pong')

        FPS = 60

        WHITE = (255, 255, 255)
        AQUA = (69, 139, 116)
        BLACK = (0, 0, 0)

        PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
        BALL_RADIUS = 7

        SCORE_FONT = pygame.font.SysFont('comicsans', 50)
        WINNING_SCORE = 10

        class Paddle:
            COLOR = WHITE
            VEL = 4

            def __init__(self, x, y, width, height):
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.width = width
                self.height = height

            def draw(self, win):
                pygame.draw.rect(
                    win, self.COLOR, (self.x, self.y, self.width, self.height))

            def move(self, up=True):
                if up:
                    self.y -= self.VEL
                else:
                    self.y += self.VEL

            def reset(self):
                self.x = self.original_x
                self.y = self.original_y

        class Ball:
            MAX_VEL = 5
            COLOR = WHITE

            def __init__(self, x, y, radius):
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.radius = radius
                self.x_VEL = self.MAX_VEL
                self.y_VEL = 0

            def draw(self, win):
                pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

            def move(self):
                self.x += self.x_VEL
                self.y += self.y_VEL

            def reset(self):
                self.x = self.original_x
                self.y = self.original_y
                self.y_VEL = 0
                self.x_VEL *= -1

        def draw(win, paddles, ball, left_score, right_score):
            win.fill(AQUA)

            left_score_text = SCORE_FONT.render(f'{left_score}', 1, WHITE)
            right_score_text = SCORE_FONT.render(f'{right_score}', 1, WHITE)
            win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
            win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width() // 2, 20))

            for paddle in paddles:
                paddle.draw(win)

            for i in range(10, HEIGHT, HEIGHT//20):
                if i % 2 == 1:
                    continue
                pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

            ball.draw(win)
            pygame.display.update()

        def handle_collision(ball, left_paddle, right_paddle):
            if ball.y + ball.radius >= HEIGHT:
                ball.y_VEL *= -1
            elif ball.y - ball.radius <= 0:
                ball.y_VEL *= -1

            if ball.x_VEL < 0:
                if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                    if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                        ball.x_VEL *= -1

                        middle_y = left_paddle.y + left_paddle.height / 2
                        difference_in_y = middle_y - ball.y
                        reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                        y_VEL = difference_in_y / reduction_factor
                        ball.y_VEL = -1 * y_VEL

            else:
                if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                    if ball.x + ball.radius >= right_paddle.x:
                        ball.x_VEL *= -1

                        middle_y = right_paddle.y + right_paddle.height / 2
                        difference_in_y = middle_y - ball.y
                        reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                        y_VEL = difference_in_y / reduction_factor
                        ball.y_VEL = -1 * y_VEL


        def handle_paddle_movement(keys, left_paddle, right_paddle):
            if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
                left_paddle.move(up=True)
            if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
                left_paddle.move(up=False)

            if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
                right_paddle.move(up=True)
            if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
                right_paddle.move(up=False)

        def main():
            run = True
            clock = pygame.time.Clock()

            left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//
                                 2, PADDLE_WIDTH, PADDLE_HEIGHT)
            right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                                  2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
            ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

            left_score = 0
            right_score = 0

            while run:
                clock.tick(FPS)
                draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        break

                keys = pygame.key.get_pressed()
                handle_paddle_movement(keys, left_paddle, right_paddle)

                ball.move()
                handle_collision(ball, left_paddle, right_paddle)

                if ball.x < 0:
                    right_score += 1
                    ball.reset()
                elif ball.x > WIDTH:
                    left_score += 1
                    ball.reset()
                won = False
                if left_score >= WINNING_SCORE:
                    won = True
                    win_text = 'Player 1 Won!'
                elif right_score >= WINNING_SCORE:
                    won = True
                    win_text = 'Player 2 Won!'

                if won:
                    text = SCORE_FONT.render(win_text, 1, WHITE)
                    WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    ball.reset()
                    left_paddle.reset()
                    right_paddle.reset()
                    left_score = 0
                    right_score = 0

            pygame.quit()

        if __name__ == '__main__':
            main()


    else:
        print("The options were pretty clear and you still chose", option, ". why?")
    print()
    menu()
    option = int(input("Enter your option: "))

print("Don't leave me with the snake!!!")
