import gpxpy
import gpxpy.gpx
from polyline.codec import PolylineCodec
import sys

def polyline_to_gpx(polyline = None):
    if polyline == None:
        raise Exception("Need a Google Polyline as parameter")

    waypoints = None
    try:
        waypoints = PolylineCodec().decode(polyline)
    except Exception as e:
        raise Exception("Error decoding polyline. err: {}".format(e))

    gpx = gpxpy.gpx.GPX()
    gpx.creator = "Ride with gpxpy"

    for point in waypoints:
        lat, lon = point
        gpx.waypoints.append(gpxpy.gpx.GPXWaypoint(lat, lon))

    return gpx.to_xml()

if __name__ == '__main__':
    print(polyline_to_gpx('egrwFpjubMNwEe@yBWqApAn@xEzBPFZJ`DXhHr@`DVLGL?bBN^qIDa@n@aBjCaHvF{Np@uBnAaDqFmEc@pAKT'))
    # polyline_to_gpx(sys.argv[1])
