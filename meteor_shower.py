# Meteor Shower by
# Max Sundell
# Created on: 2015 August 24
# Version 1.0

# Music by Jan125 (http://opengameart.org/content/stereotypical-90s-space-shooter-music)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Imports
import pygame
import random
import sys

# Version Number
version = 2.0

# Initialize PyGame
pygame.init()

# Color Variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 220, 0)
red_ = (200, 20, 20)
green_ = (20, 200, 20)

# Read Settings From File
res_w_txt = open("game_data/settings/res_w.txt", "r").read()
res_h_txt = open("game_data/settings/res_h.txt", "r").read()
fps_txt = open("game_data/settings/fps.txt", "r").read()
fullscreen_txt = open("game_data/settings/fullscreen.txt", "r").read()
mute_txt = open("game_data/settings/mute.txt", "r").read()

# Resolution Variables
res_w = int(res_w_txt)
res_h = int(res_h_txt)
fps_ = int(fps_txt)

if fullscreen_txt == "True":
    screen = pygame.display.set_mode((res_w, res_h), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
else:
    screen = pygame.display.set_mode((res_w, res_h))

# Set Caption
pygame.display.set_caption("Meteor Shower " + str(version))

# Set Icon
icon = pygame.image.load("game_data/icon.png")
pygame.display.set_icon(icon)

# FPS Variable
fps = pygame.time.Clock()

# Load Ships
ship_r = pygame.image.load("game_data/ships/1_ship_r.png")
ship_g = pygame.image.load("game_data/ships/2_ship_g.png")
ship_b = pygame.image.load("game_data/ships/3_ship_b.png")
ship_ye = pygame.image.load("game_data/ships/4_ship_y.png")
ship_t = pygame.image.load("game_data/ships/5_ship_t.png")
ship_p = pygame.image.load("game_data/ships/6_ship_p.png")

# Load Comets
comet_1 = pygame.image.load("game_data/comets/1_comet.png")
comet_2 = pygame.image.load("game_data/comets/2_comet.png")
comet_3 = pygame.image.load("game_data/comets/3_comet.png")
comet_4 = pygame.image.load("game_data/comets/4_comet.png")
comet_5 = pygame.image.load("game_data/comets/5_comet.png")

# Load Crash Sounds
crash_sound1 = pygame.mixer.Sound("game_data/crash/1.wav")
crash_sound2 = pygame.mixer.Sound("game_data/crash/2.wav")
crash_sound3 = pygame.mixer.Sound("game_data/crash/3.wav")
crash_sound4 = pygame.mixer.Sound("game_data/crash/4.wav")
crash_sound5 = pygame.mixer.Sound("game_data/crash/5.wav")

crash_sound1.set_volume(.75)
crash_sound2.set_volume(.75)
crash_sound3.set_volume(.75)
crash_sound4.set_volume(.75)
crash_sound5.set_volume(.75)

main_font = "game_data/visitor.ttf"

pause = False

# Music
if mute_txt == "False":
    pygame.mixer.music.load("game_data/intro.wav")
    pygame.mixer.music.play(-1)
elif mute_txt == "True":
    pass


# Score Counter
def score_counter(score):
    text = pygame.font.Font(main_font, 30)
    textsurf, textrect = text_objects("Score: " + str(score), text)
    textrect.center = ((res_w / 2), 15)
    screen.blit(textsurf, textrect)


# Text Objects (Center Text)
def text_objects(text, font):
    textsurface = font.render(text, True, white)
    return textsurface, textsurface.get_rect()


# Text Objects Yellow (Center Text)
def text_objects_y(text, font):
    textsurface = font.render(text, True, yellow)
    return textsurface, textsurface.get_rect()


# Text Objects GREEN (Center Text)
def text_objects_r(text, font):
    textsurface = font.render(text, True, red_)
    return textsurface, textsurface.get_rect()


# Text Objects RED (Center Text)
def text_objects_g(text, font):
    textsurface = font.render(text, True, green_)
    return textsurface, textsurface.get_rect()


def unpause():
    global pause
    if mute_txt == "False":
        pygame.mixer.music.unpause()
    elif mute_txt == "True":
        pass

    pause = False


def paused():
    if mute_txt == "False":
        pygame.mixer.music.pause()
    elif mute_txt == "True":
        pass

    # Main Loop
    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    unpause()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        # Draws "Paused" to the Screen
        text = pygame.font.Font(main_font, 100)
        textsurf, textrect = text_objects("Paused", text)
        textrect.center = ((res_w / 2), 90)
        screen.blit(textsurf, textrect)

        # Draws "Press SPACE to Continue..." to the Screen
        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = text_objects("Press SPACE to Continue...", text)
        textrect.center = ((res_w / 2), (res_h / 2))
        screen.blit(textsurf, textrect)

        # Draws "Press SPACE to Restart!" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Press ESC to go to Main Menu", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 40))
        screen.blit(textsurf, textrect)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.update()


# Main Menu
def main_menu():
    # Scrolling Background PART 1
    background = "game_data/starfield.png"
    if res_h == 1080:
        background = "game_data/starfield.png"

    if res_h == 1440:
        background = "game_data/starfield1440.png"

    if res_h == 768:
        background = "game_data/starfield768.png"
    b_1 = pygame.image.load(background).convert()
    b_2 = pygame.image.load(background).convert()
    scroll = 0

    # Red / Green Mute
    if mute_txt == "True":
        rg_fs_ = text_objects_r

    else:
        rg_fs_ = text_objects_g

    # Main Loop
    while True:

        # Scrolling Background PART 2
        screen.blit(b_1, (0, scroll))
        screen.blit(b_2, (0, scroll - res_h))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_s:
                    settings()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_m:

                    if rg_fs_ == text_objects_g:
                        rg_fs_ = text_objects_r
                        res_w_write = open("game_data/settings/mute.txt", "w")
                        res_w_write.write("True")
                        res_w_write.close()

                    elif rg_fs_ == text_objects_r:
                        rg_fs_ = text_objects_g
                        res_w_write = open("game_data/settings/mute.txt", "w")
                        res_w_write.write("False")
                        res_w_write.close()

        scroll += .5
        if scroll == res_h:
            scroll = 0

        # Draws "Meteor Shower" to the Screen
        text = pygame.font.Font(main_font, 100)
        textsurf, textrect = text_objects("Meteor Shower", text)
        textrect.center = ((res_w / 2), 90)
        screen.blit(textsurf, textrect)

        # Draws "by Max Sundell" to the Screen
        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = text_objects("By Max Sundell", text)
        textrect.center = ((res_w / 2), 140)
        screen.blit(textsurf, textrect)

        # Draws "Press SPACE to Start..." to the Screen
        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = text_objects("Press SPACE to Start...", text)
        textrect.center = ((res_w / 2), (res_h / 2))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 40)
        textsurf, textrect = text_objects_y("CONTROLS:", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 50))
        screen.blit(textsurf, textrect)

        # Draws Controls to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_y("Move: W/S/A/D", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 90))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_y("Quit: ESC", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 110))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_y("Pause: P", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 150))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = rg_fs_("Audio: M", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 170))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_y("Resolution: S", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 210))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_r("(changes apply after restart)", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 250))
        screen.blit(textsurf, textrect)

        # Draws "Version: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Version: " + str(version), text)
        textrect.center = ((res_w / 2), 15)
        screen.blit(textsurf, textrect)

        # Draws "FPS: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("FPS: " + str(fps)[11:16], text)
        textrect.center = ((res_w / 2), 40)
        screen.blit(textsurf, textrect)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.flip()


