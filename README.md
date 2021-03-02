# Euler data mmanagement scripts

### 1. pack a large dataset into multiple tar balls 
pack a large dataset into multiple tar ball in parallel 

```
python pack_dataset.py <directory-to-tar-containing file or sub directories> <directory-where-to-store-tarballs> --batch_size=<int:number of files or directories in single tar> --num_jobs=<int:num of prcoess to use to tar>
```

### 2. Unpack a large dataset of multiple tar balls 
Upack a large dataset into multiple tar ball in parallel 

```
python unpack_dataset.py <directory-where-to-untar> <directory-where-to-tarbals are-stored> --num_jobs=<int:num of prcoess to use to tar>
```