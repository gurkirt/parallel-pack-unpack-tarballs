import os, argparse
from joblib import delayed
from joblib import Parallel

def tar_a_batch(data_dir, tar_dir, batch_id, batch):
    cmd = 'tar -cf {:s}/tarball_{:d}.tar '.format(tar_dir, batch_id) 
    for dir_name in batch:
        cmd += dir_name + ' '

    os.system(cmd)

def make_batchs(dirs, batch_size):
    batchs = []
    batch = []
    for iter, dir in enumerate(dirs):
        batch.append(dir)
        if iter>0 and iter%batch_size == 0:
            batchs.append(batch) 
            batch = []
    
    return batchs

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='extract frame from videos')
    p.add_argument('data_dir', type=str,
                   help='directory containing multiple directories or files')
    p.add_argument('tar_dir', type=str,
                   help='Where multiple tarballs are going to be saved.')
    p.add_argument('--batch_size', type=int, default=2,
                   help='Number of directories/files in single tarball')
    p.add_argument('--num_jobs', type=int, default=8,
                   help='Number of parallel jobs to run')
    args = p.parse_args()
    
    dirs = os.listdir(args.data_dir)

    print('Number of directories/files :::>', len(dirs))

    batchs = make_batchs(dirs, args.batch_size)

    if not os.path.isdir(args.tar_dir):
        os.makedirs(args.tar_dir)
    owd = os.getcwd()
    #first change dir to build_dir path
    os.chdir(args.data_dir)
    status_lst = Parallel(n_jobs=args.num_jobs)(delayed(tar_a_batch)(args.data_dir, args.tar_dir, batch_id, batch) for batch_id, batch in enumerate(batchs))
    os.chdir(owd)

