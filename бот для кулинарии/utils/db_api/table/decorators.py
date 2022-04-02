import aiosqlite

def connection(func):
    async def wrapper(*args, **kwargs):
        connect=await aiosqlite.connect("data/db/database.db")
        kwargs["connect"]=connect
        
        function_result=await func(*args, **kwargs)
        await connect.commit()
        await connect.close()

        return function_result
    return wrapper