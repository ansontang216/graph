import dash
import dash_cytoscape as cyto
import dash_html_components as html
import dash_core_components as dcc
from pprint import pprint
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

countId = 0
xPos = 50
yPos = 50
# arrNodes = [('0', '0', 50, 50), ('1', '1', 100, 100)]
arrNodes = []
arrEdges = []


for i in range(100):
    arrNodes.append((str(i), "Node {}".format(i), xPos, yPos));
    if(countId >= 1):
        newEdge = (str(countId),str(countId-1))
        arrEdges.append(newEdge)
    arrEdges.append((str(countId),str(countId-20)))
    arrEdges.append((str(countId),str(countId-30)))
    countId += 1


# arrNodes.append(('0', '0', 50, 50))
# arrNodes.append( ('1', '1', 100, 100))

# nodes = [
#     {
#         'data': {'id': short, 'label': label},
#         'position': {'x': 20*lat, 'y': -20*long}
#     }
#     for short, label, long, lat in (
#         ('la', 'Los Angeles', 34.03, -118.25),
#         ('nyc', 'New York', 40.71, -74),
#         ('to', 'Toronto', 43.65, -79.38),
#         ('mtl', 'Montreal', 45.50, -73.57),
#         ('van', 'Vancouver', 49.28, -123.12),
#         ('chi', 'Chicago', 41.88, -87.63),
#         ('bos', 'Boston', 42.36, -71.06),
#         ('hou', 'Houston', 29.76, -95.37)
#     )
# ]

# edges = [
#     {'data': {'source': source, 'target': target}}
#     for source, target in (
#         ('van', 'la'),
#         ('la', 'chi'),
#         ('hou', 'chi'),
#         ('to', 'mtl'),
#         ('mtl', 'bos'),
#         ('nyc', 'bos'),
#         ('to', 'hou'),
#         ('to', 'nyc'),
#         ('la', 'nyc'),
#         ('nyc', 'bos')
#     )
# ]

nodes = [
    {
        'data': {'id': id, 'label': label},
        'position': {'x': x, 'y': y}
    }
    for id, label, x, y in arrNodes
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in arrEdges
]

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'label': 'data(label)'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'line-color': '#A3C4BC'
        }
    }
]

# arrNodes.append(('0', '0', 50, 50))
# arrNodes.append( ('1', '1', 100, 100))

app.layout = html.Div([
    # html.Div([
    #     html.Button('Add Node', id='btn-add-node', n_clicks_timestamp=0),
    #     html.Button('Remove Node', id='btn-remove-node', n_clicks_timestamp=0),
    #     dcc.Interval(
    #         id='interval-component',
    #         interval=1*1000, # in milliseconds
    #         n_intervals=0
    #     )
    # ]),

    cyto.Cytoscape(
        id='cytoscape-elements-callbacks',
        layout={'name': 'circle'},
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '800px'},
        elements=edges+nodes
    )
])


# @app.callback(Output('cytoscape-elements-callbacks', 'elements'),
#               [Input('btn-add-node', 'n_clicks_timestamp'),
#                Input('btn-remove-node', 'n_clicks_timestamp'),
#                Input('interval-component', 'n_intervals')],
#               [State('cytoscape-elements-callbacks', 'elements')])
# def update_elements(btn_add, btn_remove ,interval, elements):
#     global arrNodes
#     global arrEdges
#     global countId
#     global xPos
#     global yPos
#     # If the add button was clicked most recently
#     if int(btn_add) > int(btn_remove):
#         newNode = (str(countId),str(countId),xPos,yPos)
        
#         if(countId >= 1):
#             newEdge = (str(countId),str(countId-1))
#             arrEdges.append(newEdge)

#         arrNodes.append(newNode)
#         # elements.append(newNode)
#         countId += 1
#         xPos += 50
#         yPos += 50
#         for i in arrNodes:
#             print(arrNodes)
#             print(arrEdges)
#         # print(nodes)
#         next_node_idx = len(elements) - len(edges)

#         return edges + nodes[:next_node_idx+1]

#     # If the remove button was clicked most recently
#     elif int(btn_remove) > int(btn_add):
#         if len(elements) > len(edges):
#             return elements[:-1]

#     # Neither have been clicked yet (or fallback condition)
#     return elements


if __name__ == '__main__':
    app.run_server(debug=True)