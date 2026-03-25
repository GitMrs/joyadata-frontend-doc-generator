# joyadata-i18n

**Description**: Vue2 项目国际化重构指南，扫描 components/views/router 目录，将中文文案替换为 i18n 配置，生成 zh-cn.js 和 en-us.js。

## Basic Usage

### 在 Vue 模板中使用

```vue
<template>
  <div>
    <!-- 静态文本 -->
    <div>{{ $t('asset.ziChanMingCheng') }}</div>

    <!-- 属性绑定 -->
    <el-input :placeholder="$t('common.qingShuRu')" />

    <!-- 动态参数 -->
    <div>{{ $t('asset.zuiDuoHang', { val: maxDepth }) }}</div>
  </div>
</template>
```

### 在 Vue Script 中使用

```javascript
export default {
  methods: {
    handleSubmit() {
      this.$message.success(this.$t('common.caoZuoChengGong'))
    }
  },
  computed: {
    title() {
      return this.$t('asset.ziChanMingCheng')
    }
  }
}
```

### 在 JS 配置文件中使用

```javascript
import I18N from 'joyadata-header/src/i18n';

export const CONFIG = {
  label: I18N.t('asset.ziChanMingCheng'),
  placeholder: I18N.t('common.qingShuRu'),
  data: [
    { label: I18N.t('common.biao'), value: 'table' }
  ]
};
```

## Key 命名规范

### 基本规则

**拼音驼峰命名法**：
- 首字母小写
- 多个词直接拼接，无分隔符
- 使用完整拼音，不缩写

| 中文 | Key | ✅/❌ |
|------|-----|------|
| 浏览视角 | liuLanShiJiao | ✅ |
| 全文搜索 | quanWenSouSuo | ✅ |
| 请选择 | qingXuanZe | ✅ |
| llsc | llsc | ❌ 不要缩写 |
| liu_lan_shi_jiao | liu_lan_shi_jiao | ❌ 不要下划线 |
| LiuLanShiJiao | LiuLanShiJiao | ❌ 首字母不要大写 |

### 模块组织

**平铺结构（< 20 个 key）**：

```javascript
asset: {
  ziChanMingCheng: '资产名称',
  dingYueLiang: '订阅量',
  liuLanLiang: '浏览量'
}
```

**嵌套结构（> 20 个 key 或有子组件）**：

```javascript
assetDetails: {
  index: {
    caoZuoYinDao: '操作引导',
    shenQingDingYue: '申请订阅'
  },
  com: {
    dataItem: {
      ziDuanMing: '字段名',
      ziDuanLeiXing: '字段类型'
    }
  }
}
```

### 冲突处理

遇到 Key 重复时，添加后缀：

```javascript
// 第一次
asset: {
  ziChanMingCheng: '资产名称'
}

// 第二次遇到相同语义但不同文案
asset: {
  ziChanMingCheng: '资产名称',
  ziChanMingCheng_v2: '资产全称'
}
```

## 代码替换模式

### Vue 模板

| 场景 | 修改前 | 修改后 |
|------|--------|--------|
| 静态文本 | `<div>资产名称</div>` | `<div>{{ $t('asset.ziChanMingCheng') }}</div>` |
| 属性绑定 | `<el-input placeholder="请输入" />` | `<el-input :placeholder="$t('common.qingShuRu')" />` |
| 动态参数 | `最多{{ maxDepth }}行` | `{{ $t('asset.zuiDuoHang', { val: maxDepth }) }}` |
| 循环 | `{{ item.name }}` | `{{ $t('module.itemName', { val: item.name }) }}` |

### Vue Script

| 场景 | 修改前 | 修改后 |
|------|--------|--------|
| methods | `this.$message.success('操作成功')` | `this.$message.success(this.$t('common.caoZuoChengGong'))` |
| computed | `return '标题'` | `return this.$t('module.biaoTi')` |
| data | `label: '中文'` | `label: this.$t('module.key')` |

### JS 配置文件

**正确方式**：

```javascript
import I18N from 'joyadata-header/src/i18n';

export const CONFIG = {
  label: I18N.t('asset.ziChanMingCheng'),
  placeholder: I18N.t('common.qingShuRu'),
  data: [
    { label: I18N.t('common.biao'), value: 'table' },
    { label: I18N.t('common.shi'), value: 'view' }
  ]
};
```

**错误方式**：

