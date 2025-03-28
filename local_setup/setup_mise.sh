#!/bin/sh
echo "Installing mise from local setup"
./local_setup/install-mise
eval "$(~/.local/bin/mise activate bash --shims)"
echo 'eval "$(~/.local/bin/mise activate bash --shims)"' >> ~/.bashrc
