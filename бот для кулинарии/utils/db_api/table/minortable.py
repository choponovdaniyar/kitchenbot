from .decorators import *

class MinorTable:
    def __init__(self, name):
        self.name=name
    
    @connection
    async def push(self, data, connect: aiosqlite.core.Connection):
        cursor=await connect.cursor()
        await cursor.executemany('''
            INSERT INTO {}(name)
            VALUES (?)
        '''.format(self.name), data)
    
    @connection
    async def get_id(self, name, connect: aiosqlite.core.Connection):
        cursor=await connect.cursor()
        await cursor.execute('''
            SELECT id
            FROM {}
            WHERE name='{}' 
        '''.format(self.name, name))

        result=await cursor.fetchone()
        if result !=None:
            return result[0]
        return None
    
    @connection
    async def get_name(self, id, connect: aiosqlite.core.Connection):
        cursor=await connect.cursor()
        await cursor.execute('''
            SELECT name
            FROM {}
            WHERE id={}
        '''.format(self.name, id))

        result=await cursor.fetchone()
        if result !=None:
            return result[0]
        return None
