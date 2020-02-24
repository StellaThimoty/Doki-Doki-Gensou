# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Zeca = Character("Zekker")
define Eremes = Character("Eremes")
define Suika = Character("Suika")
define Skrk = Character("Sakurako")
define Aco = Character("Damnaku")
define Shen = Character("Shen")
define Bago = Character("Vibago")
define Sal = Character("Sal")
define Kuji = Character("Kuji")
define Machii = Character("Machii")
define Yuk = Character("Yuganu")
define Hitler = Character("Hitler")

image extras_unlock = Text("{size=60}You've unlocked the Extras Menu. Access it through the Main Menu.{/s}", text_align=0.5)
image devnotes_unlock = Text("{size=60}You've unlocked a special message. Access it through the Extras Menu.{/s}", text_align=0.5)

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.

## Setting up images for use in the splashscreen
image renpy_name = Text("{size=60}Made with Ren'Py [renpy.version_only]{/s}", text_align=0.5)

## The animation is kinda tacky so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign -0.5
    ease_quad 5.0 xalign 0.5 yalign 0.5 rotate 360
    linear 2.0 zoom 2.0

image splash_anim_2:
    "renpy_name"
    xalign 0.5 yalign 0.8 alpha 0.0
    pause 6.0
    linear 1.0 alpha 1.0

label splashscreen:

    scene black

## Here begins our splashscreen animation.
show splash_anim_1
show splash_anim_2

## The first time the game is launched, players cannot skip the animation.
if not persistent.seen_splash:

    ## No input will be detected for the set time stated.
    ## Set this to be a little longer than how long the animation takes.
    $ renpy.pause(8.5, hard=True)

    $ persistent.seen_splash = True

## Players can skip the animation in subsequent launches of the game.
else:

    if renpy.pause(8.5):

        jump skip_splash

scene black
$ persistent.sound_captions = True
with fade

label skip_splash:

    pass

return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene templo

    "A prestigiada academia gensou tem apenas os mais fortes..."
    "Fico muito nervosa aqui às vezes, sempre parece que vou levar um pau, mas consegui entrar de algum jeito..."
    "Desde sempre quis entrar aqui, mas sempre achei que era uma academia de {b}Melty{/b}, pois isso era tudo que aqueles formandos falavam..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    stop music
    scene
    with fade
    show suika tonto with dissolve
    Suika ":sadfrog:"
    show suika tonto at left with dissolve
    show sakurako bebida with dissolve
    Skrk "What is the brother~ What is the brother~ Vamos brilhar, como um diamante numa geração marcante"
    show sakurako bebida at right with dissolve
    show eremes with dissolve
    Eremes "I'M GONNA GET YOU, LIKE A SPACE BOY. {p}WOWOWOWOWOW!!{p} \O que preferes?\""
    menu:

        "Trio Parada Dura":
            jump TPD
            label TPD:
                "O Trio Parada Dura veio salvar o HTS..."
        "Chines":
            jump Meiling
            label Meiling:
                "PARA DE DAR J2A FILHO DA PUTAAAAAAAAA"
    hide suika tonto with dissolve
    hide eremes with dissolve
    hide sakurako bebida with dissolve
    "Mano programar em phyton é fácil demais"

    # This ends the game.

    return
