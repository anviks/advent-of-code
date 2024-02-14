import networkx as nx
from utils_anviks import read_data, stopwatch


@read_data("data.txt", sep2=': ')
@stopwatch
def solution(data: list[str]):
    graph = nx.Graph()

    for source, destinations in data:
        for dest in destinations.split(' '):
            graph.add_edge(source, dest)

    cut, partition = nx.stoer_wagner(graph)

    return len(partition[0]) * len(partition[1])


if __name__ == '__main__':
    print(solution())  # 533628
