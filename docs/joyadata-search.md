# joyadata-search

**Description**: 基于 `el-form` 封装的搜索组件，支持多种表单控件、高级搜索、操作按钮组等功能，适用于列表页面的搜索和操作区域。

## Basic Usage

```html
<joyadata-search :operation="searchOperation" :parmas="parmas" />

<script>
export default {
  data() {
    return {
      searchOperation: [
        {
          name: "新增",
          type: "primary",
          icon: "el-icon-plus",
          plain: true,
          handle: () => {
            this.add();
          }
        }
      ],
      parmas: [
        {
          type: "input",
          props: "name",
          placeholder: "请输入名称",
          label: "名称"
        }
      ]
    };
  }
};
</script>
```

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| **基础配置** | | | |
| type | String | `'page'` | 工作模式：`page`(页面模式，修改 URL)、`dialog`(弹框模式) |
| parmas | Array | `[]` | 搜索表单项配置数组 |
| searchProp | String | `'keywords'` | 默认搜索框的字段名 |
| placeholder | String | `''` | 默认搜索框占位符 |
| maxlength | Number | `0` | 默认搜索框最大长度 |
| searchBy | String | `''` | 搜索字段标识（用于 URL searchby 参数） |
| paramkeys | String | `undefined` | 额外的 paramkeys 参数 |
| **按钮配置** | | | |
| resetBtn | Boolean | `true` | 是否显示重置按钮 |
| searchText | String | `'搜 索'` | 搜索按钮文字 |
| operation | Array | `[]` | 操作按钮配置数组 |
| operationDrop | Object | `{num: 0}` | 操作按钮下拉配置，`num=0` 时不启用下拉 |
| operationBth | Boolean | `false` | 是否显示操作按钮区域 |
| **高级搜索** | | | |
| searchHeight | Boolean | `false` | 是否启用高级搜索功能 |
| searchHdata | Array | `[]` | 高级搜索表单项配置 |
| searchHText | String | `''` | 高级搜索按钮文字 |
| hSearchBtn | Boolean | `false` | 是否显示高级搜索按钮 |
| hLw | String | `'auto'` | 高级搜索标签宽度 |
| HSLP | String | `'right'` | 高级搜索标签位置 |
| hSearchClassName | String | `'height_search_wrap'` | 高级搜索区域类名 |
| hSearchVuex | Boolean | `true` | 是否使用 Vuex 管理高级搜索状态 |
| hOperationBth | Boolean | `true` | 高级搜索区域是否显示操作按钮 |
| **数据初始化** | | | |
| defaultStatus | Object | `{parmasForm: {}, frameTime: {}, multipleData: {}, cascaderForm: {}}` | dialog 模式下的默认值 |
| initReset | Boolean | `true` | 是否在路由变化时重置 |
| cSearch | Boolean | `true` | 每次点击是否都触发搜索 |
| tableRef | String | `'table_dom'` | 联动的表格 ref 名称 |
| defaultPage | Number | `0` | 默认页码 |
| **其他配置** | | | |
| inline | Boolean | `true` | 表单项是否行内显示 |
| disabled | Boolean | `false` | 是否禁用搜索区域 |
| unClearable | Boolean | `false` | 是否隐藏清空按钮 |
| registerSearchFn | Function | `() => false` | 自定义重置逻辑 |
| searchBase64 | Boolean | `false` | 搜索值是否 Base64 编码 |
| searchNoBase64 | Boolean | `false` | 搜索值不使用 Base64 |

## parmas 配置项说明

每个搜索表单项支持的配置：

| Parameter | Type | Description |
|-----------|------|-------------|
| type | String | 表单类型（见下方类型列表） |
| prop | String | 字段名称 |
| label | String | 标签文字 |
| placeholder | String | 占位符 |
| labelWidth | String | 标签宽度 |
| itemWidth | String | 表单项宽度 |
| float | String | 浮动方向 |
| data | Array | 选项数据（select/radio 等） |
| multiple | Boolean | 是否多选 |
| unClearable | Boolean | 是否隐藏清空按钮 |
| attrs | Object | 其他属性 |
| handle | Function | 值变化回调 |
| change | Function | 变化回调 |
| slotName | String | 自定义插槽名称 |

