from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# List of domain names to search
domain_names = [
    "achieveai.com", "astrologyai.com", "applyai.com", "helpingai.com", "helpai.com",
    "journeyai.com", "guardai.com", "tradingai.com", "tradeai.com", "thoughtai.com",
    "processai.com", "assetai.com", "marketingai.com", "systemai.com", "pathsai.com",
    "careerai.com", "versionai.com", "secretai.com", "trendai.com", "entryai.com",
    "raceai.com", "caseai.com",
]

# Set up the Selenium web driver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Uncomment for headless mode
driver = webdriver.Chrome(options=options)

def get_search_input():
    """Dynamically locate the search input field based on its id."""
    try:
        # on first site loading
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "static-domain-search-domain-search-input"))
        )
    except TimeoutException:
        # once the first search is done
        # If the first ID is not found, try the second one
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-query"))
        )

# Open Namecheap domain search page
driver.get("https://www.namecheap.com")

results = {}

try:
    for domain in domain_names:
        print("Searching:", domain)

        # Wait until the search input is visible
        search_input = get_search_input()
        # Clear the input field
        search_input.clear()

        # Enter the domain name
        search_input.send_keys(domain)
        search_input.send_keys(Keys.RETURN)

        # Wait for results to load (use WebDriverWait instead of sleep)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "domain-com"))
        )

        # Check for available domains
        try:
            available_domains = driver.find_elements(By.CLASS_NAME, "domain-com.available")
            if available_domains:
                print(f"Available domain found for {domain}.")
                for domain_element in available_domains:
                    name_element = domain_element.find_element(By.CSS_SELECTOR, "div.name h2")
                    price_element = domain_element.find_element(By.CSS_SELECTOR, "div.price strong")
                    results[domain] = {
                        "name": name_element.text,
                        "price": price_element.text
                    }
        except NoSuchElementException:
            results[domain] = "No available domains found."
        except Exception as e:
            results[domain] = f"Error retrieving availability details: {e}"

finally:
    # Close the browser
    driver.quit()

# Print the results
for domain, details in results.items():
    if isinstance(details, dict):
        print(f"{domain}: Name: {details['name']}, Price: {details['price']}")
    else:
        print(f"{domain}: {details}")
