#!/bin/bash
set -e
VERSION=${1:-1.0}
PREFIX=/opt/meshtastic-linux-client

fpm -s dir -t deb -n meshtastic-client -v "$VERSION" --prefix="$PREFIX" .
fpm -s dir -t rpm -n meshtastic-client -v "$VERSION" --prefix="$PREFIX" .
