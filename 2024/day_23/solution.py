from utils_anviks import parse_file_content, stopwatch
import networkx as nx
from pathlib import Path

file = 'data.txt'
file0 = 'example.txt'
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ('\n', '-'), str)
graph = nx.Graph(data)


@stopwatch
def part1():
    return len([
        nodes for nodes in nx.enumerate_all_cliques(graph)
        if len(nodes) == 3 and any(node[0] == 't' for node in nodes)
    ])


@stopwatch
def part2():
    lan = max((nodes for nodes in nx.enumerate_all_cliques(graph)), key=len)
    return ','.join(sorted(lan))


if __name__ == '__main__':
    print(part1())  # 1194                                      | 0.57 seconds
    print(part2())  # bd,bu,dv,gl,qc,rn,so,tm,wf,yl,ys,ze,zr    | 0.61 seconds
