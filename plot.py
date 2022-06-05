# pip install plotly 5.8.0
import plotly.graph_objects as go

def mapsInit(fig):

    fig.update_layout(
    margin ={'l':50,'t':50,'b':50,'r':50},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})
    
def addRoute(fig,name,position):
    '''
    name --> (str) name of the line
    position --> (tuple) ((lon1,lon2), (lat1,lat2))

    '''
    lonPath = position[0][0]
    latPath = position[0][1]
    city = position[1]

    fig.add_trace(go.Scattermapbox(
        name = name,
        text = city,
        mode = "markers+lines",
        lon = lonPath,
        lat = latPath,
        marker = {'size':10}))

def mark(fig ,markName, position,name='My IP'):
    '''
    position --> (tuple) (lon,lat)
    '''
    lonPath = position[0]
    latPath = position[1]
    fig.add_trace(go.Scattermapbox(
        name = name,
        text = markName,    
        mode = "markers+text",
        lon = (lonPath,),
        lat = (latPath,),
        marker = {'size': 15}
        ))
