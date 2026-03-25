---
name: "joyadata-frontend-doc-generator"
description: "Generates Vue component usage documentation from MD files. Supports joyadata component library and Vue2 i18n internationalization. Invoke when user uses joyadata-xxx components, asks for component documentation, or mentions i18n/internationalization."
---

# Joyadata Frontend Documentation Generator

This skill provides comprehensive documentation support for Joyadata component library and Vue2 internationalization (i18n) refactoring.

## When to Use

**Triggered when:**
- User uses components with `joyadata-xxx` prefix (e.g., `<joyadata-table>`, `<joyadata-form>`, `<joyadata-dialog>`, etc.)
- User asks about joyadata components usage
- User asks for component documentation
- User mentions "国际化", "i18n", "中英文", "多语言", "vue-i18n", "翻译", "多语言改造"
- User provides MD file and wants usage instructions
- User wants to convert re.md file format (convert_re)
- User asks about project setup / environment / initialization
- User performs API integration using `this.$request._get`, `this.$request._post`, etc.
- User needs file upload/download operations
- User needs to use utility methods like `deepClone`, `parseTime`, etc.

## Supported Frameworks

- Vue 2.x (based on Element UI)
- Vue 3.x (coming soon)

## Documentation Structure

```
.trae/skills/joyadata-frontend-doc-generator/
├── SKILL.md                         # Main skill file
├── scripts/                         # Tool scripts folder
│   └── convert_re.py                # re.md format converter
└── docs/                            # Documentation folder
    ├── joyadata-setup.md             # Project setup guide
    ├── joyadata-table.md            # Table component
    ├── joyadata-form.md             # Form component
    ├── joyadata-dialog.md           # Dialog component
    ├── joyadata-menu.md             # Menu component
    ├── joyadata-aside.md            # Tree component
    ├── joyadata-search.md           # Search component
    ├── joyadata-tree.md             # Tree component
    ├── joyadata-request.md          # Request methods
    └── joyadata-i18n.md              # Internationalization guide (to be added)
```

## Built-in Documentation

### 快速入门

| Document | Description |
|----------|-------------|
| [joyadata-setup](docs/joyadata-setup.md) | Project setup, initialization, API specifications |
| [convert_re](docs/joyadata-convert-re.md) | re.md file format converter |
| [joyadata-i18n](docs/joyadata-i18n.md) | Vue2 i18n internationalization guide (to be added) |

### 组件文档

| Component | Description |
|-----------|-------------|
| [joyadata-table](docs/joyadata-table.md) | Table component based on el-table |
| [joyadata-form](docs/joyadata-form.md) | Form component based on el-form |
| [joyadata-dialog](docs/joyadata-dialog.md) | Dialog component based on el-dialog |
| [joyadata-menu](docs/joyadata-menu.md) | Menu component based on el-menu |
| [joyadata-aside](docs/joyadata-aside.md) | Tree component based on el-tree |
| [joyadata-search](docs/joyadata-search.md) | Search component for pages |
| [joyadata-tree](docs/joyadata-tree.md) | Tree component based on el-tree |
| [joyadata-request](docs/joyadata-request.md) | Request encapsulation and utility methods |

---

# Part 1: Component Documentation

## Usage for Built-in Components

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

---

# Part 2: Vue2 国际化 (i18n)

## 触发条件

当用户提到以下关键词时，触发国际化支持：
- "国际化"、"i18n"、"中英文"、"多语言改造"
- "vue-i18n"、"添加英文翻译"
- "把中文改成国际化"
- "多语言支持"

## 国际化重构流程

### Step 1: 项目扫描与统计

```bash
# 统计需要处理的文件数量
find src/components -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
find src/views -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
find src/router -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
```

**重要**：必须深度扫描，重点关注 components、views、router 三个目录

### Step 2: 制定批次计划

| 文件总数 | 建议批次数 | 策略 |
|---------|----------|------|
| < 20 | 2-3 批 | 按目录分组 |
| 20-50 | 4-5 批 | 先核心组件，后业务页面 |
| > 50 | 6+ 批 | 按功能模块划分 |

