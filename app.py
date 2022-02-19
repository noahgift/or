from fastapi import FastAPI
import uvicorn

app = FastAPI()

def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1,5,10,25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem  = divmod(int(amount*100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num:coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})
    return res


@app.get("/")
async def root():
    return {"message": "Hello Greedy Algorithms"}

@app.get("/change/{dollar}/{cents}")
async def changeit(dollar: int, cents: int):
    """make change"""

    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return {"change": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')