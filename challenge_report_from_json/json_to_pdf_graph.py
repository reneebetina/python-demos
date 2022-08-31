#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

#from reportlab.lib.units import inch #import this if you will use unit of measurement

import json

#Read your JSON File
with open('input/fruits.json') as json_file:
    fruit = json.load(json_file)

# Initialize your report
styles = getSampleStyleSheet()
report = SimpleDocTemplate("output/inventory_report_with_pie_chart.pdf")

# ---------------------------------------------------------------------------------------
#PART 2 - Adding Tables to our PDFs
#>>> from reportlab.lib import colors
table_data = []
for k, v in fruit.items():
   table_data.append([k, v])

#>>> print(table_data)
#[['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]


table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

report_table = Table(data=table_data, style=table_style, hAlign="RIGHT")

#TO PRINT title and table:
#>>> report.build([report_title, report_table])


# ---------------------------------------------------------------------------------------
#PART 3 - Adding Graphics to our PDFs
# ensure you have the ff.:
#>>> from reportlab.graphics.shapes import Drawing
#>>> from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie()
report_pie.data = []
report_pie.labels = []
report_pie.width = 250
report_pie.height = 250

for fruit_name in sorted(fruit):
   report_pie.data.append(fruit[fruit_name])
   report_pie.labels.append(fruit_name)

#>>> print(report_pie.data)
#[2, 5, 8, 3, 1, 1, 13]
#>>> print(report_pie.labels)
#['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report_chart = Drawing()
report_chart.add(report_pie)

#TO PRINT title,chart and table:
report.build([report_title, report_table,report_chart])