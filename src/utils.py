import googlemaps

GOOGLE_MAPS_API_KEY = "YOUR_API_KEY_HERE"


def geocode_with_quality(address: str):
    try:
        gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
        results = gmaps.geocode(address)
        if not results:
            return {
                "lat": None,
                "lng": None,
                "location_type": None,
                "partial_match": None,
                "formatted_address": None,
            }

        r0 = results[0]
        loc = r0["geometry"]["location"]

        return {
            "lat": loc["lat"],
            "lng": loc["lng"],
            "location_type": r0["geometry"].get("location_type"),
            "partial_match": r0.get("partial_match", False),
            "formatted_address": r0.get("formatted_address"),
        }

    except Exception as e:

        print(e)

        return {
            "lat": None,
            "lng": None,
            "location_type": None,
            "partial_match": None,
            "formatted_address": None,
        }
