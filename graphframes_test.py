from pyspark.sql import SparkSession
from graphframes import GraphFrame

spark = (
    SparkSession.builder
    .config("spark.jars.packages", "graphframes:graphframes:0.8.4-spark3.5-s_2.13")
    .getOrCreate()
)

nodes = [
    (1, "Alice", 30),
    (2, "Bob", 25),
    (3, "Charlie", 35)
]
nodes_df = spark.createDataFrame(nodes, ["id", "name", "age"])

edges = [
    (1, 2, "friend"),
    (2, 1, "friend"),
    (2, 3, "friend"),
    (3, 2, "enemy")  # eek!
]
edges_df = spark.createDataFrame(edges, ["src", "dst", "relationship"])

g = GraphFrame(nodes_df, edges_df)

print("In-degrees:")
g.inDegrees.show()
print("\n")

print("Out-degrees:")
g.outDegrees.show()
print("\n")

print("Degrees:")
g.degrees.show()
print("\n")

print("Page Rank:")
g2 = g.pageRank(resetProbability=0.15, tol=0.01)
g2.vertices.show()
