# Joyadata 请求封装与公共方法

## 触发条件

**当用户进行以下操作时触发此 skill：**
- 进行接口联调，使用 `this.$request._get`、`this.$request._post` 等方法
- 询问如何使用 joyadata 封装的请求方法
- 需要进行文件上传/下载操作
- 需要使用公共方法如 `deepClone`、`parseTime` 等
- 需要进行数据存储操作（sessionStorage、localStorage）

## 技能说明

此技能提供 joyadata 项目封装的 Axios 请求方法和公共工具函数的使用指南。

### 核心功能

1. **请求方法**: `_get`、`_post`、`_delete`、`_put`、`_uploadFile`、`_downFile`
2. **公共方法**: `deepClone`、`parseTime`、`downloadFile`、`debounce` 等
3. **存储方法**: `getSession`、`setSession`、`getLocalStorage` 等
4. **时间工具**: `getToday`、`getWeekday`、`getMonth`、`getYear`

## 项目环境

- **Base URL**: `/dedp/v1` (框架已配置，使用时不需要添加前缀)
- **Token 存储**: sessionStorage / localStorage / Cookies
- **请求库**: Axios (经过封装)

---

## 请求方法

### 引入方式

```javascript
// 在组件中直接使用 this.$request
this.$request._get(url, params)
this.$request._post(url, data)
this.$request._delete(url, data)
this.$request._put(url, data)
```

### 1. GET 请求 `_get`

```javascript
// 基本用法
const { data } = await this.$request._get('/dsc/datasourceAuthorizationBlacklists', params)

// URL 带参数时会自动合并
const { data } = await this.$request._get('/dsc/list?page=1&size=10', { keywords: 'test' })
// 最终请求：/dsc/list?page=1&size=10&keywords=test
```

**参数说明**:
- `url`: 接口路径，不需要 `/dedp/v1/` 前缀
- `params`: 查询参数对象

---

### 2. POST 请求 `_post`

```javascript
// 基本用法
const { data } = await this.$request._post('/dsc/datasourceAuthorizationBlacklists', dataArray)

// 示例：添加黑名单
const params = selectData.map((item) => ({
  datasourceAuthorizationId: this.datasourceAuthorizationId,
  metadataTableCommonId: item.id,
}))
await this.$request._post('/dsc/datasourceAuthorizationBlacklists', params)
```

**参数说明**:
- `url`: 接口路径
- `data`: 请求体数据 (对象或数组)

---

### 3. DELETE 请求 `_delete`

```javascript
// 基本用法（传数组）
await this.$request._delete('/dsc/datasourceAuthorizationBlacklists', ids)

// 示例：批量删除
const ids = selectData.map((item) => item.id)
await this.$request._delete('/dsc/datasourceAuthorizationBlacklists', ids)
```

**参数说明**:
- `url`: 接口路径
- `data`: 请求体数据 (通常是 ID 数组或对象)

---

### 4. PUT 请求 `_put`

```javascript
// 基本用法
await this.$request._put('/dsc/datasourceAuthorization/123', params)

// 示例：更新配置
const params = {
  id: row.id,
  metadataFullAccess: row.metadataFullAccess,
}
await this.$request._put(`/dsc/datasourceAuthorization/${row.id}`, params)
```

**参数说明**:
- `url`: 接口路径
- `data`: 请求体数据

---

### 5. 文件上传 `_uploadFile`

```javascript
// 基本用法
const formData = {
  file: fileElement.files[0],
  name: 'test.txt'
}
await this.$request._uploadFile('/file/app/file/upload', formData)
```

**注意**: 方法内部会自动创建 FormData 对象

---

### 6. 文件下载 `_downFile`

```javascript
// 基本用法
const res = await this.$request._downFile('/dsc/export', params, 'post')

// 处理返回的 Blob
const url = window.URL.createObjectURL(new Blob([res.data]))
const link = document.createElement('a')
link.href = url
link.download = 'export.xlsx'
link.click()
```

**参数说明**:
- `url`: 接口路径
- `data`: 请求参数
- `method`: 请求方式，默认 'post'

---

## 公共方法

### 从 `joyadata-coms/src/utils` 引入

```javascript
import { deepClone, parseTime, downloadFile, downLoad } from 'joyadata-coms/src/utils'
```

---

### 1. 深拷贝 `deepClone`

```javascript
import { deepClone } from 'joyadata-coms/src/utils'

// 用法
const newData = deepClone(this.someData)

// 场景：复制选中数据避免引用问题
const selectData = deepClone(tableRef.selectData || [])
```

---

