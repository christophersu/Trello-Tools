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
      count = 0
      for line in card['desc'].splitlines():
        if count == 0:
          sys.stdout.write('  "')
        else:
          sys.stdout.write('  ')

        sys.stdout.write(line.encode('utf-8').strip())

        if count == len(card['desc'].split('\n'))-1:
          sys.stdout.write('"')

        sys.stdout.write('\n')

        count += 1