def ranking(dictionary):
    dict1 = list(dictionary.items())

    anySort = True
    while anySort:
        anySort = False
        for x in range(len(dict1) - 1):
            if dict1[x][1] < dict1[x + 1][1]:
                temp = dict1[x]
                dict1[x] = dict1[x + 1]
                dict1[x + 1] = temp
                anySort = True

    new_dic = {}
    num = 1
    x = 0
    while x < len(dict1):
        if x < len(dict1) - 1 and dict1[x][1] == dict1[x + 1][1]:
            new_dic[num] = [dict1[x][0], dict1[x + 1][0]]
            x += 2
        else:
            new_dic[num] = [dict1[x][0]]
            x += 1
        num += 1

    return new_dic

popularity_scores = {"C++": 96.7, "C": 96.7, "Java": 97.5, "Python": 100, "C#": 89.4}
print(ranking(popularity_scores))
popularity_scores2 = {"Python": 98.0, "C++": 99.0, "C#": 92.0, "Go": 92.0, "Swift": 95.0}
print(ranking(popularity_scores2))
popularity_scores3 = {"Kotlin": 87.0, "Ruby": 87.0, "JavaScript": 90.0, "TypeScript": 85.0}
print(ranking(popularity_scores3))
