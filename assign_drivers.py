# Driver assignment with hamiltonian cycles
import csv
import sys
import argparse
import hamilton_cycle.graph as hc

# Parse command line arguments
parser = argparse.ArgumentParser(description="Assign drivers to dates based on poll CSV.")
parser.add_argument("poll_csv_file", help="Path to the poll CSV file")
parser.add_argument("--debug", action="store_true", help="Enable debug mode")
parser.add_argument("--sort_drivers", action="store_true", help="Sort drivers by number of dates they indicated")
args = parser.parse_args()

poll_csv_file = args.poll_csv_file
debug = args.debug
sort_drivers = args.sort_drivers

yes_vote_text = "Ich kann"

driver_has_date = []
with open(poll_csv_file, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    header = next(csv_reader)
    all_dates = header[2:]
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

# count dates for each driver
if sort_drivers:
    n_dates_per_driver = {}
    for edge in (driver_has_date):
        n_dates_per_driver[edge['driver']] = n_dates_per_driver.get(edge['driver'], 0) + 1
    # sort drivers by number of dates they can drive
    driver_has_date.sort(key=lambda x: n_dates_per_driver[x['driver']])

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

# Check for dates without assigned drivers
for date in all_dates:
    if date not in dates:
        print(f"Warning: Date '{date}' has no drivers assigned.")
