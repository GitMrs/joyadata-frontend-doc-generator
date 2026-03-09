# joyadata-aside

**Description**: 用于目录树展示，基于 `el-tree` 封装的侧边栏树形组件，支持搜索、右键菜单、拖拽、懒加载、虚拟滚动等功能。

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

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| **基础配置** | | | |
| navVal | Array | `[]` | 树形数据源 |
| nodeKey | String | `'id'` | 树节点的唯一标识字段 |
| defaultProps | Object | `{children: 'children', label: 'label', isLeaf: 'isLeaf'}` | 树节点字段映射配置 |
| expand | Boolean | `true` | 是否默认展开所有节点 |
| defaultExpandedKeys | Array | `[]` | 默认展开的节点 key 数组 |
| indent | Number | `20` | 树节点缩进距离（px） |
| **标题配置** | | | |
| showTitle | Boolean | `true` | 是否显示标题栏 |
| hiddenTitle | Boolean | `true` | 是否隐藏标题（配合 showTitle 使用） |
| titletree | String | `''` | 标题文本 |
| titlePosition | String | `'up'` | 标题位置，可选 `'up'` 或 `'down'` |
| asideTreeIcon | String/Boolean | `'aside_tree_icon'` | 标题图标名称 |
| titleFn | Boolean | `false` | 是否开启标题点击自定义事件 |
| titleTooltip | Object | `{show: true}` | 标题提示配置 `{show: boolean, content: string}` |
| iconList | Array | `[]` | 标题右侧操作按钮列表 |
| **搜索配置** | | | |
| showSearch | Boolean | `true` | 是否显示搜索框 |
| searchPosition | String | `'down'` | 搜索框位置，可选 `'up'` 或 `'down'` |
| placeholder | String | `''` | 搜索框占位符 |
| maxlength | Number | `256` | 搜索框最大输入长度 |
| defaultSearch | Boolean | `true` | 是否使用默认搜索过滤 |
| isFilterNode | Boolean | `true` | 是否内部控制搜索 |
| **类型切换配置** | | | |
| showType | String | `'select'` | 类型切换器样式，可选 `'select'` 或 `'radio'` |
| radioType | String | `'button'` | radio 样式，可选 `'button'` 或默认样式 |
| typeData | Array | `[]` | 类型切换数据 |
| defaultTreeType | String | `'treeType'` | URL 中的类型参数名 |
| typeControl | String | `'URL'` | 类型控制方式 |
| **交互配置** | | | |
| expandOnClickNode | Boolean | `true` | 点击节点是否展开/收起 |
| accordion | Boolean | `false` | 是否开启手风琴模式 |
| draggable | Boolean | `false` | 是否开启拖拽 |
| dragNoinner | Boolean | `false` | 拖拽时禁止作为子节点插入 |
| showCheckbox | Boolean | `false` | 是否显示复选框 |
| disabled | Boolean | `false` | 是否禁用 |
| lazy | Boolean | `false` | 是否开启懒加载 |
| loadNode | Function | - | 懒加载函数 |
| **右键菜单配置** | | | |
| isContextmenu | Boolean | `false` | 是否开启右键菜单 |
| contextData | Array | `[]` | 右键菜单项数据 |
| contextmenuPre | Function | `() => true` | 右键菜单显示前预处理函数 |
| **图标与渲染** | | | |
| showIcon | Boolean | `false` | 是否显示节点图标 |
| defaultIcon | String | `'tree_mulushu'` | 默认节点图标 |
| isContentRender | Boolean | `false` | 是否开启自定义节点渲染 |
| renderContentFn | Function | `() => {}` | 自定义节点渲染函数 |
| maxLength | Number | `100` | 节点文本最大长度 |
| **虚拟滚动** | | | |
| virtual | Boolean | `false` | 是否启用虚拟滚动树 |
| virtualHeight | String | `'calc(100vh - 20px)'` | 虚拟滚动容器高度 |
| itemSize | Number | `40` | 虚拟滚动每项高度（px） |
| **布局与尺寸** | | | |
| autoResize | Boolean | `true` | 是否开启拖拽调整宽度 |
| leftWidth | Number | `300` | 组件默认宽度（px） |
| leftMaxWidth | Number | `window.body.width / 2` | 拖拽时最大宽度（px） |
| refName | String | `'asideRefs'` | 组件 ref 名称 |
| **Vuex 集成** | | | |
| noVuex | Boolean | `false` | 不使用 Vuex 共享数据 |
| url | String | `''` | 通过 Vuex 获取树数据的 URL |
| **其他配置** | | | |
| currentKeyProps | String | `'id'` | URL 中当前选中节点的参数名 |
| resetCurrentKey | Boolean | `true` | 是否重置当前选中 key |
| showMore | Boolean | `false` | 鼠标悬停显示更多操作 |
| moreData | Array | `[]` | 更多操作数据 |
| moreProps | String | `'disabled'` | 判断是否显示更多的字段名 |
| batch | Boolean | `false` | 是否启用批量选择模式 |
| batchName | String | `''` | 批量模式名称 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| changeAside | `(data, node)` | 节点点击事件，返回节点数据和节点对象 |
| typeChange | `(type)` | 类型切换事件，返回当前选中的类型值 |
| titleFn | `-` | 标题点击事件（需 `titleFn=true`） |
| toggleAside | `(isOpen)` | 侧边栏展开/收起事件，返回当前状态 |
| filterChange | `(value)` | 搜索内容变化事件（需 `defaultSearch=false`） |
| filterNode | `(value, data)` | 自定义搜索过滤事件（需 `isFilterNode=false`） |
| nodeExpand | `(data)` | 节点展开事件 |
| nodeDragOver | `(draggingNode, dropNode, event)` | 拖拽经过节点事件 |
| node-contextmenu | `(event, data, node, obj)` | 右键菜单事件 |

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

