# joyadata-form

**Description**: 基于 `el-form` 封装的表单组件，支持多种表单项类型、自动校验、禁用控制等功能，可通过配置化的 `main` 数组快速构建表单。

## Basic Usage

```html
<joyadata-form
  ref="formDom"
  :main="main"
  label-width="130px"
  :rules="rules"
  :disable="model === 'look'"
/>

<script>
export default {
  props: {
    model: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      main: [
        {
          type: "input",
          props: "name",
          label: "分类名称",
          placeholder: "分类名称",
          width: "100%",
        },
      ],
      rules: {
        name: [
          { required: true, message: "请输入分类名称", trigger: "blur" },
        ],
      },
    };
  },
};
</script>
```

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| main | Array | `[]` | 【必填】表单项配置数组 |
| rules | Object | `{}` | 表单校验规则 |
| labelWidth | String | `'120px'` | 表单标签宽度 |
| labelLeft | Boolean | `false` | 标签文字是否左对齐 |
| disable | Boolean | `false` | 全局禁用表单（权限最高） |
| model | String | `'input'` | 表单模式：`input`(输入模式)、`detail`(详情模式) |
| authLWidth | Boolean | `false` | 是否自动计算标签宽度（仅中文生效） |
| attrs | Object | `{}` | 传递给 el-form 的其他属性 |
| selfName | String | `''` | 自定义名称 |
| selfMethod | String | `''` | 自定义方法名 |

## Slots

| Slot Name | Parameters | Description |
|-----------|------------|-------------|
| top | `-` | 表单顶部插槽 |
| default | `-` | 默认插槽 |
| 动态插槽 | `{scope}` | 通过 `item.slotName` 指定的自定义插槽 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| changeForm | `(form)` | 表单数据变化时触发（防抖 500ms） |

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Return | Description |
|--------|------------|--------|-------------|
| resetFields | `-` | `-` | 重置表单字段 |
| validateField | `(prop)` | `-` | 校验指定字段 |
| clearValidate | `-` | `-` | 清除校验状态 |
| initForm | `(val)` | `-` | 初始化表单数据 |
| setFrameDate | `(props, data)` | `-` | 设置时间范围选择器的值 |
| setTimeRadio | `(result)` | `-` | 设置时间单选按钮的值 |

## main 配置项说明

### 核心参数

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | String | 是 | 表单项类型（见下方类型列表） |
| props | String | 是 | 表单字段名称，对应 `form` 对象的 key |
| label | String | 否 | 表单标签名称 |
| width | String | 否 | 表单项宽度，默认 `'100%'` |
| placeholder | String | 否 | 占位符文本 |
| disablePlaceholder | String | 否 | 禁用时的占位符 |
| disabled | Boolean | 否 | 是否禁用该项 |
| hidden | Boolean | 否 | 是否隐藏该项 |
| required | Boolean | 否 | 是否必填（影响标签样式） |
| float | String | 否 | 浮动方向：`'left'` / `'right'` |
| className | String | 否 | 自定义类名 |
| classNameFn | Function | 否 | 动态类名函数 |
| attrs | Object | 否 | 传递给表单控件的额外属性 |
| listener | Object | 否 | 事件监听器 |
| labelAttr | Object | 否 | 传递给 label 的额外属性 |
| handle | Function | 否 | 值变化时的回调函数 |

### 表单项类型 (type)