```javascript
// ❌ 不要用 created()
export default {
  data() {
    return { label: '' }
  },
  created() {
    this.label = this.$t('module.key')  // 不要这样做
  }
}

// ❌ 不要用 computed（在配置文件中）
export default {
  computed: {
    label() {
      return this.$t('module.key')  // 不要这样做
    }
  }
}
```

## 动态值处理

### 参数化格式

**i18n 配置**：

```javascript
// 使用 {val} 作为占位符
key: '最多{val}行'
welcome: '欢迎，{name}'
result: '找到{count}条结果'
```

**代码调用**：

```javascript
// Vue 模板中
{{ $t('module.key', { val: maxDepth }) }}
{{ $t('module.welcome', { name: userName }) }}
{{ $t('module.result', { count: total }) }}

// Vue script 中
this.$t('module.key', { val: maxDepth })
this.$t('module.welcome', { name: userName })

// JS 文件中
I18N.t('module.key', { val: maxDepth })
I18N.t('module.welcome', { name: userName })
```

### 禁止的模式

```javascript
// ❌ 错误：使用 .replace()
this.$t('key').replace('5', maxDepth)

// ❌ 错误：使用模板字符串拼接
`${this.$t('key')}${maxDepth}`

// ✅ 正确：使用参数化
this.$t('key', { val: maxDepth })
```

## 特殊情况处理

### 路由 meta.title

```javascript
// router/index.js
{
  path: '/home',
  meta: { title: 'router.shouYe', code: 'home' }  // 使用 key 字符串
}

// 在组件中使用
computed: {
  pageTitle() {
    return this.$t(this.$route.meta.title)  // 动态获取
  }
}
```

### Tab name 属性

```vue
<!-- ❌ 错误：使用中文作为标识符 -->
<el-tab-pane :label="$t('assetDetails.index.shuJuXiang')" name="数据项">

<!-- ✅ 正确：使用英文标识符 -->
<el-tab-pane :label="$t('assetDetails.index.shuJuXiang')" name="dataItem">
```

**原因**：`name` 属性是程序标识符，应用英文而不是中文

### 动态类名

```vue
<!-- ❌ 错误 -->
:class="'中文类名'"

<!-- ✅ 正确：使用拼音或英文 -->
:class="'leiMing'"

<!-- 或者直接用对象语法 -->
:class="{ active: isActive }"
```

## 国际化配置文件

### zh-cn.js

```javascript
export default {
  // 通用模块
  common: {
    qingShuRu: '请输入',
    qingXuanZe: '请选择',
    biao: '表',
    shi: '视图',
    caoZuoChengGong: '操作成功',
    caoZuoShiBai: '操作失败'
  },

  // 路由模块
  router: {
    shouYe: '首页',
    ziChanGuanLi: '资产管理'
  },

  // 业务模块
  asset: {
    ziChanMingCheng: '资产名称',
    dingYueLiang: '订阅量',
    liuLanLiang: '浏览量',
    liuLanShiJiao: '浏览视角',
    quanWenSouSuo: '全文搜索',
    shenQingQuanXian: '申请权限',
    zuiDuoHang: '最多{val}行'
  }
}
```

### en-us.js

```javascript
export default {
  // 通用模块
  common: {
    qingShuRu: 'Please input',
    qingXuanZe: 'Please select',
    biao: 'Table',
    shi: 'View',
    caoZuoChengGong: 'Operation successful',
    caoZuoShiBai: 'Operation failed'
  },

  // 路由模块
  router: {
    shouYe: 'Home',
    ziChanGuanLi: 'Asset Management'
  },

  // 业务模块
  asset: {
    ziChanMingCheng: 'Asset Name',
    dingYueLiang: 'Subscriptions',
    liuLanLiang: 'Page Views',
    liuLanShiJiao: 'Browse Perspective',
    quanWenSouSuo: 'Full Text Search',
    shenQingQuanXian: 'Apply Permission',
    zuiDuoHang: 'Max {val} rows'
  }
}
```

## 国际化重构流程

### Step 1: 项目扫描与统计

```bash
# 统计需要处理的文件数量
find src/components -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
find src/views -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
find src/router -type f \( -name "*.vue" -o -name "*.js" \) | wc -l
```

### Step 2: 制定批次计划

| 文件总数 | 建议批次数 | 策略 |
|---------|----------|------|
| < 20 | 2-3 批 | 按目录分组 |
| 20-50 | 4-5 批 | 先核心组件，后业务页面 |
| > 50 | 6+ 批 | 按功能模块划分 |

