def isSafe(level):
  diff = [b-a for a, b in zip(level, level[1:])]
  all_decreasing = all(map(lambda x: 1<=x<=3,diff))
  all_increasing = all(map(lambda x: -3<=x<=-1,diff))
  return all_decreasing or all_increasing


with open("input.txt") as f:
  reports = [list(map(int, line.split())) for line in f]


print(sum(isSafe(r) for r in reports))