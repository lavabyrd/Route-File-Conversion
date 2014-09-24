import csv


def route_replace():
	with open("rca original.txt", 'rb') as i:
		reader = csv.reader(i, delimiter = '|', quoting = csv.QUOTE_MINIMAL)
		with open("fixed.txt", 'wb') as o:
			writer = csv.writer(o, delimiter = '|', quoting = csv.QUOTE_MINIMAL)
			for row in reader:
				if row[8] == "SX01":
					row[8] = "GW05"
					row[9] = "GW05"
					writer.writerow(row)
				elif row[8] == "SX02":
					row[8] = "GW06"
					row[9] = "GW06"
					writer.writerow(row)
				elif row[8] == "SX03":
					row[8] = "NWX1"
					row[9] = "NWX1"
					writer.writerow(row)
				elif row[8] == "SX04":
					row[8] = "NWX2"
					row[9] = "NWX2"
					writer.writerow(row)
				elif row[8] == "SX05":
					row[8] = "NWX3"
					row[9] = "NWX3"
					writer.writerow(row)
				elif row[8] == "SX07":
					row[8] = "NWX4"
					row[9] = "NWX4"
					writer.writerow(row)
				else:
					writer.writerow(row)


def route_check():
	with open("rca.txt", 'rb') as i:
		reader = csv.reader(i, delimiter = '|', quoting = csv.QUOTE_MINIMAL)
		with open("rca_final.txt", 'wb') as o:
			writer = csv.writer(o, delimiter = '|', quoting = csv.QUOTE_MINIMAL)
			for row in reader:
				if row[8] != row[9]:
					row[8] = row[9]
					writer.writerow(row)
				else:
					writer.writerow(row)
