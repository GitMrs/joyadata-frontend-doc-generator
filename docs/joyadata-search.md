# joyadata-search

**Description**: 用于页面搜索和操作（新增、导出、导入），基于 el-form 封装的 joyadata-search 组件！

## Basic Usage (Page)

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

| Prop Name | Type | Description |
|-----------|------|-------------|
| type | String | 模式: dialog / page |
| searchBy | String | 搜索字段 |
| parmas | Array | 搜索条件配置 |
| placeholder | String | 搜索提示语 |
| operation | Array | 操作按钮配置 |
| operatioDown | Object | 下拉操作: {num: 0} |
| disabled | Boolean | 是否禁用 |
| paramkeys | String | 额外参数 |
| maxlength | Number | 最长字符数 |
| searchText | String | 搜索按钮文字 |
| searchHeight | Boolean | 开启高级搜索 |
| searchHdata | Array | 高级搜索数据 |
| searchHText | String | 高级搜索按钮文字 |
| hLw | String | 高级搜索文字宽度 |
| cSearch | Boolean | 每次点击都搜索 |
| tableRef | String | 关联 table 的 ref，默认 table_dom |
| operationDrop | Object | 下拉菜单配置 |
| hSearchClassName | String | 高级搜索 class，默认 height_search_wrap |
| hSearchVuex | Boolean | 高级搜索使用 vuex |
| defaultStatus | Object | dialog 模式默认参数 |
| hSearchBtn | Boolean | 是否显示高级搜索按钮，默认 true |

## parmas (Search Fields)

| Type | Description |
|------|-------------|
| input | 输入框 |
| frame | 单独时间区间 |
| daterange | 连续时间区间 |
| select | 下拉选择 |
| selectTree | 树形下拉 |
| radio | 单选 |
| cascader | 级联选择 |

## parmas Item Structure

```javascript
parmas: [
  {
    type: "input",        // 输入框类型
    props: "name",        // 字段名
    placeholder: "请输入", // 提示文字
    label: "名称"         // 标签名
  }
]
```

## operation (Buttons)

```javascript
operation: [
  {
    name: "新增",           // 按钮名称
    type: "primary",        // 按钮类型
    icon: "el-icon-plus",   // 图标
    plain: true,            // 朴素按钮
    permission: () => false, // 权限控制
    handle: () => {         // 点击事件
      this.add();
    }
  }
]
```

## defaultStatus (Dialog Mode)

```javascript
defaultStatus: {
  parmasForm: { status: '全部' },                    // 普通类型
  frameTime: { createTime: ['2023-10-14', '2023-10-30'] },  // 时间类型
  multipleData: { roleId: ['1', '2', '3'] },       // 多选类型
  cascaderForm: { roleId: ['1', '2', '3'] }        // 级联类型
}
```

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| searchFn | row | dialog 模式下，点击搜索时触发 |
| searchResetFn | - | dialog 模式下，点击重置时触发 |
| registerSearchFn | - | page 模式下，重置时触发 |

## Usage in Dialog

```html
<template>
  <joyadata-dialog ref="dialog" title="选择" width-type="table" :footer="false">
    <joyadata-search
      ref="searchValue"
      type="dialog"
      :parmas="parmas"
      @searchFn="searchFn"
      @searchResetFn="searchResetFn"
    />
    <joyadata-table-dom
      ref="table_table_dom"
      type="dialog"
      :url="fileUrl"
      :column="column"
      height="400px"
    />
  </joyadata-dialog>
</template>

<script>
export default {
  data() {
    return {
      parmas: [
        { label: "搜索", type: "input", prop: "keywords" },
        { label: "更新时间", type: "frame", prop: "lastModificationTime" }
      ],
      fileUrl: "/api/list",
      column: [
        { name: "名称", prop: "name" }
      ]
    };
  },
  methods: {
    open() {
      this.$refs.dialog.open();
      this.searchResetFn();
    },
    searchFn(row) {
      this.$refs.table_table_dom.search = { ...row };
      this.$refs.table_table_dom.searchFn();
    },
    searchResetFn() {
      this.$refs.searchValue.restParmas();
      this.$refs.table_table_dom.search = {};
      this.$refs.table_table_dom.searchFn();
    }
  }
};
</script>
```

## Advanced Search

```javascript
parmas: [
  {
    type: "input",
    props: "name",
    label: "名称"
  }
],
searchHeight: true,  // 开启高级搜索
searchHdata: [       // 高级搜索配置
  {
    type: "input",
    props: "code",
    label: "编码"
  },
  {
    type: "daterange",
    props: "time",
    label: "时间"
  }
]
```

## Important Notes

1. **parmas 为必填**: 配置搜索字段
2. **operation**: 配置操作按钮（新增、导出、导入等）
3. **type 选项**:
   - `page`: 页面搜索模式
   - `dialog`: 弹框搜索模式
4. **tableRef 联动**: 与 table 组件配合使用，自动传递搜索参数
5. **高级搜索**: 设置 `searchHeight: true` + `searchHdata` 配置
