import fitz

doc=fitz.open("File_name")
page=doc[0] 

# To extract text
text=page.get_text()
print("First page's text:\n",text) # checks whether the text is extracted or not

# To add text
page.insert_text((100,100),"This text is added",fontsize=12,color=(1,0,0))

# To draw shapes
page.draw_rect((50,50,150,150),color=(1,0,0),width=2)

# To insert image
pix=fitz.Pixmap("image.png")
page.insert_image(page.rect,pixmap=pix)

# To extract image from a PDF
for img in fitz.get_images(full=True):
    xref=img[0]
    pix=fitz.Pixmap(doc,xref)
    if pix.n < 5:
        pix.save(f"image_{xref}.png")

# To merge 2 PDFs
doc_1=fitz.open("file1.pdf")
doc_2=fitz.open("file2,pdf")
doc_1.insert_pdf(doc_2)
doc_1.save("merged_PDf")

# To extract pages of a PDF(split PDf)
new_doc=fitz.open()
new_doc.insert_image(doc,page=1,to_page=3)
new_doc.save("subset.pdf")

# To reorder or delete pages
doc.delete_page(0) 
doc.move_page(2,0) # move page 3 to the beginning

# To add a password to a PDF
doc.save("protected.pdf",encryption=fitz.PDF_ENCRYPT_AES_256,owner_pw="1890")

# To set Metadata
print(doc.metadata)
doc.set_metadata({"title":"Title","author":"Me"})

# To render page as image
pix=page.get_pixmap(dpi=150)
pix.save("page.png")


# To highlight a particular text
search_term="important word"

for page_num in range(doc.get_count):
    page=doc[page_num]

text_instances=page.search_for(search_term,quads=False)
for inst in text_instances:
    highlight=page.add_highlight(inst)
    highlight.update()

doc.save("highlighted.pdf")

# To save and close a PDF
doc.save("edited.pdf")
doc.close()


