import pymupdf

doc = pymupdf.open("./agency-template.pdf")
page = doc[-1]

text_rect = (90, 140, 150, 160)
text = " السيِّدة نجوى محمَّد أحمد"

image_rect = (150, 670, 200, 700)

page.insert_htmlbox(text_rect, text)
page.insert_image(image_rect, filename="./signature.png")

doc.save("text.pdf")
