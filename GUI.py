import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Text to slide')
window_surface = pygame.display.set_mode((500, 500))

background = pygame.Surface((800, 600))
background.fill(pygame.Color("#FFFFFF"))

manager = pygame_gui.UIManager((800, 600))

# Bestaande knoppen

uitzetknop = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 425), (500, 75)),
    text='Zet tekst om naar powerpoint presentatie.',
    manager=manager
)

# Kleur voor uitzetknop
uitzetknop.colours['normal_bg'] = pygame.Color("#388328")
uitzetknop.colours['hovered_bg'] = pygame.Color("#46a442")
uitzetknop.colours['active_bg'] = pygame.Color("#2e7d32")
uitzetknop.rebuild()

tekstbox = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((0, 0), (500, 425)),
    manager=manager
)


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
                    title="Kies een tekstbestand",
                    filetypes=[("*afbeelding", "*.txt")]
                )

                if bestand:
                    print("Je hebt gekozen:", bestand)
                    from uitlezen import importtekst
                    print(importtekst)
                else:
                    print("Geen bestand gekozen")


                # Tekst uit het tekstvak ophalen en printen
                print("Tekstbox inhoud:", tekstbox.get_text())
                print("De tekst wordt nu omgezet naar een powerpointpresentatie")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
