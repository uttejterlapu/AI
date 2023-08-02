class CustomDictionary:
    def __init__(self):
        self.my_dict = {}

    def insert_list(self, key_value_list):
        for key, value in key_value_list:
            self.my_dict[key] = value

    def print_dict(self):
        print(self.my_dict)
    
    def bfs(self, queue, visited, node):
        if node not in self.my_dict:
            print("Start node not found in the dictionary.")
            return

        visited.append(node)
        queue.append(node)

        while queue:
            m = queue.pop(0)
            print(m, end=" ")

            for neighbour in self.my_dict[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

if __name__ == '__main__':
    my_dict_obj = CustomDictionary()
    n = int(input("Enter the number of nodes : "))
    key_value_list = []
    for i in range(n):
        node_name, e = map(int, input(f"Enter node name  and number of nodes it connected to : ").split())
        edges = []
        for j in range (e):
            edges.append(int(input(f"enter the {node_name} it connected to : ")))
        key_value_list.append((node_name, edges))
    my_dict_obj.insert_list(key_value_list)
    visited = []
    queue = []
    start_node = int(input("Enter the start node: "))
    print("Following is the Breadth-First Search:")
    my_dict_obj.bfs(queue, visited, start_node)
