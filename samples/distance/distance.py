import sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT)

from core.distances import api as dist_api

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

euclidean_distance = dist_api.compute(a, b, 'euclidean')
manhattan_distance = dist_api.compute(a, b, 'manhattan')
chessboard_distance = dist_api.compute(a, b, 'chessboard')
minkowski_distance = dist_api.compute(a, b, 'minkowski')
cosine_distance = dist_api.compute(a, b, 'cosine')
hamming_distance = dist_api.compute(a, b, 'hamming')

print(f'Euclidean Distance: {euclidean_distance}')
print(f'Manhattan Distance: {manhattan_distance}')
print(f'Chessboard Distance: {chessboard_distance}')        
print(f'Minkowski Distance: {minkowski_distance}')
print(f'Cosine Distance: {cosine_distance}')
print(f'Hamming Distance: {hamming_distance}')

print('-' * 40)
# Example of using distance methods

x1, y1 = 1, 2
x2, y2 = 4, 6
euclidean_dist = dist_api.distance(x1, y1, x2, y2, 'euclidean')
manhattan_dist = dist_api.distance(x1, y1, x2, y2, 'manhattan')
chesboard_dist = dist_api.distance(x1, y1, x2, y2, 'chessboard')
minkowski_dist = dist_api.distance(x1, y1, x2, y2, 'minkowski')
cosine_dist = dist_api.distance(x1, y1, x2, y2, 'cosine')
hamming_dist = dist_api.distance(x1, y1, x2, y2, 'hamming')

print(f'Euclidean Distance between points: {euclidean_dist}')
print(f'Manhattan Distance between points: {manhattan_dist}')
print(f'Chessboard Distance between points: {chesboard_dist}')
print(f'Minkowski Distance between points: {minkowski_dist}')
print(f'Cosine Distance between points: {cosine_dist}')
print(f'Hamming Distance between points: {hamming_dist}')



