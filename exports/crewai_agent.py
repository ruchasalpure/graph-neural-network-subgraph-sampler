from crewai import Agent

graph_neural_network_subgraph_sampler = Agent(
    role="Graph Neural Network Subgraph Sampler",
    goal="Deliver high-precision autonomous Graph Neural Network Subgraph Sampler operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
