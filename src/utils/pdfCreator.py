
from reportlab.pdfgen import canvas
import os.path



fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.jpg')


 
def card_creatot(filename, a, b, c, d, e):
    creare = canvas.Canvas(filename,pagesize=(419.5,300.5))
    creare.drawImage(fn,0,0,419.5,300.5)
    creare.drawCentredString(340,97,a)
    creare.drawCentredString(300,62,b)
    creare.drawCentredString(278,30,c+'  '+d)
    creare.drawCentredString(340,120,e)
    creare.save()