## 支持的表单类型 (type)

| 类型值 | 说明 | 特有参数 |
|-------|------|---------|
| `input` | 文本输入框 | `maxlength` |
| `select` | 下拉选择框 | `groups`、`multipleCheckbox` |
| `selectTree` | 树形选择器 | `multiple`、`normalizer`、`key`、`labelSlot` |
| `cascader` | 级联选择器 | `data`、`filterMethod`、`noCheckStrictly`、`cascaderSlotName` |
| `frame` | 时间范围（分开的两个选择器） | `format`、`valueFormat` |
| `daterange` | 时间范围（一个选择器） | `format`、`valueFormat`、`timeMultiple`、`typeRange` |
| `radio` | 单选框组 | `data`、`width` |
| `slotName` | 自定义插槽 | - |

## operation 配置说明

操作按钮数组配置格式：

```javascript
operation: [
  {
    name: '新增',           // 按钮文字
    type: 'primary',        // 按钮类型
    icon: 'el-icon-plus',   // 图标类名
    plain: true,            // 是否朴素按钮
    handle: () => {},       // 点击回调
    permission: () => {},   // 权限控制函数，返回 true 禁用
    hidden: () => {},       // 隐藏控制函数，返回 true 隐藏
    slotName: 'custom',     // 使用插槽
    toolTips: '提示信息',   // Tooltip 提示
    effect: 'dark',         // Tooltip 主题
    placement: 'top'        // Tooltip 位置
  }
]
```

## operationDrop 配置说明

操作按钮下拉配置：

```javascript
operationDrop: {
  num: 2,                  // 从第几个按钮开始使用下拉菜单（0=不启用）
  end: 4,                  // 结束位置（可选），之后按钮不放入下拉
  dropdownText: '更多',     // 下拉按钮文字
  dropdownType: 'primary',  // 下拉按钮类型
  dropdownNoPlain: false,  // 下拉按钮是否朴素
  svg: 'icon-name',        // 图标名称
  more: true,              // 是否显示下拉箭头
  toolTip: '提示',         // Tooltip 提示
  effect: 'dark'           // Tooltip 主题
}
```

## 事件说明 (Events)

| Event Name | Parameters | Description |
|------------|------------|-------------|
| searchFn | `(parmas)` | 点击搜索按钮时触发 |
| searchResetFn | `-` | 点击重置按钮时触发 |
| hSearchFn | `(hSearchVal)` | 高级搜索展开/收起时触发 |

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Description |
|--------|------------|-------------|
| restParmas | `(type)` | 重置搜索参数 |
| setValue | `(value)` | 设置默认搜索框的值 |
| setSearchDisabled | `(disabled)` | 设置搜索按钮禁用状态 |
| changeParmas | `(key, value)` | 修改指定参数的值 |

## 使用示例

### 基础搜索

```vue
<template>
  <joyadata-search
    :parmas="parmas"
    :operation="operation"
  />
</template>

<script>
export default {
  data() {
    return {
      parmas: [
        {
          type: 'input',
          prop: 'name',
          placeholder: '请输入名称',
          label: '名称'
        }
      ],
      operation: [
        {
          name: '新增',
          type: 'primary',
          icon: 'el-icon-plus',
          handle: () => {
            console.log('新增')
          }
        }
      ]
    }
  }
}
</script>
```

### 弹框模式使用

```vue
<template>
  <joyadata-dialog
    ref="dialog"
    title="选择数据"
    :footer="false"
  >
    <joyadata-search
      ref="searchValue"
      type="dialog"
      :parmas="parmas"
      @searchFn="searchFn"
      @searchResetFn="searchResetFn"
    />
    <joyadata-table
      ref="table_dom"
      :url="dataUrl"
      :column="column"
    />
  </joyadata-dialog>
</template>

<script>
export default {
  data() {
    return {
      dataUrl: '',
      parmas: [
        {
          type: 'input',
          prop: 'keywords',
          label: '搜索'
        }
      ],
      column: []
    }
  },
  methods: {
    open() {
      this.$refs.dialog.open()
    },
    searchFn(params) {
      this.$refs.table_dom.search = params
      this.$refs.table_dom.searchFn()
    },
    searchResetFn() {
      this.$refs.searchValue.restParmas()
      this.$refs.table_dom.search = {}
      this.$refs.table_dom.searchFn()
    }
  }
}
</script>
```

