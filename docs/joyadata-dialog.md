# joyadata-dialog

**Description**: 基于 `el-dialog` 封装的弹框组件，支持拖拽、全屏、数据变更检测、自动表单校验等功能。

## Basic Usage

```html
<joyadata-dialog
  ref="dialog"
  :title="title"
  width="600px"
  :footer="model !== 'look'"
  @affirm="affirm"
>
  <!-- 弹框内容 -->
</joyadata-dialog>

<script>
export default {
  methods: {
    open(row = {}) {
      this.$refs.dialog.open();
    },
    affirm(form) {
      console.log(form);
      this.$refs.dialog.handleClose();
    }
  }
};
</script>
```

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| **基础配置** | | | |
| title | String | `''` | 弹框标题 |
| top | String | `'15vh'` | 弹框距离顶部的距离 |
| widthType | String | `'form'` | 预设宽度类型：`table`(1200px)、`form`(800px)、`inDialog`(600px)、`sure`(400px) |
| width | String | `'30%'` | 自定义宽度（需配合 `widthType='other'` 使用） |
| dialogDrag | Boolean | `false` | 是否支持拖拽 |
| fullscreen | Boolean | `false` | 是否全屏显示 |
| appendToBody | Boolean | `false` | 是否嵌套弹框，插入到 body |
| className | Object | `{}` | 自定义类名对象 |
| **按钮配置** | | | |
| footer | Boolean | `true` | 是否显示底部操作栏 |
| sureText | String | `''` | 确定按钮文案（默认使用 i18n） |
| cancelText | String | `''` | 取消按钮文案（默认使用 i18n） |
| **头部/底部** | | | |
| header | Boolean | `true` | 使用默认头部，设为 false 可通过 `title` 插槽自定义 |
| slotFooter | Boolean | `false` | 使用插槽自定义底部，设为 true 可通过 `footer` 插槽自定义 |
| **数据变更检测** | | | |
| closeConfirm | Boolean | `false` | 关闭前检测数据变更，有变更时弹出确认框 |
| closeConfirmText | String | `''` | 关闭确认提示文案 |
| autoConfirm | Boolean | `true` | 自动检测数据变化（通过 JSON 对比），设为 false 需配合 `validateForm` 使用 |
| validateForm | Function | `() => false` | 自定义校验函数（`autoConfirm=false` 时生效），返回 true 弹出确认框 |
| autoCloseDialog | Boolean | `true` | 是否自动关闭弹框，设为 false 需手动调用关闭 |
| **Ref 配置** | | | |
| formRef | String | `'formDom'` | 内部使用的表单 ref 名称 |
| tableRef | String | `'dialog_table_ref'` | 内部使用的表格 ref 名称 |
| searchRef | String | `'dialog_search_ref'` | 内部使用的搜索 ref 名称 |
| **其他** | | | |
| dialogOption | Object | `-` | 其他 element-dialog 属性 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| affirm | `(form)` | 点击确定按钮时触发，参数为表单数据 |
| handle | `({flag})` | 关闭弹框时触发，`flag=true` 表示主动关闭，`flag=false` 表示点击关闭按钮 |
| noFormRef | `({flag})` | 无 formRef 时的关闭回调 |
| open | `-` | 弹框打开事件（el-dialog 原生） |

## Slots

| Slot Name | Description |
|-----------|-------------|
| default | 弹框主体内容 |
| title | 自定义标题（需 `header=false`） |
| footer | 自定义底部操作栏（需 `slotFooter=true`） |

## 联合 joyadata-form 使用

> **重要**: joyadata-form 的 ref 建议使用 `formDom`，这样 joyadata-dialog 内部会自动做校验！

