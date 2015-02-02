import networkx as nx

g = nx.DiGraph()

# print nx.info(g)
# print

print "Nodes:", g.nodes()
print "Edges:", g.edges()
print

print "X props:", g.node['X']
print "Y props:", g.node['Y']

print "X=>Y props:", g['X']['Y']
print

g.node['X'].update({'prop1' : 'value1'})
print "X props:", g.node['X']
print

g['X']['Y'].update({'label' : 'label1'})
print "X=>Y props:", g['X']['Y']
