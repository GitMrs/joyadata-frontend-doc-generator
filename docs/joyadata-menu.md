# joyadata-menu

**Description**: 用于左侧菜单展示，基于 el-menu 封装的 joyadata-menu 组件！

## Basic Usage

```html
<joyadata-menu :menu-data="menuData" />

<script>
export default {
  data() {
    return {
      menuData: [],
    };
  },
  mounted() {
    this.getMenu();
  },
  methods: {
    getMenu() {
      this.$request
        ._get("/api/getMenu", {
          menuCode: this.$route.path.split("/")[1],
          productCode: "tenant",
        })
        .then((res) => {
          this.menuData =
            res.result &&
            res.result.map((item) => {
              return {
                name: item.name,
                code: item.code,
                children: item.children,
              };
            });
        });
    },
  },
};
</script>
```

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| menuData | Array | - | 渲染用的菜单数据 |
| currentIndex | Number | - | 当前选中的，和路由配对的规则 |

## menuData 数据结构

```javascript
menuData: [
  {
    name: "菜单名称",
    code: "menu_code",
    children: [
      {
        name: "子菜单名称",
        code: "sub_menu_code",
        children: []
      }
    ]
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| name | string | 菜单显示名称 |
| code | string | 菜单标识（用于路由匹配） |
| children | Array | 子菜单数组 |

## Important Notes

1. **menuData 为必填项**: 用于渲染菜单数据
2. **currentIndex**: 用于手动控制当前选中的菜单项
3. **路由匹配**: 通过 code 与路由进行匹配，高亮当前菜单
4. **层级支持**: 支持多级子菜单（children 嵌套）
