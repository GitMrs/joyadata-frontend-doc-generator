# joyadata-aside

**Description**: 用于目录树展示，基于 el-tree 封装的 joyadata-aside 组件！

## Basic Usage

```html
<template>
  <div class="tree">
    <joyadata-aside
      :show-title="true"
      titletree="目录树"
      :title-fn="true"
      :no-vuex="true"
      :show-search="true"
      node-key="id"
      :expand="false"
      :nav-val="navVal"
      show-type="radio"
      @changeAside="changeAside"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      navVal: [
        {
          label: "根节点",
          id: "1",
          children: [
            { label: "子节点", id: "1-1" }
          ]
        }
      ]
    };
  },
  methods: {
    changeAside(node) {
      console.log(node);
      this.$router.push({
        path: this.$route.path,
        query: { id: node.id }
      });
    }
  }
};
</script>

<style scoped>
.tree {
  width: 220px;
}
</style>
```

## Props

| Prop Name | Type | Description |
|-----------|------|-------------|
| showTitle | Boolean | 是否展示标题 |
| titletree | String | 标题名称 |
| titleFn | Boolean | 开启标题自定义函数 |
| noVuex | Boolean | 不使用 vuex 共享数据 |
| showSearch | Boolean | 展示搜索框 |
| placeholder | String | 搜索框提示语 |
| nodeKey | String | tree 的唯一标识 |
| expand | Boolean | 是否默认展开 |
| navVal | Array | 树数据 |
| iconList | Array | 操作区域的图标 |
| defaultTreeType | string | 当前 url 上的 treeType |
| showType | string | select/radio 模式 |
| typeData | Array | showType 存在时的数据 |
| draggable | Boolean | 是否支持拖拽 |
| dragNoinner | Boolean | 拖拽时不允许拖入子节点 |
| disabled | Boolean | 是否禁用 |
| showCheckbox | Boolean | 是否显示 checkbox |
| accordion | Boolean | 是否开启手风琴模式 |
| isContextmenu | Boolean | 是否开启右键菜单 |
| contextData | Array | 右键菜单数据 |
| expandOnClickNode | Boolean | 是否开启联动点击 |
| currentKeyProps | String | 当前 url 上的 keyProps |
| maxLength | Number | 最大显示字符数 |
| lazy | Boolean | 是否开启懒加载 |
| loadNode | Function | 懒加载方法 |
| showIcon | Boolean | 是否显示 icon |
| defaultProps | Object | tree 默认配置 |
| titleTooltip | Object | 标题提示 |
| isContentRender | Boolean | 是否开启自定义渲染 |
| renderContentFn | Function | 自定义渲染函数 |
| isFilterNode | Boolean | 是否自行控制搜索 |
| autoResize | Boolean | 自动调整高度 |
| toggleAside | Function | 收起/展开时触发的方法 |
| leftWidth | String/Number | aside 默认宽度 |
| leftMaxWidth | Number | 拖拽时最大宽度 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| typeChange | val | 切换类型时触发 |
| changeAside | node | 选中节点时触发 |

## navVal 数据结构

```javascript
navVal: [
  {
    label: "节点名称",
    id: "1",
    children: [
      {
        label: "子节点",
        id: "1-1",
        children: []
      }
    ]
  }
]
```

## 右键菜单 (contextData)

```javascript
contextData: [
  { name: "编辑", key: "edit" },
  { name: "删除", key: "del" }
]
```

## 完整示例

```html
<template>
  <div class="tree">
    <joyadata-aside
      :show-title="true"
      titletree="测试目录"
      :title-fn="true"
      :no-vuex="true"
      :show-search="true"
      node-key="id"
      :expand="false"
      show-type="radio"
      radio-type="button"
      :nav-val="navVal"
      :is-contextmenu="true"
      :context-data="contextData"
      @typeChange="typeChange"
      @changeAside="changeAside"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      navVal: [
        {
          label: "1",
          id: "1",
          children: [{ label: "1-1", id: "1-1" }]
        }
      ],
      contextData: [
        { name: "编辑", key: "edit" },
        { name: "删除", key: "del" }
      ]
    };
  },
  methods: {
    typeChange(val) {
      console.log(val);
    },
    changeAside(node) {
      this.$router.push({
        path: this.$route.path,
        query: { id: node.id }
      });
    }
  }
};
</script>
```

## Important Notes

1. **nodeKey 为必填**: 用于 tree 的唯一标识
2. **navVal 为必填**: 树结构数据
3. **showType 选项**: 
   - `select`: 下拉选择
   - `radio`: 单选按钮组
4. **懒加载**: 设置 `lazy: true` + `loadNode` 方法
5. **拖拽**: 设置 `draggable: true`，可配合 `dragNoinner` 控制拖拽范围
