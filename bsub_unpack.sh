echo "temp directory for the job" $TMPDIR
TARGET_DIR=${TMPDIR}/data/
mkdir -p $TARGET_DIR
echo  $TARGET_DIR
SOURCE_DIR=/cluster/work/cvl/gusingh/data/ava/frames-tarballs/
time python unpack_dataset.py ${TARGET_DIR} ${SOURCE_DIR} --num_jobs=16
ls -lh ${TARGET_DIR}

#python tools/run_net.py --cfg config/AVA/SLOWFAT.yml AVA.FRAMES_DIR ${TARGET_DIR}
