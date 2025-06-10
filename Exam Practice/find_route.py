def find_route(key, rout):
    distance=0
    paths=[]
    a=key
    paths.append(a)
    while a in rout:
        distance+=rout[a][1]
        paths.append(rout[a][0])
        a=rout[a][0]
    return (paths, distance)

routes={"i":("j", 4.0), "a":("b", 3.4), "j":("k", 6.0), "c":("d", 5.6), "b":("c", 4.0)}
print(find_route("a", routes))
print(find_route("b", routes))