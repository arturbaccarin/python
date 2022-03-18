import asyncio

# coroutine - a function which can pause and resume its execution.
async def diz_oi(): # transforma a função em uma corotina
    print('Oi...')


# el = event loop
el = asyncio.get_event_loop()
el.run_until_complete(diz_oi())
el.close()