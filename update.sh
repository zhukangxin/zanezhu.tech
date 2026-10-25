#!/usr/bin/env bash
# 服务器自动更新脚本：从 GitHub 拉取最新内容，有变化时重新生成网站
# 手动运行:  bash /opt/zanezhu.tech/update.sh
# 自动运行:  加入 crontab，每 5 分钟检查一次（见 README）
set -e
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
WEB_DIR="/var/www/zanezhu.tech"
cd "$REPO_DIR"
git fetch -q origin main
if [ "$1" != "--force" ] && [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ]; then
  exit 0   # 没有新内容
fi
git reset -q --hard origin/main
python3 build.py
mkdir -p "$WEB_DIR"
rsync -a --delete dist/ "$WEB_DIR/"
echo "$(date '+%F %T') updated to $(git rev-parse --short HEAD)"
