#!/bin/bash
unset YARN_VERSION && rm -rf /opt/yarn*
rm -rf /bin/sh && ln -s /bin/bash /bin/sh
git config --global core.editor 'code --wait'
