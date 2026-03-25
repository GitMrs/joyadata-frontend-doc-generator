# Joyadata Frontend Documentation Generator

> 基于 Trae AI 的 Joyadata 前端文档生成与国际化辅助工具

## 简介

Joyadata Frontend Documentation Generator 是一个集成在 Trae AI 中的 skill，为 Joyadata 前端组件库提供智能文档查询和 Vue2 项目国际化重构支持。

### 主要功能

- 🤖 **组件文档生成** - 自动识别 joyadata-xxx 组件并提供完整使用文档
- 🌐 **国际化重构** - Vue2 项目 i18n 改造指南，支持中英文切换
- 🔧 **工具支持** - re.md 格式转换工具
- 📚 **完整示例** - 每个组件配有可运行的代码示例
- 🔄 **实时更新** - 修改 MD 文件即可更新文档

## 功能特性

### 组件文档

- 自动识别组件并提供 Props、Events、Methods、Slots 说明
- 结构化的文档模板，便于快速查阅
- 实际可运行的代码示例
- 覆盖 7+ 个核心组件

### 国际化支持

- Vue2 项目国际化重构 SOP
- Key 命名规范与最佳实践
- 完整的代码替换模式
- 质量检查清单

## 支持的组件

| 组件 | 说明 | 文档状态 |
|------|------|---------|
| joyadata-table | 表格组件，基于 el-table，支持虚拟滚动、列过滤、拖拽排序 | ✅ 完整 |
| joyadata-form | 表单组件，基于 el-form，支持 25+ 种表单类型 | ✅ 完整 |
| joyadata-dialog | 弹框组件，基于 el-dialog，支持数据变更检测 | ✅ 完整 |
| joyadata-menu | 菜单组件，基于 el-menu，支持多级菜单和路由匹配 | ✅ 完整 |
| joyadata-aside | 目录树组件，基于 el-tree，支持搜索、右键菜单、拖拽 | ✅ 完整 |
| joyadata-search | 搜索组件，支持高级搜索、批量操作 | ✅ 完整 |
| joyadata-tree | 树组件，基于 el-tree，支持懒加载、虚拟滚动 | ✅ 完整 |
| joyadata-data-import | 数据源引入组件，集成树+搜索+表格 | ✅ 完整 |
| joyadata-request | 请求封装与工具方法，支持 GET/POST/上传/下载 | ✅ 完整 |

## 项目文档

| 文档 | 类型 | 说明 |
|------|------|------|
| [joyadata-setup](docs/joyadata-setup.md) | 项目指南 | 项目环境搭建、初始化、接口规范 |
| [joyadata-table](docs/joyadata-table.md) | 组件文档 | 表格组件完整文档 |
| [joyadata-form](docs/joyadata-form.md) | 组件文档 | 表单组件完整文档 |
| [joyadata-dialog](docs/joyadata-dialog.md) | 组件文档 | 弹框组件完整文档 |
| [joyadata-menu](docs/joyadata-menu.md) | 组件文档 | 菜单组件完整文档 |
| [joyadata-aside](docs/joyadata-aside.md) | 组件文档 | 目录树组件完整文档 |
| [joyadata-search](docs/joyadata-search.md) | 组件文档 | 搜索组件完整文档 |
| [joyadata-tree](docs/joyadata-tree.md) | 组件文档 | 树组件完整文档 |
| [joyadata-request](docs/joyadata-request.md) | 工具文档 | 请求封装与工具方法完整文档 |
| [joyadata-i18n](docs/joyadata-i18n.md) | 国际化指南 | Vue2 i18n 重构完整 SOP |
| [joyadata-convert-re](docs/joyadata-convert-re.md) | 工具文档 | re.md 格式转换工具 |

## 目录结构

```
.trae/skills/joyadata-frontend-doc-generator/
├── README.md                       # 本文件
├── SKILL.md                        # Skill 主配置文件
├── scripts/                        # 工具脚本
│   └── convert_re.py              # re.md 格式转换工具
└── docs/                           # 文档文件夹
    ├── joyadata-setup.md           # 项目环境搭建指南
    ├── joyadata-table.md           # 表格组件文档
    ├── joyadata-form.md            # 表单组件文档
    ├── joyadata-dialog.md          # 弹框组件文档
    ├── joyadata-menu.md            # 菜单组件文档
    ├── joyadata-aside.md           # 目录树组件文档
    ├── joyadata-search.md          # 搜索组件文档
    ├── joyadata-tree.md            # 树组件文档
    ├── joyadata-dataimport.md      # 数据引入组件文档
    ├── joyadata-request.md         # 请求封装与工具方法文档
    ├── joyadata-i18n.md            # 国际化指南（新增）
    └── joyadata-convert-re.md      # 转换工具文档（新增）
```

## 使用方法

### 组件文档查询

**触发方式**：

1. **代码中使用组件**
   ```vue
   <joyadata-table :column="column" :mock-data="data" />
   ```

2. **直接询问**
   - "joyadata-form 组件怎么使用？"
   - "表格组件有哪些属性？"
   - "如何初始化项目？"

3. **询问 API 与工具方法**
   - "joyadata 如何发送请求？"
   - "如何配置 axios？"
   - "如何上传下载文件？"
   - "有哪些工具方法可用？"

### 国际化支持

**触发关键词**：

