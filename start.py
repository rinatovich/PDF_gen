from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



# myCanvas = canvas.Canvas('myfile.pdf', pagesize=A4)
# myCanvas.showPage()
# myCanvas.save()
cm = 2.54


c = "C:\\Users\\user\\Desktop\\PDF\\hello.pdf"
elements = []

doc = SimpleDocTemplate(c, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)

data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
LIST_STYLE = TableStyle(
    [('GRID', (1, 1), (-1, -1), 1, colors.green),
     ('BOX', (1, 2), (1, -1), 2, colors.red),
     ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
     ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
     ])
table = Table(data, colWidths=None, rowHeights=None, style=LIST_STYLE, splitByRow=1, repeatRows=0, repeatCols=0, rowSplitRange=True, spaceBefore=None, spaceAfter=None, cornerRadii=None)

elements.append(table)
doc.build(elements)

