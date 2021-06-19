from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

session = HTMLSession()

def get_video_info(url):
    # download HTML code
    response = session.get(url)
    # execute Javascript
    response.html.render(sleep=1, timeout=20)
    # create beautiful soup object to parse HTML
    soup = bs(response.html.html, "html.parser")
    # open("index.html", "w").write(response.html.html)
    # initialize the result
    result = {}
    # video title
    result["title"] = soup.find("h1").text.strip()    
    # video views (converted to integer)
    result["views"] = int(''.join([ c for c in soup.find("span", attrs={"class": "view-count"}).text if c.isdigit() ]))
    # video description
    result["description"] = soup.find("yt-formatted-string", {"class": "content"}).text
    # date published
    result["date_published"] = soup.find("div", {"id": "date"}).text[1:]
    # get the duration of the video
    result["duration"] = soup.find("span", {"class": "ytp-time-duration"}).text
    # get the video tags
    result["tags"] = ', '.join([ meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"}) ])
    # number of likes
    text_yt_formatted_strings = soup.find_all("yt-formatted-string", {"id": "text", "class": "ytd-toggle-button-renderer"})
    result["likes"] = ''.join([ c for c in text_yt_formatted_strings[0].attrs.get("aria-label") if c.isdigit() ])
    result["likes"] = 0 if result['likes'] == '' else int(result['likes'])
    # number of dislikes
    result["dislikes"] = ''.join([ c for c in text_yt_formatted_strings[1].attrs.get("aria-label") if c.isdigit() ])
    result['dislikes'] = 0 if result['dislikes'] == '' else int(result['dislikes'])
    # channel details
    channel_tag = soup.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a")
    # channel name
    channel_name = channel_tag.text
    # channel URL
    channel_url = f"https://www.youtube.com{channel_tag['href']}"
    # number of subscribers as str
    channel_subscribers = soup.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()
    result['channel'] = {'name': channel_name, 'url': channel_url, 'subscribers': channel_subscribers}
    return result

url = "https://youtu.be/1bwhyD7RPVw"

print(get_video_info(url))

# def search_dict(partial, key):
#     if isinstance(partial, dict):
#         for k, v in partial.items():
#             if k == key:
#                 yield v
#             else:
#                 for o in search_dict(v, key):
#                     yield o
#     elif isinstance(partial, list):
#         for i in partial:
#             for o in search_dict(i, key):
#                 yield o

# def find_value(html, key, num_sep_chars=2, separator='"'):
#     start_pos = html.find(key) + len(key) + num_sep_chars
#     end_pos = html.find(separator, start_pos)
#     return html[start_pos:end_pos]

# def get_comments(url):
#     session = requests.Session()
#     # make the request
#     res = session.get(url)
#     # extract the XSRF token
#     xsrf_token = find_value(res.text, "XSRF_TOKEN", num_sep_chars=3)