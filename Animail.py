import requests
import smtplib
from bs4 import BeautifulSoup as bs
from os import path

############################################

def main():

    anime1 = []
    url = []
    try:
        with open("db/Anime.txt",'r') as file:
            for name in file:
                anime1.append(name.strip())
    except:
        print("No file found")
        exit()

    try:
        with open("db/links.txt",'r') as file:
            for link in file:
                url.append(link.strip())
    except:
        print("No file found")
        exit()
    currentCount = 0
    anicount = 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    for curl in url:

        response = requests.get(curl, headers=headers)

        soup = bs(response.text,"lxml")
        pageUpper = soup.text.upper()
        found = pageUpper.count(anime1[anicount].upper() +" EPISODE") + pageUpper.count(anime1[anicount].upper() +" SEASON")

        filepath ="db/"+anime1[anicount]+".txt"
        firstcheck = path.exists(filepath)

    # checks if there is a database for the anime if not, creates one  and "registers" it
        if not firstcheck:
            with open(filepath,"w") as file:
                file.write(str(found))
                # anime now registered message
        # otherwise, checks if the found number is greater than what was in the DB
        # if so, sends message, and updates the database
        else:
            with open(filepath,"r") as file:
                currentCount = int(file.read())
                print(f"total count of {anime1[anicount]} Episode found on page: {str(currentCount)}")
            if found > currentCount:
                sendMessage(anime1[anicount],url[anicount])
                with open(filepath,"w") as file:
                    file.write(str(found))
        anicount+=1


def sendMessage(anime,url):
    #send message

    # create an email message with just a subject line,
    SUBJECT = 'New '+anime+' episode!'
    TEXT = 'New Episode of ' +anime+" out now!\n view now @ " +url
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # set the 'from' address,
    fromaddr = 'gabriel.r.mata96@gmail.com'
    # set the 'to' addresses,
    #fill out with to addresses
    *********toaddrs = []********

    # setup the email server,
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # add my account login name and password,
    #needs to be filled in with email and server password
    *********server.login()*************

    # Print the email's contents
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
    print('Message: ' + msg)


    # send the email
    server.sendmail(fromaddr, toaddrs, msg)
    # disconnect from the server
    server.quit()

if __name__ == '__main__':
    main()