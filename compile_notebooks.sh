#!/usr/bin/env bash
for d in example*; do
    echo "=== Converting $d ==="
    cd $d
    for f in *.ipynb; do
        for o in html ; do # I removed PDF (it looks bad)
            echo "Converting $f to $o..."
            jupyter nbconvert --log-level=ERROR --to $o $f
        done
    done
    cd ..; echo ""
done
