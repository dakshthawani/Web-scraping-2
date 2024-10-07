# Web Scraping Project: Extracting Headlines from Wikipedia

This project demonstrates a basic web scraping workflow using Python. It fetches the page content of a specified Wikipedia article, extracts headlines, and stores them in a text file. If new headlines are found, it sends a placeholder email notification.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)

## Project Overview
This script scrapes the headlines (e.g., `<h1>`, `<h2>`, etc.) from a given Wikipedia page, extracts them using a defined YAML configuration file (`extract.yaml`), and stores the extracted data in `data.txt`. The project uses the `requests` and `selectorlib` libraries.

## Requirements
- Python 3.x
- Required Python libraries:
  - `requests`
  - `selectorlib`

Install the required libraries using:
```bash
pip install requests selectorlib
```

## Project Structure

├── extract.yaml     # YAML file defining the structure of elements to be extracted

├── main.py          # The main script for scraping, extracting, and storing data

├── data.txt         # Stores the extracted headlines

├── README.md        # This README file

## Usage
1. Clone this repository or download the script files.
2. Ensure you have the required dependencies installed (see [Requirements](#requirements)).
3. Create an extract.yaml file in the same directory with the following contents:
```bash
headlines:
    css: 'h1, h2, h3, h4, h5, h6'
    multiple: true
```
4. Run the script:
```bash
python main.py
```
5. Check the `data.txt` file to see the extracted headlines.

## How It Works
1. `scrape(url)`: This function sends an HTTP GET request to the specified `url` and retrieves the page's HTML content.

2. `extract(source)`: Using `selectorlib` and the `extract.yaml` file, this function extracts the headlines (using the CSS selectors defined in `extract.yaml`).

3. `store(extracted)`: Writes the extracted headlines to `data.txt`, each headline on a new line.

4. `send_mail()`: Placeholder function for sending an email when new headlines are found.

5. Main Program:

- The script scrapes the URL and extracts the headlines.
- It stores the headlines in `data.txt`.
- If new headlines are found (not present in the `data.txt` file), it triggers the `send_mail()` function.
