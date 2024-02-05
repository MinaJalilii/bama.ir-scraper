# Bama.ir Scraper

This Python script scrapes car advertisements from Bama.ir and saves the results in a CSV file.

## Overview

The Bama.ir Scraper is a Python script that uses `requests_html` to extract car advertisement data from Bama.ir's API. It fetches information such as title, price, mileage, location, and time, and saves it into a CSV file.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/bama.ir-scraper.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd bama.ir-scraper
   ```

3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   **or install only the required library:**
   ```bash
   pip install requests-html
   ```
5. **Run the script:**
   ```bash
   python scraper.py
   ```

   This will scrape data from Bama.ir and save it to `results.csv`.

## Configuration

- The base URL for Bama.ir is set to `https://bama.ir/cad/api/search`. You can modify the `bama_url` variable in `scraper.py` if needed.

- The script loops through 4 pages of the website. Adjust the range in the loop in `scraper.py` based on your requirements.

## Scraped Details
The script is designed to scrape various details from Bama.ir, including but not limited to:

- Title
- Price
- Mileage
- Location
- Time

Feel free to explore the script and customize it according to your specific scraping needs. The `scraper.py` file can be modified to include additional details based on the structure of the data available on Bama.ir.

## Error Handling

- The script includes error handling for HTTP errors and general exceptions. If an error occurs during scraping, the script will print an error message.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

