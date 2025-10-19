import pygame
import pygame_gui
import tkinter as tk
from tkinter import filedialog
#from uitlezen import bestandlezen

from pptx import Presentation
import os

pygame.init()

pygame.display.set_caption('Text to slide')
window_surface = pygame.display.set_mode((500, 500))

background = pygame.Surface((800, 600))
background.fill(pygame.Color("#FFFFFF"))

manager = pygame_gui.UIManager((800, 600))

# Bestaande knoppen

uitzetknop = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 425), (500, 75)),
    text='Import tekstbestand.',
    manager=manager
)

textbox = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((0, 75), (500, 350)),
    html_text='upload een text bestand om te veranderen in een presentatie',
    manager=manager
)

titlebox = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((0, 0), (500, 75)),
    html_text='text to slide',
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

                        slidelijsten = {}
                        slidenummer = 0

                        for zin in allezinnen:
                            zin = zin.strip()

                            if zin.startswith("#"):
                                zin = zin[1:]
                                if 0 in slidelijsten and slidelijsten[0] is not None:
                                    slidelijsten[0].append(zin)
                                else:
                                    slidelijsten[0] = []
                                    slidelijsten[0].append(zin)
                                
                            elif zin.startswith("@"):
                                slidenummer = slidenummer + 1
                                zin = zin[1:] #haalt @ weg uit presentatie
                                slidelijsten[slidenummer] = [zin]                            
                            else:
                                if slidenummer not in slidelijsten:
                                    #als de eerste zin(nen) geen @ of # hebben
                                    slidenummer = 1
                                    slidelijsten[slidenummer] = []
                                slidelijsten[slidenummer].append(zin)
                        

                        prs = Presentation()

                        # Maak een titelslide (optioneel)
                        def titelslideophalen():
                            slide_layout = prs.slide_layouts[0]  # Titel-layout
                            slide = prs.slides.add_slide(slide_layout)
                            title = slide.shapes.title
                            subtitle = slide.placeholders[1]

                            title.text = slidelijsten[0][0]
                            subtitle.text = "\n".join(slidelijsten[0][1:]).strip()

                        # Maak de inhoudslides
                        def inhoudslides():
                            for nummer, zinnen in slidelijsten.items():  # 
                                if nummer == 0: #sla de gegevens van de titelslide over
                                    continue

                                slide_layout = prs.slide_layouts[1]  # De layout (van de library) voor "Titel en inhoud"
                                slide = prs.slides.add_slide(slide_layout)

                                title = slide.shapes.title
                                content = slide.placeholders[1]

                                

                                # Dit is voor de eerste zin in de list
                                if len(zinnen) > 0:
                                    title.text = zinnen[0].strip()

                                # dit is voor de rest van de zinnen in de list
                                if len(zinnen) > 1:
                                    inhoud = "\n".join(zinnen[1:]).strip()
                                    content.text = inhoud

                        def bestandopslaan():
                            downloads = os.path.join(os.path.expanduser("~"), "Downloads")
                            PPTXbestand = os.path.join(downloads, "Menu.pptx")

                            prs.save(PPTXbestand)
                            print(f"Presentatie opgeslagen als: {PPTXbestand}")

                        titelslideophalen()
                        inhoudslides()
                        bestandopslaan()
                    
                    print("Gekozen bestand:", bestand)      
                    slidelijsten = bestandlezen(bestand)


                    
                else:
                    print("Geen bestand gekozen")

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