- "国际化"、"i18n"、"中英文"、"多语言"
- "vue-i18n"、"添加英文翻译"
- "把中文改成国际化"

**AI 将提供**：
- 完整的国际化重构流程
- Key 命名规范
- 代码替换模式
- 质量检查清单
- 常见问题解决方案

## 添加新文档

### 添加新组件文档

1. 在 `docs/` 文件夹下创建新文件：`docs/joyadata-xxx.md`
2. 使用标准模板编写内容
3. Skill 会自动识别新组件

### 文档模板

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

| Method | Parameters | Description |
|--------|------------|-------------|

## Slots

| Slot Name | Parameters | Description |
|----------|------------|-------------|

## Important Notes

重要说明
```

## 常见组合模式

### 列表页完整结构

```vue
<template>
  <div>
    <!-- 搜索区域 -->
    <joyadata-search
      ref="searchRef"
      :parmas="parmas"
      :operation="operation"
      @searchFn="searchFn"
    />

    <!-- 批量操作 + 表格 -->
    <joyadata-table
      ref="tableRef"
      :column="column"
      :url="tableUrl"
      :selection="true"
      :batch-data="batchData"
      @selectData="handleSelectData"
    />

    <!-- 弹框 + 表单 -->
    <joyadata-dialog
      ref="dialog"
      title="新增"
      @affirm="handleConfirm"
    >
      <joyadata-form
        ref="formDom"
        :main="main"
        :rules="rules"
      />
    </joyadata-dialog>
  </div>
</template>
```

### 侧边栏布局

```vue
<template>
  <div class="layout">
    <!-- 侧边栏 -->
    <joyadata-aside
      ref="asideRef"
      :nav-val="treeData"
      @changeAside="handleNodeClick"
    />

    <!-- 主内容区 -->
    <div class="main-content">
      <!-- 主内容 -->
    </div>
  </div>
</template>
```

### 国际化集成

```javascript
// zh-cn.js
export default {
  common: {
    qingShuRu: '请输入',
    qingXuanZe: '请选择',
    caoZuoChengGong: '操作成功'
  },
  table: {
    ziChanMingCheng: '资产名称',
    chuangJianShiJian: '创建时间'
  }
}

// Vue 模板中使用
<el-input :placeholder="$t('common.qingShuRu')" />
<div>{{ $t('table.ziChanMingCheng') }}</div>

// JS 配置文件中
import I18N from 'joyadata-header/src/i18n';
export const CONFIG = {
  label: I18N.t('table.ziChanMingCheng')
};
```

### 请求与工具方法集成

```javascript
// 在 Vue 组件中使用请求方法
export default {
  methods: {
    async fetchData() {
      // GET 请求
      const res = await this.$request._get('/api/data', { id: 1 });

      // POST 请求
      const result = await this.$request._post('/api/save', { name: 'test' });

      // 上传文件
      await this.$request._uploadFile('/api/upload', formData);

      // 下载文件
      await this.$request._downFile('/api/download', { id: 1 });
    },

    handleData() {
      // 深拷贝
      const copy = this.$utils.deepClone(originalData);

      // 时间格式化
      const timeStr = this.$utils.parseTime(new Date(), '{y}-{m}-{d}');

      // 存储
      this.$storage.setLocalStorage('key', value);
      const data = this.$storage.getLocalStorage('key');
    }
  }
}
```

## 工具使用

### convert_re 工具

将 re.md 格式的表格配置转换为 key=value 格式。

**输入**：
```
table	[{"prop": "name", "name": "名称"}, {"prop": "time", "name": "时间"}]
```

**输出**：
```
table.name=名称
table.time=时间
```

**使用方法**：
```bash
python scripts/convert_re.py --input re.md --output converted.txt
```

## 文档规范

### 组件文档必须包含

- ✅ Basic Usage（基础用法）
- ✅ Props（所有属性，含类型和默认值）
- ✅ Events（所有事件）
- ✅ Methods（公共方法）
- ✅ Slots（插槽）
- ✅ Important Notes（注意事项）

### 代码示例规范

- 使用完整的 Vue 组件示例
- 包含必要的 data、methods、computed
- 添加注释说明关键配置
- 确保代码可运行

## 技术栈

- **框架**: Vue 2.x (Element UI)
- **国际化**: vue-i18n
- **AI**: Trae AI Skill
- **文档格式**: Markdown
- **工具**: Python 3.x

## 相关资源

- [Element UI 文档](https://element.eleme.io/)
- [vue-i18n 文档](https://kazupon.github.io/vue-i18n/)
- [Joyadata CLI](https://www.npmjs.com/package/joyadata-cli)
- [组件库源码](http://39.107.213.160/joyadata-web/joyadata-vue-template/)

## 更新日志

### v2.0.0 (2026-03-25)

- ✨ 新增 Vue2 国际化重构支持
- ✨ 新增 joyadata-data-import 组件文档
- ✨ 新增 convert_re 工具文档
- 🔧 更新所有组件文档，补充 Props、Events、Methods、Slots
- 🔧 完善文档模板和示例
- 📝 重构 README 结构

### v1.0.0 (2026-03-03)

- 🎉 首次发布
- 📚 支持 7 个核心组件文档

---

**维护者**: @无名草
**版本**: 2.0.0
**更新日期**: 2026-03-25
