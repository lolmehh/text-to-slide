from pptx import Presentation
import os

from GUI import slidelijsten  # Zorg dat GUI.py 'slidelijsten' exporteert (globale variabele)
print(slidelijsten)

prs = Presentation()

# Maak een titelslide (optioneel)
def titelslideophalen():
    slide_layout = prs.slide_layouts[0]  # Titel-layout
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = "Text to Slide"
    subtitle.text = "Automatisch gegenereerde presentatie"

titelslideophalen()


# Maak de inhoudslides
def inhoudslides():
    for nummer, zinnen in slidelijsten.items():
        slide_layout = prs.slide_layouts[1]  # "Titel en inhoud" layout
        slide = prs.slides.add_slide(slide_layout)

        title = slide.shapes.title
        content = slide.placeholders[1]

        # Eerste zin = titel (bijv.)
        if len(zinnen) > 0:
            title.text = zinnen[0].strip()

        # Rest = inhoud van de slide
        if len(zinnen) > 1:
            inhoud = "\n".join(zinnen[1:]).strip()
            content.text = inhoud


inhoudslides()

# Opslaan in Downloads
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
PPTXbestand = os.path.join(downloads, "voorbeeld.pptx")

prs.save(PPTXbestand)
print(f"Presentatie opgeslagen als: {PPTXbestand}")
