import functools


def print_iter(iterator):
    @functools.wraps(iterator)
    def decorator(*args, **kwargs):
        inner_iterator = iterator(*args, **kwargs)
        # file_output = open(args[1], 'w')
        # print("drgdfg", file_output)
        # print(args[1])
        for count, name in inner_iterator:
            # print(name + " has " + str(count) + " researches", file_output)
            print(name + " has " + str(count) + " researches")
            yield count, name
        #file_output.close()
    return decorator

@print_iter
class Graph_Iterator:
    def __init__(self, graph, result_path):
        self.graph = graph
        self.research_count_per_researcher = []
        for name in graph:
            self.research_count_per_researcher.append([graph[name].count(name), name])
        self.research_count_per_researcher = sorted(self.research_count_per_researcher)
        self.research_count_per_researcher.reverse()

    def __iter__(self):
        return self.graph_generator()

    def graph_generator(self):
        for count, name in self.research_count_per_researcher:
            yield count, name

