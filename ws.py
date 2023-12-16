
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("h1", attrs={"class":'sc-1g3sn3w-12 jUtCZM'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("p", attrs={'class':'sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ'}).text.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("p", attrs={'class':'sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Rating
def get_location(soup):

    try:
        location = soup.find("span", attrs={'class':'sc-1x0vz2r-0 iotEHk'}).text.strip()
    
    except AttributeError:
        try:
            location = soup.find("span", attrs={'class':'sc-1x0vz2r-0 iotEHk'}).string.strip()
        except:
            location = ""	

    return location

# Function to extract Number of User Reviews
def get_time(soup):
    try:
        time = soup.find("time").string.strip()

    except AttributeError:
        time = ""	

    return time

# Function to extract Availability Status
def get_description(soup):
    try:
        description = soup.find("p", attrs={'class':'sc-ij98yj-0 fAYGMO'})
        description = description.text.strip()

    except AttributeError:
        description = "Not Available"	

    return description

# ETL function
def run_etl(link):

    try:
        load_dotenv()

        # add your user agent 
        usrAgnt = os.getenv("USER_AGENT")
        HEADERS = ({'User-Agent':usrAgnt, 'Accept-Language': 'en-US, en;q=0.5'})

        # HTTP Request
        webpage = requests.get(link, headers=HEADERS)

        # Soup Object containing all data
        soup = BeautifulSoup(webpage.content, "html.parser")

        comments = soup.find_all("div", attrs={'class':'comment-text'})
        comments_list = []

        # Loop for extracting links from Tag Objects
        for comment in comments:
                comments_list.append(comment.find("p").text.strip())
        
        return comments_list
    except requests.exceptions.RequestException as e:
        # Handle any request exception (e.g., connection error)
        return f"Error: {e}"

    except Exception as e:
        # Handle any other exception that might occur
        return f"An unexpected error occurred: {e}"


    

if __name__ == "__main__":
    print(run_etl("https://www.hespress.com/"))