# Python program for solution of hamiltonian cycle problem

import csv
import sys
import hamilton_cycle.graph as hc

# Driver assignment
poll_csv_file = sys.argv[1]
debug = len(sys.argv) > 2 != ""

yes_vote_text = "Ich kann"

driver_has_date = []
with open(poll_csv_file, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    header = next(csv_reader)
    for row in csv_reader:
        driver = row[0]
        for vote, date in zip(row[2:], header[2:]):
            # ignore utility columns (count for sorting drivers)
            if date.lower() == "count":
                next
            # ignore utility rows (no driver assigned)
            if driver == "":
                next
            if (vote == yes_vote_text):
                driver_has_date.extend([{'driver': driver, 'date': date}])

is_driver = {}
is_date = {}
for edge in driver_has_date:
    is_driver[edge['driver']] = 1
    is_date[edge['date']] = 1
drivers = is_driver.keys()
dates = is_date.keys()
n_drivers = len(drivers)
n_dates = len(dates)
start_node = 'Start'
vertices = [start_node]
vertices.extend(dates)
vertices.extend(drivers)
n_vertices = len(vertices)
g1 = hc.Graph(vertices)
for edge in driver_has_date:
    g1.graph[vertices.index(edge['driver'])][vertices.index(edge['date'])] = 1

for date in dates:
    for driver in drivers:
        g1.graph[vertices.index(date)][vertices.index(driver)] = 1

for driver in drivers:
    g1.graph[vertices.index(start_node)][vertices.index(driver)] = 1
for driver in drivers:
    for other_driver in drivers:
        g1.graph[vertices.index(driver)][vertices.index(other_driver)] = 1
for date in dates:
    g1.graph[vertices.index(date)][vertices.index(start_node)] = 1

# Print the solution
if g1.hamCycle(debug):
    g1.printAssignment(drivers, dates)