### 2. 时间格式化 `parseTime`

```javascript
import { parseTime } from 'joyadata-coms/src/utils'

// 用法
parseTime(new Date().getTime(), '{y}-{m}-{d} {h}:{i}:{s}')
// 输出："2024-03-20 10:30:00"

parseTime(new Date(), '{y}-{m}-{d}')
// 输出："2024-03-20"
```

---

### 3. 文件下载 `downloadFile` / `downLoad`

```javascript
import { downloadFile, downLoad } from 'joyadata-coms/src/utils'

// downloadFile: 从 Blob 下载
downloadFile(blobObject, 'filename', 'xlsx')

// downLoad: 直接 URL 下载
downLoad('http://example.com/file.xlsx', 'filename.xlsx', '_blank')
```

---

### 4. 防抖 `debounce`

```javascript
import { debounce } from 'joyadata-coms/src/utils'

// 用法
const handleSearch = debounce(() => {
  this.searchFn()
}, 500)
```

---

### 5. 类型判断

```javascript
import { isType, isArray, isObject, checkType } from 'joyadata-coms/src/utils'

// 用法
isArray([1, 2, 3])           // true
isObject({ a: 1 })           // true
checkType([])                // "Array"
checkType({})                // "Object"
```

---

### 6. 表格数据格式化 `formateTable`

```javascript
import { formateTable } from 'joyadata-coms/src/utils'

// 用法：空值显示 '-'
formateTable('', '-')        // "-"
formateTable(null, '-')      // "-"
formateTable(0, '-')         // 0
formateTable('test', '-')    // "test"
```

---

### 7. 文件大小转换 `conver`

```javascript
import { conver } from 'joyadata-coms/src/utils'

// 用法
conver(1024)                 // "1KB"
conver(1048576)              // "1MB"
conver(1073741824)           // "1GB"
```

---

### 8. 存储方法 (auth.js)

```javascript
import {
  getToken, setToken, removeToken,
  getSession, setSession, removeSession,
  getLocalStorage, setLocalStorage, removeLocalStorage
} from 'joyadata-coms/src/utils/auth'

// SessionStorage
setSession({ key: 'value' }, 'myKey')
const data = getSession('myKey')
removeSession('myKey')

// LocalStorage
setLocalStorage({ key: 'value' }, 'myKey')
const data = getLocalStorage('myKey')
removeLocalStorage('myKey')

// Token (根据配置使用 session/cookie)
setToken('token123')
const token = getToken()
```

---

### 9. 时间工具

```javascript
import { getToday, getWeekday, getMonth, getYear } from 'joyadata-coms/src/utils'

// 几天前
getToday(7)                  // "2024-03-13" (7 天前)

// 几周前/后 (s: 开始，e: 结束)
getWeekday('s', 1)           // 下周的周一
getWeekday('e', -1)          // 上周的周日

// 几月前后
getMonth('s', -1)            // 上月第一天
getMonth('e', 0)             // 本月最后一天

// 几年前后
getYear('s', -1)             // 去年第一天
getYear('e', 1)              // 明年最后一天
```

---

### 10. 复制文本 `copyText`

```javascript
import { copyText } from 'joyadata-coms/src/utils'

// 用法
copyText('要复制的文本')
```

---

## 响应拦截器说明

### 响应码处理

| Code | 说明 | 处理方式 |
|------|------|----------|
| 0 | 成功 | 返回数据 |
| 2 | 成功，无 message | 前端自定义提示 |
| -2 | 成功，警告提示 | Message.warning |
| -3 | 授权过期 | 跳转授权页面 |
| -99 | 授权过期 | 跳转授权页面 |
| 402 | 请求成功，需要处理 | 返回数据 |
| 其他 | 失败 | Message.error + reject |

---

## 使用示例

### 完整的增删改查示例

