class Graph:
  def __init__(self):
    self.adj_list = {}

  def __str__(self):
    str = ''
    for i, vertex in enumerate(self.adj_list):
      if i != 0:
        str+='\n'
      str+=f'{vertex}: {self.adj_list[vertex]}'
    return str
  
  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = []
      return True
    return False

  def add_edge(self, v1, v2):
    self.add_vertex(v1)
    self.add_vertex(v2)
    if v2 not in self.adj_list[v1]:
      self.adj_list[v1]+=[v2]
    if v1 not in self.adj_list[v2]:
      self.adj_list[v2]+=[v1]

  def remove_edge(self, v1, v2):
    self.adj_list[v1].remove(v2)
    self.adj_list[v2].remove(v1)

  def remove_vertex(self, vertex):
    if self.adj_list[vertex]:
      for v in self.adj_list[vertex]:
        self.adj_list[v].remove(vertex)
      self.adj_list.pop(vertex)
      return True
    return False


print('\nCreate Graph and Add Vertex')
my_graph=Graph()
my_graph.add_vertex('A')
print(my_graph)

print('\nAdd Edge')
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('D', 'B')
my_graph.add_edge('A', 'D')
print(my_graph)

print('\nRemove Edge')
my_graph.remove_edge('A', 'B')
print(my_graph)

print('\nRemove Vertex')
my_graph.remove_vertex('A')
print(my_graph)