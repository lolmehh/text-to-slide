from pptx import Presentation
import os

# Maak een nieuwe presentatie
prs = Presentation()

slide_layout = prs.slide_layouts[0]  # Titel slide

slide = prs.slides.add_slide(slide_layout)

title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Banaan"
subtitle.text = "Ik maak graag bananen en aardbeien en sprint review."

slide_layout2 = prs.slide_layouts[1]  # Titel + inhoud
slide2 = prs.slides.add_slide(slide_layout2)

title2 = slide2.shapes.title
content = slide2.placeholders[1]

title2.text = "een slide"
content.text = "Eerste punt om over te hebben \nTweede punt\nDerde punt"


downloads = os.path.join(os.path.expanduser("~"), "Downloads")
bestand = os.path.join(downloads, "voorbeeld.pptx")


prs.save(bestand)