# TODO Restart Program When User Changes Resolution and Audio Settings
# Settings
def settings():
    # Scrolling Background PART 1
    background = "game_data/starfield.png"
    if res_h == 1080:
        background = "game_data/starfield.png"

    if res_h == 1440:
        background = "game_data/starfield1440.png"

    if res_h == 768:
        background = "game_data/starfield768.png"
    b_1 = pygame.image.load(background).convert()
    b_2 = pygame.image.load(background).convert()
    scroll = 0

    # Red / Green Fullscreen
    if fullscreen_txt == "True":
        rg_fs = text_objects_g

    else:
        rg_fs = text_objects_r

    if res_h_txt == "768":
        rg_fs2 = text_objects_g
    else:
        rg_fs2 = text_objects_r

    if res_h_txt == "1080":
        rg_fs3 = text_objects_g
    else:
        rg_fs3 = text_objects_r

    if res_h_txt == "1440":
        rg_fs4 = text_objects_g
    else:
        rg_fs4 = text_objects_r

    # Main Loop
    while True:

        # Scrolling Background PART 2
        screen.blit(b_1, (0, scroll))
        screen.blit(b_2, (0, scroll - res_h))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    rg_fs2 = text_objects_g
                    rg_fs3 = text_objects_r
                    rg_fs4 = text_objects_r
                    res_w_write = open("game_data/settings/res_w.txt", "w")
                    res_w_write.write("1366")
                    res_w_write.close()

                    res_h_write = open("game_data/settings/res_h.txt", "w")
                    res_h_write.write("768")
                    res_h_write.close()

                if event.key == pygame.K_2:
                    rg_fs2 = text_objects_r
                    rg_fs3 = text_objects_g
                    rg_fs4 = text_objects_r
                    res_w_write = open("game_data/settings/res_w.txt", "w")
                    res_w_write.write("1920")
                    res_w_write.close()

                    res_h_write = open("game_data/settings/res_h.txt", "w")
                    res_h_write.write("1080")
                    res_h_write.close()

                if event.key == pygame.K_3:
                    rg_fs2 = text_objects_r
                    rg_fs3 = text_objects_r
                    rg_fs4 = text_objects_g
                    res_w_write = open("game_data/settings/res_w.txt", "w")
                    res_w_write.write("2560")
                    res_w_write.close()

                    res_h_write = open("game_data/settings/res_h.txt", "w")
                    res_h_write.write("1440")
                    res_h_write.close()

                if event.key == pygame.K_4:

                    if rg_fs == text_objects_r:
                        rg_fs = text_objects_g
                        res_w_write = open("game_data/settings/fullscreen.txt", "w")
                        res_w_write.write("True")
                        res_w_write.close()

                    elif rg_fs == text_objects_g:
                        rg_fs = text_objects_r
                        res_w_write = open("game_data/settings/fullscreen.txt", "w")
                        res_w_write.write("False")
                        res_w_write.close()

                if event.key == pygame.K_RETURN:
                    main_menu()

        scroll += .5
        if scroll == res_h:
            scroll = 0

        # Draws "Settings" to the Screen
        text = pygame.font.Font(main_font, 80)
        textsurf, textrect = text_objects("Resolution:", text)
        textrect.center = ((res_w / 2), (res_h / 2 - 150))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs2("1) 1366 x 768", text)
        textrect.center = ((res_w / 2), (res_h / 2 - 75))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs3("2) 1920 x 1080", text)
        textrect.center = ((res_w / 2), (res_h / 2))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs4("3) 2560 x 1440", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 75))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs("4) FULLSCREEN", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 150))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("(Press ENTER To Continue...)", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 225))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_r("(changes apply after restart)", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 250))
        screen.blit(textsurf, textrect)

        # Draws "Version: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Version: " + str(version), text)
        textrect.center = ((res_w / 2), 15)
        screen.blit(textsurf, textrect)

        # Draws "FPS: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("FPS: " + str(fps)[11:16], text)
        textrect.center = ((res_w / 2), 40)
        screen.blit(textsurf, textrect)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.flip()


