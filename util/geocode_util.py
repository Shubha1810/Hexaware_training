import requests


class GeoCodeUtil:
    @staticmethod
    def get_coordinates(location_name):
        try:
            url = "https://nominatim.openstreetmap.org/search"
            params = {
                'q': location_name,
                'format': 'json'
            }
            response = requests.get(url, params=params, headers={'User-Agent': 'CARS-System'})
            data = response.json()
            if data:
                lat = float(data[0]['lat'])
                lon = float(data[0]['lon'])
                return lat, lon
            else:
                raise ValueError("Location not found.")
        except Exception as e:
            print(f"Error fetching coordinates: {e}")
            return None, None
