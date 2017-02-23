from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import ast
import requests
import os
from io import BytesIO
import sys
import dota2api
import time

def get_data(api, runs, curr_run, heroes_list):
    '''Gets data from the api and from the saved .txt file
    Takes the api key, the number of times it should access this data, its current run number, and a hero list (only used if called recursively)
    Returns a list of every matches' heroes and whether or not that hero won'''
    matches = api.get_match_history()['matches']
    for m in matches:
        #Temp_match stores a match from match history to get details from
        temp_match = api.get_match_details(m['match_id'])
        for p in temp_match['players']:
            try:
                #heroes_list stores a list of every hero in every game and whether or not they won
                heroes_list.append((p['hero_name'], [int(temp_match['radiant_win'] == (p['player_slot'] < 100)), 1]))
            except KeyError:
                continue
    if curr_run != runs:
        #Wait 10 minutes, then retrieve data again
        time.sleep(600)
        return get_data(api, runs, curr_run + 1, heroes_list)
    else:
        data_file = open('hero_data.txt', 'r')
        if os.path.getsize('hero_data.txt') > 0:
            for line in data_file:
                if len(str(line)) > 5:
                    #adds data from hero_data.txt to the hero_list to record more data
                    heroes_list.append(ast.literal_eval(line))
        return heroes_list

def win_loss(api):
    '''Combines the hero list from get_data into a dictionary containing each hero's total wins and total games
    Takes api key
    Returns dictionary of each hero's name, wins, and games
    '''
    #The second argument in get_data() controls how man multiples of 100 matches you wish to parse. Each extra value increases the time it takes to parse by 10 minutes, because it has to wait for matches to finish
    heroes_list = get_data(api, 1, 1, [])
    heroes_win_loss = dict()
    for h in heroes_list:
        try:
            #If key exists in dictionary, add to win/loss ratio
            heroes_win_loss[h[0]][0] += h[1][0]
            heroes_win_loss[h[0]][1] += h[1][1]
        except KeyError:
            #If key doesn't exist, make key and value
            heroes_win_loss[h[0]] = [h[1][0], h[1][1]]
    return heroes_win_loss

def analyze_winrates(api):
    '''Calculates and returns the win/loss percentage for each hero as a sorted list with best winrate first.
    Also writes this data to a .txt file for future use
    Takes api key
    Returns an updated .txt file and each hero's win/loss percentage
    '''
    heroes_win_loss = win_loss(api)
    #Condenses the list so each hero only has 1 entry
    heroes_winrates = sorted(heroes_win_loss.items(), key=lambda x: x[1][0]/x[1][1])
    heroes_winrates.reverse()
    data_file = open('hero_data.txt', 'w')
    for item in heroes_winrates:
        #Add current hero data to hero_data.txt for future references
        data_file.write('\n%s' % str(item))
    return heroes_winrates

def image_getter(api, hero_list):
    '''This access the Valve Dota 2 API for a different reason:
    to get the (shrinked) portaits for each hero to make a visual representation of the results
    Takes api key and sorted list of heroes to order the portraits by hero winrate
    Returns sorted list of smaller hero portraits by winrate
    '''
    responses = []
    imgs = []
    for i in hero_list:
        for h in api.get_heroes()['heroes']:
            if i[0] in h.values():
                #imgs is a list of all hero portraits taken from the dota 2 api
                imgs.append(Image.open(BytesIO(requests.get(h['url_vertical_portrait']).content)))
                break
    for x in range(0, len(imgs)):
        #resizes image to 20x23 pixels
        imgs[x].thumbnail((20,23))
    return imgs

if __name__ == "__main__":
    api = dota2api.Initialise("15AAE9A1476574CC7F10222BAC216383")
    data_file = open('hero_data.txt', 'r')
    heroes_winrates = analyze_winrates(api)
    imgs = image_getter(api, heroes_winrates)
    widths, heights = zip(*(i.size for i in imgs))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height + 12), (255,255,255))
    x_offset = 0
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 11)
    for im in imgs:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
        d = ImageDraw.Draw(new_im)
        d.text((2 + imgs.index(im)*20, 22), str(round(100*(heroes_winrates[imgs.index(im)][1][0]/heroes_winrates[imgs.index(im)][1][1]))), font = fnt, fill=(255, 0, 0))
    print(heroes_winrates)
    new_im.save('test.jpg')