# Settings 2
# TODO Time-Based Movement
'''
def settings2():
    # Scrolling Background PART 1
    background = "game_data/starfield.png"
    if res_h == 1080:
        background = "game_data/starfield.png"

    if res_h == 1440:
        background = "game_data/starfield1440.png"

    if res_h == 768:
        background = "game_data/starfield768.png"
    b_1 = pygame.image.load(background).convert()
    b_2 = pygame.image.load(background).convert()
    scroll = 0

    if fps_txt == "30":
        rg_fs5 = text_objects_g
    else:
        rg_fs5 = text_objects_r

    if fps_txt == "60":
        rg_fs6 = text_objects_g
    else:
        rg_fs6 = text_objects_r

    if fps_txt == "120":
        rg_fs7 = text_objects_g
    else:
        rg_fs7 = text_objects_r

    # Main Loop
    while True:

        # Scrolling Background PART 2
        screen.blit(b_1, (0, scroll))
        screen.blit(b_2, (0, scroll - res_h))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    rg_fs5 = text_objects_g
                    rg_fs6 = text_objects_r
                    rg_fs7 = text_objects_r
                    res_h_write = open("game_data/settings/fps.txt", "w")
                    res_h_write.write("30")
                    res_h_write.close()

                if event.key == pygame.K_2:
                    rg_fs5 = text_objects_r
                    rg_fs6 = text_objects_g
                    rg_fs7 = text_objects_r
                    res_h_write = open("game_data/settings/fps.txt", "w")
                    res_h_write.write("60")
                    res_h_write.close()

                if event.key == pygame.K_3:
                    rg_fs5 = text_objects_r
                    rg_fs6 = text_objects_r
                    rg_fs7 = text_objects_g
                    res_h_write = open("game_data/settings/fps.txt", "w")
                    res_h_write.write("120")
                    res_h_write.close()

                if event.key == pygame.K_RETURN:
                    main_menu()

        scroll += .5
        if scroll == res_h:
            scroll = 0

        # Draws "Settings" to the Screen
        text = pygame.font.Font(main_font, 100)
        textsurf, textrect = text_objects("Settings", text)
        textrect.center = ((res_w / 2), 90)
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 80)
        textsurf, textrect = text_objects("FPS Cap:", text)
        textrect.center = ((res_w / 2), (res_h / 2 - 150))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs5("1) 30 FPS", text)
        textrect.center = ((res_w / 2), (res_h / 2 - 75))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs6("2) 60 FPS", text)
        textrect.center = ((res_w / 2), (res_h / 2))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = rg_fs7("3) 120 FPS", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 75))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("(Press ENTER To Continue...)", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 150))
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects_r("(changes apply after restart)", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 175))
        screen.blit(textsurf, textrect)

        # Draws "Version: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Version: " + str(version), text)
        textrect.center = ((res_w / 2), 15)
        screen.blit(textsurf, textrect)

        # Draws "FPS: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("FPS: " + str(fps)[11:16], text)
        textrect.center = ((res_w / 2), 40)
        screen.blit(textsurf, textrect)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.flip()'''


