#! /bin/bash
wget https:https://go.dev/dl/go1.19.3.darwin-amd64.pkg
sudo installer -package ~/Downloads/go1.19.3.darwin-amd64.pkg -target /
echo "Golang Installed"
