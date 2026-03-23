---
name: "joyadata-frontend-doc-generator"
description: "Generates Vue component usage documentation from MD files. Invoke when user uses joyadata-xxx components or asks for component documentation."
---

# Component Documentation Generator

This skill generates Vue component usage documentation for joyadata component library.

## When to Use

**Triggered when:**
- User uses components with `joyadata-xxx` prefix (e.g., `<joyadata-table>`, `<joyadata-form>`, `<joyadata-dialog>`, etc.)
- User asks about joyadata components usage
- User asks for component documentation
- User asks about project setup / environment / initialization
- User asks about API requests / axios usage
- User provides MD file and wants usage instructions
- User wants to convert re.md file format (convert_re)
- User performs API integration using `this.$request._get`, `this.$request._post`, etc.
- User asks how to use joyadata encapsulated request methods
- User needs file upload/download operations
- User needs to use utility methods like `deepClone`, `parseTime`, etc.
- User needs to perform data storage operations (sessionStorage, localStorage)

## Supported Frameworks

- Vue 2.x (based on Element UI)
- Vue 3.x (coming soon)

## Documentation Structure

```
.trae/skills/joyadata-frontend-doc-generator/
├── SKILL.md                # Main skill file
├── scripts/                # 工具脚本文件夹
│   └── convert_re.py       # re.md 格式转换工具
└── docs/                   # Component documentation folder
    ├── joyadata-setup.md    # 项目环境搭建指南
    ├── joyadata-table.md   # 表格组件
    ├── joyadata-form.md    # 表单组件
    ├── joyadata-dialog.md  # 弹框组件
    ├── joyadata-menu.md    # 菜单组件
    ├── joyadata-aside.md   # 目录树组件
    ├── joyadata-search.md  # 搜索组件
    ├── joyadata-tree.md    # 树组件
    └── ...
```

## Built-in Documentation

### 快速入门

| Document | Description |
|----------|-------------|
| [joyadata-setup](docs/joyadata-setup.md) | 项目环境搭建、初始化、接口规范 |
| [convert_re](docs/joyadata-convert-re.md) | re.md 文件格式转换工具 |

### 组件文档

| Component | Description |
|-----------|-------------|
| [joyadata-table](docs/joyadata-table.md) | 表格组件，基于 el-table 封装 |
| [joyadata-form](docs/joyadata-form.md) | 表单组件，基于 el-form 封装 |
| [joyadata-dialog](docs/joyadata-dialog.md) | 弹框组件，基于 el-dialog 封装 |
| [joyadata-menu](docs/joyadata-menu.md) | 菜单组件，基于 el-menu 封装 |
| [joyadata-aside](docs/joyadata-aside.md) | 目录树组件，基于 el-tree 封装 |
| [joyadata-search](docs/joyadata-search.md) | 搜索组件，用于页面搜索和操作 |
| [joyadata-tree](docs/joyadata-tree.md) | 树组件，基于 el-tree 封装 |
| [joyadata-request](docs/joyadata-request.md) | 请求封装与公共方法 |

## Usage

### For Built-in Components

When user asks about a specific joyadata-xxx component:

1. Check if there's a corresponding MD file in the `docs/` folder
2. Read the documentation file
3. Present structured documentation to user including:
   - Basic usage
   - Props (all attributes)
   - Events
   - Methods
   - Code examples
   - Important notes

### For Unknown Components

If user asks about a component that doesn't have documentation:

1. Ask user to provide the component's MD documentation file
2. Or generate generic documentation based on Vue component patterns
3. Suggest adding new documentation to docs folder

### For New Components

To add new component documentation:

1. Create new MD file in `docs/` folder: `docs/joyadata-xxx.md`
2. Include all component details (props, events, slots, examples)
3. The skill will automatically find and use it

## Processing Steps

1. Parse user's question to identify the component name
2. Check docs folder for component-specific MD file
3. If found, read and parse the documentation
4. If not found, ask user to provide MD file
5. Present structured documentation with examples

## Documentation Template

Each component documentation should include:

```markdown
# Component Name

**Description**: Brief description of the component

## Basic Usage

Code example for basic usage

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|

## Methods

| Method Name | Parameters | Description |
|-------------|------------|-------------|

## Important Notes

Key points to remember
```

## Guidelines

1. **Language**: Output in the same language as user's request (Chinese)
2. **Completeness**: Include all props, events, slots, and methods
3. **Examples**: Provide practical, runnable code examples
4. **Best Practices**: Add tips and common use cases
5. **Code Formatting**: Use proper Vue/HTML code blocks

## Common Component Patterns

### Table + Form + Dialog

```vue
<!-- Search -->
<joyadata-search :operation="operation" :parmas="parmas" />

<!-- Table -->
<joyadata-table ref="tableRef" :column="column" :mock-data="data" />

<!-- Dialog + Form -->
<joyadata-dialog ref="dialog" title="标题" @affirm="affirm">
  <joyadata-form ref="formDom" :main="main" :rules="rules" />
</joyadata-dialog>
```

### Sidebar + Tree

```vue
<!-- Menu -->
<joyadata-menu :menu-data="menuData" />

<!-- Tree/Aside -->
<joyadata-aside :nav-val="treeData" @changeAside="changeAside" />
```

## convert_re 工具

### 功能说明

`convert_re.py` 是一个用于将 re.md 文件转换为 key=value 格式的工具脚本。

### 适用场景

- 需要将表格配置的 JSON 数据转换为属性映射格式
- 批量生成 prop 与 name 的对应关系
- 数据格式迁移和转换

### 输入格式

```
table	[{"prop": "name", "name": "名称"}, {"prop": "time", "name": "时间"}]
```

### 输出格式

```
table.name=名称
table.time=时间
```

### 使用方法

```bash
python scripts/convert_re.py --input re.md
```

指定输出文件：

```bash
python scripts/convert_re.py --input re.md --output converted.txt
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| --input | re.md | 输入文件路径 |
| --output | converted_re.md | 输出文件路径 |
