import aiohttp
import asyncio
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

from loguru import logger

class WebScraper:
    async def __get_useragnet(self):
        return UserAgent().random


    async def __get_headers(self):
        return {
            "user-agent": await self.__get_useragnet()
        }


    async def get__html(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False,headers=await self.__get_headers()) as response:
                html = await response.text()
                logger.info("<status [{}]> <url [{}]>".format(response.status,response.url))
                return html


    async def parse(self):
        info = [list(), list(), list(), list(), list(), list(), list(), list(), list()]
        for x in range(1,2):
            url = "https://www.koolinar.ru/recipes?page={}".format(x)
            for link in (await self.get__recipe_link(url))[:5]:
                row = await self.parse__recipe_info(link)
                for col in range(9):
                    info[col].append(tuple([row[col]]))
        
        return info


    async def get__recipe_link(self, url="https://www.koolinar.ru/recipes?page=2"):
        html = await self.get__html(url)
        soup = BeautifulSoup(html, "lxml")
        try:
            items = soup.find("div", class_='itemListElement').find_all("div", class_="b-item")
        except AttributeError:
            return []
        
        links = ["https://www.koolinar.ru{}".format(item.find("a", class_="b-item__main").attrs["href"])for item in items]
        return links


    async def parse__recipe_info(self, url):
        html = await self.get__html(url)
        soup = BeautifulSoup(html, "lxml")
        try:
            title = soup.find("h1").text
        except AttributeError:
            return


        try:
            category, subcategory = [item.text for item in soup.find("ul", class_="u-list-inline").find_all("span", itemprop="name")[-2:]]        
        except IndexError:
            category, subcategory = None, None
        except AttributeError:
            category, subcategory = None, None


        try:
            kitchen, level =[item.text for item in soup.find_all("p", class_="p-tooltip")[:2]]
        except IndexError:
            kitchen, level = None, None
        

        try:
            ingredients = [item.text for item in soup.find_all("li", itemprop="recipeIngredient")[1:]]
            ingredients = "|||".join(ingredients)
        except IndexError:
            ingredients = ""

        try:
            video_link = soup.find("iframe").attrs["src"]
        except AttributeError:
            video_link = ""


        try:
            for block in soup.find_all("div", class_="b-page-block"):
                try:
                    if block.find("h2", class_="b-page-block__title").text == "Пошаговый рецепт приготовления":
                        cooking = [item.text for item in block.find_all("p")]
                        break
                except AttributeError as ae:
                    if "object has no attribute 'text'" not in str(ae):
                        raise ae
            cooking = "|||".join(cooking)
        except AttributeError:
            cooking = ""
        except UnboundLocalError:
            cooking = ""

        row = (title,url,category,subcategory,kitchen,level,ingredients,cooking,video_link)
        return row
    
        


if __name__ == "__main__":
    ws = WebScraper()
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ws.parse())      