from urllib import request

file_url = input('Enter the website from where you want to download source code: ')

def download_file_information(url):
    #open url file_url
    fileOpen = request.urlopen(url)
    #read the file
    file_info = fileOpen.read()
    # convert binary code to readable string
    file_info_str = str(file_info)

    #Splt the single line to multiple lines
    file_lines = file_info_str.split('\\n')

    #create a new file to store source code
    newfile = open('file.html',"w")
    # store the info in the new file created
    for info in file_lines:
        newfile.write(info + '\n')
    #close the file
    newfile.close()

download_file_information(file_url)
