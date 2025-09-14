# Driver Assignment

A simple project for managing driver assignments. This repository provides tools and scripts to allocate drivers to tasks efficiently.

## Features

- Assign drivers to tasks based on availability
- Simple configuration and setup

## Installation

```bash
git clone https://github.com/yourusername/driver_assignment.git
cd driver_assignment
```

## Usage

1. Export a CSV file from a [Bitpoll poll](https://bitpoll.de/).
2. Run the assignment script:
    ```bash
    python assign_drivers.py poll.csv --sort_drivers
    ```
3. Assignment is printed to the console

## CSV Format

The assignment script expects the CSV file to follow the format exported by Bitpoll. The file should contain:

- The first row with column headers (`Name`, `Datetime` - ignored, followed by task or time slot columns)
- Each subsequent row represents a driver and their availability for each task or slot with "Ich kann" meaning they accept the date.

Example:

```csv
Name,Datetime,Task 1,Task 2,Task 3
Alice,ignored,Ich kann,no,Ich kann
Bob,ignored,no,Ich kann,Ich kann
Charlie,ignored,Ich kann,Ich kann,no
```

Ensure your CSV matches this structure for correct processing.

## License

This project is licensed under the MIT License.