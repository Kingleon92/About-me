from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Get the title of the webpage
title = driver.title

# Set an explicit wait to wait for the text box and submit button
wait = WebDriverWait(driver, 10)

# Find the text box
text_box = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))

# Find the submit button
submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))

# Enter text in the text box
text_box.send_keys("Selenium")

# Click the submit button
submit_button.click()

# Find the message element and get its text
message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
text = message.text

# Print the retrieved text
print("Message:", text)

# Add a delay to keep the browser window open for 10 seconds
time.sleep(40)

# Quit the WebDriver
driver.quit()