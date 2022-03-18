import asyncio


async def diz_oi_demorado():
    print('Oi...')
    await asyncio.sleep(2) # você vai utilizar o await sempre que for executar uma função assíncrona
    print('todos...')



el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()