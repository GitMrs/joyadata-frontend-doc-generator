# joyadata-tree

**Description**: 用于 tree 目录展示，基于 el-tree 封装的 joyadata-tree 组件！

## Basic Usage

```html
<joyadata-tree
  ref="treeRef"
  :nav-val="navVal"
  :expand="false"
  node-key="id"
  @changeAside="changeAside"
/>

<script>
export default {
  data() {
    return {
      navVal: []
    };
  },
  mounted() {
    this.getTree();
  },
  methods: {
    getTree() {
      this.$request.get("/api/tree").then((res) => {
        this.navVal = res.result;
      });
    },
    changeAside(node) {
      this.$router.push({
        query: { id: node.id }
      });
    }
  }
};
</script>
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
| iconList | Array | 操作区域图标 |
| defaultTreeType | string | 当前 url 上的 treeType |
| showType | string | select/radio 模式 |
| typeData | Array | showType 存在时的数据 |
| draggable | Boolean | 是否支持拖拽 |
| disabled | Boolean | 是否禁用 |
| showCheckbox | Boolean | 是否显示 checkbox |
| accordion | Boolean | 是否开启手风琴模式 |
| isContextmenu | Boolean | 是否开启右键菜单 |
| contextData | Array | 右键菜单数据 |
| contextmenuPre | Function | 右击前置事件 |
| expandOnClickNode | Boolean | 是否开启联动点击 |
| currentKeyProps | String | 当前 url 上的 keyProps |
| maxLength | Number | 最大显示字符数 |
| lazy | Boolean | 是否开启懒加载 |
| loadNode | Function | 懒加载方法 |
| showIcon | Boolean | 是否显示 icon |
| defaultProps | Object | tree 默认配置: { children: 'children', label: 'label' } |
| titleTooltip | Object | 标题提示 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| typeChange | val | 类型切换时触发 |
| changeAside | node | noVuex 为 true 时，选中节点触发 |
| titleFn | - | 点击标题时触发 |

## navVal 数据结构

```javascript
navVal: [
  {
    label: "根节点",
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

## 右键菜单

```javascript
contextData: [
  { name: "编辑", key: "edit" },
  { name: "删除", key: "del" }
]
```

## 结合 Vuex 使用

```html
<joyadata-tree
  ref="treeRef"
  :nav-val="navVal"
  :expand="false"
  node-key="id"
/>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["currentTreeItem"])
  },
  watch: {
    currentTreeItem(val) {
      this.$router.push({
        query: {
          id: val.id,
          page: 0,
          categoryType: val.categoryType
        }
      });
    }
  },
  mounted() {
    this.getTree();
  },
  methods: {
    getTree() {
      this.$request.get("/api/tree").then((res) => {
        this.navVal = res.result;
        this.$nextTick(() => {
          const { id } = this.$route.query;
          this.$refs.treeRef.$refs.tree.setCurrentKey(id);
        });
      });
    }
  }
};
</script>
```

## 与路由联动

```javascript
watch: {
  "$route.query"(query) {
    if (!query.pager) {
      this.getTree();
    }
  }
},
methods: {
  getTree() {
    this.$request.get("/api/tree").then((res) => {
      this.navVal = res.result;
      this.$nextTick(() => {
        const { id } = this.$route.query;
        this.$refs.treeRef.$refs.tree.setCurrentKey(id);
      });
    });
  }
}
```

## Important Notes

1. **nodeKey 为必填**: 用于 tree 的唯一标识
2. **navVal 为必填**: 树结构数据
3. **与 Vuex 配合**: 可结合 Vuex 实现选中节点同步
4. **与路由配合**: 可通过 setCurrentKey 方法同步选中状态
5. **与 joyadata-aside 对比**: joyadata-tree 是简化版树组件，适合纯树展示场景
