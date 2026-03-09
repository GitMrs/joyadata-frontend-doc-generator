# joyadata-table

**Description**: 基于 `el-table` 封装的表格组件，支持动态列配置、列过滤、拖拽排序、虚拟滚动、批量操作等功能。

## Basic Usage

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :mock-data="mockData"
    :selection="false"
    :sort-index="true"
    height="600px"
  />
</template>

<script>
export default {
  data() {
    return {
      column: [
        { name: "名称", prop: "name", align: "left" },
        { name: "时间", prop: "time", type: "time" }
      ],
      mockData: [
        { id: 1, name: "测试", time: new Date().getTime() }
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
| url | String | `''` | 获取数据的 API 地址 |
| column | Array | `[]` | 表头配置数组 |
| type | String | `'page'` | 工作模式：`page`(页面模式)、`dialog`(弹框模式) |
| rowKey | String | `'id'` | 表格行唯一标识字段 |
| height | String | `'auto'` | 表格高度 |
| data | Array | `[]` | 静态数据（不请求 API 时） |
| mockData | Array | `[]` | 模拟数据（用于测试） |
| showTable | Boolean | `true` | 是否显示表格 |
| isEmpty | Boolean | `true` | 是否使用默认空数据提示 |
| defaultValue | String | `'-'` | 数据为空时的默认显示值 |
| **选择配置** | | | |
| selection | Boolean | `true` | 是否显示复选框 |
| select | Boolean | `false` | 是否支持跨页选择 |
| selectDelayTime | Number | `300` | 跨页选择延迟时间 (ms) |
| radio | Boolean | `false` | 是否支持单选（selection 为 true 时有效） |
| radioType | String | `'checkbox'` | 单选样式：`'checkbox'`/`'radio'` |
| selectedMax | Number | `99999` | 最大选择数量 |
| selectedMaxFn | Function | `null` | 自定义超出最大选择的回调 |
| selectable | Function | `-` | 复选框禁用判断函数 `(row) => Boolean` |
| **排序与序号** | | | |
| sortIndex | Boolean | `true` | 是否显示序号列 |
| sortWidth | Number | `70` | 序号列宽度 |
| sortBy | String | `''` | 默认排序字段 |
| sortAuto | Boolean | `false` | 是否自动保存排序状态 |
| isSortSave | Boolean | `false` | 是否保存排序到后台 |
| multipleSort | Boolean | `false` | 是否支持多列排序 |
| **树形数据** | | | |
| treeProps | Object | `{children: 'children', hasChildren: 'hasChildren'}` | 树形数据配置 |
| defaultExpandAll | Boolean | `false` | 树形数据是否默认全部展开 |
| expandRowKeys | Array | `[]` | 默认展开的行 key 数组 |
| **分页配置** | | | |
| pagination | Boolean | `true` | 是否开启分页 |
| initPager | Number | `0` | 每页条数（0 为自动计算） |
| initPage | Number | `0` | 默认当前页 |
| defaultPage | Number | `0` | 默认页码 |
| fixedPager | Number | `0` | 分页数量修正值 |
| pagerCount | Number | `7` | 页码按钮数量 |
| pageSizes | Array | `[10, 20, 30, 40, 50, 100, 200, 500]` | 每页条数选项 |
| **列配置** | | | |
| useColumn | String | `'useColumn'` | 列渲染模式 |
| filterColumn | Boolean | `false` | 是否开启列过滤（列设置） |
| columnSession | Boolean | `false` | 是否使用本地存储保存列配置 |
| symbolKey | String | `''` | 列配置的唯一标识 |
| isheaderDragend | Boolean | `true` | 是否允许列宽拖拽保存 |
| isDragColumn | Boolean | `false` | 是否允许列拖拽排序 |
| isDragColumnFn | Boolean | `false` | 是否开启列拖拽回调 |
| **高级搜索联动** | | | |
| hSearchClassName | String | `'height_search_wrap'` | 高级搜索区域类名 |
| hSearchVuex | Boolean | `true` | 是否使用 Vuex 管理高级搜索状态 |
| hSearchVal | Boolean | `false` | 高级搜索展开状态 |
| fixedHSearchH | String | `'0px'` | 高级搜索高度补偿值 |
| **冻结与固定** | | | |
| fixed | Object | `{sort: false, select: false}` | 固定列配置 |
| **虚拟滚动** | | | |
| vData | Boolean | `false` | 是否开启虚拟滚动 |
| vDelayTime | Number | `10` | 虚拟滚动防抖时间 |
| vFixedPager | Number | `3` | 虚拟滚动预加载行数 |
| rowHeight | Number | `36` | 行高（虚拟滚动使用） |
| **搜索与过滤** | | | |
| searchBy | String | `''` | 搜索字段配置 |
| searchValue | String | `''` | 本地搜索关键词 |
| filterRow | Function | `null` | 本地过滤函数 |
| paramkeys | Object | `{}` | 额外请求参数 |
| mapKeyParmas | Object | `{}` | 参数键名映射 |
| inParmas | Object | `{}` | 初始请求参数 |
| getMethod | String | `'get'` | 请求方法 |
| **批量操作** | | | |
| batchData | Array | `[]` | 批量操作按钮配置 |
| batchClass | Boolean | `false` | 批量操作按钮特殊样式 |
| **其他配置** | | | |
| tableRowClassName | Function | `-` | 行类名函数 |
| spanMethod | Function | `-` | 合并行/列函数 |
| calcHeight | Number | `220` | 高度计算补偿值 |
| initData | Boolean | `true` | 是否自动初始化数据 |
| initC | Boolean | `true` | 是否初始化列配置 |
| initReset | Boolean | `true` | 路由变化时是否重置 |
| mergeParams | Boolean | `false` | 是否用 URL 参数覆盖 props |
| allCheck | Boolean | `false` | 是否显示全选 |
| allCheckDisalbed | Boolean | `true` | 全选是否禁用 |
| tableId | String | `'multipleTable'` | 表格元素 ID |
| popoverKey | String | `''` | popover 删除时的行标识字段 |
| bId | String | `'id'` | 业务 ID 字段名 |
| resizeObserverTable | Boolean | `true` | 是否监听表格大小变化 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| selectionChange | `(selection)` | 选择变化时触发 |
| selectData | `(data)` | 选中数据变化时触发 |
| changeSelectData | `(data)` | 选中数据改变事件 |
| changeRadioCurrent | `({id, row})` | 单选改变时触发 |
| rowClick | `({row, column, event})` | 行点击事件 |
| cellClick | `({row, column, cell, event})` | 单元格点击事件 |
| rowDblclick | `({row, column, event})` | 行双击事件 |
| cellDblclick | `({row, column, cell, event})` | 单元格双击事件 |
| rowContextmenu | `({row, column, event})` | 行右键事件 |
| headerContextmenu | `({column, event})` | 表头右键事件 |
| cellMouseEnter | `({row, column, cell, event})` | 单元格移入事件 |
| cellMouseLeave | `({row, column, cell, event})` | 单元格移出事件 |
| expandChange | `({row, expandedRows})` | 展开/收起行事件 |
| sortHandle | `(sort)` | 自定义排序事件 |
| filterChange | `(val)` | 筛选条件变化事件 |
| headerDragend | `({newWidth, oldWidth, column, event})` | 表头拖拽结束事件 |
| dataChange | `({newVal, oldVal})` | 数据变化事件 |
| afterData | `(res)` | 获取数据后处理事件 |
| getRowClass | `(row)` | 获取行类名 |
| chidrenLoad | `({tree, treeNode, resolve})` | 懒加载子数据事件 |
| sureColumn | `({checkColumn, type})` | 列设置确认事件 |
| resetColumn | `-` | 列重置事件 |
| vScrollEnd | `-` | 虚拟滚动触底事件 |
| vScrollTop | `-` | 虚拟滚动到顶部事件 |

## Slots

| Slot Name | Parameters | Description |
|-----------|------------|-------------|
| slotMain | `{data}` | 自定义表格主体内容 |
| slotEmpty | `-` | 自定义空数据提示 |
| columnSlot | `-` | 自定义列配置 |
| `{prop}_header` | `{scope}` | 自定义列头（如：`name_header`） |
| `{prop}_expand` | `{scope}` | 自定义展开行内容 |
| batch | `-` | 批量操作插槽 |

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Return | Description |
|--------|------------|--------|-------------|
| init | `(options)` | `-` | 重新加载数据 |
| searchFn | `(val)` | `-` | 执行搜索 |
| getSelectData | `-` | `Array` | 获取选中数据 |
| setSelectData | `(data)` | `-` | 设置选中数据 |
| getData | `-` | `Array` | 获取表格数据 |
| deleteSelectRow | `(row)` | `-` | 删除指定选中行 |
| toggleSelection | `-` | `-` | 切换选中状态 |
| resetTable | `-` | `-` | 重置表格 |
| tableResize | `-` | `-` | 重新计算表格布局 |
| getActiveThead | `-` | `Object` | 获取当前排序状态 |
| setActiveThead | `(key, value)` | `-` | 设置排序状态 |
| getCurrentRadio | `-` | `String` | 获取当前单选值 |
| setCurrentRadio | `(val)` | `-` | 设置当前单选值 |
| clearValidate | `-` | `-` | 清除筛选和排序 |

### init 方法参数

```javascript
// 重新加载数据
this.$refs.tableRef.init()

// 不显示 loading
this.$refs.tableRef.init({ noLoading: true })

// 改变选中的数据
this.$refs.tableRef.init({ selectData: [] })
```

## column 配置说明

### 核心参数

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | String | 是 | 列标题（支持国际化） |
| enName | String | 否 | 英文标题 |
| localName | Boolean | 否 | 是否使用本地化名称 |
| prop | String | 是 | 字段属性名 |
| width | String/Number | 否 | 列宽 |
| align | String | 否 | 对齐方式：`left`/`center`/`right` |
| fixed | String/Boolean | 否 | 是否固定：`true`/`false`/`left`/`right` |
| sortable | Boolean | 否 | 是否可排序 |
| sortType | String | 否 | 排序类型：`custom`/`multiple` |
| tooltip | Boolean | 否 | 是否显示溢出提示 |
| hidden | Boolean | 否 | 是否隐藏该列 |
| visible | Boolean | 否 | 列设置中是否可见 |
| noCheck | Boolean | 否 | 列设置中是否不可取消 |
| checkDisabled | Boolean | 否 | 列设置中是否禁用 |
| attrs | Object | 否 | 传递给 el-table-column 的属性 |
| class | Function/String | 否 | 单元格类名 |
| className | String | 否 | 列类名 |
| formate | Function | 否 | 数据格式化函数 |
| click | Function | 否 | 单元格点击回调 |
| render | Function | 否 | 自定义渲染函数 (h, {row, index, column}) |
| header_render | Function | 否 | 自定义表头渲染函数 |
| filteredValue | Function | 否 | 筛选值函数 |
| labelTip | Object | 否 | 表头提示配置 |
| tipsIcon | String | 否 | 提示图标类名 |
| notify | Object | 否 | 通知配置 |
| notifyFn | Function | 否 | 通知回调函数 |

### type 类型说明

| Type | Description | Special Props |
|------|-------------|---------------|
| `index`/`sortIndex` | 序号列 | `index`: 序号类型 |
| `time` | 时间列（自动格式化） | - |
| `slot` | 自定义插槽列 | `slot_name`: 插槽名称 |
| `slotColumn` | 自定义列插槽 | `slot_name`: 插槽名称 |
| `statusIcon` | 状态图标列 | `statusProps`, `statusColors`, `svg` |
| `switch` | 开关列 | `activeValue`, `inactiveValue`, `activeColor`, `inactiveColor`, `autoSwitch`, `change`, `disabled` |
| `expand` | 展开列 | - |
| `calcWidth` | 自动计算宽度列 | `click`: 点击回调 |
| 普通列 | 无 type 或空 | 直接显示字段值 |

### 操作列配置

```javascript
{
  name: '操作',
  prop: 'Actions',
  width: '200px',
  fixed: 'right',
  align: 'center',
  indent: 40,          // 每个按钮的宽度补偿
  fixedNum: 0,         // 额外宽度补偿
  dropdown: true,      // 是否开启下拉更多
  dropdownNum: 3,      // 下拉按钮数量阈值
  dropdownText: '更多', // 下拉按钮文字
  group: [
    {
      name: '编辑',           // 按钮名称
      type: 'primary',        // 按钮类型（也可为函数）
      plain: true,            // 是否朴素按钮
      icon: 'el-icon-edit',   // 图标
      iconType: 'svg',        // 图标类型：svg/i
      tooltip: '提示信息',     // Tooltip 提示
      tooltipAttr: {},        // Tooltip 配置
      permission: (row) => {}, // 权限判断，返回 true 禁用
      hidden: (row) => {},     // 隐藏判断，返回 true 隐藏
      renderBtn: (row) => {},  // 按钮是否显示判断
      handle: (row, scope) => {}, // 点击回调
      nameFn: (row) => {}     // 动态按钮名称
    },
    {
      name: '删除',
      type: 'popover',        // 使用确认框
      permission: (row) => {},
      handle: (row, closePopover, scope) => {}
    },
    {
      name: '上传',
      type: 'file',           // 文件上传
      plain: true,
      handle: (file, row, scope) => {}
    }
  ]
}
```

## 使用示例

### 基础表格

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
    :pagination="true"
    height="500px"
  />
</template>

<script>
export default {
  data() {
    return {
      tableUrl: '/api/list',
      column: [
        { name: '名称', prop: 'name' },
        { name: '描述', prop: 'description' },
        { name: '创建时间', prop: 'createTime', type: 'time' }
      ]
    }
  }
}
</script>
```

### 带选择和操作的表格

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
    :selection="true"
    :select="true"
    :selected-max="10"
    @selectData="handleSelectData"
  />
</template>

<script>
export default {
  data() {
    return {
      tableUrl: '/api/list',
      column: [
        { name: '名称', prop: 'name' },
        {
          name: '状态',
          prop: 'status',
          type: 'switch',
          activeValue: 1,
          inactiveValue: 0,
          change: (row) => {
            console.log('状态变化', row)
          }
        },
        {
          name: '操作',
          prop: 'Actions',
          fixed: 'right',
          group: [
            {
              name: '编辑',
              type: 'primary',
              handle: (row) => {
                this.edit(row)
              }
            },
            {
              name: '删除',
              type: 'danger',
              permission: (row) => row.locked,
              handle: (row) => {
                this.$confirm('确认删除？', '提示', () => {
                  this.delete(row)
                })
              }
            }
          ]
        }
      ]
    }
  },
  methods: {
    handleSelectData(data) {
      console.log('选中数据:', data)
    }
  }
}
</script>
```

### 带列过滤和拖拽

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
    :filter-column="true"
    :symbol-key="symbolKey"
    :isheader-dragend="true"
    :is-drag-column="true"
  />
</template>

<script>
export default {
  data() {
    return {
      symbolKey: 'product_module_table',
      column: [
        { name: '名称', prop: 'name', width: 150 },
        { name: '编码', prop: 'code', width: 120 },
        { name: '描述', prop: 'description' }
      ]
    }
  }
}
</script>
```

### 自定义渲染列

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
  />
</template>

<script>
export default {
  data() {
    return {
      column: [
        {
          name: '输入框',
          prop: 'input',
          type: 'slot',
          slot_name: 'inputSlot',
          tooltip: false
        },
        {
          name: '渲染列',
          prop: 'renderCol',
          type: 'slot',
          render: (h, { row, index }) => {
            return h('el-tag', { props: { type: 'success' }}, row.value)
          }
        },
        {
          name: '操作',
          prop: 'Actions',
          group: [
            {
              name: '查看详情',
              type: 'text',
              class: (row) => row.disabled ? 'disabled' : '',
              handle: (row) => {
                this.view(row)
              }
            }
          ]
        }
      ]
    }
  }
}
</script>
```

### 状态图标列

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
  />
</template>

<script>
export default {
  data() {
    return {
      column: [
        {
          name: '状态',
          prop: 'status',
          type: 'statusIcon',
          statusProps: {
            0: 'el-icon-close',
            1: 'el-icon-check'
          },
          statusColors: {
            0: '#f56c6c',
            1: '#67c23a'
          }
        },
        {
          name: '级别',
          prop: 'level',
          type: 'statusIcon',
          svg: true,
          statusProps: {
            1: 'level_low',
            2: 'level_mid',
            3: 'level_high'
          }
        }
      ]
    }
  }
}
</script>
```

### 虚拟滚动表格

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
    :v-data="true"
    :row-height="40"
    @vScrollEnd="loadMore"
  />
</template>

<script>
export default {
  methods: {
    loadMore() {
      console.log('触底加载更多')
    }
  }
}
</script>
```

### 树形表格

```vue
<template>
  <joyadata-table
    ref="tableRef"
    :column="column"
    :url="tableUrl"
    :default-expand-all="false"
    :tree-props="{children: 'children', hasChildren: 'hasChildren'}"
    @expandChange="handleExpand"
  />
</template>

<script>
export default {
  methods: {
    handleExpand({ row, expandedRows }) {
      console.log('展开变化', row)
    }
  }
}
</script>
```

## Fixed Configuration

```javascript
fixed: {
  sort: true,    // 固定序号列
  select: true   // 固定选择列
}
```

## Important Notes

1. **数据刷新**: 修改、删除数据后，调用 `this.$refs.tableRef.init()` 刷新表格

2. **列配置保存**: 开启 `filterColumn` 和 `symbolKey` 后，列配置会自动保存到后台

3. **唯一标识**: `symbolKey` 建议使用 `${产品名}_${模块名}_table` 格式，保证唯一性

4. **虚拟滚动**: 开启 `vData` 后，需配合 `rowHeight` 和 `vScrollEnd` 事件使用

5. **跨页选择**: 开启 `select` 后，选中数据会跨页保持，调用 `init()` 时自动恢复

6. **排序保存**: 开启 `isSortSave` 后，排序状态会保存到后台

7. **权限控制**: 操作列按钮可通过 `permission` 函数控制禁用状态

8. **国际化**: 列名 `name` 支持通过 i18n 配置，或传入 `enName` 英文字段

9. **type 模式**: 默认为 `'page'`，会根据 URL 变化改变数据；`'dialog'` 用于弹框内表格

10. **selection 开启 checkbox 多选**，`radio` 在 selection 为 true 时支持单选
