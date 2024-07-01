import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Be a Frog")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
gold = (255, 223, 0)

# Player properties
player_size = 50
player_x = 100
player_y = screen_height - player_size - 100
player_speed = 5
player_jump_speed = 18  
gravity = 1
jump = False
jump_speed = 30  

# Obstacle properties
obstacle_speed = 5
obstacle_width = 30  
obstacle_height = 30  
obstacles = []

# Coin properties
coin_size = 20
coins = []

# Timer
clock = pygame.time.Clock()
score = 0
high_score = 0
coins_collected = 0

def create_obstacle():
    obstacle_type = random.choice(['ground', 'floating'])
    if obstacle_type == 'ground':
        obstacle = [screen_width, screen_height - obstacle_height - 100, obstacle_width, obstacle_height]
    else:
        obstacle = [screen_width, random.randint(screen_height // 2, screen_height - 200), obstacle_width, obstacle_height]
    return obstacle

def create_coin():
    coin_y = random.randint(screen_height // 2, screen_height - 200)
    coin = [screen_width, coin_y, coin_size, coin_size]
    return coin

def draw_background():
    for y in range(screen_height):
        color = (y * 255 // screen_height, y * 255 // screen_height, 255)
        pygame.draw.line(screen, color, (0, y), (screen_width, y))

def draw_restart_button():
    font = pygame.font.Font(None, 74)
    text = font.render("Restart", True, black)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 7 + 50))
    screen.blit(text, text_rect)
    return text_rect

def draw_game_over_screen(score, high_score, coins_collected):
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Game Over", True, black)
    game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2 - 80))
    screen.blit(game_over_text, game_over_rect)

    score_text = font.render(f"Score: {score}", True, black)
    score_rect = score_text.get_rect(center=(screen_width / 2, screen_height / 5 -70))
    screen.blit(score_text, score_rect)

    coins_text = font.render(f"Coins: {coins_collected}", True, black)
    coins_rect = coins_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    screen.blit(coins_text, coins_rect)

def game_loop():
    global player_y, jump, jump_speed, obstacles, coins, score, high_score, coins_collected
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not jump:
            jump = True
            jump_speed = player_jump_speed

        # Player movement
        if jump:
            player_y -= jump_speed
            jump_speed -= gravity
            if jump_speed < -player_jump_speed:
                jump = False
                jump_speed = player_jump_speed
        else:
            player_y = min(player_y + gravity, screen_height - player_size - 100)

        # Obstacle movement
        for obstacle in obstacles:
            obstacle[0] -= obstacle_speed
        if not obstacles or obstacles[-1][0] < screen_width - 200:
            obstacles.append(create_obstacle())

        # Coin movement
        for coin in coins:
            coin[0] -= obstacle_speed
        if not coins or coins[-1][0] < screen_width - 200:
            coins.append(create_coin())

        # Remove obstacles that have left the screen
        obstacles = [obs for obs in obstacles if obs[0] > -obs[2]]
        coins = [coin for coin in coins if coin[0] > -coin[2]]

        # Collision detection for obstacles
        for obstacle in obstacles:
            if player_x + player_size > obstacle[0] and player_x < obstacle[0] + obstacle[2] and \
               player_y + player_size > obstacle[1] and player_y < obstacle[1] + obstacle[3]:
                running = False

        # Collision detection for coins
        for coin in coins:
            if player_x + player_size > coin[0] and player_x < coin[0] + coin[2] and \
               player_y + player_size > coin[1] and player_y < coin[1] + coin[3]:
                coins.remove(coin)
                coins_collected += 1

        # Draw background
        draw_background()

        # Draw player
        pygame.draw.rect(screen, green, (player_x, player_y, player_size, player_size))

        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, red, obstacle)

        # Draw coins
        for coin in coins:
            pygame.draw.rect(screen, gold, coin)

        # Display score and coins collected
        score += 1
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, (10, 10))

        coins_text = font.render(f"Coins: {coins_collected}", True, black)
        screen.blit(coins_text, (10, 50))

        # Update display
        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

    if score > high_score:
        high_score = score
    return score

def main():
    global player_y, jump, jump_speed, obstacles, coins, score, high_score, coins_collected
    while True:
        score = game_loop()
        screen.fill(white)
        draw_game_over_screen(score, high_score, coins_collected)
        text_rect = draw_restart_button()
        pygame.display.flip()

        restart = False
        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_rect.collidepoint(event.pos):
                        restart = True
                        player_y = screen_height - player_size - 100
                        jump = False
                        jump_speed = 30
                        obstacles = []
                        coins = []
                        score = 0
                        coins_collected = 0

main()