### 高级搜索

```vue
<template>
  <joyadata-search
    :parmas="parmas"
    :searchHdata="searchHdata"
    :searchHeight="true"
    searchHText="高级搜索"
  />
</template>

<script>
export default {
  data() {
    return {
      parmas: [
        {
          type: 'input',
          prop: 'name',
          label: '名称'
        }
      ],
      searchHdata: [
        {
          type: 'select',
          prop: 'status',
          label: '状态',
          data: [
            { label: '启用', value: '1' },
            { label: '禁用', value: '0' }
          ]
        },
        {
          type: 'daterange',
          prop: 'createTime',
          label: '创建时间',
          format: 'yyyy-MM-dd',
          valueFormat: 'yyyy-MM-dd'
        }
      ]
    }
  }
}
</script>
```

### 操作按钮组（带下拉）

```vue
<template>
  <joyadata-search
    :parmas="parmas"
    :operation="operation"
    :operationDrop="operationDrop"
  />
</template>

<script>
export default {
  data() {
    return {
      parmas: [],
      operation: [
        { name: '新增', type: 'primary', icon: 'el-icon-plus', handle: () => {} },
        { name: '导出', type: 'success', icon: 'el-icon-download', handle: () => {} },
        { name: '导入', type: 'warning', icon: 'el-icon-upload2', handle: () => {} },
        { name: '批量删除', type: 'danger', icon: 'el-icon-delete', handle: () => {} }
      ],
      operationDrop: {
        num: 2,  // 从第 3 个按钮开始放入下拉菜单
        dropdownText: '更多操作'
      }
    }
  }
}
</script>
```

### 复杂搜索场景

```vue
<template>
  <joyadata-search
    :parmas="parmas"
    :operation="operation"
    searchBy="name,code"
  />
</template>

<script>
export default {
  data() {
    return {
      parmas: [
        {
          type: 'input',
          prop: 'name',
          label: '名称',
          maxlength: 50
        },
        {
          type: 'select',
          prop: 'type',
          label: '类型',
          data: [
            { label: '类型 1', value: '1' },
            { label: '类型 2', value: '2' }
          ]
        },
        {
          type: 'selectTree',
          prop: 'orgId',
          label: '组织',
          data: [],
          normalizer: (node) => ({
            id: node.id,
            label: node.name,
            children: node.children
          })
        },
        {
          type: 'cascader',
          prop: 'region',
          label: '地区',
          data: [],
          filterMethod: (node, keyword) => {
            return node.text.toUpperCase().includes(keyword.toUpperCase())
          }
        },
        {
          type: 'frame',
          prop: 'timeRange',
          label: '时间范围'
        }
      ],
      operation: [
        {
          name: '搜索',
          type: 'primary',
          icon: 'el-icon-search'
        }
      ]
    }
  }
}
</script>
```

## defaultStatus 详细说明

dialog 模式下的默认值配置：

```javascript
defaultStatus: {
  // 普通表单默认值
  parmasForm: {
    status: 'all',
    keywords: ''
  },
  // 时间范围默认值
  frameTime: {
    createTime: ['2023-01-01', '2023-12-31']
  },
  // 多选默认值
  multipleData: {
    roleIds: ['1', '2', '3']
  },
  // 级联选择默认值
  cascaderForm: {
    region: ['110000', '110100']
  }
}
```

## Important Notes

1. **type 模式区别**：
   - `page` 模式：搜索会修改 URL，适合列表页面
   - `dialog` 模式：搜索触发事件，适合弹框内搜索

2. **时间范围格式**：
   - `frame`：两个独立的日期选择器
   - `daterange`：一个日期范围选择器

3. **多选处理**：多选的值会自动用逗号拼接成字符串

4. **级联选择器**：支持单选和多选，多选时使用 `/` 拼接

5. **Base64 编码**：开启 `searchBase64` 后，搜索关键词会进行 Base64 编码

6. **操作按钮权限**：通过 `permission` 和 `hidden` 函数控制按钮显示和禁用
