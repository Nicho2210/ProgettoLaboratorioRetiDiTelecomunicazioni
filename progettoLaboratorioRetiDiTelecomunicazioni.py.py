import copy  # Import the copy module to create deep copies of objects

# Node class represents each node in the network with its unique id, neighbors, and routing table
class Node:
    def __init__(self, node_id, neighbors):
        """
        Initialize a Node object.
        
        Parameters:
        node_id (int): The unique identifier for the node.
        neighbors (dict): A dictionary where keys are neighbor node IDs and values are the distances to those neighbors.
        """
        self.node_id = node_id  # Set the node's unique ID
        self.neighbors = neighbors  # Set the node's neighbors and their respective distances
        self.routing_table = {node_id: (0, None)}  # Initialize the routing table with the node's ID, distance 0, and no next hop

        # Add entries to the routing table for each neighbor with their distance and next hop (which is the neighbor itself)
        for neighbor, distance in neighbors.items():
            self.routing_table[neighbor] = (distance, neighbor)

    def update_routing_table(self, table, source_id):
        """
        Update the node's routing table based on the received routing table from another node.
        
        Parameters:
        table (dict): The routing table received from another node.
        source_id ()
        """
        # Get the distance to the source node (if it's a neighbor) or set it to infinity
        neighbor_distance = self.neighbors.get(source_id, float('inf'))

        # Update the current node's routing table based on the received information
        for destination, (distance, next_hop) in table.items():
            if destination != self.node_id:

                if next_hop == self.node_id:
                    continue

                # Calculate the new distance by adding the neighbor's distance
                new_distance = distance + neighbor_distance

                # If the new distance is shorter, update the routing table
                if new_distance < self.routing_table.get(destination, (float("inf"), None))[0]:
                    self.routing_table[destination] = (new_distance, source_id)

    def get_routing_table(self):
        """
        Get a deep copy of the node's routing table.
        
        Returns:
        dict: A copy of the node's routing table.
        """
        return copy.deepcopy(self.routing_table)  # Return a deep copy of the routing table

    def print_routing_table(self):
        """
        Print the node's routing table in a readable format.
        """
        print(f"Routing table for node {self.node_id}:")
        # Print each destination, its distance, and the next hop
        for destination, (distance, next_hop) in self.routing_table.items():
            print(f"  Destination: {destination}, Distance: {distance}, Next Hop: {next_hop}")
        print()  

# Create a list of nodes in the network with their neighbors and distances
nodes = [
    Node("A", {"B": 1, "F": 3}),
    Node("B", {"A": 1, "F": 1, "C": 3}),
    Node("C", {"B": 3, "D": 2}),
    Node("D", {"C": 2, "F": 6, "E": 1}),
    Node("E", {"B": 5, "D": 1, "F": 2}),
    Node("F", {"A": 3, "B": 1, "D": 6, "E": 2}),
]

# Simulate the routing process
def simulate_routing(nodes):
    """
    Simulate the Distance Vector Routing process for all nodes in the network.
    
    Parameters:
    nodes (list): A list of Node objects that represents the network.
    """
    # Run the simulation for a fixed number of iterations (convergence)
    for i in range(len(nodes)):
        print(f"--- Iteration {i + 1} ---")

        # Update routing tables for all nodes
        for current_node in nodes:
            for other_node in nodes:
                if current_node.node_id != other_node.node_id:
                    # Update the current node's routing table with the routing table from another node
                    current_node.update_routing_table(other_node.get_routing_table(), other_node.node_id)

        # Print the routing table of each node after the update
        for node in nodes:
            node.print_routing_table()

# Run the simulation of routing
simulate_routing(nodes)
