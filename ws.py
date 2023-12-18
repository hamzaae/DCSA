
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

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

        title = soup.find("h1", attrs={'class':'post-title'}).text.strip()
        comments = soup.find_all("div", attrs={'class':'comment-text'})
        comments_list = []

        # Loop for extracting links from Tag Objects
        for comment in comments:
                comments_list.append(comment.find("p").text.strip())
        
        return title, comments_list
    except requests.exceptions.RequestException as e:
        # Handle any request exception (e.g., connection error)
        return f"Error: {e}"

    except Exception as e:
        # Handle any other exception that might occur
        return f"An unexpected error occurred: {e}"


    

if __name__ == "__main__":
    print(run_etl(""))