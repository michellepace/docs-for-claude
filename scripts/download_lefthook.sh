#!/bin/bash
set -e

COPIED_URL="https://github.com/evilmartians/lefthook/tree/master/docs/mdbook"

COLLECTION_DIR="lefthook"
DOWNLOAD_TEMP="lefthook/download_temp"
CLONE_URL="https://github.com/evilmartians/lefthook.git"
DOCS_PATH="docs/mdbook"
BRANCH="master"

mkdir -p lefthook/download_temp && cd lefthook/download_temp
git init
git remote add origin https://github.com/evilmartians/lefthook.git
git config core.sparseCheckout true
echo "docs/mdbook/*" > .git/info/sparse-checkout
git pull origin master --depth=1
rsync -av --include='*/' --include='*.mdx' --include='*.md' --exclude='*' \
    docs/mdbook/ ../../lefthook/
cd ../..
rm -rf lefthook/download_temp
npx markdownlint-cli2 --fix "lefthook/**/*.md"