| 类型值 | 说明 | 特有参数 |
|-------|------|---------|
| `input` | 文本输入框 | `trim`、`max`、`append`、`icon`、`appendText`、`appendTooltip`、`unit`、`tagValue`、`noClearable`、`noSpace` |
| `password` | 密码输入框 | `noShowPassword` |
| `validPass` | 密码强度验证 | - |
| `inputNumber` | 数字输入框 | `min`、`max`、`unit` |
| `select` | 下拉选择框 | `data`、`multiple`、`groups`、`noClearable`、`noFilterable` |
| `selectTree` | 树形选择器 | `vuex`、`data`、`multiple`、`normalizer`、`key`、`labelSlot`、`emptyText` |
| `radio` | 单选框组 | `data`、`attrs` |
| `checkbox` | 复选框组 (label 为 value) | `data` |
| `checkboxValue` | 复选框组 (label 显示) | `data` |
| `switch` | 开关 | `activeValue`、`inactiveValue`、`activeColor`、`inactiveColor` |
| `cascader` | 级联选择器 | `data`、`filterable`、`collapseTags`、`multiple`、`noCheckStrictly`、`filterMethod`、`cascaderSlotName` |
| `dataPick` | 日期选择器 | `timeType`、`timeFormat`、`format`、`pickerOptions`、`separator`、`startPickerOptions`、`endPickerOptions` |
| `timePick` | 时间选择器 | `attrs` |
| `timeRadio` | 时间范围单选 | `originTime`、`timeRadioWidth` |
| `textarea` | 文本域 | `rows`、`max`、`noWordLimit`、`noClearable` |
| `upload` | 文件上传 | `multiple`、`desc`、`handleRemove`、`handleChange`、`handlePreview`、`handleExceed`、`downLoad`、`downFileDesc`、`fileIcon` |
| `uploadImg` | 图片上传 | `ref` |
| `uploadFile` | 文件上传组件 | `ref` |
| `cron` | Cron 表达式 | `tabPane` |
| `selectIConFont` | 图标选择器 | - |
| `addUser` | 用户选择器 | - |
| `text` | 纯文本展示 | - |
| `slot` | 自定义插槽 | `name`、`slotTips`、`tipsColor` |
| `divider` | 分割线 | `position`、`htmlDom` |
| `customCron` | 自定义 Cron | - |

## 各类型详细配置

### input - 文本输入框

```javascript
{
  type: 'input',
  props: 'fieldName',
  label: '字段名称',
  placeholder: '请输入',
  max: 256,              // 最大长度，默认 256
  trim: true,            // 是否自动 trim，默认 true
  noClearable: false,    // 是否隐藏清空按钮
  noSpace: false,        // 是否禁止空格输入
  unit: '元',            // 后置单位
  // 后置插槽配置
  append: true,
  icon: 'el-icon-warning',  // 后置图标
  appendText: '按钮文字',   // 后置文字
  appendTooltip: '提示信息', // 后置 tooltip
  appendClick: (val) => {}, // 后置点击事件
  // 标签输入框
  tagValue: true,
  closable: false,
  focus: (val) => {},
  remove: (tag, props) => {},
  handle: (val) => {}
}
```

### select - 下拉选择框

```javascript
{
  type: 'select',
  props: 'fieldName',
  label: '下拉选择',
  data: [
    { label: '选项 1', value: '1' },
    { label: '选项 2', value: '2' }
  ],
  multiple: false,        // 是否多选
  noClearable: false,      // 是否隐藏清空按钮
  noFilterable: false,     // 是否禁用搜索功能
  groups: [                // 分组选项
    { label: '分组 1', data: [{ label: '1', value: '1' }] }
  ]
}
```

### selectTree - 树形选择器

```javascript
{
  type: 'selectTree',
  props: 'fieldName',
  label: '树形选择',
  vuex: 'none',            // 'use' 使用 Vuex，'none' 使用本地 data
  data: [],                // 树形数据（vuex='none' 时）
  multiple: false,         // 是否多选
  key: 'id',               // 唯一标识字段
  normalizer: (node) => ({ // 数据格式化
    id: node.id,
    label: node.name,
    children: node.children
  }),
  emptyText: '暂无数据',
  labelSlot: 'customLabel', // 自定义选项插槽名
  handle: (node, item) => {},
  deselect: (node, item) => {},
  clearTreeSelectHande: (node, item) => {},
  input: (node, item) => {},
  open: (item) => {}
}
```

