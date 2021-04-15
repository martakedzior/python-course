graph = {
    'dom': ['szkoła', 'kościół', 'bar'],
    'szkoła': ['szpital', 'dom'],
    'szpital': ['szkoła', 'bar', 'kino', 'teatr'],
    'teatr': ['szpital', 'kino'],
    'kino': ['kościół', 'szpital', 'teatr', ],
    'kościół': ['dom', 'bar', 'kino', ],
    'bar': ['dom', 'kościół', 'szpital', ]
}

# for item in graph:
#     print(item, '-', '-'.join(graph[item]))

for item in graph:
    print('-----> krawędzie z ', item)
    for e in graph[item]:
        print(item, '---', e)
