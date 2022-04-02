import aiosqlite
import asyncio
from pathlib import Path
from scripts.webscraper import WebScraper

from .table.decorators import *
from .table.minortable import MinorTable
from .table.maintable import MainTable




class DataBase:
    path=Path(__file__)
    table=dict()


    @connection
    async def bulid(self, connect: aiosqlite.core.Connection):
        wb=WebScraper()
        dt=await wb.parse()
        main_table=list()
        
        it=0
        for el in self.table:
            await self.table[el].push(set(dt[it]))
            it +=1

        for x in range(len(dt[0])):
            col=0
            main_row=list()
            for el in self.table:
                id=await self.table[el].get_id(dt[col][x][0])
                main_row.append(id)
                col +=1
            main_table.append(tuple(main_row))
        await self.MainTable.push(main_table)

    @connection
    async def run(self, connect: aiosqlite.core.Connection):
        cursor=await connect.cursor()
        with open("data/db/sqlrun.txt", "r", encoding="utf-8") as f: 
            exec=f.read()
        await cursor.executescript(exec)


        self.table["recipe"]=MinorTable("recipe")
        self.table["url"]=MinorTable("url")
        self.table["category"]=MinorTable("category")
        self.table["subcategory"]=MinorTable("subcategory")
        self.table["kitchen"]=MinorTable("kitchen")
        self.table["level"]=MinorTable("level")
        self.table["ingredient"]=MinorTable("ingredient")
        self.table["cook"]=MinorTable("cook")
        self.table["video_link"]=MinorTable("video_link")

        self.MainTable=MainTable()

        
        await self.bulid()
            

        


if __name__ =="__main__":
    print("start")
    db=DataBase()
    asyncio.run(db.run())