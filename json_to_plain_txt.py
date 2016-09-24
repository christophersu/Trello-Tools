import json
import sys

with open('input.json') as data_file:    
  data = json.load(data_file)
  items = {}
  for card in data['cards']:
    if card['idList'] not in items:
      items[card['idList']] = []
    items[card['idList']].append(card)

  for key, value in items.iteritems():
    print '- ' + key
    indent = '  '
    for card in value:
      item = indent + '- ' + card['name'].strip()
      for label in card['labels']:
        item += ' #' + label['name'].replace(' ', '_').lower()
      
      print item.encode('utf-8')
      
      if 'desc' in card and card['desc']:
        for line in card['desc'].splitlines():
          print indent + '  ' + line.encode('utf-8')