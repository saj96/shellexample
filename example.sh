#!/usr/bin/env bash
function lazygit() {
    git init
    git add .
    git commit -a -m "$1"
    git push
}
NAME="Erykah"
if echo "Hello $NAME!"; then
    lazygit "upload this shell script"
fi 


