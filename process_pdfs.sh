#!/bin/bash
conda activate MinerU
# 检查是否提供了目录路径参数
if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/your/directory"
  exit 1
fi

# 获取目录路径参数
directory="$1"

# 检查目录是否存在
if [ ! -d "$directory" ]; then
  echo "Error: Directory $directory does not exist."
  exit 1
fi

# 遍历目录下所有的PDF文件
for pdf_file in "$directory"/*.pdf; do
  if [ -f "$pdf_file" ]; then
    # 执行magic-pdf命令
    magic-pdf pdf-command --pdf "$pdf_file" --inside_model true
  fi
done
