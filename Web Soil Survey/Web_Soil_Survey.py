from selenium import webdriver
# Basic libraries that define settings for webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Basic libraries that interacts with webpages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from tkinter import Tk, Button, Label, Frame, messagebox

# Path to the ChromeDriver executable
CHROMEDRIVER_PATH = r"D:\Dev\Python\Selenium\\133.0.6943.54\chromedriver-win64\chromedriver.exe"

# Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--start-maximized')

# Initialize WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Main variables 
base_url = 'https://websoilsurvey.nrcs.usda.gov/app/WebSoilSurvey.aspx'

# Function to locate expand address
def locate_and_click_expand_address_button(driver):
    """
    Locates the 'Expand Address' button and clicks it.
    
    Args:
        driver: The Selenium WebDriver instance.
    """
    try:
        # Wait for the element to be present and clickable
        expand_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='right']//span[@class='unfold' and @role='button' and .//span[@class='sr-only' and text()='Expand Address']]"))
        )
        
        # Click the button
        expand_button.click()
        print("Expand Address button clicked successfully.")
    except Exception as e:
        print(f"Failed to locate or click the Expand Address button: {e}")
        
# Function to locate expand address
def locate_and_click_soil_map_tab(driver):
    """
    Locates the 'Soil Map' tab and clicks it.
    
    Args:
        driver: The Selenium WebDriver instance.
    """
    try:
        # Wait for the element to be present and clickable
        expand_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td[@class='tabs']//td[@class='tab-inactive']/div[@id='Soil_Map']"))
        )
        
        # Click the button
        expand_button.click()
        print("Soil Map tab button clicked successfully.")
    except Exception as e:
        print(f"Failed to locate or click the Soil Map tab: {e}")
 
def fill_address_input(driver, test_address):
    """
    Fills the address textarea with the provided test_address using XPath.
    
    Args:
        driver: The Selenium WebDriver instance.
        test_address (str): The address to fill into the textarea.
    """
    try:
        # Wait for the textarea to be present using XPath
        address_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@name='address' and @label='Address']"))
        )
        
        # Clear any existing text (optional)
        address_textarea.clear()
        
        # Fill the textarea with the test_address
        address_textarea.send_keys(test_address)
        print(f"Address textarea filled with: {test_address}")
    except Exception as e:
        print(f"Failed to locate or fill the address textarea: {e}")

def extract_table_data(driver):
    # Define the XPath for the table
    table_xpath = "//table[contains(@class, 'data') and contains(@class, 'first') and contains(@class, 'last')]"
    
    # Define the XPath for all rows inside the tbody section of the table
    rows_xpath = f"{table_xpath}/tbody/tr"
    
    # Initialize a list to store extracted data
    table_data = []
    
    # Locate all table rows within the tbody
    rows = driver.find_elements(By.XPATH, rows_xpath)
    
    # Loop through each row to extract data
    for row in rows:
        # Find all the columns (td elements) in the current row
        cells = row.find_elements(By.XPATH, ".//td")
        
        # Extract text from each cell and strip any extra whitespace
        row_data = [cell.text.strip() for cell in cells]
        
        # Convert row data into a dictionary using column labels as keys
        if len(row_data) == 4:  # Ensure we have the correct number of columns
            row_dict = {
                "Map Unit Symbol": row_data[0],
                "Map Unit Name": row_data[1],
                "Acres in AOI": row_data[2],
                "Percent of AOI": row_data[3]
            }
            table_data.append(row_dict)
    
    return table_data

# Funtions related to GUI
def wait_for_user_to_enter_address (driver):
    print ('Address Entery Confirmed')
    # Placeholder for your get_data function
    print("Getting data...")

# Main function to save data 
def extracting_data(driver):
    # Placeholder for your save_data function
    print ('Main function to extract all data from the page')


def on_address_entered():
    print("Address entered, proceeding to drawing shape...")
    label.config(text="Please draw your AOI and click 'I Drew AOI'.")

def on_aoi_drawn():
    print("AOI drawn, proceeding to extracting data...")
    extracting_data(driver)
    label.config(text="AOI Draw, Proceeding to extracting data.")
    driver.quit()

# Initialize the main window
root = Tk()
root.title("Browser Automation")

# Create a label to provide instructions
label = Label(root, text="Please enter the address")
label.pack(pady=10)

# Create the first button for entering the address
address_button = Button(root, text="I Entered Address", command=on_address_entered)
address_button.pack(pady=5)

# Create the second button for drawing the AOI
aoi_button = Button(root, text="I Drew AOI Shape", command=on_aoi_drawn)
aoi_button.pack(pady=5)

# Addres Example for Testing Saved Here
test_address = '524 boston port madison ct'

# Start the browser automation
try:
    while True:
        # Initialize WebDriver
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print('Initializing browser settings ...')
        
        #time.sleep(5)
        driver.get(base_url)
        print ('Visiting webpage')
        time.sleep(10)
        
        locate_and_click_expand_address_button (driver)
        time.sleep(1)
        
        fill_address_input (driver, test_address)
        
        # Pause and wait for user input
        input("Set View, Adjust View and Draw AOI and Press Enter to continue...")
        time.sleep (2)

        locate_and_click_soil_map_tab (driver)
        
        time.sleep (10)
        
        data_in_soil_map = extract_table_data (driver)
        print (data_in_soil_map)
        
        time.sleep (5)
        
        # Start the GUI event loop
        #root.mainloop()

except Exception as e:
    print("Error occurred: ", e)
finally:
    driver.quit()

