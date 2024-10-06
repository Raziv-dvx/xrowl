import requests
import sys
import time
import threading
from prettytable import PrettyTable

def loading_animation():
    """Shows a loading animation while fetching data."""
    for _ in range(10):
        for c in ['|', '/', '-', '\\']:
            print(f'\rSearching for IP... {c}', end='', flush=True)
            time.sleep(0.1)

def display_results(all_results):
    """Displays results in a two-column pretty table format."""

    # Create a PrettyTable instance
    table = PrettyTable()

    # Define the field names for the two columns: "Enquiry" and "Results"
    table.field_names = ["Enquiry", "Results"]

    # Add rows to the table (each row for each field in all_results)
    for label, data in all_results.items():
        table.add_row([label, data])

    # Print the table
    print(table)

def get_city_country_info(city, country):
    """Fetches detailed information about the city or country."""
    url = f"https://restcountries.com/v3.1/name/{country}"
    country_info = {}
    try:
        response = requests.get(url)
        data = response.json()
        country_info['Timezone'] = data[0].get('timezones', ['N/A'])[0]
        country_info['Currency'] = list(data[0].get('currencies', {'N/A': {}}).keys())
    except Exception as e:
        print(f"Error fetching country info: {e}")
    return country_info

def get_ip_info(ip, suspected_country, enquiry_area):
    results = {}
    api_services = []

    # Adjusting server names to align with API services
    if enquiry_area == '1':
        api_services.append("ip-api.com")
    elif enquiry_area == '2':
        api_services.extend(["ip-api.com", "ipinfo.io"])
    elif enquiry_area == '3':
        api_services.extend(["ip-api.com", "ipinfo.io", "ipwhois.app"])
    else:
        print("Invalid selection for enquiry area.")
        return

    # Start loading animation in a separate thread
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()

    # Fetch data from APIs
    for service in api_services:
        if service == "ip-api.com":
            url = f"http://ip-api.com/json/{ip}"
        elif service == "ipinfo.io":
            url = f"https://ipinfo.io/{ip}/json"
        elif service == "ipwhois.app":
            url = f"https://ipwhois.app/json/{ip}"
        else:
            continue

        try:
            response = requests.get(url)
            data = response.json()
            results[service] = data
        except Exception as e:
            print(f"Error fetching data from {service}: {e}")

    # Stop loading animation
    animation_thread.join()
    print("\rData fetched successfully!\n")

    # Ensure results are not empty before proceeding
    if not results:
        print("No data returned from any server.")
        return

    # Extract data from the most informative server (first available service)
    server_data = results[api_services[0]]

    all_results = {
        "IP Address": server_data.get('query', 'N/A'),
        "Continent Code": server_data.get('continentCode', 'N/A'),
        "Country Code": server_data.get('countryCode', 'N/A'),
        "Country Name": server_data.get('country', 'N/A'),
        "Region Name": server_data.get('regionName', 'N/A'),
        "City": server_data.get('city', 'N/A'),
        "ISP": server_data.get('isp', 'N/A'),
        "Website": server_data.get('org', 'N/A')
    }

    # Display the results in a two-column table
    display_results(all_results)

    if suspected_country and all_results:
        country_info = get_city_country_info(all_results['City'], suspected_country)
        print(f"Timezone: {country_info.get('Timezone', 'N/A')}")
        print(f"Currency: {', '.join(country_info.get('Currency', ['N/A']))}")

    # Generate links for Google Maps and Wikipedia
    if server_data:
        latitude = server_data.get('lat', 'N/A')
        longitude = server_data.get('lon', 'N/A')
        google_maps_link = f"https://www.google.com/maps/@{latitude},{longitude},10z"
        print(f"Google Maps: {google_maps_link}")

        if suspected_country:
            wiki_link = f"https://en.wikipedia.org/wiki/{suspected_country.replace(' ', '_')}"
        else:
            wiki_link = f"https://en.wikipedia.org/wiki/{server_data.get('country', '').replace(' ', '_')}"

        print(f"Wikipedia: {wiki_link}")

def main():
    while True:
        print("\nWelcome to the IP Tracker!")
        print("Please answer the following questions:")

        ip = input("1. IP address (paste the IP address): ")
        if ip.strip() == '##':
            break

        suspected_country = input("2. Suspected country (leave blank if unknown): ")
        if suspected_country.strip() == '##':
            break

        print("3. Select enquiry area:")
        print("   1. Small (use one request service)")
        print("   2. Wide (use two request services)")
        print("   3. Worldwide (use three request services)")
        enquiry_area = input("   Enter your choice (1, 2, or 3): ")
        if enquiry_area.strip() == '##':
            break

        get_ip_info(ip, suspected_country, enquiry_area)

if __name__ == "__main__":
    main()
