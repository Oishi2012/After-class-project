import pygame

# Start Pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Program")

# Colors
PINK = (255, 192, 203)
BLUE = (0, 0, 255)
BG_COLOR = (100, 150, 200)

# Font
font = pygame.font.SysFont(None, 40)


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


class Quiz:

    def __init__(self):

        self.questions = [

            "What is the capital of Bangladesh?",

            "How many sides does a triangle have?",

            "Which language is used to style a webpage?"

        ]

        self.options = [

            ["Dhaka", "London", "Paris"],

            ["3", "4", "5"],

            ["HTML", "CSS", "Python"]

        ]

        self.answers = [

            "Dhaka",

            "3",

            "CSS"

        ]

        self.score = 0


    def quiz(self):

        for question_number in range(len(self.questions)):

            print(self.questions[question_number])

            print("1.", self.options[question_number][0])

            print("2.", self.options[question_number][1])

            print("3.", self.options[question_number][2])

            answer = input("Enter your answer: ")

            if answer == self.answers[question_number]:

                self.score += 1


        return self.score


# Create Quiz
quiz_game = Quiz()


# Create buttons
button_one = Button("", 50, 350, 200, 100)

button_two = Button("", 300, 350, 200, 100)

button_three = Button("", 550, 350, 200, 100)


# Game loop
running = True

question_number = 0

result = ""

user_answer = ""


while running:

    # Background color
    screen.fill(BG_COLOR)


    if question_number < len(quiz_game.questions):

        # Show question
        question_text = font.render(

            quiz_game.questions[question_number],

            True,

            BLUE

        )

        screen.blit(question_text, (50, 100))


        # Show options
        button_one.text = quiz_game.options[question_number][0]

        button_two.text = quiz_game.options[question_number][1]

        button_three.text = quiz_game.options[question_number][2]


        button_one.draw()

        button_two.draw()

        button_three.draw()


    else:

        # Show final score
        result_text = font.render(

            "Final Score: " + str(quiz_game.score),

            True,

            BLUE

        )

        screen.blit(result_text, (250, 250))


    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()


            # User answer
            if button_one.is_clicked(mouse_pos):

                user_answer = quiz_game.options[question_number][0]


            elif button_two.is_clicked(mouse_pos):

                user_answer = quiz_game.options[question_number][1]


            elif button_three.is_clicked(mouse_pos):

                user_answer = quiz_game.options[question_number][2]


            # Compare answer
            if user_answer:

                if user_answer == quiz_game.answers[question_number]:

                    quiz_game.score += 1


                question_number += 1

                user_answer = ""


    pygame.display.update()


pygame.quit()