from discordBot_schoolInfo import *
import asyncio

async def main():
    date = ""   
    while True:
        print("testing day")
        if date != getCurrentDate():
            await nextDay()
        else:
            date = getCurrentDate()
        time.sleep(timeBetweenChecks)


asyncio.run(main())

