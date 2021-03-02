echo "temp directory for the job" $TMPDIR
TARGETDIR=${TMPDIR}/data/
mkdir -p $TARGETDIR
echo  $TARGETDIR
time python unpack_dataset.py ${TARGETDIR} /cluster/work/cvl/gusingh/data/ava/frames-tarballs/ --num_jobs=8
#du -hs $TARGETDIR
ls -lh ${TARGETDIR}

