#-----Script to automatically download youtube videos--------#
# Make sure you have selenium and chromedriver installed in your device
# You also need to add chromedriver to PATH in environmental variable
# And you are good to GO!
from selenium import webdriver
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

urls = [
    # Enter the youtube video URls you want to download here
    "https://www.youtube.com/watch?v=ULG0z8EjU_M",
    "https://www.youtube.com/watch?v=gCMU9LdUV5o"
]
left_urls=[]

# Website from which we will download our youtube videos
webpage = "https://en.savefrom.net/1-youtube-video-downloader-1/"
# add the Path where you have downloaded your chrome driver
driver=webdriver.Chrome(executable_path='<path>\chromedriver.exe')

for url in urls:
    driver.get(webpage)
    driver.maximize_window()
    # Here we are finding the search box
    input=driver.find_element_by_name("sf_url")
    input.send_keys(url)
    print("URL entered.\n")
    # Here we are finding the Download button and then clicking it
    send_req=driver.find_element_by_name("sf_submit")
    send_req.click()

    # All the try exception blocks are used so that you don't need to worry if your code crash
    # and if any of the link didn't get downloaded ill save if for your in a text file so that you
    # don't need worry about videos that are not downloaded

    # This try/except block wait for the download box to appear
    try:
        WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"clip")))
    except TimeoutException:
        print("Server Time Out or there is some problem with the url.\n")

    # This try/except block wait for the download link to appear and download it if it appears.
    try:
        WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"def-btn-box")))
        print("Ready to download...\n")
        download = driver.find_element_by_class_name('def-btn-box')
        download.click()
        print("Done!\n")
    except TimeoutException:
        print("Cannot find download link\n")
        left_urls.append(url)
    driver.refresh()

# Final logic to store the URL's which are not downloaded in undownloaded.txt
if len(left_urls):
    with open('undownloaded.txt','a') as nw_file:
        nw_file.write('\n')
        for url in left_urls:
            nw_file.write('"'+url+'",\n')
        nw_file.write("_"*100)
else:
    print("All the videos were succesfully downloaded!!")
    print("_"*100)
