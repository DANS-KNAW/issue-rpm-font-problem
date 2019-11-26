#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
RPMBUILD=$SCRIPTDIR/rpmbuild

pushd rpmbuild/SPECS || exit
rpmbuild -bb font-rpm-1.0-1.spec --define "_topdir $RPMBUILD"
popd || exit

