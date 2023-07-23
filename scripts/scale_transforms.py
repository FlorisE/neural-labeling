import os
import argparse
import json
import numpy as np

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Scales the transform positions')
	parser.add_argument('scale', type=float)
	parser.add_argument('--transforms_file', default='transforms.json')
	args = parser.parse_args()
	with open(args.transforms_file, 'r+') as f:
		transforms_json = json.load(f)
		for frame in transforms_json['frames']:
			for i in range(3):
				frame['transform_matrix'][i][3] *= args.scale
				pos = np.matrix(frame['transform_matrix'])[0:3,3]
		f.seek(0)
		json.dump(transforms_json, f, indent=2)
