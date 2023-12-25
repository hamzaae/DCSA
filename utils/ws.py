
from bs4 import BeautifulSoup
import requests
# from dotenv import load_dotenv
# import os

# ETL function
def run_etl(link):
    try:
        # load_dotenv()

        # add your user agent 
        # usrAgnt = os.getenv("USER_AGENT")
        usrAgnt = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
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
    print(run_etl("https://www.hespress.com/%d8%ac%d8%af%d9%84-%d9a7%d9%84%d9%85%d9%88%d8%aa%d9%89-%d8%a8%d8%a7%d9%84%d8%ac%d8%af%d9%8a%d8%af%d8%a9-1283197.html"))