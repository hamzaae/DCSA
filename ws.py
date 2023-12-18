
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
        HEADERS = ({'User-Agent': usrAgnt, 'Accept-Language': 'en-US, en;q=0.5'})

        # HTTP Request
        webpage = requests.get(link, headers=HEADERS)

        # Soup Object containing all data
        soup = BeautifulSoup(webpage.content, "html.parser")

        title_element = soup.find("h1", attrs={'class': 'post-title'})
        comments_elements = soup.find_all("div", attrs={'class': 'comment-text'})

        if title_element and comments_elements:
            title = title_element.text.strip()
            comments_list = [comment.find("p").text.strip() for comment in comments_elements]
            return title, comments_list
        else:
            return None, None

    except requests.exceptions.RequestException as e:
        # Handle any request exception (e.g., connection error)
        return f"Error: {e}", None

    except Exception as e:
        # Handle any other exception that might occur
        return f"An unexpected error occurred: {e}", None



    

if __name__ == "__main__":
    print(run_etl(""))