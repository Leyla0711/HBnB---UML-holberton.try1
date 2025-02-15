from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define the Presentation Layer (Services, API)
dot.node('PresentationLayer', 'Presentation Layer\n(ServiceAPI, Controllers)', shape='box', style='filled', fillcolor='lightblue')

# Define the Business Logic Layer (Models)
dot.node('BusinessLogicLayer', 'Business Logic Layer\n(Facade, User, Place, Review, Amenity)', shape='box', style='filled', fillcolor='lightgreen')

# Define the Persistence Layer (Database Access)
dot.node('PersistenceLayer', 'Persistence Layer\n(DatabaseAccess, Repositories)', shape='box', style='filled', fillcolor='lightyellow')

# Show communication paths (edges)
dot.edge('PresentationLayer', 'BusinessLogicLayer', label='Facade Pattern')
dot.edge('BusinessLogicLayer', 'PersistenceLayer', label='Database Operations')

# Render the graph to a file (e.g., PNG or PDF)
dot.render('high_level_package_diagram', format='png', cleanup=True)

# To display the diagram in Jupyter Notebook (if using one)
dot.view()
