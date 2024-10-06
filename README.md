# Xrowl

Xrowl is a Python-based IP tracker tool that fetches detailed information about IP addresses using various public APIs. It provides information such as the geographical location, ISP details, and more, and formats the output using tables.

**Note:** This is the very first version of the CLI tool—more of a draft version. Future updates and improvements are planned.

## Overview

-  IP address information 
  - ip-api.com
  - ipinfo.io
  - ipwhois.app
-  (LII) feature planned for future releases.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Installing 

Clone the repository and install the required packages using the following commands:

```bash
git clone https://github.com/Raziv-dvx/xrowl.git
cd xrowl
pip install prettytable requests chardet
```

## Usage

1. Run the script:

   ```bash
   python xrowl.py
   ```

2. Follow the prompts to enter:
   - The IP address you want to track.
   - A suspected country (optional).
   - The enquiry area (choose between small, wide, or worldwide).

3. The script will fetch and display the results in a structured format.

## Example Output

```
Welcome to the IP Tracker!
Please answer the following questions:
1. IP address (paste the IP address): 8.8.8.8
2. Suspected country (leave blank if unknown): United States
3. Select enquiry area:
   1. Small (use one request service)
   2. Wide (use two request services)
   3. Worldwide (use three request services)
   Enter your choice (1, 2, or 3): 3

Data fetched successfully!

+----------------+----------------+
| Enquiry        | Results        |
+----------------+----------------+
| IP Address     | 8.8.8.8       |
| Continent Code | NA             |
| Country Code   | US             |
| Country Name   | United States   |
| Region Name    | California     |
| City           | Mountain View  |
| ISP            | Google LLC     |
| Website        | Google LLC     |
+----------------+----------------+

Timezone: America/Los_Angeles
Currency: USD
Google Maps: https://www.google.com/maps/@37.386051,-122.083851,10z
Wikipedia: https://en.wikipedia.org/wiki/United_States
```

## Future Updates

- Implement more detailed error handling for API requests.
- Add support for more data sources to increase the information provided.
- Improve the user interface for better user experience.
-  (LII) feature to be added soon.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or open an issue if you'd like to contribute to the project.

```

