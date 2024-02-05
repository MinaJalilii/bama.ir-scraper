import requests_html
import csv


def scrape_bama_data(url):
    try:
        # Open a CSV file for writing with UTF-8 encoding
        with open('results.csv', 'w', encoding='utf-8') as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            # Use Persian headers for the CSV file
            writer.writerow(['title', 'price', 'mileage', 'location', 'time'])

            # Create an HTML session using requests_html
            session = requests_html.HTMLSession()

            # Loop through pages of the website
            for j in range(0, 4):  # The number 4 means it loops through 4 pages or 4 times scrolling
                # Make a GET request to the provided URL
                r = session.get(f'{url}?pageIndex={j}')
                # Raise an exception for bad status codes
                r.raise_for_status()
                # Parse the JSON response
                js = r.json()

                # Loop through the ads in the JSON response
                for i in js['data']['ads']:
                    # Check if the entry is an advertisement
                    if i['type'] == 'ad':
                        # Extract title, price, mileage, location, and time from the ad details
                        title = i['detail']['title']
                        if i['price']['type'] == 'negotiable':
                            price = "Negotiable"
                        else:
                            price = i['price']['price']
                        mileage = i['detail']['mileage']
                        location = i['detail']['location']
                        time = i['detail']['time']
                    else:
                        # Skip if the entry is not an advertisement
                        continue
                    # Write the extracted data to the CSV file
                    writer.writerow([title, price, mileage, location, time])
    except requests_html.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests_html.RequestException as e:
        print(f"Request error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Provide the base URL for Bama website
bama_url = 'https://bama.ir/cad/api/search'
# Call the function with the dynamic URL
scrape_bama_data(bama_url)
