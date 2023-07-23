import argparse
import os
import shutil

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Some simple image processing steps')
	parser.add_argument('--source_dir', type=str, default='rgbd')
	parser.add_argument('--target_dir', type=str, required=False)
	parser.add_argument('--subsample', type=int, default=1)
	parser.add_argument('--image_ext', type=str, default='jpg')
	args = parser.parse_args()
	source_dir = args.source_dir
	target_dir = args.target_dir or source_dir

	if not os.path.exists(target_dir):
		os.makedirs(target_dir)
		subsample_steps = args.subsample
		jpgs = sorted([fn for fn in os.listdir(source_dir) if fn.endswith(args.image_ext)])
		max_length = max(map(len, jpgs))
		for jpg in jpgs:
			jpg_len = len(jpg)
			if jpg_len < max_length:
				diff = max_length - jpg_len
				shutil.copy(source_dir + os.sep + jpg, target_dir + os.sep + diff * '0' + jpg)
			else:
				shutil.copy(source_dir + os.sep + jpg, target_dir + os.sep + jpg)
		jpgs = sorted(os.listdir(target_dir))
		if subsample_steps != 1:
			for i, jpg in enumerate(jpgs):
				if i % subsample_steps != 0:
					os.remove(target_dir + os.sep + jpg)