## Slots

| Slot Name | Parameters | Description |
|-----------|------------|-------------|
| default | `-` | 默认插槽，可自定义整个树组件内容（设置后搜索和树都不显示） |
| batch | `-` | 批量操作区域插槽（需 `batch=true`） |
| 动态插槽 | `{item}` | 标题操作按钮的自定义插槽，通过 `iconList[i].slotName` 指定 |

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Return | Description |
|--------|------------|--------|-------------|
| setCurrentKey | `(currentKey)` | `-` | 设置当前选中节点 |
| setCheckedKeys | `(keys)` | `-` | 设置复选框选中的节点 key 数组 |
| setCheckedNodes | `(nodes)` | `-` | 设置复选框选中的节点数组 |
| getCheckedKeys | `-` | `Array` | 获取复选框选中的节点 key 数组 |
| getCheckedNodes | `-` | `Array` | 获取复选框选中的节点数组 |
| changeCurrentKey | `(currentKey)` | `-` | 设置当前高亮节点 |
| unfoldCatalog | `-` | `Array` | 展开所有目录节点，返回展开的 key 数组 |
| foldCatalog | `-` | `-` | 折叠所有目录节点 |

```javascript
// 示例：通过 ref 调用方法
this.$refs.asideRefs.setCurrentKey('1-1');
this.$refs.asideRefs.unfoldCatalog();
```

## iconList 配置格式

标题右侧的操作按钮通过 `iconList` 配置：

```javascript
iconList: [
  {
    icon: 'el-icon-plus',      // 图标类名
    type: 'i',                  // 图标类型：'i' 或 'svg'
    text: '新增',               // 按钮文本（可选）
    tips: '新增节点',           // 提示文本
    handle: () => {             // 点击回调
      console.log('新增')
    },
    permission: () => {         // 权限控制函数，返回 true 禁用
      return false
    },
    hidden: () => {             // 隐藏控制函数，返回 true 隐藏
      return false
    },
    slotName: 'customAction'    // 使用插槽的名称
  }
]
```

## contextData 配置格式

右键菜单项通过 `contextData` 配置：

```javascript
contextData: [
  {
    name: '编辑',      // 菜单项名称
    key: 'edit',       // 菜单项唯一标识
    handle: (data) => { // 点击回调（可选，也可以通过事件监听）
      console.log('编辑', data)
    }
  },
  {
    name: '删除',
    key: 'del'
  }
]
```

## 完整示例

### 带类型切换和右键菜单的树

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

### 懒加载示例

```html
<template>
  <joyadata-aside
    :lazy="true"
    :load-node="loadNode"
    :nav-val="treeData"
    node-key="id"
  ></joyadata-aside>
</template>

<script>
export default {
  data() {
    return {
      treeData: []
    }
  },
  methods: {
    loadNode(node, resolve) {
      if (node.level === 0) {
        // 加载根节点
        setTimeout(() => {
          resolve([
            { label: '一级 1', id: '1' },
            { label: '一级 2', id: '2' }
          ])
        }, 500)
      } else {
        // 加载子节点
        setTimeout(() => {
          resolve([
            { label: `${node.label}-子 1`, id: `${node.id}-1`, isLeaf: true }
          ])
        }, 500)
      }
    }
  }
}
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
6. **虚拟滚动**: 大数据量时建议开启 `virtual: true` 并设置 `itemSize`
7. **通过 ref 调用方法**: 如 `setCurrentKey`、`getCheckedNodes` 等
