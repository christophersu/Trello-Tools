import json
import sys

with open('input.json') as data_file:    
  data = json.load(data_file)
  for card in data['cards']:
    item = '- ' + card['name']
    for label in card['labels']:
      item += ' #' + label['name'].replace(' ', '_').lower()
    
    print item.encode('utf-8').strip()
    
    if 'desc' in card and card['desc']:
      for line in card['desc'].splitlines():
        print '  ' + line.encode('utf-8').strip()