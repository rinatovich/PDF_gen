from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import requests
import json
from collections import namedtuple
import os
#!/usr/bin/python
# -*- coding: utf-8 -*-



url = 'http://192.168.10.185:5555/api/0/report'
data = {
    "from": "05-10-2022",
    "to": "05-18-2022",
    "bank_codes": ["00820", "00821", "00822"]
}

#getting objects
# response = requests.post(url,data=data)
# response_text = response.text
# list = json.loads(response_text)
# if not list:
list = json('./json.json')
print(type(dict))
#getting objects




pdfReportPages = "C:\\Users\\User\\Desktop\\PDF\\test.pdf"
doc = SimpleDocTemplate(pdfReportPages, pagesize=A4)

pdfmetrics.registerFont(TTFont('regular', 'Arial.ttf'))

# container for the "Flowable" objects
elements = []
styles = getSampleStyleSheet()
styles["Normal"].fontName = 'regular'
styleN = styles["Normal"]

# Make heading for each column and start data list
column0Heading = "T/p"
column1Heading = "Банк"
column2Heading = "Ходим Ф.И.Ш"
column3Heading = "Курилма \nхолати"
column4Heading = "Холат юз берган \nвахт"
column5Heading = "Холат \nдавомийлиги"

style = [('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                       ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                       ('LINEBELOW', (3, 0), (-1, -1), 1, colors.black),
                       ('BOX', (0, 0), (-1, -1), 1, colors.green),
                       ('BOX', (0, 0), (0, -1), 1, colors.blue),
                       ('BOX', (0, 0), (1, -1), 1, colors.purple),
                       ('BOX', (0, 0), (2, -1), 1, colors.black),
                       ('BOX', (0, 0), (3, -1), 1, colors.black),
                        ('BOX', (0, 0), (4, -1), 1, colors.black),
                        ('BACKGROUND', (0, 0), (5, 0), colors.lightblue),

                       ]

# Assemble data for each column using simple loop to append it into data list
data = [[Paragraph(column0Heading, styleN),Paragraph(column1Heading, styleN), Paragraph(column2Heading, styleN),Paragraph(column3Heading, styleN),Paragraph(column4Heading, styleN),Paragraph(column5Heading, styleN)]]
id=1
temp_bank = None
temp_username = None
for bank in list:
    for user in bank['data']:
        for log in user['device_log']:
            if temp_bank!=bank['bank_code']:
                print('Bingo')
                style.append(('BACKGROUND', (0, id), (5, id), colors.black),)
            if temp_bank==bank['bank_code']:
                if temp_username==user['fullname']:
                    data.append([id, '' , '', Paragraph(str(log['status']), styleN),Paragraph(log['arrived_time'], styleN), Paragraph(log['duration'], styleN)])
                else:
                    data.append([id, '', Paragraph(user['fullname'], styleN), Paragraph(str(log['status']), styleN),Paragraph(log['arrived_time'], styleN), Paragraph(log['duration'], styleN)])
            else:
                data.append([id,Paragraph(bank['bank_code'],styleN),Paragraph(user['fullname'],styleN),Paragraph(str(log['status']),styleN),Paragraph(log['arrived_time'],styleN),Paragraph(log['duration'],styleN)])
            temp_bank = bank['bank_code']
            temp_username =user['fullname']
            id+=1

tableThatSplitsOverPages = Table(data, [1*cm,5*cm,4*cm,2*cm,2*cm], repeatRows=1)
tableThatSplitsOverPages.hAlign = 'CENTER'
print(style)
tblStyle = TableStyle(style)
tableThatSplitsOverPages.setStyle(tblStyle)
elements.append(tableThatSplitsOverPages)
doc.build(elements)