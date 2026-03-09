# joyadata-menu

**Description**: 基于 `el-menu` 封装的侧边栏菜单组件，支持多级菜单、自动路由匹配、折叠展开等功能，通常用于系统侧边导航。

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
                icon: item.icon,
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
| menuData | Array | `[]` | 【必填】菜单数据数组 |
| currentIndex | Number | `0` | 与路由匹配的层级索引，用于确定当前激活菜单 |
| useVuex | Boolean | `false` | 是否使用 Vuex 管理菜单状态 |

## 特性说明

1. **自动路由匹配** - 根据当前路由自动高亮对应菜单项
2. **支持多级菜单** - 通过 `children` 属性实现无限层级嵌套
3. **折叠/展开** - 与 Vuex 的 `isFold` 状态联动，支持菜单宽度自适应
4. **国际化适配** - 自动根据语言环境调整菜单宽度（中文 220px，英文 300px）

## menuData 数据结构

```javascript
[
  {
    name: '菜单名称',        // 菜单显示文本
    code: 'menu-code',      // 菜单唯一标识（用于路由匹配）
    icon: 'icon-name',      // 图标类名（可选）
    children: [             // 子菜单（可选）
      {
        name: '子菜单',
        code: 'sub-menu-code',
        icon: 'sub-icon',   // 子菜单图标（可选）
        children: []        // 支持多级嵌套
      }
    ]
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| name | string | 菜单显示名称 |
| code | string | 菜单标识（用于路由匹配，必填） |
| icon | string | 图标类名（可选） |
| children | Array | 子菜单数组（可选，支持多级嵌套） |

## 使用示例

### 基础用法

```vue
<template>
  <div class="layout">
    <joyadata-menu :menu-data="menuData" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      menuData: [
        {
          name: '首页',
          code: 'home',
          icon: 'el-icon-s-home'
        },
        {
          name: '系统管理',
          code: 'system',
          icon: 'el-icon-setting',
          children: [
            {
              name: '用户管理',
              code: 'user'
            },
            {
              name: '角色管理',
              code: 'role'
            }
          ]
        }
      ]
    }
  }
}
</script>
```

### 动态获取菜单数据

```vue
<template>
  <joyadata-menu
    :menu-data="menuData"
    :current-index="1"
  />
</template>

<script>
export default {
  data() {
    return {
      menuData: []
    }
  },
  mounted() {
    this.getMenu()
  },
  methods: {
    getMenu() {
      this.$request
        ._get('/api/menu', {
          menuCode: this.$route.path.split('/')[1],
          productCode: 'tenant'
        })
        .then((res) => {
          this.menuData = (res.result || []).map(item => ({
            name: item.name,
            code: item.code,
            icon: item.icon,
            children: item.children || []
          }))
        })
    }
  }
}
</script>
```

### 使用 Vuex 管理

```vue
<template>
  <joyadata-menu
    :menu-data="menuData"
    :use-vuex="true"
  />
</template>

<script>
export default {
  computed: {
    menuData() {
      return this.$store.state.user.menuList
    }
  }
}
</script>
```

### 菜单数据完整示例

```javascript
const menuData = [
  {
    name: '工作台',
    code: 'workspace',
    icon: 'el-icon-s-platform',
    path: '/workspace'
  },
  {
    name: '数据管理',
    code: 'data',
    icon: 'el-icon-s-data',
    children: [
      {
        name: '数据源',
        code: 'datasource',
        path: '/data/source'
      },
      {
        name: '数据质量',
        code: 'quality',
        children: [
          {
            name: '质量规则',
            code: 'rule'
          },
          {
            name: '质量报告',
            code: 'report'
          }
        ]
      }
    ]
  },
  {
    name: '系统设置',
    code: 'settings',
    icon: 'el-icon-s-tools',
    children: [
      {
        name: '用户管理',
        code: 'user'
      },
      {
        name: '角色权限',
        code: 'role'
      }
    ]
  }
]
```

## currentIndex 参数说明

`currentIndex` 用于指定与路由匹配的菜单层级：

```javascript
// currentIndex: 0 (默认)
// 匹配规则：优先使用 matched[1].path，否则使用当前 route.path
// 适用于：一级菜单直接对应页面的场景

// currentIndex: 1
// 匹配规则：使用 matched[1].path
// 适用于：二级菜单对应页面的场景

// currentIndex: 2
// 匹配规则：使用 matched[2].path
// 适用于：三级菜单对应页面的场景
```

## 路由配置建议

```javascript
// router.js
const routes = [
  {
    path: '/system',
    component: Layout,
    children: [
      {
        path: 'user',
        name: 'User',
        component: () => import('@/views/system/user'),
        meta: {
          code: 'user',  // 用于菜单匹配
          title: '用户管理'
        }
      },
      {
        path: 'role',
        name: 'Role',
        component: () => import('@/views/system/role'),
        meta: {
          code: 'role',
          title: '角色管理'
        }
      }
    ]
  }
]
```

## 与折叠状态联动

组件会自动监听 Vuex 中的 `isFold` 状态：

```javascript
// Vuex store
state: {
  isFold: 'fold'  // 'fold' | 'unfold'
}

// 折叠时菜单宽度变为 65px
// 展开时菜单宽度变为 220px（中文）/ 300px（英文）
```

## 样式定制

组件使用了以下 CSS 变量（可通过全局样式覆盖）：

```scss
// 菜单项高度
.el-menu-item, .el-submenu__title {
  height: 48px;
  line-height: 48px;
}

// 激活背景色（需定义 $menu-active 变量）
.el-menu-item.is-active {
  background-color: $menu-active;
}
```

## Important Notes

1. **menuData 为必填项**: 用于渲染菜单数据
2. **code 字段必填**: 菜单项的 `code` 字段用于路由匹配，必须唯一且与路由配置一致
3. **currentIndex**: 用于手动控制当前选中的菜单项，默认 0
4. **路由匹配规则**: 默认通过 `routeMeta.code` 或 `route.query.routeCode` 进行匹配
5. **折叠功能**: 折叠状态由 Vuex 统一管理，组件本身不控制折叠切换
6. **菜单高度**: 组件高度固定为 `calc(100% - 25px)`，超出会自动出现滚动条
7. **图标支持**: 支持 Element UI 图标类名或自定义图标
8. **层级支持**: 支持多级子菜单（children 嵌套）