### cascader - 级联选择器

```javascript
{
  type: 'cascader',
  props: 'fieldName',
  label: '级联选择',
  data: [
    {
      label: '选项 1',
      value: '1',
      children: [{ label: '子选项 1', value: '1-1' }]
    }
  ],
  filterable: true,        // 是否可搜索
  collapseTags: false,     // 多选时是否折叠
  multiple: false,         // 是否多选
  noCheckStrictly: false,  // 是否严格的选择任意一级选项
  filterMethod: (node, keyword) => {}, // 自定义搜索方法
  cascaderSlotName: 'customCascader'   // 自定义选项插槽名
}
```

### dataPick - 日期选择器

```javascript
{
  type: 'dataPick',
  props: 'fieldName',
  label: '日期选择',
  timeType: 'date',        // year/month/date/dates/week/datetime/datetimerange/daterange
  timeFormat: 'yyyy-MM-dd', // 绑定值格式
  format: 'yyyy-MM-dd',     // 显示格式
  // 或使用范围模式
  timeType: 'frame',
  separator: '-',
  startPickerOptions: {},   // 开始日期配置
  endPickerOptions: {}      // 结束日期配置
}
```

### switch - 开关

```javascript
{
  type: 'switch',
  props: 'fieldName',
  label: '开关',
  activeValue: true,       // 选中值
  inactiveValue: false,    // 未选中值
  activeColor: '#13ce66',  // 选中颜色
  inactiveColor: '#ff4949' // 未选中颜色
}
```

### slot - 自定义插槽

```javascript
{
  type: 'slot',
  name: 'customSlot',      // 插槽名称
  props: 'fieldName',
  label: '自定义',
  slotTips: '提示信息',    // 插槽下方提示
  tipsColor: 'red'
}
```

### divider - 分割线

```javascript
{
  type: 'divider',
  position: 'left',        // left/center/right
  label: '分组标题',
  htmlDom: '<span>HTML 内容</span>'
}
```

### textarea - 文本域

```javascript
{
  type: 'textarea',
  props: 'fieldName',
  label: '备注',
  rows: 4,                 // 显示行数
  max: 500,                // 最大字符数
  noWordLimit: false       // 是否隐藏右下角字数统计
}
```

### upload - 文件上传

```javascript
{
  type: 'upload',
  props: 'files',
  label: '文件上传',
  multiple: true,          // 是否支持多选
  desc: '支持上传多个文件',
  handleRemove: (file, fileList) => {},
  handleChange: (file, fileList) => {},
  handlePreview: (file) => {},
  handleExceed: (files, fileList) => {},
  downLoad: true,          // 是否显示下载按钮
  downFileDesc: '下载',
  fileIcon: 'el-icon-document'
}
```

### timeRadio - 时间范围单选

```javascript
{
  type: 'timeRadio',
  props: 'timeRange',
  label: '时间范围',
  originTime: '2020-01-01',  // 起始时间，默认 1970-01-01
  timeRadioWidth: '220px',
  handle: (row) => {}
}
```

## 标签提示配置

当字段需要提示时，可配置：

```javascript
{
  type: 'input',
  props: 'fieldName',
  label: '字段名',
  labelTips: '这是提示内容',      // 提示内容（支持 HTML）
  tooltip: true,                 // 使用 Tooltip 显示
  tooltipEffect: 'dark',         // dark/light
  placement: 'top',              // top/top-start/top-end 等
  tooltipAttr: {},               // Tooltip 额外属性
  tipsFn: (item) => {}           // 点击提示图标回调
}
```

## 使用示例

### 基础表单