# Game Loop
def game_loop():
    global pause
    # Scrolling Background PART 1
    background = "game_data/starfield.png"
    if res_h == 1080:
        background = "game_data/starfield.png"

    if res_h == 1440:
        background = "game_data/starfield1440.png"

    if res_h == 768:
        background = "game_data/starfield768.png"
    b_1 = pygame.image.load(background).convert()
    b_2 = pygame.image.load(background).convert()
    scroll = 0

    # Ship Variables
    ship_x = (res_w / 2 - 32)
    ship_y = (res_h - 96)

    change_x = 0
    change_y = 0

    # Color Generator
    colornum = random.randrange(0, 5)
    ship_color = [ship_r, ship_g, ship_b, ship_ye, ship_t, ship_p]
    ship_w = 64
    comet_w = 150

    # Crash Generator
    crashnum = random.randrange(0, 4)
    crash_sound_ = [crash_sound1, crash_sound2, crash_sound3, crash_sound4, crash_sound5]

    # Comet Variables 1
    comet_x = random.randrange(-64, res_w - 64)
    comet_y = -600
    comet_speed = 5

    # Comet Variables 2
    comet_x_2 = random.randrange(-64, res_w - 64)
    comet_y_2 = -1200
    comet_speed_2 = 5

    # Comet Variables 3
    comet_x_3 = random.randrange(-64, res_w - 64)
    comet_y_3 = -1800
    comet_speed_3 = 5

    # Comet Variables 4
    comet_x_4 = random.randrange(-64, res_w - 64)
    comet_y_4 = -2400
    comet_speed_4 = 5

    # Comet Variables 5
    comet_x_5 = random.randrange(-64, res_w - 64)
    comet_y_5 = -3000
    comet_speed_5 = 5

    score = 0

    # Music
    if mute_txt == "False":
        pygame.mixer.music.load("game_data/level1.wav")
        pygame.mixer.music.play(-1)
    elif mute_txt == "True":
        pass

    # Main Loop
    while True:

        # Scrolling Background PART 2
        screen.blit(b_1, (0, scroll))
        screen.blit(b_2, (0, scroll - res_h))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # TODO FIX BUG WHEN USING BOTH ARROW KEYS AND W/S/A/D
            # Moves Ship UP AND DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_y += -10
                if event.key == pygame.K_DOWN:
                    change_y += 10
                # W / S
                if event.key == pygame.K_w:
                    change_y += -10
                if event.key == pygame.K_s:
                    change_y += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    change_y += 10
                if event.key == pygame.K_DOWN:
                    change_y += -10
                # W / S
                if event.key == pygame.K_w:
                    change_y += 10
                if event.key == pygame.K_s:
                    change_y += -10

            # Moves Ship LEFT AND RIGHT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x += -10
                if event.key == pygame.K_RIGHT:
                    change_x += 10
                # A / D
                if event.key == pygame.K_a:
                    change_x += -10
                if event.key == pygame.K_d:
                    change_x += 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    change_x += 10
                if event.key == pygame.K_RIGHT:
                    change_x += -10
                # A / D
                if event.key == pygame.K_a:
                    change_x += 10
                if event.key == pygame.K_d:
                    change_x += -10

                if event.key == pygame.K_p:
                    pause = True
                    paused()

        ship_x += change_x
        ship_y += change_y

        scroll += 1
        if scroll == res_h:
            scroll = 0

        if res_h == 1080:
            # Collision RIGHT
            if ship_x > res_w - 64:
                ship_x = res_w - 64
            # Collision LEFT
            if ship_x <= -1:
                ship_x = 0

            # Collision DOWN
            if ship_y > res_h - 64:
                ship_y = 1080 - 64
            # Collision UP
            if ship_y <= -1:
                ship_y = 0

        if res_h == 1440:
            # Collision RIGHT
            if ship_x > res_w - 64:
                ship_x = res_w - 64
            # Collision LEFT
            if ship_x <= -1:
                ship_x = 0

            # Collision DOWN
            if ship_y > res_h - 64:
                ship_y = 1440 - 64
            # Collision UP
            if ship_y <= -1:
                ship_y = 0

        if res_h == 768:
            # Collision RIGHT
            if ship_x > res_w - 64:
                ship_x = res_w - 64
            # Collision LEFT
            if ship_x <= 0:
                ship_x = 0

            # Collision DOWN
            if ship_y > res_h - 64:
                ship_y = 768 - 64
            # Collision UP
            if ship_y <= -1:
                ship_y = 0

        # Draws Ship RANDOM
        screen.blit(ship_color[colornum], (ship_x, ship_y))

        # Draw Comets
        screen.blit(comet_1, (comet_x, comet_y))
        screen.blit(comet_2, (comet_x_2, comet_y_2))
        screen.blit(comet_3, (comet_x_3, comet_y_3))
        screen.blit(comet_4, (comet_x_4, comet_y_4))
        screen.blit(comet_5, (comet_x_5, comet_y_5))

        # Comet Logic
        comet_y += comet_speed
        comet_y_2 += comet_speed_2
        comet_y_3 += comet_speed_3
        comet_y_4 += comet_speed_4
        comet_y_5 += comet_speed_5

        if comet_y > res_h:
            comet_y = 0 - 256
            comet_x = random.randrange(-64, res_w - -64)
            comet_speed += 1

            score += 1

        if comet_y_2 > res_h:
            comet_y_2 = 0 - 256
            comet_x_2 = random.randrange(-64, res_w - 64)
            comet_speed_2 += 1

            score += 1

        if comet_y_3 > res_h:
            comet_y_3 = 0 - 256
            comet_x_3 = random.randrange(-64, res_w - 64)
            comet_speed_3 += 1

            score += 1

        if comet_y_4 > res_h:
            comet_y_4 = 0 - 256
            comet_x_4 = random.randrange(-64, res_w - 64)
            comet_speed_4 += 1

            score += 1

        if comet_y_5 > res_h:
            comet_y_5 = 0 - 256
            comet_x_5 = random.randrange(-64, res_w - 64)
            comet_speed_5 += 1

            score += 1

        # Comet Collision with Ship
        if comet_y < ship_y < comet_y + comet_w or comet_y < ship_y + ship_w < comet_y + comet_w:

            if comet_x < ship_x < comet_x + comet_w or comet_x < ship_x + ship_w < comet_x + comet_w:
                # Write Score to game_data/score_file.txt
                if mute_txt == "False":
                    pygame.mixer.Sound.play(crash_sound_[crashnum])
                elif mute_txt == "True":
                    pass

                score_text = str(score)
                score_file = open("game_data/score_file.txt", "w")
                score_file.write(score_text)
                score_file.close()

                high_score_file_r = open("game_data/high_score_file.txt", "r").read()
                if int(high_score_file_r) < score:
                    high_score_file = open("game_data/high_score_file.txt", "w")
                    high_score_file.write(score_text)
                    high_score_file.close()
                    print(high_score_file_r)

                game_over()
        # Comet 2
        if comet_y_2 < ship_y < comet_y_2 + comet_w or comet_y_2 < ship_y + ship_w < comet_y_2 + comet_w:

            if comet_x_2 < ship_x < comet_x_2 + comet_w or comet_x_2 < ship_x + ship_w < comet_x_2 + comet_w:
                # Write Score to game_data/score_file.txt
                if mute_txt == "False":
                    pygame.mixer.Sound.play(crash_sound_[crashnum])
                elif mute_txt == "True":
                    pass

                score_text = str(score)
                score_file = open("game_data/score_file.txt", "w")
                score_file.write(score_text)
                score_file.close()

                high_score_file_r = open("game_data/high_score_file.txt", "r").read()
                if int(high_score_file_r) < score:
                    high_score_file = open("game_data/high_score_file.txt", "w")
                    high_score_file.write(score_text)
                    high_score_file.close()
                    print(high_score_file_r)

                game_over()
        # Comet 3
        if comet_y_3 < ship_y < comet_y_3 + comet_w or comet_y_3 < ship_y + ship_w < comet_y_3 + comet_w:

            if comet_x_3 < ship_x < comet_x_3 + comet_w or comet_x_3 < ship_x + ship_w < comet_x_3 + comet_w:
                # Write Score to game_data/score_file.txt
                if mute_txt == "False":
                    pygame.mixer.Sound.play(crash_sound_[crashnum])
                elif mute_txt == "True":
                    pass

                score_text = str(score)
                score_file = open("game_data/score_file.txt", "w")
                score_file.write(score_text)
                score_file.close()

                high_score_file_r = open("game_data/high_score_file.txt", "r").read()
                if int(high_score_file_r) < score:
                    high_score_file = open("game_data/high_score_file.txt", "w")
                    high_score_file.write(score_text)
                    high_score_file.close()
                    print(high_score_file_r)

                game_over()
        # Comet 4
        if comet_y_4 < ship_y < comet_y_4 + comet_w or comet_y_4 < ship_y + ship_w < comet_y_4 + comet_w:

            if comet_x_4 < ship_x < comet_x_4 + comet_w or comet_x_4 < ship_x + ship_w < comet_x_4 + comet_w:
                # Write Score to game_data/score_file.txt
                if mute_txt == "False":
                    pygame.mixer.Sound.play(crash_sound_[crashnum])
                elif mute_txt == "True":
                    pass

                score_text = str(score)
                score_file = open("game_data/score_file.txt", "w")
                score_file.write(score_text)
                score_file.close()

                high_score_file_r = open("game_data/high_score_file.txt", "r").read()
                if int(high_score_file_r) < score:
                    high_score_file = open("game_data/high_score_file.txt", "w")
                    high_score_file.write(score_text)
                    high_score_file.close()
                    print(high_score_file_r)

                game_over()
        # Comet 5
        if comet_y_5 < ship_y < comet_y_5 + comet_w or comet_y_5 < ship_y + ship_w < comet_y_5 + comet_w:

            if comet_x_5 < ship_x < comet_x_5 + comet_w or comet_x_5 < ship_x + ship_w < comet_x_5 + comet_w:
                # Write Score to game_data/score_file.txt
                if mute_txt == "False":
                    pygame.mixer.Sound.play(crash_sound_[crashnum])
                elif mute_txt == "True":
                    pass

                score_text = str(score)
                score_file = open("game_data/score_file.txt", "w")
                score_file.write(score_text)
                score_file.close()

                high_score_file_r = open("game_data/high_score_file.txt", "r").read()
                if int(high_score_file_r) < score:
                    high_score_file = open("game_data/high_score_file.txt", "w")
                    high_score_file.write(score_text)
                    high_score_file.close()
                    print(high_score_file_r)

                game_over()

        # Draws "FPS: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("FPS: ", text)
        textrect.center = (43, 15)
        screen.blit(textsurf, textrect)

        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects(str(fps)[11:16], text)
        textrect.center = (120, 15)
        screen.blit(textsurf, textrect)

        # Draw Score
        score_counter(score)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.flip()


