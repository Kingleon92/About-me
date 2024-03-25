import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("http://localhost:3000/")  # Replace with your website URL

# Track start time
start_time = time.time()

# Track scroll position
prev_scroll_position = 0

# Track button clicks
button_click_count = 0

# Track page title and paragraph text
metrics = []

try:
    while True:
        # Calculate presence time
        presence_time = time.time() - start_time

        # Track scrolling
        current_scroll_position = driver.execute_script("return window.pageYOffset")
        scroll_distance = abs(current_scroll_position - prev_scroll_position)

        # Track button clicks (example: clicking a button with id "my-button")
        # button = driver.find_element(By.ID, "my-button")
        # button.click()
        # button_click_count += 1

        # Track title and paragraph contents
        title = driver.title
        paragraph_text = driver.find_element(By.TAG_NAME, "p").text

        # Save metrics in a dictionary
        metric = {
            "presence_time_seconds": presence_time,
            "scroll_distance_pixels": scroll_distance,
            "title": title,
            "paragraph_text": paragraph_text
        }
        metrics.append(metric)

        time.sleep(2)  # Wait for 2 seconds before the next iteration

except KeyboardInterrupt:
    print("Script stopped by user")

finally:
    # Write metrics to CSV file
    with open("metrics.csv", "w", newline="") as csvfile:
        fieldnames = ["presence_time_seconds", "scroll_distance_pixels", "title", "paragraph_text"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics)

    # Quit the WebDriver
    driver.quit()
