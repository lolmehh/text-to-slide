import pygame
import pygame_gui
import tkinter as tk
from tkinter import filedialog

pygame.init()

pygame.display.set_caption('Text to slide')
window_surface = pygame.display.set_mode((500, 500))

background = pygame.Surface((800, 600))
background.fill(pygame.Color("#FFFFFF"))

manager = pygame_gui.UIManager((800, 600), 'theme.json')

# Bestaande knoppen

uitzetknop = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 425), (500, 75)),
    text='Import tekstbestand.',
    manager=manager
)

titelvak = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((0, 100), (500, 75)),
    text='Text to slide',
    manager=manager
)

# Kleur voor uitzetknop
uitzetknop.colours['normal_bg'] = pygame.Color("#000000")
uitzetknop.colours['hovered_bg'] = pygame.Color("#232323")
uitzetknop.colours['active_bg'] = pygame.Color("#000000")
uitzetknop.rebuild()

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == uitzetknop   :
                import tkinter as tk
                from tkinter import filedialog

                root = tk.Tk()
                root.withdraw()     
                bestand = filedialog.askopenfilename(
                    title="Voeg tekstbestand toe:",
                    filetypes=[("*Tekstbestand", "*.txt")]
                )

                if bestand:
                    def bestandlezen(bestand):
                        with open(bestand, "r") as f:
                            text = f.read()

                        allezinnen = text.split('.')

                        for zin in allezinnen:
                            zin = zin.strip()
                            if zin: 
                                print(zin + ".")

                        for zin in allezinnen:
                            zin = zin.strip()
                            if zin.startswith("@"):
                                print(zin, "Dit is de titel")


                    bestandlezen(bestand)
                    
                    print("Je hebt gekozen:", bestand)

                else:
                    print("Geen bestand gekozen")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
