wget $(cat kdevelop-python.spec | grep Source0 | awk '{print $2}')
mkdir -p ~/rpmbuild/SOURCES
mv kdev-python-*.tar.bz2 ~/rpmbuild/SOURCES
cp *.patch ~/rpmbuild/SOURCES
rpmbuild -ba --clean kdevelop-python.spec


