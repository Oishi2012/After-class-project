import pygame
import random

# Start Pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dice Rolling Simulator")

# Colors
PINK = (255, 192, 203)
BLUE = (0, 0, 255)
BG_COLOR = (100, 150, 200)

# Font
font = pygame.font.SysFont(None, 60)

# Dice sides
dice_sides = ["1", "2", "3", "4", "5", "6"]


class Button:

    def __init__(self, text, x, y, width, height):

        self.rect = pygame.Rect(x, y, width, height)

        self.text = text


    def draw(self):

        pygame.draw.rect(screen, PINK, self.rect)

        text_surface = font.render(self.text, True, BLUE)

        text_rect = text_surface.get_rect(center=self.rect.center)

        screen.blit(text_surface, text_rect)


    def is_clicked(self, pos):

        return self.rect.collidepoint(pos)


# Create buttons
roll_button = Button("Roll Dice", 100, 450, 200, 100)

yes_button = Button("Yes", 350, 450, 150, 100)

no_button = Button("No", 550, 450, 150, 100)


# Game loop
running = True

dice_result = ""

ask_again = False


while running:

    # Background color
    screen.fill(BG_COLOR)


    # Draw buttons
    if ask_again == False:

        roll_button.draw()

    else:

        yes_button.draw()

        no_button.draw()


    # Show dice result
    result_text = font.render(dice_result, True, BLUE)

    result_rect = result_text.get_rect(center=(400, 250))

    screen.blit(result_text, result_rect)


    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()


            # Roll the dice
            if ask_again == False and roll_button.is_clicked(mouse_pos):

                dice_number = random.randint(1, 6)

                dice_result = "Dice Side: " + str(dice_number)

                ask_again = True


            # Roll again
            elif ask_again == True and yes_button.is_clicked(mouse_pos):

                dice_number = random.randint(1, 6)

                dice_result = "Dice Side: " + str(dice_number)


            # Stop rolling
            elif ask_again == True and no_button.is_clicked(mouse_pos):

                dice_result = "Thank you for playing!"

                ask_again = False


    pygame.display.update()


pygame.quit()