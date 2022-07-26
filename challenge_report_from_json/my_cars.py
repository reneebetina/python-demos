#!/usr/bin/env python3

import os
import challenge_send_email.emails as emails  #importing my own python module
import json
import locale
import sys


from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}

  max_sales = 0
  max_sales_model = ""


  year_sales = {}

  for item in data:
#    print(item)
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # MAX SALES
    if item["total_sales"] > max_sales:
      max_sales = item["total_sales"]
      max_sales_model =  "{} {}".format(item["car"]["car_make"],item["car"]["car_model"])
 #     print("*******"+max_sales_model)

    # MOST POPULAR CAR YEAR
    if item["car"]["car_year"] not in year_sales.keys():
      year_sales[item["car"]["car_year"]] = item["total_sales"]
    else:
      year_sales[item["car"]["car_year"]] += item["total_sales"]


  year_sales = {k: v for k, v in sorted(year_sales.items(), key=lambda item: item[1], reverse=True)}
  maxyear = next(iter(year_sales))
  maxyear_sales = year_sales[maxyear]

 # dict_sorted= OrderedDict(sorted(year_sales.items()))
 # print(dict_sorted)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales_model, max_sales),
    "The most popular year was {} with {} sales.".format(maxyear, maxyear_sales)
  ]

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("input/car_sales.json")
  summary = process_data(data)
  print(summary)

  # Turn this into a PDF report
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate("output/report_cars.pdf")

  # Send the PDF report as an email attachment
  report_title = Paragraph("Sales summary for last month", styles["h1"])

  summary1 = Paragraph(summary[0]+"<br/>", styles["BodyText"])
  summary2 = Paragraph(summary[1]+"<br/>", styles["BodyText"])
  summary3 = Paragraph(summary[2]+"<br/><br/>", styles["BodyText"])

  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
  report_table = Table(data=cars_dict_to_table(data), style=table_style, hAlign="LEFT")
  report.build([report_title, summary1, summary2, summary3, report_table])

  sender = "automation@example.com" #configure this
  receiver = "automation@example.com" #configure this
  subject = "Sales summary for last month"
  body = summary[0] + "\n" + summary[1] + "\n" + summary[2] + "\n"
  message = emails.generate_email(sender, receiver, subject, body, "output/report_cars.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)