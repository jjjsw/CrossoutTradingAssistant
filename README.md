# Crossout Trading Assistant
A personal project, tells me what items to trade to maximise profit

Written in Python, using libraries BeautifulSoup 4 + selenium

# Context:

## What is Crossout?
> Crossout is a free-to-play vehicular combat video game focused on building and driving custom vehicles in PvP and PvE scenarios. --Wikipedia

## Items and in-game market:
A lot of the items involved in building your car are tradable and craftable in the in-game market using the in-game currency "Coins". Each item can be crafted with 2 types of ingredients: lower level items, and materials. The lowest level items are purely made of materials.

To acquire powerful high level items, grinding the game is an option but it takes too much time. So the best option to quickly get lots of coins is by "playing the market" which is to craft profitable items and sell them to gain coins.

The market allows players to post a **sell offer** for an item or material they own, and set a price at which they want to sell them at. Players can also post a **buy order** for an item/material and set a price at which they want to buy them at. Since the buyer almost always wants to buy something for as little as possible, while the seller wants to sell it as high as possible, each tradable item/material always has their lowest offer price being larger than their highest order price. 

To buy item/material, you can either:
- buy it at the lowest offer price, where the game immediately processes your order and you receive it instantly, or
- buy it at a price higher than the lowest offer price, where the game creates an order and waits an unknown amount of time before processing it.

To save time, I will buy things at their lowest offer price.

## Pros and cons of [CrossoutDB](https://crossoutdb.com/) from my view:
**Pros:**

This player-made website is wonderful as it gets real-time trading data of items and materials from the game, displaying them in neat tables. 

Common fields of tables are: '''sell price''', '''craft cost (sell)''' (crafting cost where you buy all ingredients at lowest offer price), '''buy price''', '''craft cost (buy)''' (crafting cost where you buy all ingredients at highest order price), '''crafting margin'''.

Clicking on an item/material in the table takes you to a detailed page with more pricing information, such as crafting cost and profit, where profit = sell price - craft cost, and of course craft cost depends on whether you buy the ingredients or craft them yourself, and if buying, which price you buy at (lowest offer price or highest order price?)

When I trade, I naturally want to sell items with highest profit.

**Cons:**

The main con is that the useful information (profit) is hidden in each item page, instead of on the table. There are tens or hundreds of items in each level, so manually clicking each item page to check profit is very tedious.

**The goal of this personal project: to automate navigating through each item page and extracting their profit**

