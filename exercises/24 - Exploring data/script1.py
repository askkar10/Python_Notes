import pandas as pd
grid = [[1,2,3],[4,5,6],[7,8,9]]
dg = pd.DataFrame(grid)
print(dg);print("--")
dg = pd.DataFrame(grid,columns=["one","two","three"])
print(dg);print("--")
print(dg["two"]);print("---")
print(list(x[1]  for x in grid));print("---")
for row in dg["two"]:
    print(row)
print("---")
edges = dg[["one","three"]]
print(edges);print("---")
print(edges.add(2));print("---")
print(edges.value_counts());print("---")
dg = pd.DataFrame(grid,columns=["one","two","three"])
dg.to_csv("dg_out.csv")
dg.to_json("dg_out.json")