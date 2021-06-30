from pomegranate import *

start = DiscreteDistribution({
    "sol": 0.75,
    "chuva": 0.25
})

transitions = ConditionalProbabilityTable([
    ["sol", "sol", 0.9],
    ["sol", "chuva", 0.1],
    ["chuva", "sol", 0.6],
    ["chuva", "chuva", 0.4]
], [start])

model = MarkovChain([start, transitions])

print(model.sample(100))