```vue
<template>
  <joyadata-form
    ref="formDom"
    :main="main"
    :rules="rules"
    label-width="120px"
    @changeForm="handleChange"
  />
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'input',
          props: 'name',
          label: '名称',
          placeholder: '请输入名称',
          rules: [{ required: true, message: '请输入名称' }]
        },
        {
          type: 'select',
          props: 'type',
          label: '类型',
          data: [
            { label: '类型 1', value: '1' },
            { label: '类型 2', value: '2' }
          ]
        },
        {
          type: 'textarea',
          props: 'remark',
          label: '备注',
          rows: 4
        }
      ],
      rules: {
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleChange(form) {
      console.log('表单数据变化:', form)
    }
  }
}
</script>
```

### 使用插槽自定义

```vue
<template>
  <joyadata-form ref="formDom" :main="main" label-width="120px">
    <!-- 自定义图片上传插槽 -->
    <template #imageUpload="{ scope }">
      <el-upload
        :action="uploadUrl"
        :on-success="handleSuccess"
      >
        <el-button size="small">上传图片</el-button>
      </el-upload>
    </template>
  </joyadata-form>
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'slot',
          name: 'imageUpload',
          props: 'imageUrl',
          label: '图片'
        }
      ]
    }
  }
}
</script>
```

### 时间范围选择

```vue
<template>
  <joyadata-form ref="formDom" :main="main" label-width="120px" />
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'timeRadio',
          props: 'timeRange',
          label: '时间范围',
          originTime: '2020-01-01',  // 至今的开始时间
          handle: (row) => {
            console.log('选择的时间:', row)
          }
        }
      ]
    }
  }
}
</script>
```

### 文件上传

```vue
<template>
  <joyadata-form ref="formDom" :main="main" label-width="120px" />
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'upload',
          props: 'files',
          label: '文件上传',
          multiple: true,
          desc: '支持上传多个文件',
          handleRemove: (file, fileList) => {
            console.log('移除文件:', file)
          },
          handleChange: (file, fileList) => {
            console.log('文件变化:', fileList)
          },
          handlePreview: (file) => {
            console.log('预览文件:', file)
          }
        }
      ]
    }
  }
}
</script>
```

### 树形选择器

```vue
<template>
  <joyadata-form ref="formDom" :main="main" label-width="120px" />
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'selectTree',
          props: 'categoryId',
          label: '分类选择',
          vuex: 'none',
          data: [
            {
              id: '1',
              name: '分类 1',
              children: [
                { id: '1-1', name: '子分类 1' }
              ]
            }
          ],
          normalizer: (node) => ({
            id: node.id,
            label: node.name,
            children: node.children
          })
        }
      ]
    }
  }
}
</script>
```

## 与 joyadata-dialog 配合使用

```vue
<template>
  <joyadata-dialog
    ref="dialog"
    title="表单弹窗"
    :footer="true"
    @affirm="handleConfirm"
  >
    <joyadata-form
      ref="formDom"
      :main="main"
      :rules="rules"
      label-width="120px"
    />
  </joyadata-dialog>
</template>

<script>
export default {
  data() {
    return {
      main: [
        {
          type: 'input',
          props: 'name',
          label: '名称',
          placeholder: '请输入名称'
        }
      ],
      rules: {
        name: [
          { required: true, message: '请输入名称', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    open() {
      this.$refs.dialog.open()
    },
    handleConfirm(form) {
      console.log('表单数据:', form)
      // 提交逻辑...
    }
  }
}
</script>
```

## Important Notes

1. **disable 优先级**: 外层 disable 权限大于内部 disabled
2. **main 为必填项**: 必须配置表单内容
3. **type 为必填项**: 必须指定表单类型
4. **props 为必填项**: 必须指定表单字段 key
5. **数据初始化**: 使用 `initForm()` 方法或直接赋值 `this.$refs.formDom.form = data` 来初始化表单
6. **时间范围**: 使用 `timeType='frame'` 时，表单值为数组 `[startDate, endDate]`
7. **selectTree 数据源**: 建议使用 `vuex='none'` 传入本地数据，避免 Vuex 状态混乱
