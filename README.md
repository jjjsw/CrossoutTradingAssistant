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
To automate navigating through each item page in CrossoutDB and extracting their profit, and having the option to export data into CSV (Excel for now) for visual analysis. When I gather enough data, I can also put them in softwares like R for a more statistical analysis.

## How to use:
Hit "run", there will be prompts and helpful (hopefully) error messages guiding you to enter the correct prompts. 

**Note**: after it opens chrome, there might be an ad coming up occupying the whole screen. Please manually close it ASAP, so the program can run smoothly. This part of the program is the only case needing manual operation, as I don't know how to deal with this kind of ad (I cannot inspect its elements as it disappears as soon as I try to). 
