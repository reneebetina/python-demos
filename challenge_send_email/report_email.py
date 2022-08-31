#!/usr/bin/env python3
import reports
import emails
import os 
from datetime import date


#BASEPATH_SUPPLIER_TEXT_DES = os.path.expanduser('~') + '/some/path/here'
BASEPATH_SUPPLIER_TEXT_DES = 'data/descriptions/'
list_text_files = os.listdir(BASEPATH_SUPPLIER_TEXT_DES)

text_data = []
for text_file in list_text_files:
	with open(BASEPATH_SUPPLIER_TEXT_DES + text_file, 'r') as f:
		text_data.append([line.strip() for line in f.readlines()])
		f.close()

report = []
def process_data(data):
	for item in data:
		report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
	return report


if __name__ == "__main__":

	summary = process_data(text_data)

	# Generate a paragraph that contains the necessary summary
	paragraph = "<br/><br/>".join(summary)

	# Generate the PDF report
	title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
	attachment = "tmp/processed.pdf"

	reports.generate_report(attachment, title, paragraph)

	# Send the email
	subject = "MAIL Completed - Online Fruit Store"
	sender = "automation_sender@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate_email(sender, receiver, subject, body, attachment)
	#print(message)

	# Send will only be successful if you configure your SMTP correctly
	# check your emails.py
	emails.send_email(message)