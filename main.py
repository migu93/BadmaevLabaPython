import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Click to Draw")

# Set the background color to white
screen.fill((255, 255, 255))

# Отрисовка линии по алгоритму Брезензема
def draw_line(screen, start, end, color):
    # Get the x and y coordinates of the start and end points
    x1, y1 = start
    x2, y2 = end

    # Calculate the differences between the start and end points
    dx = x2 - x1
    dy = y2 - y1

    # Determine the sign of the slope
    sx = 1 if dx > 0 else -1
    sy = 1 if dy > 0 else -1

    # Set the initial error
    err = dx - dy

    while True:
        # Draw the pixel at the current position
        pygame.draw.rect(screen, color, (x1, y1, 1, 1))

        # If the current position is the end point, exit the loop
        if x1 == x2 and y1 == y2:
            break

        # Calculate the new error
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy


# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        # Handle the quit event
        if event.type == pygame.QUIT:
            running = False

        # Handle left mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Draw a pixel at the mouse position
            pygame.draw.rect(screen, (0, 0, 0), (mouse_pos[0], mouse_pos[1], 1, 1))

    draw_line(screen, (100, 100), (300, 300), (0, 0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
