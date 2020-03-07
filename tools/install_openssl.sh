#!/bin/bash

set -e

if [[ -f /tmp/openssl.installed ]] ; then
    return 0
fi

wget https://www.openssl.org/source/openssl-1.1.1d.tar.gz
tar xzvf openssl
pushd openssl-1.1.1d
./config
make
sudo make install
popd

touch /tmp/openssl.installed