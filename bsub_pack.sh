echo "temp directory for the job" $TMPDIR
SOURCE_DIR=/cluster/work/cvl/gusingh/data/ava/frames_x256/
TARGET_DIR=/cluster/work/cvl/gusingh/data/ava/frames-tarballs/ 

time python pack_dataset.py ${SOURCE_DIR} ${TARGET_DIR} --num_jobs=8
#du -hs $TARGETDIR
ls -lh ${TARGET_DIR}

