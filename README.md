# Euler data management scripts

## 1. pack a large dataset into multiple tar balls 
Brake a large dataset and pack into multiple tar ball in parallel 

```
python pack_dataset.py <directory-to-tar-containing file or sub directories>\
    <directory-where-to-store-tarballs> \
    --batch_size=<int:number of files or directories in single tar> \
    --num_jobs=<int:num of prcoess to use to tar>
```

You can use `bsub_pack.sh` for your guidance.

I use directories as basis for splitting/batching tarballs while pack but you uncomment line 43 in `pack_dataset.py` for finer control and modify accordingly.

## 2. Unpack a large dataset of multiple tar balls 
Upack a large dataset broken into multiple tarballs 

```
python unpack_dataset.py <directory-where-to-untar>\
            <directory-where-to-tarbals are-stored>\
            --num_jobs=<int:num of prcoess to use to tar>
```

#### Unpack within a batch-job
  - Use `bsub_unpack.sh` as guidance for submitting batch job on eular
  - Use `${TMPDIR}` and `TARGETDIR=${TMPDIR}/data/`
  - Unpack all tarballs in parallel into `TARGETDIR`
