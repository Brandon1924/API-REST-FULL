import requests

def api():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=15"
    try:
        res = requests.get(url)
        datos = res.json()

        terremotos = datos ['features']
        numTerr = 1
        for terremoto in terremotos:
            lugar = terremoto[ 'properties']['place']
            magnitud = terremoto[ 'properties']['mag']
            coordenadas = terremoto[ 'geometry' ]['coordinates']
            longitud = coordenadas [0]
            latitud = coordenadas [1]
            profundidad = coordenadas [2]

            print(f"Lugar: {lugar}, Magnitud: {magnitud}")
            print (f"Coordenadas: Longitud {longitud}, Latitud {latitud}, Profundidad {profundidad}")
            numTerr +=1

    except Exception as e:
        print(f"Error: {e}")

    input("Enter para salir")
api()