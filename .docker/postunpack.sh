#!/bin/bash

cat > "/usr/sbin/install_packages" <<-'EOF'
#!/bin/sh
set -e
set -u
export DEBIAN_FRONTEND=noninteractive
n=0
max=2
until [ $n -gt $max ]; do
    set +e
    (
      apt-get update -qq &&
      apt-get install -y --no-install-recommends "$@"
    )
    CODE=$?
    set -e
    if [ $CODE -eq 0 ]; then
        break
    fi
    if [ $n -eq $max ]; then
        exit $CODE
    fi
    echo "apt failed, retrying"
    n=$(($n + 1))
done
rm -r /var/lib/apt/lists /var/cache/apt/archives
EOF
chmod 0755 "/usr/sbin/install_packages"

install_packages nginx

rm -rf /usr/share/nginx/html /etc/nginx/sites-available/default
mv /scripts/nginx.conf /etc/nginx/sites-available/default
rm -rf /usr/share/nginx/html
mv /app/backend/static /usr/share/nginx/html

## Symlinking logs to stdout and stderr
ln -sf /dev/stdout /var/log/nginx/access.log
ln -sf /dev/stderr /var/log/nginx/error.log
