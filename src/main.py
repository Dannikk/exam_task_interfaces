import src.directory_reader as dr
import src.graph_iterator as gi


def get_names(research):
    names = research.split()[:-1]
    it = iter(names)
    names = [first_name + " " + second_name for first_name, second_name in zip(it, it)]
    return names


def get_unique_names(file_path):
    names = set()
    with dr.DirReader(file_path) as file_names:
        for file_name in file_names:
            with open(file_name) as file_input:
                ln = file_input.readline()
                for research in file_input:
                    names.update(set(get_names(research)))
    return names


def fill_values(graph, research):
    names = get_names(research)
    for name in names:
        graph[name].extend(names)
    return graph


def graph_builder(names, file_path):
    graph = dict(key_val for key_val in [(name, []) for name in names])
    with dr.DirReader(file_path) as file_names:
        for file_name in file_names:
            with open(file_name) as file_input:
                ln = file_input.readline()
                for research in file_input:
                    graph = fill_values(graph, research)
    return graph


def read_graph(file_path):
    names = get_unique_names(file_path)
    graph = graph_builder(names, file_path)
    return graph


def main():
    #file_path = input("Enter filepath")
    file_path = "C:\\Users\\nikit\\PycharmProjects\\exam_task_interfaces\\data"
    graph = read_graph(file_path)
    result_path = "result.txt"
    graph_iter = gi.Graph_Iterator(graph, result_path)
    for count, name in graph_iter:
        pass

main()