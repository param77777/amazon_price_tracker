# Amazon Price Tracker

This Python script monitors the price of an item on a given website and sends an email alert when the price drops below a specified threshold.

## Features
- Scrapes item price from the target website using BeautifulSoup.
- Sends an email notification if the price is below a set threshold.

## Prerequisites
Before running this script, ensure you have the following:

1. Python 3.x installed on your system.
2. The following Python libraries installed:
   - `beautifulsoup4`
   - `python-dotenv`
   - `requests`
   - `smtplib` (default library)

## Setup

1. Clone this repository or copy the script to your local system.
2. Create a `.env` file in the root directory and add your email credentials:
   ```
   MY_EMAIL=your_email@gmail.com
   MY_PASSWORD=your_password
   ```
3. Replace the URL in the `practice_url` variable with the desired webpage to monitor.
4. Set the `buy_price` variable to your desired price threshold.

## Notes
- Ensure the website being scraped allows automated requests and complies with their terms of service.
- The `MY_EMAIL` must be a Gmail account, as the script uses Gmail's SMTP server. Ensure you enable "Less Secure App Access" in your Google account settings or use an App Password if 2FA is enabled.
- The class name used in `soup.find(class_="a-offscreen")` should match the target element's class name on the webpage. Update this as needed.

## Example Output
If the price drops below the threshold, you'll receive an email with the subject and body:

**Subject:** Price Alert: Item is below $100!  
**Body:** The current price is $99.99. Check it out here: https://appbrewery.github.io/instant_pot/

---

Feel free to customize the script and README file as needed for your specific use case. Happy coding!
