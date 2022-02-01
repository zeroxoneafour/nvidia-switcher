#!/bin/sh
# A build script

version="0.0.1"

rpmdev-setuptree
cp -r nvidia-switcher nvidia-switcher-$version
tar cf ~/rpmbuild/SOURCES/nvidia-switcher-$version.tar nvidia-switcher-$version
rm -r nvidia-switcher-$version
cp nvidia-switcher.spec ~/rpmbuild/SPECS/nvidia-switcher.spec
rpmbuild -bb ~/rpmbuild/SPECS/nvidia-switcher.spec