```html
<template>
  <joyadata-dialog
    ref="dialog"
    :title="title"
    width="600px"
    :footer="model !== 'look'"
    @affirm="affirm"
  >
    <joyadata-form
      ref="formDom"
      :main="main"
      label-width="130px"
      :rules="rules"
      :disable="model === 'look'"
    />
  </joyadata-dialog>
</template>

<script>
export default {
  props: {
    title: { type: String, default: "" },
    model: { type: String, default: "" },
  },
  data() {
    return {
      main: [
        {
          type: "input",
          props: "name",
          label: "名称",
          placeholder: "请输入",
        },
      ],
      rules: {
        name: [{ required: true, message: "不能为空", trigger: "blur" }],
      },
    };
  },
  methods: {
    open(row = {}) {
      this.$refs.dialog.open();
      if (row.id) {
        this.$nextTick(() => {
          this.$refs.formDom.form = { ...row };
        });
      }
    },
    affirm(form) {
      this.$refs.dialog.loading = true;
      // 处理表单提交
      this.$request.post("/api/xxx", form).then(() => {
        this.$message.success("操作成功");
        this.$parent.getData();
        this.$refs.dialog.handleClose();
      });
    },
  },
};
</script>
```

## 联合 Table 使用

使用 `joyadata-table-dom`（不是 joyadata-table）

```html
<template>
  <joyadata-dialog
    ref="dialog"
    :title="title"
    width-type="table"
    :footer="false"
    @handle="handleClose"
  >
    <joyadata-search
      ref="searchValue"
      type="dialog"
      :parmas="parmas"
      @searchFn="searchFn"
    />
    <joyadata-table-dom
      ref="table_table_dom"
      type="dialog"
      :selection="false"
      :url="fileUrl"
      :column="column"
      height="400px"
    />
  </joyadata-dialog>
</template>

<script>
import JoyadataTableDom from "@/components/common/TableDom";

export default {
  components: { JoyadataTableDom },
  data() {
    return {
      column: [
        { name: "名称", prop: "name" },
        { name: "时间", prop: "time" },
      ],
      parmas: [
        { label: "搜索", type: "input", prop: "keywords" },
      ],
      fileUrl: "/api/list",
    };
  },
  methods: {
    open(row) {
      this.$refs.dialog.open();
    },
    searchFn(row) {
      this.$refs.table_table_dom.search = row;
      this.$refs.table_table_dom.searchFn();
    },
    handleClose() {
      // 关闭前的处理
    },
  },
};
</script>
```

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Description |
|--------|------------|-------------|
| open | `(obj)` | 打开弹框，`obj` 可选：`{flag: boolean, noReset: boolean}` |
| handleClose | `(flag)` | 关闭弹框，`flag=true` 表示主动关闭 |
| sureFn | `-` | 触发确定按钮操作 |
| collectOldData | `(data)` | 收集旧数据用于对比（`closeConfirm=true` 时使用） |
| resetFields | `(ref)` | 重置指定 ref 的表单字段 |
| loading | `Boolean` | 控制确定按钮 loading 状态 |

### open 方法参数说明

```javascript
this.$refs.dialog.open({
  flag: false,    // 是否重置表格/搜索，默认 false 不重置
  noReset: true   // 是否不重置表单，默认 true 不重置
})
```

### closeConfirm 工作流程

1. 设置 `closeConfirm=true` 开启数据变更检测
2. 打开弹框时自动收集初始数据
3. 关闭时对比当前数据与初始数据
4. 有变化时弹出确认框，用户确认后才关闭

### autoConfirm 与 validateForm

- `autoConfirm=true`（默认）：自动对比 JSON 字符串判断数据变化
- `autoConfirm=false`：调用 `validateForm` 函数自定义判断逻辑
  - 返回 `true`：弹出确认框
  - 返回 `false`：直接关闭弹框

## widthType 与宽度对应表

| widthType 值 | 实际宽度 |
|-------------|---------|
| `table` | 1200px |
| `form` | 800px |
| `inDialog` | 600px |
| `sure` | 400px |
| `other` | 使用 `width` 属性的值 |

## Important Notes

1. **formRef 建议**: 使用 `formDom` 作为 ref，内部会自动校验
2. **widthType 选项**:
   - `table`: 1200px
   - `form`: 800px
   - `inDialog`: 600px
   - `sure`: 400px
3. **autoCloseDialog**: 默认为 true，false 时需手动关闭
4. **联合 form 使用**: 可以自动获取表单数据进行校验
5. **closeConfirm**: 开启后会在数据变更时提示确认
