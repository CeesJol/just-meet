from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import os


def check_button_status(driver):
    try:
        # Find the button by its ID
        button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[contains(@class, "css-4hueae") and contains(text(), "14")]'))
        )

        # Check if the button is disabled
        if not button.is_enabled():
            print(datetime.datetime.now(), "oh no!")
        else:
            print(datetime.datetime.now(), "oh yes!")
            os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format("De knop is enabled!", "just-meet"))

    except Exception as e:
        print(f"Error: {e}")


# Set up the webdriver (assuming you have downloaded chromedriver and it's in the PATH)
driver = webdriver.Chrome()

# Navigate to the webpage
# driver.get("https://widget.thefork.com/nl/2e177ddb-bd65-4b4b-a0f5-731c147a5593")


# date-2024-02-14

# Run the script indefinitely
while True:
    # Refresh the page
    # driver.refresh()
    driver.get(
        "https://widget.thefork.com/nl/2e177ddb-bd65-4b4b-a0f5-731c147a5593")

    # Click on day button
    vandaag_div = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="css-1ygkeox" and text()="Vandaag"]'))
    )
    vandaag_div.click()

    # Check the button status
    check_button_status(driver)

    # Wait for a minute before checking again
    time.sleep(60)

# Close the webdriver when done
driver.quit()
