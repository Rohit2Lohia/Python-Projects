response = requests.get("https://www.walmart.com/search/?query=water&cat_id=0")
doc = BeautifulSoup(response.text, 'html.parser')

title_tags = doc.find_all(class_='prod-ProductTitle')

for title in title_tags[:5]:
    print(title.text.strip())



# import scrapy
# from scrapy.http import FormRequest
# from scrapy.utils.response import open_in_browser
#
# class FirstSpider(scrapy.Spider):
#     name="FirstSpider"
#
#     find_video='https://en.savefrom.net/savefrom.php'
#     start_urls = [
#         find_video
#     ]
#         # for url in urls:
#         #     yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         #extract dynamic data from the webpage to fill up the formdata-
#             # Example to fetch csrf token what we can do is:
#             # token= response.css('input[name="csrf_token"]::attr(value)').extract_first() //After this we can use this csrf token in out code
#         # Create python directory with form value-
#         data={
#             'sf_url': 'https://www.youtube.com/watch?v=ULG0z8EjU_M',
#             'sf_submit': '',
#             'new': '1',
#             'lang': 'en',
#             'app': '',
#             'country': 'in',
#             'os': 'Windows',
#         }
#         # Submit a post request to it-
#         yield scrapy.FormRequest(url=self.find_video, formdata=data, callback=self.start_scraping)
#
#     def start_scraping(self, response):
#         # Parse the downloading link of the video
#         open_in_browser(response)
#         print("In Succesfully!!!!!!!!!!!!!")
#         for lk in response.css('div.info-box'):
#             yield {
#                 'video_title': lk.css('div.row title::text').extract_first(),
#                 'video_link': lk.css('div.def-btn-box::attr(href)').extract_first()
#             }
#             print("Done Succesfully!!!!!!!!!!!!!")
