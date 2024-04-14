import os
import colorsys
from PIL import Image, ImageDraw, ImageFont

# Function to create the color representation
def create_color_image(text):
    # Define chromatic values for each letter of the Hebrew alphabet
    def generate_chromatic_values():
        chromatic_values = {}
        num_colors = 22
        hue_step = 360 / num_colors
        hue = 0
        for i, char in enumerate(hebrew_alphabet):
            chromatic_values[char] = colorsys.hsv_to_rgb(hue / 360, 1, 1)
            hue += hue_step
        return chromatic_values

    # Set up image parameters
    image_width = 36 * 100  # 36 inches * 100 pixels/inch
    image_height = 36 * 100  # 36 inches * 100 pixels/inch
    font_size = 55
    font_path = "/Users/iangonsher/PycharmProjects/pythonProject2/EZEKIEL_13_14/DrugulinCLM-Bold.ttf"
    font = ImageFont.truetype(font_path, font_size)
    margin = 20
    space_width = 55  # Width of white space between words

    # Generate chromatic values
    chromatic_values = generate_chromatic_values()

    # Create a blank image
    image = Image.new("RGB", (image_width, image_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Calculate the number of lines needed for each color
    num_colors = len(chromatic_values)
    lines_per_color = image_height // num_colors

    # Reverse the text to render from right to left
    text = text[::-1]

    # Draw the text with colors and rectangles
    x = margin
    for char in text.strip():
        if char == ' ':
            x += space_width  # Add white space between words
            continue

        if char in chromatic_values:
            color = tuple(int(c * 255) for c in chromatic_values[char])
            # Draw rectangle
            draw.rectangle([(x, 0), (x + font_size, image_height)], fill=color)
            # Draw text
            text_bbox = draw.textbbox((x, 0), char, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            draw.text((x + (font_size - text_width) // 2, (image_height - text_height) // 2), char, font=font,
                      fill=(255, 255, 255))
            # Move to the next position
            x += font_size

    # Save the image to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Specify DPI when saving
    dpi = 300
    image.save(os.path.join(desktop_path, "EZEKIEL1_13.jpg"), dpi=(dpi, dpi))

# Hebrew alphabet
hebrew_alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'

# Text to be represented
text = """
וּדְמ֨וּת הַחַיּ֜וֹת מַרְאֵיהֶ֣ם כְּגַחֲלֵי־אֵ֗שׁ בֹּֽעֲרוֹת֙ כְּמַרְאֵ֣ה הַלַּפִּדִ֔ים הִ֕יא מִתְהַלֶּ֖כֶת בֵּ֣ין הַחַיּ֑וֹת וְנֹ֣גַהּ לָאֵ֔שׁ וּמִן־הָאֵ֖שׁ יוֹצֵ֥א בָרָֽק׃ 



"""
# Create the color image
create_color_image(text)

# this works except that the colors might not be exactly right and it is not always dividing words properly