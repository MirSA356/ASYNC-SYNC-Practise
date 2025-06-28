#async example just like dosri biwi

import asyncio

async def dosri_biwi():
    print("Pani ubalna shuru kr diya Sain...")
    await asyncio.sleep(3)
    print("Pani ubal gya Sain...")

async def dosri_biwias():
    print("Roti banana shuru krdiya hai Sain...")
    await asyncio.sleep(5)
    print("Roti bana di hai Sain...")

async def dosrishadi():
    await asyncio.gather(
          dosri_biwi(),
          dosri_biwias() 
    )

asyncio.run(dosrishadi())    
         