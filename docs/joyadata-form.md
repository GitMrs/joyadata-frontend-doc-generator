# joyadata-form

**Description**: 用于表单数据目录展示，基于 el-form 封装的 joyadata-form 组件！

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
| labelLeft | String | - | 文字居左 |
| disable | Boolean | - | 全体禁用，权限最高 |
| labelWidth | String | - | 文字宽度 |
| main | Array | - | 【必填】表单内容 |
| rules | Array | - | 表单验证规则 |

## main Core Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| type | string | 【必填】类型: input/select/cascader/radio/checkbox/selectTree/password/validPass/switch/timeRadio |
| props | string | 【必填】表单字段 key |
| width | number | 当前行的宽度 |
| label | string | 展示的文字 |
| data | Array | type 为 select/radio/checkbox/selectTree 时的数据 |
| clearable | Boolean | 是否开启清空 |
| suffix | string | 文字后缀 |
| className | string | 自定义 class |
| placeholder | string | 默认 placeholder |
| disablePlaceholder | string | 禁用时的 placeholder |
| disabled | Boolean | 是否禁用（外层 disable 权限更高） |
| handle | Function | 单独调用方法 |
| hidden | Boolean | 是否渲染该项 |
| unit | String | input/inputNumber 后置单位展示 |
| float | string | 居左/居右，默认居左 |
| attrs | Object | 其他 el-form-item 参数 |

## type: input

| Parameter | Type | Description |
|-----------|------|-------------|
| noTrim | Boolean | 是否开启 trim 过滤，默认 true |
| max | number | 最大输入字符数，默认 64 |
| append | Boolean | 是否开启后置功能 |
| icon | String | append 为 true 时，后面展示的 icon |
| appendText | String | append 为 true 时，追加的文字 |

## type: switch

| Parameter | Type | Description |
|-----------|------|-------------|
| activeValue | number/string | 选中时的值 |
| inactiveValue | number | 未选中时的值 |
| activeColor | number | 选中时的颜色 |
| inactiveColor | number | 未选中时的颜色 |

## type: select

| Parameter | Type | Description |
|-----------|------|-------------|
| groups | Array | 层级 select |
| data | Array | 选项数据 [{label, value}] |
| multiple | Boolean | 是否多选 |
| noChildrenText | string | 无 children 时的提示文字 |
| noOptionsText | string | 无 options 时的提示文字 |
| noResultsText | string | 无 results 时的提示文字 |
| normalizer | Function | 数据渲染配置 (id, label, children) |
| deselect | Function | 删除时调用的方法 |
| clearOnSelect | Function | 全部清空时调用的方法 |
| formatSelect | Function | 失去焦点时调用的方法 |

## type: selectTree

| Parameter | Type | Description |
|-----------|------|-------------|
| vuex | string | 【必填】是否开启 vuex，use/none（建议用 none） |
| key | string | 选中 key，默认 id |
| multiple | Boolean | 是否多选 |

## type: radio / checkbox

| Parameter | Type | Description |
|-----------|------|-------------|
| data | Array | 选项数据 [{label, value}] |

## type: inputNumber

| Parameter | Type | Description |
|-----------|------|-------------|
| min | number | 最小值 |
| max | number | 最大值 |

## type: cascader

| Parameter | Type | Description |
|-----------|------|-------------|
| filterable | boolean | 是否可检索 |
| collapseTags | boolean | 多选时是否折叠 Tag |
| data | Array | 级联数据 |

## type: datePicker

| Parameter | Type | Description |
|-----------|------|-------------|
| timeType | string | 显示类型: year/month/date/dates/week/datetime/datetimerange/daterange/monthrange |
| timeFormat | string | 绑定值的格式 |
| format | string | 显示格式 |

## type: timeRadio

| Parameter | Type | Description |
|-----------|------|-------------|
| originTime | string | 起始时间，默认 1970-01-01 |

## type: textarea

| Parameter | Type | Description |
|-----------|------|-------------|
| rows | number | 展示高度 |
| noWordLimit | Boolean | 是否展示右下角文字统计 |

## type: text

默认展示文本（只读）

## labelTips

当 main 对象中存在 labelTips 时：

| Parameter | Type | Description |
|-----------|------|-------------|
| labelTips | Boolean | 是否开启 tooltip |
| tooltipEffect | string | tips 样式 |
| placement | string | tips 位置 |

## Custom Slot (Image Upload)

```html
<joyadata-form
  ref="formDom"
  :disable="disable"
  :main="form"
  :rules="rules"
  label-width="120px"
>
  <el-form-item
    ref="iconDom"
    slot="iconSlot"
    slot-scope="{ scope }"
    :prop="scope.props"
    :label="scope.label + ':'"
  >
    <el-upload
      ref="files"
      action="#"
      :on-change="fileChange"
      :show-file-list="false"
      :auto-upload="false"
    >
      <img v-if="imageUrl" :src="imageUrl" class="avatar" />
      <i v-else class="el-icon-plus"></i>
    </el-upload>
  </el-form-item>
</joyadata-form>

<script>
export default {
  data() {
    return {
      main: [
        {
          slotName: "iconSlot",
          props: "iconData",
          label: "icon",
          width: "100%",
        },
      ],
    };
  },
};
</script>
```

## Important Notes

1. **disable 优先级**: 外层 disable 权限大于内部 disabled
2. **main 为必填项**: 必须配置表单内容
3. **type 为必填项**: 必须指定表单类型
4. **props 为必填项**: 必须指定表单字段 key
