# joyadata-data-import

**Description**: 基于数据源引入场景封装的综合组件，集成左侧树形目录、搜索区域、表格列表、批量操作等功能，适用于数据源引入和管理的统一处理。

## Basic Usage

```vue
<template>
  <joyadata-data-import
    ref="joyadataDI"
    :table-do="tableDo"
    :table-column="tableColumn"
  />
</template>

<script>
export default {
  data() {
    return {
      // 操作列自定义
      tableDo: (vue) => {
        return [
          {
            name: '操作',
            prop: 'Actions',
            width: '100',
            group: [
              {
                name: '取消引入',
                plain: true,
                type: () => 'primary',
                permission: () => false,
                handle: (row) => {
                  vue.$refs['joyadataDI'].deleteData(row)
                }
              },
              {
                name: '应用详情',
                plain: true,
                type: () => 'primary',
                handle: (row) => {
                  vue.requrData(row)
                }
              }
            ]
          }
        ]
      },
      // 表格列全部自定义
      tableColumn: (vue) => {
        return [
          {
            name: '数据源名称',
            prop: 'dataName',
            align: 'left',
            handle: (row) => {
              vue.openLook(row)
            }
          },
          {
            name: '数据源类型',
            prop: 'dataType',
            align: 'left',
            tooltip: true
          },
          {
            name: '业务系统',
            prop: 'businessName',
            align: 'left',
            tooltip: true
          },
          {
            name: '驱动版本',
            prop: 'dataVersion',
            align: 'left',
            tooltip: true,
            visible: false
          },
          {
            name: '数据源版本',
            prop: 'dbVersion',
            align: 'left',
            tooltip: true,
            visible: false
          },
          {
            name: '备注',
            prop: 'remark',
            align: 'left',
            tooltip: true,
            visible: false
          },
          {
            name: '连接状态',
            prop: 'status',
            tooltip: true,
            align: 'left',
            formate: (row) => {
              return row.status === 1 ? '连接成功' : '连接失败'
            },
            class: (row) => {
              return row.status ? 'table_text_success' : 'table_text_danger'
            }
          },
          {
            name: '创建人',
            prop: 'createBy',
            tooltip: true,
            align: 'center'
          },
          {
            name: '创建时间',
            prop: 'createTime',
            tooltip: true,
            type: 'time'
          }
        ]
      }
    }
  },
  methods: {
    requrData(row) {
      console.log('应用详情', row)
    },
    openLook(row) {
      console.log('查看数据源', row)
    }
  }
}
</script>
```

## Props

| Prop Name | Type | Default | Description |
|-----------|------|---------|-------------|
| tableDo | Function | `() => []` | 自定义表格操作列的方法 |
| tableColumn | Function | `() => []` | 自定义表格全部 column 的方法 |
| operation | Function | `() => []` | 自定义搜索区域操作按钮的方法 |
| batchBtn | Function | `() => []` | 自定义批量操作按钮的方法 |
| noOperation | Boolean | `false` | 是否不显示操作区域 |

## Events

| Event Name | Parameters | Description |
|------------|------------|-------------|
| deleteData | `{ row }` | 删除单条数据后触发 |
| changeSelectData | `(selectData)` | 表格选择数据变化时触发 |
| addSuccess | `(data)` | 添加数据成功后触发 |

## Methods

通过 ref 可以调用以下公共方法：

| Method | Parameters | Description |
|--------|------------|-------------|
| importAll | `-` | 打开引入数据源弹框 |
| deleteData | `(row, confirmTips)` | 取消引入单条数据 |
| unImport | `-` | 批量取消引入 |

## 使用示例

### 基础用法

```vue
<template>
  <joyadata-data-import
    ref="joyadataDI"
    :table-do="tableDo"
    :table-column="tableColumn"
  />
</template>

<script>
export default {
  data() {
    return {
      // 操作列自定义
      tableDo: (vue) => {
        return [
          {
            name: '操作',
            prop: 'Actions',
            width: '100',
            group: [
              {
                name: '取消引入',
                plain: true,
                type: () => 'primary',
                permission: () => false,
                handle: (row) => {
                  vue.$refs['joyadataDI'].deleteData(row)
                }
              },
              {
                name: '应用详情',
                plain: true,
                type: () => 'primary',
                handle: (row) => {
                  vue.requrData(row)
                }
              }
            ]
          }
        ]
      },
      // 表格列全部自定义
      tableColumn: (vue) => {
        return [
          {
            name: '数据源名称',
            prop: 'dataName',
            align: 'left',
            handle: (row) => {
              vue.openLook(row)
            }
          },
          {
            name: '数据源类型',
            prop: 'dataType',
            align: 'left',
            tooltip: true
          },
          {
            name: '业务系统',
            prop: 'businessName',
            align: 'left',
            tooltip: true
          },
          {
            name: '连接状态',
            prop: 'status',
            tooltip: true,
            align: 'left',
            formate: (row) => {
              return row.status === 1 ? '连接成功' : '连接失败'
            },
            class: (row) => {
              return row.status ? 'table_text_success' : 'table_text_danger'
            }
          },
          {
            name: '创建时间',
            prop: 'createTime',
            tooltip: true,
            type: 'time'
          }
        ]
      }
    }
  },
  methods: {
    requrData(row) {
      console.log('应用详情', row)
    },
    openLook(row) {
      console.log('查看数据源', row)
    }
  }
}
</script>
```

