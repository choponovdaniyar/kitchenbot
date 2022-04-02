from .decorators import *

class MainTable:
    name = "main"
    @connection
    async def push(self, data, connect: aiosqlite.core.Connection):
        cursor=await connect.cursor()
        await cursor.executemany('''
            INSERT INTO {}(
                recipe,
                url,
                category,
                subcategory,
                kitchen,
                level,
                ingredient,
                cook,
                video_link
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''.format(self.name), data)
    