```vue
<script>
import { deepClone } from 'joyadata-coms/src/utils'

export default {
  data() {
    return {
      list: [],
      loading: false,
    }
  },
  methods: {
    // 查询列表
    async getList() {
      try {
        this.loading = true
        const params = {
          page: 0,
          pager: 10,
          keywords: this.keywords,
        }
        const { result = [] } = await this.$request._get(
          '/dsc/datasourceAuthorizationBlacklists',
          params,
        )
        this.list = result
      } catch (error) {
        console.error('查询失败:', error)
      } finally {
        this.loading = false
      }
    },

    // 添加
    async handleAdd(row) {
      try {
        const params = {
          datasourceAuthorizationId: this.id,
          metadataTableCommonId: row.id,
        }
        await this.$request._post(
          '/dsc/datasourceAuthorizationBlacklists',
          params,
        )
        this.$message.success('添加成功')
        this.getList()
      } catch (error) {
        this.$message.error(error || '添加失败')
      }
    },

    // 删除
    async handleDelete(id) {
      try {
        await this.$request._delete(
          '/dsc/datasourceAuthorizationBlacklists',
          [id],
        )
        this.$message.success('删除成功')
        this.getList()
      } catch (error) {
        this.$message.error(error || '删除失败')
      }
    },

    // 批量删除
    async handleBatchDelete() {
      const selectData = deepClone(this.$refs.table.selectData || [])
      if (!selectData.length) {
        return this.$message.warning('请选择数据')
      }

      const ids = selectData.map(item => item.id)
      try {
        await this.$request._delete(
          '/dsc/datasourceAuthorizationBlacklists',
          ids,
        )
        this.$message.success('批量删除成功')
        this.$refs.table.init()
      } catch (error) {
        this.$message.error(error || '删除失败')
      }
    },
  },
}
</script>
```

---

## 注意事项

1. **接口前缀**: 不需要添加 `/dedp/v1/`，框架已配置
2. **Token**: 请求拦截器自动添加，不需要手动处理
3. **错误处理**: 使用 try-catch 包裹异步请求
4. **Loading**: 请求拦截器会自动显示/隐藏全局 Loading
5. **深拷贝**: 操作数组/对象前使用 `deepClone` 避免引用问题
6. **表格刷新**: 增删改后调用 `this.$refs.table.init()` 刷新数据
7. **重置勾选**: 操作后调用 `this.$refs.table.toggleSelection()` 重置勾选状态

---

## 快速参考表

| 方法 | 用途 | 示例 |
|------|------|------|
| `this.$request._get` | GET 请求 | `await this.$request._get('/list', params)` |
| `this.$request._post` | POST 请求 | `await this.$request._post('/save', data)` |
| `this.$request._delete` | DELETE 请求 | `await this.$request._delete('/delete', ids)` |
| `this.$request._put` | PUT 请求 | `await this.$request._put('/update', data)` |
| `this.$request._uploadFile` | 文件上传 | `await this.$request._uploadFile('/upload', formData)` |
| `this.$request._downFile` | 文件下载 | `await this.$request._downFile('/export', params)` |
| `deepClone()` | 深拷贝 | `deepClone(obj)` |
| `parseTime()` | 时间格式化 | `parseTime(timestamp, '{y}-{m}-{d}')` |
| `downloadFile()` | Blob 下载 | `downloadFile(blob, name, suffix)` |
| `getSession()` | 获取 Session | `getSession('key')` |
| `setSession()` | 设置 Session | `setSession(data, 'key')` |

## 使用规则

### 1. 接口前缀规则

**不需要**添加 `/dedp/v1/` 前缀，框架已自动配置

```javascript
// ✅ 正确
await this.$request._get('/dsc/list', params)

// ❌ 错误
await this.$request._get('/dedp/v1/dsc/list', params)
```

### 2. 请求方法选择

| 操作 | 方法 | 说明 |
|------|------|------|
| 查询列表 | `_get` | 传递 params 参数 |
| 新增/提交 | `_post` | 传递 data 数据 |
| 删除 | `_delete` | 传递 ID 数组或对象 |
| 修改 | `_put` | 传递 data 数据 |
| 上传 | `_uploadFile` | 传递文件数据对象 |
| 下载 | `_downFile` | 返回 Blob 对象 |

### 3. 错误处理

使用 try-catch 包裹异步请求：

```javascript
try {
  const { data } = await this.$request._get('/api/list', params)
  // 处理数据
} catch (error) {
  console.error('操作失败:', error)
  this.$message.error(error || '操作失败')
}
```

### 4. 数据拷贝

操作数组/对象前使用 `deepClone` 避免引用问题：

```javascript
import { deepClone } from 'joyadata-coms/src/utils'

const selectData = deepClone(this.$refs.table.selectData || [])
```

### 5. 表格刷新

增删改后调用 `init()` 刷新表格：

```javascript
// 删除成功后刷新
await this.$request._delete('/api/delete', ids)
this.$message.success('删除成功')
this.$refs.table.init()
```

## 文件位置

- 请求封装：`node_modules/joyadata-coms/src/lib/method.js`
- 工具方法：`node_modules/joyadata-coms/src/utils/index.js`
- 存储方法：`node_modules/joyadata-coms/src/utils/auth.js`
- 请求配置：`node_modules/joyadata-header/src/utils/request.js`