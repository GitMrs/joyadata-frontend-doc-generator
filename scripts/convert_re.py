#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_re - re.md 文件格式转换工具
Usage: python convert_re.py --input re.md [--output converted_re.md]

将制表符分隔的 re.md 文件转换为 key.prop=name 格式
输入: table\t[{"prop": "name", "name": "名称"}]
输出: table.name=名称
"""

import json
import argparse
import os

def convert_re_file(input_path, output_path=None):
    """re.md文件处理"""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"输入文件不存在: {input_path}")
    
    input_dir = os.path.dirname(os.path.abspath(input_path))
    input_name = os.path.splitext(os.path.basename(input_path))[0]
    
    if output_path is None:
        output_path = os.path.join(input_dir, f"{input_name}_converted.txt")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    
    for line in lines:
        parts = line.split('\t', 1)
        if len(parts) < 2:
            new_lines.append(line)
            continue
        
        key_part, json_part = parts
        try:
            data = json.loads(json_part)
            for item in data:
                prop = item.get('prop')
                name = item.get('name')
                if prop and name:
                    new_line = f"{key_part}.{prop}={name}\n"
                    new_lines.append(new_line)
        except json.JSONDecodeError:
            new_lines.append(line)
    
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"转换完成: {input_path} -> {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert re.md file to key=value format')
    parser.add_argument('--input', required=True, help='输入文件路径 (支持绝对路径和相对路径)')
    parser.add_argument('--output', default=None, help='输出文件路径 (默认: 输入文件同目录的 xxx_converted.txt)')
    args = parser.parse_args()
    
    convert_re_file(args.input, args.output)
