# joyadata-table

**Description**: 用于 table 数据展示，基于 el-table 封装的 joyadata 组件！

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
| showTitle | Boolean | - | 是否展示标题 |
| type | String | 'page' | 默认为 page，跟随 url 变化改变数据 |
| fixed | Object | - | 冻结 sort,select |
| rowKey | String | - | 表格唯一 key |
| selection | Boolean | - | 是否开启 checkbox |
| select | Boolean | - | 是否支持选择完，分页，选择依旧存在 |
| selectDelayTime | Number | - | 选中分页，调用选中再次选中延迟时间 |
| selectedMax | Number | 99999 | 最大选择数 |
| selectedMaxFn | Function | - | 自定义最大选择数量的方法 |
| radio | Boolean | - | selection 为 true 时支持单选 |
| treeProps | Object | - | tree 性的结构 |
| mockData | Array | - | 模拟数据 |
| searchBy | sortBy | - | 搜索的关键字 |
| sortBy | sortBy | - | 排序的关键字 |
| paramkeys | Object | - | 其它参数 |
| sortIndex | Boolean | - | 是否出现序号 |
| height | String | - | table 的高度 |
| url | String | - | 获取数据的 url |
| column | Array | - | 表头信息 |
| pagination | Boolean | - | 是否开启分页 |
| tableRowClassName | Function | - | 动态添加行样式 |
| calcHeight | Number | 220 | 动态计算 pager，细调数据 |
| useColumn | String | 'useColumn' | 使用内部的 column |
| defaultExpandAll | Boolean | - | 当为 tree 行数据时，是否全部展开 |
| selectable | Function | - | 依据当前数据是否禁用 checkbox |
| showTable | Boolean | - | 是否每次都销毁 |
| initPager | Number | - | 每页展示多少条，0 为自动计算 |
| initPage | Number | 0 | 默认当前页 |
| defaultValue | String | '-' | 数据为空时的默认展示 |
| expandChange | Function | - | 异性 tree 时，点击展开方法 |
| spanMethod | Function | - | 通过当前数据，合并行或者列 |
| filterColumn | Boolean | - | 是否开启列过滤 |
| columnSession | Boolean | - | 是否开启本地列存储 |
| mergeParams | Boolean | - | 是否用浏览器参数，覆盖传入的参数 |
| isEmpty | Boolean | true | 使用默认的暂无数据 |
| allCheck | Boolean | - | 开启全选 |
| initData | Boolean | true | 默认自动赋值 |
| fixedPager | Number | 0 | 自动计算当前页面数量时，修复条数 |
| sortAuto | Boolean | false | 自动开启排序方法 |
| hSearchClassName | String | 'height_search_wrap' | 高级搜索的 class |
| hSearchVuex | Boolean | - | 高级搜索的 vuex 控制 |
| hSearchVal | Boolean | - | 高级搜索的值控制 |
| symbolKey | String | - | filterColumn 为 true 时，后台联动 column 关键字 |
| isheaderDragend | Boolean | - | table 表头的拖拽宽度保存 |
| tableId | String | - | 获取 tableId |
| isDragColumn | Boolean | - | 开启拖拽的逻辑 |
| levelProp | String | - | table 带层级拖拽时，记录 level 的字符 |
| pidProp | String | - | table 带层级拖拽时，计算父级的 key |
| popoverKey | Boolean | - | table 删除为 popover 时的唯一值 |
| rowHeight | Number | 41 | table 数据的高度 |
| mapKeyParmas | Object | - | 映射 parmas 参数的 key 的值 |

## Column Configuration

### Basic Column

```javascript
column: [
  { name: "名称", prop: "name", align: "left" },
  { name: "名称1", prop: "name1" }
]
```

### Column with Slot

```javascript
column: [
  {
    name: "自定义",
    prop: "custom",
    type: "slot",
    slot_name: "slot_name"
  }
]
```

```html
<template slot="slot_name" slot-scope="{ scope }">
  <el-tag type="success">{{ scope.name }}</el-tag>
</template>
```

### Column with Input

```javascript
column: [
  {
    name: "请输入",
    prop: "input",
    type: "slot",
    render: (h, { index, row }) => {
      return <el-input v-model={row.input} size="mini" />;
    }
  }
]
```

### Column with Operations

```javascript
column: [
  {
    name: "操作",
    width: "300px",
    group: [
      {
        name: "编辑",
        plain: true,
        type: () => { return "primary"; },
        handle: (row) => { /* 处理编辑 */ }
      },
      {
        name: "删除",
        plain: true,
        type: () => { return "danger"; },
        handle: (row, { $index }) => { /* 处理删除 */ }
      }
    ]
  }
]
```

## Fixed Configuration

```javascript
fixed: {
  sort: true,
  select: true
}
```

## Methods

### init()

表格数据初始化或刷新。

```javascript
this.$refs.tableRef.init()
```

### init() with Options

| Option | Type | Description |
|--------|------|-------------|
| noLoading | Boolean | 开启后不获取数据不用 loading |
| selectData | Array | 调用时，改变选中的数据 |

```javascript
this.$refs.tableRef.init()
this.$refs.tableRef.init({ selectData: [] })
this.$refs.tableRef.init({ noLoading: true })
```

## Important Notes

1. 修改/删除后必须调用 `this.$refs.tableRef.init()`
2. filterColumn: 是否开启列过滤
3. columnSession: 是否开启本地列存储
4. type 默认为 'page'，会根据 URL 变化改变数据
5. selection 开启 checkbox 多选，radio 在 selection 为 true 时支持单选
