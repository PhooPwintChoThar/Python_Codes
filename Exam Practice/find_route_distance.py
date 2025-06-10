def find_route_distance(key, routes):
    if key not in routes:
        return 0
    return routes[key][1]+find_route_distance(routes[key][0], routes)

routes={"i":("j", 4.0), "a":("b", 3.4), "j":("k", 6.0), "c":("d", 5.6), "b":("c", 4.0)}
print(find_route_distance("b", routes))