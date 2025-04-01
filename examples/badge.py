import badger2040
import jpegdec


# Global Constants
WIDTH = badger2040.WIDTH  # 296
HEIGHT = badger2040.HEIGHT  # 128
IMAGE_WIDTH = 128
LABEL_SIZE = 1
TEXT_SIZE = 3
LEFT_PADDING = 0
LABEL_TOP_PADDING = 0
LABEL_HEIGHT = LABEL_SIZE * 8
TEXT_HEIGHT = TEXT_SIZE * 8
ROW_HEIGHT = LABEL_HEIGHT + TEXT_HEIGHT

# Data to display
BADGE_PATH = "/badges/badge.txt"
DEFAULT_TEXT = """First
MyFirstName
Last
MyLastName
Company/Role
MyCompanyName
GitHub
MyGitHubHandle
/badges/badge.jpg
"""

# ------------------------------
#      Drawing functions
# ------------------------------


# Draw the badge, including user text
def draw_badge():
    display.set_pen(15)
    display.clear()

    # Draw badge image
    jpeg.open_file(badge_image)
    jpeg.decode(WIDTH - IMAGE_WIDTH, 0)

    # Set the font to be used for all the text
    display.set_pen(0)
    display.set_font("bitmap8")

    # Draw the first label and text
    display.text(
        label_one,
        LEFT_PADDING,
        LABEL_TOP_PADDING,
        WIDTH,
        LABEL_SIZE
    )
    display.text(
        text_one,
        LEFT_PADDING,
        LABEL_HEIGHT,
        WIDTH,
        TEXT_SIZE
    )

    # Draw the second label and text
    display.text(
        label_two,
        LEFT_PADDING,
        ROW_HEIGHT,
        WIDTH,
        LABEL_SIZE,
    )
    display.text(
        text_two,
        LEFT_PADDING,
        ROW_HEIGHT + LABEL_HEIGHT,
        WIDTH,
        TEXT_SIZE,
    )

    # Draw the third label and text
    display.text(
        label_three,
        LEFT_PADDING,
        ROW_HEIGHT * 2,
        WIDTH,
        LABEL_SIZE,
    )
    display.text(
        text_three,
        LEFT_PADDING,
        ROW_HEIGHT * 2 + LABEL_HEIGHT,
        WIDTH,
        TEXT_SIZE,
    )
    
    # Draw the fourth label and text
    display.text(
        label_four,
        LEFT_PADDING,
        ROW_HEIGHT * 3,
        WIDTH,
        LABEL_SIZE,
    )
    display.text(
        text_four,
        LEFT_PADDING,
        ROW_HEIGHT * 3 + LABEL_HEIGHT,
        WIDTH,
        TEXT_SIZE,
    )
    
    # Update the whole display
    display.update()


# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger and set it to update NORMAL
display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

jpeg = jpegdec.JPEG(display.display)

# Open the badge file
try:
    badge = open(BADGE_PATH, "r")
except OSError:
    with open(BADGE_PATH, "w") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
    badge = open(BADGE_PATH, "r")

# Read in the next 8 lines of labels and text
label_one = "First Name" 
text_one = badge.readline()  
label_two = "Last Name"
text_two = badge.readline()  
label_three = "Company"
text_three = badge.readline()  
label_four = "GitHub"
text_four = badge.readline()

# Read in the next line for the path to the image file
badge_image = "/badges/badge.jpg"

# ------------------------------
#       Main program
# ------------------------------

draw_badge()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()

