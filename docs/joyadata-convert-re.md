# convert_re

**Description**: re.md 文件格式转换工具，用于将表格配置的 JSON 数据转换为 key=value 格式。

## 功能说明

将制表符分隔的 re.md 文件转换为 `key.prop=name` 格式的输出文件。

## 输入格式

```
table	[{"prop": "name", "name": "名称"}, {"prop": "time", "name": "时间"}]
form	[{"prop": "title", "name": "标题"}, {"prop": "status", "name": "状态"}]
```

## 输出格式

```
table.name=名称
table.time=时间
form.title=标题
form.status=状态
```

## 使用方法

```bash
python scripts/convert_re.py --input re.md
```

指定输出文件：

```bash
python scripts/convert_re.py --input re.md --output converted.txt
```

## 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| --input | re.md | 输入文件路径 |
| --output | converted_re.md | 输出文件路径 |

## 示例

### 输入文件 (re.md)

```
user	[{"prop": "username", "name": "用户名"}, {"prop": "email", "name": "邮箱"}]
role	[{"prop": "rolename", "name": "角色名"}, {"prop": "description", "name": "描述"}]
```

### 输出文件 (converted_re.md)

```
user.username=用户名
user.email=邮箱
role.rolename=角色名
role.description=描述
```

## 注意事项

- 输入文件使用制表符 (`\t`) 分隔键和 JSON 部分
- JSON 数组中每个对象必须包含 `prop` 和 `name` 字段
- 无法解析的行会原样保留到输出文件中
