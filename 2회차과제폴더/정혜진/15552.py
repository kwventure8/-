#15552
import sys

A = int(input())

for i in range(A):
  B,C = map(int,sys.stdin.readline().split())
  print(B+C)
