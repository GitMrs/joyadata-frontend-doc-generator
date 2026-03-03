# Joyadata 组件文档 Skill

> 基于 Trae AI 打造的智能组件文档生成工具

## 简介

Joyadata Component Doc Generator 是一个集成在 Trae AI 中的 skill，专门为 Joyadata 前端组件库提供智能文档查询功能。当你在代码中使用 `joyadata-xxx` 组件时，AI 会自动识别并提供完整的使用文档。

## 功能特性

- 🤖 **自动识别** - AI 自动识别代码中的组件并提供文档
- 📚 **模块化文档** - 每个组件独立文档，易于维护
- 💻 **完整示例** - 每个组件配有可运行的代码示例
- 🔄 **实时更新** - 修改 MD 文件即可更新文档

## 支持的组件

| 组件 | 说明 | 文档 |
|------|------|------|
| joyadata-table | 表格组件，基于 el-table | ✅ |
| joyadata-form | 表单组件，基于 el-form | ✅ |
| joyadata-dialog | 弹框组件，基于 el-dialog | ✅ |
| joyadata-menu | 菜单组件，基于 el-menu | ✅ |
| joyadata-aside | 目录树组件，基于 el-tree | ✅ |
| joyadata-search | 搜索组件 | ✅ |
| joyadata-tree | 树组件 | ✅ |

## 项目文档

| 文档 | 说明 |
|------|------|
| joyadata-setup | 项目环境搭建指南 |

## 目录结构

```
.trae/skills/component-doc-generator/
├── SKILL.md                # Skill 主文件
└── docs/                   # 组件文档
    ├── joyadata-setup.md   # 环境搭建指南
    ├── joyadata-table.md   # 表格组件
    ├── joyadata-form.md    # 表单组件
    ├── joyadata-dialog.md  # 弹框组件
    ├── joyadata-menu.md    # 菜单组件
    ├── joyadata-aside.md   # 目录树组件
    ├── joyadata-search.md  # 搜索组件
    └── joyadata-tree.md    # 树组件
```

## 使用方法

### 触发方式

在 Trae AI 中使用以下方式触发：

1. **代码中使用组件**
   ```vue
   <joyadata-table :column="column" :mock-data="data" />
   ```

2. **直接询问**
   - "joyadata-form 组件怎么使用？"
   - "表格组件有哪些属性？"
   - "如何初始化项目？"

3. **询问 API**
   - "joyadata 如何发送请求？"
   - "如何配置 axios？"

### 在 Trae AI 中使用

当你在代码中输入 `joyadata-` 开头的组件时，skill 会自动被触发并提供相应的文档。

## 添加新组件

如需添加新组件的文档：

1. 在 `docs/` 文件夹下创建新文件：`docs/joyadata-xxx.md`
2. 参考现有文档格式编写内容
3. Skill 会自动识别新组件

## 文档模板

```markdown
# joyadata-xxx

**Description**: 组件简短描述

## Basic Usage

基本用法示例代码

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

重要说明
```

## 常见组合

### 列表页

```vue
<joyadata-search :operation="operation" :parmas="parmas" />
<joyadata-table ref="tableRef" :column="column" :mock-data="data" />
<joyadata-dialog ref="dialog" title="标题" @affirm="affirm">
  <joyadata-form ref="formDom" :main="main" :rules="rules" />
</joyadata-dialog>
```

### 侧边栏

```vue
<joyadata-menu :menu-data="menuData" />
<joyadata-aside :nav-val="treeData" @changeAside="changeAside" />
```

## 技术栈

- **框架**: Vue 2.x (Element UI)
- **AI**: Trae AI Skill
- **文档格式**: Markdown

## 相关资源

- [Element UI 文档](https://element.eleme.io/)
- [Joyadata CLI](https://www.npmjs.com/package/joyadata-cli)
- [组件库源码](http://39.107.213.160/joyadata-web/joyadata-vue-template/)

---

**作者**: @无名草  
**版本**: 1.0.0  
**更新日期**: 2026-03-03
