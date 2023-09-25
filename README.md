# Crossout Trading Assistant
A personal project, tells me what items to trade to maximise profit

Written in Python, using libraries BeautifulSoup 4 + selenium

## Crossout
> Crossout is a free-to-play vehicular combat video game focused on building and driving custom vehicles in PvP and PvE scenarios. --Wikipedia

A lot of the items involved in building your car are tradable and craftable in the in-game market using the in-game currency "Coins". It somewhat behaves like a real market so there are things like supply/demand, elasticity of demand, etc.

Item prices are available at CrossoutDB, a player-made (not me!) website

## Pros and cons of [CrossoutDB](https://crossoutdb.com/) from my view:
**Pros:**
This website is wonderful as it gets real-time trading data of items and materials from the game, displaying them in neat tables. Clicking on an item/material in the table takes you to a detailed page with more pricing information, which contains the profit for that item.

**Cons:**
The most useful information (profit) is hidden in each item page, instead of on the table. There are tens or hundreds of items in each level, so manually clicking each item page to check profit is very tedious.

## Goal of this project:
To automate navigating through each item page in CrossoutDB and extracting their profit, and having the option to export data into Excel for visual analysis