### Step 3: 提取中文并生成 Key 映射

**命名规则**：
- 使用拼音驼峰：`liuLanShiJiao`、`quanWenSouSuo`
- 模块结构：`moduleName.keyName` 或 `moduleName.subModule.keyName`
- 冲突处理：加后缀 `_v2`、`_v3`

**示例映射表**：

| 原文 | Key | 所属模块 |
|------|-----|---------|
| 资产名称 | ziChanMingCheng | asset |
| 申请权限 | shenQingQuanXian | asset |

### Step 4: 更新 i18n 配置文件

在 `src/locales/zh-cn.js` 和 `src/locales/en-us.js` 中添加：

```javascript
// zh-cn.js
export default {
  asset: {
    ziChanMingCheng: '资产名称',
    shenQingQuanXian: '申请权限',
  }
}

// en-us.js
export default {
  asset: {
    ziChanMingCheng: 'Asset Name',
    shenQingQuanXian: 'Apply for Permission',
  }
}
```

### Step 5: 修改代码文件

**Vue 文件 template 中**：
```vue
<div>{{ $t('asset.ziChanMingCheng') }}</div>
<el-input :placeholder="$t('common.qingShuRu')" />
```

**Vue 文件 script 中**：
```javascript
this.$message.success(this.$t('common.caoZuoChengGong'))
```

**JS 文件中（关键！）**：
```javascript
// ✅ 正确：直接使用 I18N.t()
import I18N from 'joyadata-header/src/i18n';

export const CONFIG = {
  label: I18N.t('asset.ziChanMingCheng'),
};

// ❌ 错误：不要使用 created()
export default {
  created() {
    this.label = this.$t('asset.ziChanMingCheng')  // 不要这样做
  }
}
```

**Router 文件中**：
```javascript
meta: { title: 'router.shouYe' }
```

### Step 6: 质量检查

```bash
# 1. 检查遗漏的中文
grep -rn "[\u4e00-\u9fa5]\+" src --include="*.vue" --include="*.js" | grep -v "\$t(" | grep -v "I18N.t(" | grep -v "//"

# 2. 检查 .replace() 反模式
grep -rn "\.replace(" src --include="*.vue" --include="*.js"

# 3. 检查语法和编译
npm run lint && npm run build
```

## 强制规则

### 1. 不盘点现有配置
- ❌ 不要扫描 zh-cn.js/en-us.js 的现有内容
- ✅ 直接写新模块
- ✅ 遇到冲突时加后缀

### 2. 动态值处理

```javascript
// i18n 配置
key: '最多{val}行'

// 代码中
this.$t('key', { val: maxDepth })  // 或 I18N.t('key', { val: maxDepth })
```

**禁止使用 `.replace()`**：
```javascript
// ❌ 错误
this.$t('key').replace('5', maxDepth)

// ✅ 正确
this.$t('key', { val: maxDepth })
```

### 3. JS 文件必须引入 I18N

```javascript
import I18N from 'joyadata-header/src/i18n';

export const data = {
  label: I18N.t('module.key')
};
```

## 常见问题

### Key 重复
使用后缀区分：`asset_ziChanMingCheng_v2`

### 动态值显示为 {val}
检查是否使用了 `this.$t('key', { val: value })` 格式

### I18N 未定义
确保每个 JS 文件顶部有 `import I18N from 'joyadata-header/src/i18n'`

---

# Part 3: Tools

## convert_re 工具

### 功能说明

`convert_re.py` 将 re.md 文件转换为 key=value 格式。

### 适用场景

- 将表格配置的 JSON 数据转换为属性映射格式
- 批量生成 prop 与 name 的对应关系

### 使用方法

```bash
# 基础使用
python scripts/convert_re.py --input re.md

# 指定输出文件
python scripts/convert_re.py --input re.md --output converted.txt
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| --input | re.md | 输入文件路径 |
| --output | converted_re.md | 输出文件路径 |

---

# 参考文档

详细规范见：
- 国际化规范：[vue-i18n/references/conventions.md](../md/vue-i18n/references/conventions.md)
