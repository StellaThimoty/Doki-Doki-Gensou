# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Zeca = Character("Zekker", color="#ff4026")
define Eremes = Character("Eremes", color="#ff4026")
define Suika = Character("Suika", color="#3498db")
define Skrk = Character("Sakurako", color="#1f8b4c")
define Shen = Character("Shen", color="#ff4026")
define Bago = Character("Vibago", color="#11806a")
define Sal = Character("Sal", color="#11806a")
define Kuji = Character("Kuji", color="#f1c40f")
define Machii = Character("Machii", color="#ffffff")
define Hitler = Character("Hitler", color="#965b0e")

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

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.caption:

        menu:

            "Do you want sound captions on? They describe music and sound effects in text.{fast}"

            "On":

                $ persistent.sound_captions = True

            "Off":

                pass

        menu:

            "Do you want image captions on? They describe game visuals in text.{fast}"
            "On":

                $ persistent.image_captions = True

            "Off":

                pass

        "These options can be changed at any time in the menu.{fast}"

        ## This message will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.caption = False

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
    with fade

    label skip_splash:

        pass

    return

## The game starts here.

label start:
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ play_music(profundo)
    scene sonho
    $ achievement.grant("Novato")
    "A prestigiada academia gensou tem apenas os mais fortes jogadores de HTS..."
    "E depois de muito tentar, eu finalmente consegui ingressar nela!"
    "Foi muito difícil aquela prova...{p}Notação, Framedata, ainda nem sei direito o que é tudo isso!"
    Hitler "Ei, garota que está lendo isso, acorda..."
    "Ainda assim, finalmente vou poder aprender sobre esse jogo que tanto amo!"
    Hitler "VAGABUNDA, VOCÊ VAI SE ATRASAR!"
    $ shake()
    stop music
    scene black with fade
    scene quarto_protag with fade and dissolve
    $ play_sound(alarme)
    "Que? Mas oque? O que tá acontecendo?"
    "Que sonho mais doido que eu tive..."
    show hitler with dissolve
    Hitler "Finalmente acordou...{p}Seguinte garota, me pagaram pra te ajudar."
    stop sound
    $ play_music(cringe,5)
    "HITLER!!??? VOCÊ NÃO TÁ MORTO? PORQUE VOCÊ TEM ASAS?"
    Hitler "Cala a boca meu de-"
    "VOCÊ É UMA FADA?{p}NOSSA, ENTÃO FADAS SÃO REAIS???{p}EU SABIA QUE VOCÊS EXIST-{p}"
    $ shake()
    Hitler "OLHA AQUI SUA PUTINHA, VOCÊ QUER ME OUVIR OU NÃO?"
    "\Aquietar o faixo?"
    menu:
        "Não. É a porra do hitler!":
            jump hitlerman
        "Sim, vou me acalmar e ouvir.":
            jump acalmar

    label hitlerman:
        hide hitler
        scene black with dissolve
        "Ignorando o hitler, eu fui para a academia, ganhei um diploma e me formei."
        "{b}Bad End{p}Vê se joga essa porra.{p}Bgs asshole."
        return

    label acalmar:
    "Okay... Eu não devia fazer isso, mas vou te ouvir."
    Hitler "Eu fui pago pra te ajudar, sou sua fada madrinha e vou te ajudar a conquistar seu amor de HTS, é meu dever como mentor, por isso me escute."
    "O-Okay eu acho... Obrigada"
    Hitler "Primeiro você vai para a escola, pois você já tá atrasada moleca."
    "!!!{p}Verdade! Tenho que correr!!{p}Vou pegar uma torrada, passar geléia, colocar na minha boca e correr pra escola!"
    $ play_sound(doorf)
    scene cidade_protag with fade and dissolve
    "Estou atrasada, estou atrasadaaa!"
    $ shake()
    "Aiii!!{p}Nossa, desculpa desculpa desculpa! Eu trombei em você, desculpa!"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    stop music
    with fade
    show suika tonto with dissolve
    Suika ":sadfrog:"
    show suika tonto at left with dissolve
    show sakurako bebida with dissolve
    Skrk "What is the brother~ What is the brother~ Vamos brilhar, como um diamante numa geração marcante"
    show sakurako bebida at right with dissolve
    show eremes with dissolve
    Skrk "Bora bater botão"
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

label credits:

    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ show_quick_menu = False

    scene black with fade

    ## Find "End Credits Scroll" in screens.rpy to change text.
    call screen credits

    $ persistent.credits_seen = True

    # $ _game_menu_screen = "save"

    scene black
    with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    ## We re-enable the quickscreen as the credits are over.

    $ show_quick_menu = True

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results

    centered "Fin"

    if persistent.game_clear:

        pass

    else:

        if readtotal == 100:

            $ achievement.grant("Completionist")
            show devnotes_unlock at truecenter

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    # This ends the game.
    return
