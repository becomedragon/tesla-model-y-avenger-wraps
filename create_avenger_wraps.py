#!/usr/bin/env python3
"""
Create Tesla Model Y custom wraps with Avengers themes
- Iron Man theme: Red and Gold with arc reactor
- Captain America theme: Red, White, Blue with star
"""

from PIL import Image, ImageDraw, ImageFont
import math

def create_iron_man_wrap(size=1024):
    """Create Iron Man themed wrap"""
    # Create image with metallic red background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Metallic red background gradient
    for i in range(size):
        alpha = int(255 * (i / size))
        color = (180 + i//5, 20, 10, 255)
        draw.rectangle([(0, i), (size, i+1)], fill=color)

    # Gold accents - angular panels
    gold_color = (218, 165, 32)
    # Side panels
    draw.polygon([(0, size//3), (size//4, size//2), (size//3, size), (0, size)], fill=(200, 150, 20))
    draw.polygon([(size, size//3), (size*3//4, size//2), (size*2//3, size), (size, size)], fill=(200, 150, 20))

    # Arc reactor circle in center (chest area)
    center_x, center_y = size // 2, size // 2
    reactor_radius = size // 6

    # Outer glow
    for r in range(reactor_radius + 50, reactor_radius, -5):
        alpha = int(255 * (1 - (r - reactor_radius) / 50))
        draw.ellipse([(center_x - r, center_y - r), (center_x + r, center_y + r)],
                     fill=(0, 100, 255, alpha // 4))

    # Main reactor circle
    draw.ellipse([(center_x - reactor_radius, center_y - reactor_radius),
                  (center_x + reactor_radius, center_y + reactor_radius)],
                 fill=(50, 150, 255), outline=(200, 200, 255), width=5)

    # Inner triangle
    triangle_size = reactor_radius // 2
    draw.polygon([
        (center_x, center_y - triangle_size),
        (center_x - triangle_size * 0.866, center_y + triangle_size * 0.5),
        (center_x + triangle_size * 0.866, center_y + triangle_size * 0.5)
    ], fill=(200, 220, 255))

    # Gold tech lines
    draw.line([(center_x - reactor_radius - 30, center_y), (center_x + reactor_radius + 30, center_y)],
              fill=(218, 165, 32), width=8)
    draw.line([(center_x, center_y - reactor_radius - 30), (center_x, center_y + reactor_radius + 30)],
              fill=(218, 165, 32), width=8)

    # Add "STARK" text at bottom
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
    except:
        font = ImageFont.load_default()

    text = "STARK"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (size - text_width) // 2
    text_y = size - 120
    draw.text((text_x, text_y), text, fill=(218, 165, 32), font=font, stroke_width=2, stroke_fill=(0, 0, 0))

    return img

def create_captain_america_wrap(size=1024):
    """Create Captain America themed wrap"""
    # Create image
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Base - Navy blue background
    draw.rectangle([(0, 0), (size, size)], fill=(0, 35, 102))

    # Concentric circles for the shield
    center_x, center_y = size // 2, size // 2
    shield_radius = size // 3

    # White outer ring
    draw.ellipse([(center_x - shield_radius, center_y - shield_radius),
                  (center_x + shield_radius, center_y + shield_radius)],
                 fill=(255, 255, 255))

    # Red ring
    red_radius = int(shield_radius * 0.8)
    draw.ellipse([(center_x - red_radius, center_y - red_radius),
                  (center_x + red_radius, center_y + red_radius)],
                 fill=(200, 16, 46))

    # White ring
    white_radius = int(shield_radius * 0.6)
    draw.ellipse([(center_x - white_radius, center_y - white_radius),
                  (center_x + white_radius, center_y + white_radius)],
                 fill=(255, 255, 255))

    # Red ring
    red_radius2 = int(shield_radius * 0.4)
    draw.ellipse([(center_x - red_radius2, center_y - red_radius2),
                  (center_x + red_radius2, center_y + red_radius2)],
                 fill=(200, 16, 46))

    # Blue center
    blue_radius = int(shield_radius * 0.2)
    draw.ellipse([(center_x - blue_radius, center_y - blue_radius),
                  (center_x + blue_radius, center_y + blue_radius)],
                 fill=(0, 35, 102))

    # White star in center
    star_points = []
    for i in range(10):
        angle = math.radians(-90 + i * 36)
        radius = blue_radius * 0.9 if i % 2 == 0 else blue_radius * 0.5
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        star_points.append((x, y))

    draw.polygon(star_points, fill=(255, 255, 255), outline=(200, 200, 200), width=2)

    # Add wings on sides (abstract)
    wing_color = (200, 180, 140)
    for y in range(size//3, 2*size//3, 20):
        # Left wing
        draw.polygon([
            (0, y),
            (size//5, y - 20),
            (size//5, y + 20)
        ], fill=wing_color)
        # Right wing
        draw.polygon([
            (size, y),
            (size*4//5, y - 20),
            (size*4//5, y + 20)
        ], fill=wing_color)

    # Add stripes at top and bottom
    stripe_height = size // 10
    for i in range(5):
        y_pos = i * stripe_height
        color = (200, 16, 46) if i % 2 == 0 else (255, 255, 255)
        draw.rectangle([(0, y_pos), (size, y_pos + stripe_height)], fill=color)

        y_pos_bottom = size - (i + 1) * stripe_height
        draw.rectangle([(0, y_pos_bottom), (size, y_pos_bottom + stripe_height)], fill=color)

    # Add "AVENGERS" text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica-Bold.ttc", 100)
    except:
        font = ImageFont.load_default()

    text = "AVENGERS"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (size - text_width) // 2
    text_y = size // 2 + shield_radius + 50
    draw.text((text_x, text_y), text, fill=(200, 200, 200), font=font, stroke_width=3, stroke_fill=(0, 35, 102))

    return img

def main():
    """Create both wraps and save them"""
    print("Creating Iron Man wrap...")
    iron_man = create_iron_man_wrap(1024)
    iron_man.save('iron_man_wrap.png', 'PNG', optimize=True)
    print(f"✓ Iron Man wrap saved (size: {len(iron_man.tobytes())} bytes)")

    print("\nCreating Captain America wrap...")
    cap_america = create_captain_america_wrap(1024)
    cap_america.save('captain_america_wrap.png', 'PNG', optimize=True)
    print(f"✓ Captain America wrap saved (size: {len(cap_america.tobytes())} bytes)")

    print("\n✅ Both wraps created successfully!")
    print("Files: iron_man_wrap.png, captain_america_wrap.png")

if __name__ == "__main__":
    main()
