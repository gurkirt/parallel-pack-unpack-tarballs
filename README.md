# Euler data management scripts

## 1. pack a large dataset into multiple tar balls 
Brake a large dataset and pack into multiple tar ball in parallel 

```
python pack_dataset.py <directory-to-tar-containing file or sub directories>\
    <directory-where-to-store-tarballs> \
    --num_batchs=<int:number of tarball to create from give directory> \
    --num_jobs=<int:num of prcoess to use to tar>
```

You can use `bsub_pack.sh` for your guidance.

I use directories as basis for splitting/batching tarballs while pack but you uncomment line 48 and see line 9 in `pack_dataset.py` for finer control and modify accordingly.

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

### Stats for unpacking

Following are time report to unpack `16` tarballs made of `152GB`

I measure time with two ways: 1. time taken to finish the `bsub_unpack.sh`; 2. Real time reported by putting `time` command in front of `python unpack_dataset.py`.

| Number of threads | Job time |   Real |
|:--:|:--:|:--:|
| 1 | 19:20 |   14:35 |
| 4 | 12:10 |   07:12 |
| 16 | 07:20 |   02:49 |