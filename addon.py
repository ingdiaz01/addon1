import sys
import xbmcgui
import xbmcplugin
import json

# Cargar la lista JSON
data = '''
[
  {
    "teams": "18:40 Detroit Tigers vs Minnesota Twins",
    "hora": "6:40 PM",
    "urlhome": "https://mlbbox.me/mlb//detroit-tigers-vs-minnesota-twins-live/mlb/stream-2",
    "urlvise": "https://mlbbox.me/mlb//detroit-tigers-vs-minnesota-twins-live/mlb/stream-3"
  },
  {
    "teams": "18:40 Philadelphia Phillies vs Pittsburgh Pirates",
    "hora": "6:40 PM",
    "urlhome": "https://mlbbox.me/mlb//philadelphia-phillies-vs-pittsburgh-pirates-live/mlb/stream-2",
    "urlvise": "https://mlbbox.me/mlb//philadelphia-phillies-vs-pittsburgh-pirates-live/mlb/stream-3"
  },
  {
    "teams": "18:50 Tampa Bay Rays vs San Francisco Giants",
    "hora": "6:50 PM",
    "urlhome": "https://mlbbox.me/mlb//tampa-bay-rays-vs-san-francisco-giants-live/mlb/stream-2",
    "urlvise": "https://mlbbox.me/mlb//tampa-bay-rays-vs-san-francisco-giants-live/mlb/stream-3"
  },
  {
    "teams": "19:05 Baltimore Orioles vs Milwaukee Brewers",
    "hora": "7:05 PM",
    "urlhome": "https://mlbbox.me/mlb//baltimore-orioles-vs-milwaukee-brewers-live/mlb/stream-2",
    "urlvise": "https://mlbbox.me/mlb//baltimore-orioles-vs-milwaukee-brewers-live/mlb/stream-3"
  }
]
'''

# Convertir la cadena JSON a una lista de diccionarios
games = json.loads(data)

# Crear una lista de elementos para mostrar en Kodi
list_items = []
for game in games:
    list_item = xbmcgui.ListItem(label=game["teams"], label2=game["hora"])
    list_item.setInfo('video', {'title': game["teams"], 'genre': 'MLB'})
    url = game["urlhome"]  # Puedes cambiar a urlvise si es necesario
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=list_item)

# Indicar a Kodi que muestre la lista de elementos
xbmcplugin.endOfDirectory(int(sys.argv[1]))