### Step 3: 提取中文并生成 Key 映射

**命名规则**：
- 使用拼音驼峰
- 模块结构：`moduleName.keyName`
- 冲突处理：加后缀 `_v2`

**示例映射表**：

| 原文 | Key | 所属模块 |
|------|-----|---------|
| 资产名称 | ziChanMingCheng | asset |
| 申请权限 | shenQingQuanXian | asset |

### Step 4: 更新 i18n 配置文件

在 `src/locales/zh-cn.js` 和 `src/locales/en-us.js` 中添加新模块。

### Step 5: 修改代码文件

按上述代码替换模式修改所有文件。

### Step 6: 质量检查

```bash
# 1. 检查遗漏的中文
grep -rn "[\u4e00-\u9fa5]\+" src --include="*.vue" --include="*.js" | grep -v "\$t(" | grep -v "I18N.t(" | grep -v "//"

# 2. 检查 .replace() 反模式
grep -rn "\.replace(" src --include="*.vue" --include="*.js"

# 3. 检查语法
npm run lint

# 4. 编译检查
npm run build
```

## 质量检查清单

### 代码检查

- [ ] 所有 `.vue` 文件的中文文案已替换为 `$t()`
- [ ] 所有 `.js` 文件的中文文案已替换为 `I18N.t()`
- [ ] 所有 JS 文件顶部有 `import I18N from 'joyadata-header/src/i18n'`
- [ ] 没有使用 `.replace()` 处理动态值
- [ ] 没有在 JS 配置文件中使用 `created()` 获取 i18n 值
- [ ] 路由 `meta.title` 使用的是 key 字符串
- [ ] Tab `name` 属性使用英文标识符

### 配置检查

- [ ] `zh-cn.js` 和 `en-us.js` 都添加了新模块
- [ ] Key 命名符合拼音驼峰规范
- [ ] 动态值使用 `{val}` 占位符
- [ ] 没有重复的 Key（或已用后缀区分）

### 运行时检查

- [ ] 切换中英文，页面正常显示
- [ ] 没有显示 `{val}` 或 `{key}` 的原始占位符
- [ ] 动态参数正确显示（如最大行数）
- [ ] 所有表单、弹窗、提示信息国际化
- [ ] 路由标题正确显示

## 常见问题与解决

| 错误 | 原因 | 解决方法 |
|------|------|---------|
| `[vue-i18n] Cannot translate keypath` | Key 未定义 | 检查 zh-cn.js 和 en-us.js 是否都添加了该 key |
| 页面显示 `{val}` | 未使用参数化格式 | 改为 `this.$t('key', { val: value })` |
| `I18N is not defined` | 未引入 I18N | 在 JS 文件顶部添加 `import I18N from 'joyadata-header/src/i18n'` |
| `this.$t is not a function` | 在 JS 配置文件中使用了 `this.$t()` | 改为 `I18N.t()` |
| 动态值不更新 | 使用了 `.replace()` | 改用参数化格式 `this.$t('key', { val: value })` |
| Tab 切换失败 | name 属性使用中文 | 改用英文标识符 |

## 命令速查

```bash
# 统计未替换的中文数量
grep -ro "[\u4e00-\u9fa5]\+" src/views --include="*.vue" | wc -l

# 查找特定文件中的中文
grep -n "[\u4e00-\u9fa5]\+" src/views/asset/index.vue

# 检查 .replace() 反模式
grep -rn "\.replace(" src --include="*.vue" --include="*.js"

# 检查遗漏的中文（排除注释和 i18n 调用）
grep -rn "[\u4e00-\u9fa5]\+" src --include="*.vue" --include="*.js" | grep -v "\$t(" | grep -v "I18N.t(" | grep -v "//"
```

## Important Notes

1. **JS 文件必须引入 I18N**: 在每个 JS 文件顶部添加 `import I18N from 'joyadata-header/src/i18n'`

2. **禁止使用 .replace()**: 动态值必须使用参数化格式 `$t('key', { val: value })`

3. **不盘点现有配置**: 直接写新模块，遇到冲突时加后缀

4. **扫描范围必须完整**: components、views、router 三个目录都要深度扫描

5. **Tab name 使用英文**: name 属性是程序标识符，应用英文而不是中文

6. **路由使用 key 字符串**: meta.title 应使用如 `'router.shouYe'` 的 key 字符串

7. **Key 命名规范**: 使用拼音驼峰，首字母小写，无分隔符，完整拼音不缩写