# Game Over
def game_over():
    # Scrolling Background PART 1
    background = "game_data/starfield.png"
    if res_h == 1080:
        background = "game_data/starfield.png"

    if res_h == 1440:
        background = "game_data/starfield1440.png"

    if res_h == 768:
        background = "game_data/starfield768.png"
    b_1 = pygame.image.load(background).convert()
    b_2 = pygame.image.load(background).convert()
    scroll = 0

    # Read from game_data/score_file.txt
    score_txt = open("game_data/score_file.txt", "r").read()
    high_score_txt = open("game_data/high_score_file.txt", "r").read()

    # Music
    if mute_txt == "False":
        pygame.mixer.music.load("game_data/death.wav")
        pygame.mixer.music.play(-1)
    elif mute_txt == "True":
        pass

    # Main Loop
    while True:

        # Scrolling Background PART 2
        screen.blit(b_1, (0, scroll))
        screen.blit(b_2, (0, scroll - res_h))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    # Music
                    if mute_txt == "False":
                        pygame.mixer.music.load("game_data/intro.wav")
                        pygame.mixer.music.play(-1)
                    elif mute_txt == "True":
                        pass

                    main_menu()

        scroll += .5
        if scroll == res_h:
            scroll = 0

        # Draws "GAME OVER!" to the Screen
        text = pygame.font.Font(main_font, 100)
        textsurf, textrect = text_objects("GAME OVER", text)
        textrect.center = ((res_w / 2), (res_h / 2 - 200))
        screen.blit(textsurf, textrect)

        # Draws "Score: X" to the Screen
        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = text_objects("Score: " + score_txt, text)
        textrect.center = ((res_w / 2), (res_h / 2 - 140))
        screen.blit(textsurf, textrect)

        # Draws "High Score: X" to the Screen
        text = pygame.font.Font(main_font, 40)
        textsurf, textrect = text_objects("High Score: " + high_score_txt, text)
        textrect.center = ((res_w / 2), (res_h / 2 - 100))
        screen.blit(textsurf, textrect)

        # Draws "Press SPACE to Restart!" to the Screen
        text = pygame.font.Font(main_font, 50)
        textsurf, textrect = text_objects("Press SPACE to Restart...", text)
        textrect.center = ((res_w / 2), (res_h / 2))
        screen.blit(textsurf, textrect)

        # Draws "Press SPACE to Restart!" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Press ESC to go to Main Menu", text)
        textrect.center = ((res_w / 2), (res_h / 2 + 40))
        screen.blit(textsurf, textrect)

        # Draws "Version: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("Version: " + str(version), text)
        textrect.center = ((res_w / 2), 15)
        screen.blit(textsurf, textrect)

        # Draws "FPS: X" to the Screen
        text = pygame.font.Font(main_font, 30)
        textsurf, textrect = text_objects("FPS: " + str(fps)[11:16], text)
        textrect.center = ((res_w / 2), 40)
        screen.blit(textsurf, textrect)

        # FPS and FLIP
        fps.tick(fps_)
        pygame.display.flip()


main_menu()

# Quit Game
pygame.quit()
sys.exit()
