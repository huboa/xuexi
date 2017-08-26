from multiprocessing import Pool
import os
if __name__ == '__main__':
    p=Pool(4)

print(os.cpu_count())