### 自定义操作按钮和批量按钮

```vue
<template>
  <joyadata-data-import
    ref="joyadataDI"
    :table-do="tableDo"
    :table-column="tableColumn"
    :operation="operation"
    :batch-btn="batchBtn"
  />
</template>

<script>
export default {
  data() {
    return {
      tableDo: (vue) => [],
      tableColumn: (vue) => [],
      // 自定义搜索区域操作按钮
      operation: (vue) => {
        return [
          {
            name: '刷新',
            type: 'success',
            icon: 'el-icon-refresh',
            plain: true,
            handle: () => {
              vue.$refs.table_dom.init()
            }
          }
        ]
      },
      // 自定义批量操作按钮
      batchBtn: (vue) => {
        return [
          {
            name: '批量导出',
            type: 'warning',
            plain: true,
            permission: () => {
              return vue.$refs.table_dom?.selectData?.length === 0
            },
            handle: () => {
              console.log('批量导出', vue.$refs.table_dom.selectData)
            }
          }
        ]
      }
    }
  }
}
</script>
```

### 隐藏操作区域

```vue
<template>
  <joyadata-data-import
    ref="joyadataDI"
    :table-do="tableDo"
    :table-column="tableColumn"
    :no-operation="true"
  />
</template>

<script>
export default {
  data() {
    return {
      tableDo: (vue) => [],
      tableColumn: (vue) => []
    }
  }
}
</script>
```

### 监听事件

```vue
<template>
  <joyadata-data-import
    ref="joyadataDI"
    :table-do="tableDo"
    :table-column="tableColumn"
    @deleteData="handleDeleteData"
    @changeSelectData="handleChangeSelect"
    @addSuccess="handleAddSuccess"
  />
</template>

<script>
export default {
  data() {
    return {
      tableDo: (vue) => [],
      tableColumn: (vue) => []
    }
  },
  methods: {
    handleDeleteData({ row }) {
      console.log('删除数据', row)
    },
    handleChangeSelect(selectData) {
      console.log('选择数据变化', selectData)
    },
    handleAddSuccess(data) {
      console.log('添加成功', data)
    }
  }
}
</script>
```

## 默认表格列配置

组件内置默认的表格列配置，当 `tableColumn` 返回空数组时使用：

```javascript
[
  {
    name: '数据源名称',
    prop: 'dataName',
    align: 'left',
    handle: (row) => {
      vue.openLook(row)
    }
  },
  {
    name: '数据源类型',
    prop: 'dataType'
  },
  {
    name: '数据源 IP',
    prop: 'ip'
  },
  {
    name: '业务系统',
    prop: 'businessSystemName'
  },
  {
    name: '驱动版本',
    prop: 'dataVersion',
    visible: false
  },
  {
    name: '数据源版本',
    prop: 'dbVersion',
    visible: false
  },
  {
    name: '备注',
    prop: 'dataDesc',
    visible: false
  },
  {
    name: '连接状态',
    prop: 'status',
    align: 'center',
    formate: (row) => {
      return row.status ? '连接成功' : '连接失败'
    },
    class: (row) => {
      return row.status ? 'table_text_success_point' : 'table_text_danger_point'
    }
  },
  {
    name: '创建人',
    prop: 'createBy'
  },
  {
    name: '创建时间',
    prop: 'createTime',
    type: 'time'
  }
]
```

## 默认操作列配置

组件内置默认的操作列配置，当 `tableDo` 返回空数组时使用：

```javascript
[
  {
    name: '操作',
    prop: 'Actions',
    width: '100',
    group: [
      {
        name: '取消引入',
        plain: true,
        type: () => 'primary',
        permission: () => false,
        handle: (row) => {
          vue.deleteData(row)
        }
      }
    ]
  }
]
```

## 访问内部组件

可通过以下方式访问内部子组件实例：

```javascript
// 访问内部表格实例
this.$refs.joyadataDI.$refs.table_dom

// 访问内部搜索实例
this.$refs.joyadataDI.$refs.Search

// 访问内部树实例
this.$refs.joyadataDI.$refs.treeAside
```

## Important Notes

1. **组件结构**: 组件内部集成 `joyadata-aside`（左侧树）、`joyadata-search`（搜索区）、`joyadata-table`（表格）三个子组件

2. **数据联动**: 左侧树形目录切换会自动刷新表格数据，URL 参数会同步更新

3. **自定义优先级**: `tableColumn` 和 `tableDo` 返回空数组时使用内置默认配置

4. **批量操作**: 批量按钮通过 `batchBtn` 配置，组件内置"批量取消引入"按钮

5. **权限控制**: 通过 `permission` 函数控制按钮的禁用状态

6. **表格 Ref**: 可通过 `this.$refs.joyadataDI.$refs.table_dom` 访问内部表格实例

7. **搜索 Ref**: 可通过 `this.$refs.joyadataDI.$refs.Search` 访问内部搜索实例

8. **树 Ref**: 可通过 `this.$refs.joyadataDI.$refs.treeAside` 访问内部树实例
