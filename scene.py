import random
# Example 1

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_snow(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_smoke(canvas, scene_width, scene_height)
    draw_house(canvas, scene_width, scene_height)
    draw_fence(canvas, scene_width, scene_height)
    draw_snowman(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_fence(canvas, scene_width, scene_height):
    for i in range(0, scene_width, 24 ):
        h = 80
        draw_rectangle(canvas, i, 0, i+ 20, h, fill="gray")

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    

def draw_snowman(canvas, scene_width, scene_height):
    # for i in range(20):
    #     x = random.randint(150, 330)
    #     y = random.randint(150, 225)
    #     draw_oval(canvas, 1 + x, 1 + y, x + 50, y + 50, fill="white", outline="white")
    draw_oval(canvas, 225, 125, 300, 200, fill="white", outline="grey")
    draw_oval(canvas, 230, 185, 290, 235, fill="white", outline="grey")
    draw_oval(canvas, 240, 225, 280, 265, fill="white", outline="grey")
    draw_oval(canvas, 250, 250, 253, 253, fill="black", outline="black")
    draw_oval(canvas, 270, 250, 267, 253, fill="black", outline="black")
    #draw_oval(canvas, 270, 180, 230, 200, fill="black", outline="black")
    #draw_oval(canvas, 255, 220, 250, 220, fill="black", outline="black")
    #draw_oval(canvas, 255, 240, 255, 230, fill="black", outline="black")
    draw_polygon(canvas, 260, 250, 255, 245, 265, 245, fill ="orange", outline="orange")
    

def draw_snow(canvas, scene_width, scene_height):
    for i in range(700):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        draw_oval(canvas, 0 + x, 0 + y, x + 15, y + 15, fill="white", outline="white")

def draw_smoke(canvas, scene_width, scene_height):
    for i in range(8):
        x = random.randint(590, 610)
        y = random.randint(330, 450)
        radius = random.randint(10, 20)
        draw_oval(canvas, x - radius, y - radius, x + radius, y + radius, fill="grey", outline="grey")

def draw_clouds(canvas, scene_width, scene_height):
    draw_oval(canvas, 250, 400, 400, 475, fill ="snow1", outline="snow1")
    draw_oval(canvas, 300, 350, 500, 455, fill ="snow1", outline="snow1")
    draw_oval(canvas, 150, 370,300, 500, fill ="snow1", outline="snow1")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="white")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_house(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 700, 50, 400, 200, fill="olive")
    draw_line(canvas, 500, 200, 500, 0)
    draw_rectangle(canvas, 500, 200, 650, 300, fill="brown")
    draw_rectangle(canvas, 485, 50, 415, 150, fill="brown")
    draw_rectangle(canvas, 625, 50, 575, 125, fill="brown")
    draw_rectangle(canvas, 615, 275, 585, 325, fill="black")
    draw_rectangle(canvas, 565, 125, 515, 175, fill="blue")
    draw_rectangle(canvas, 680, 125, 635, 175, fill="blue")
    draw_rectangle(canvas, 560, 125, 515, 175, fill="blue")
    draw_polygon(canvas, 450, 300, 400, 200, 500, 200, fill="brown")
    draw_polygon(canvas, 650, 300, 650, 200, 700, 200, fill="brown")
    draw_polygon(canvas, 500, 200, 500, 300, 450, 300, fill="brown")
    draw_line(canvas, 500, 200, 500, 300, fill = "brown", width = 1)
    draw_line(canvas, 650, 200, 650, 300, fill = "brown", width = 1)
    

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)
main()