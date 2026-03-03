# joyadata-dialog

**Description**: 用于弹框展示，基于 el-dialog 封装的 joyadata-dialog 组件！

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
| top | String | - | 弹框距离顶部的高度 |
| title | String | - | 弹框名称 |
| dialogDrag | Boolean | - | 是否支持拖拽 |
| widthType | String | - | 弹框类型: table(1000px)/form(800px)/inDialog(600px)/sure(400px) |
| width | String | - | 自定义宽度（widthType 为 other 时使用） |
| sureText | String | - | 确定按钮文案 |
| cancelText | String | - | 取消按钮文案 |
| closeConfirm | Boolean | - | 是否开启关闭前的 confirm |
| closeConfirmText | String | - | closeConfirm 为 true 时的 confirm 文案 |
| autoConfirm | Boolean | true | 自动比较输入前后的值并提示确认 |
| validateForm | Function | - | autoConfirm 为 false 时的校验方法 |
| footer | Boolean | - | 是否显示底部操作 |
| header | Boolean | true | 是否显示头部（可自定义 slot） |
| appendToBody | Boolean | - | 嵌套弹框使用 |
| slotFooter | Boolean | false | 自定义 footer 插槽 |
| fullscreen | Boolean | - | 是否全屏显示 |
| className | Object | - | 自定义 class |
| dialogOption | Object | - | 其他 element-dialog 属性 |
| formRef | String | 'formDom' | 内部 form 的 ref |
| tableRef | String | 'dialog_table_ref' | 内部 table 的 ref |
| searchRef | String | 'formDom' | 内部 search 的 ref |
| autoCloseDialog | Boolean | true | 自动关闭弹框 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| handle | - | 关闭弹框前的方法 |
| affirm | form | 点击确定的方法 |

##联合 joyadata-form 使用

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

**重要**: joyadata-form 的 ref 建议使用 `formDom`，这样 joyadata-dialog 内部会自动做校验！

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

### open()

打开弹框

```javascript
this.$refs.dialog.open()
```

### handleClose()

关闭弹框

```javascript
this.$refs.dialog.handleClose()
```

### loading

控制确定按钮 loading 状态

```javascript
this.$refs.dialog.loading = true  // 显示 loading
this.$refs.dialog.loading = false  // 关闭 loading
```

## Important Notes

1. **formRef 建议**: 使用 `formDom` 作为 ref，内部会自动校验
2. **widthType 选项**:
   - `table`: 1000px
   - `form`: 800px
   - `inDialog`: 600px
   - `sure`: 400px
3. **autoCloseDialog**: 默认为 true，false 时需手动关闭
4. **联合 form 使用**: 可以自动获取表单数据进行校验
