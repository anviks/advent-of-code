from utils_anviks import parse_file_content, stopwatch
import networkx as nx

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n', '-'), str)
graph = nx.Graph(data)


@stopwatch
def part1():
    connected = [nodes for nodes in nx.enumerate_all_cliques(graph) if len(nodes) == 3]
    t_connected = [nodes for nodes in connected if any(node[0] == 't' for node in nodes)]
    return len(t_connected)


@stopwatch
def part2():
    lan = max((nodes for nodes in nx.enumerate_all_cliques(graph)), key=len)
    return ','.join(sorted(lan))


if __name__ == '__main__':
    print(part1())  # 1194                                      | 0.57 seconds
    print(part2())  # bd,bu,dv,gl,qc,rn,so,tm,wf,yl,ys,ze,zr    | 0.61 seconds
