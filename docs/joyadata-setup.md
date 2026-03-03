# Joyadata 项目环境搭建指南

本指南帮助你快速搭建 Joyadata 前端开发环境。

## 项目介绍

Joyadata 是一套基于 Element UI 二次封装的前端统一控制平台，用于：
- 统一产品风格
- 统一操作逻辑
- 团队快速上手

### 核心模块

| 模块 | 说明 |
|------|------|
| joyadata-coms | 封装的基础组件库 |
| joyadata-header | 公共页面（登录、404、头部菜单等） |
| joyadata-vue-template | 项目模板 |

---

## NRM 配置

配置 npm 内网/外网地址：

```bash
# 1. 安装 nrm
npm i -g nrm

# 2. 添加内网地址
nrm add joyadata http://192.168.90.126:8081/repository/joyadata-npm-group/

# 3. 添加外网地址
nrm add joyadata http://112.126.29.199:8081/repository/joyadata-npm-group/

# 4. 切换源
nrm use joyadata

# 5. 下载依赖
yarn add joyadata-coms joyadata-header
```

**常见问题**: 下载失败时删除 `yarn.lock` 或 `package-lock.json` 重新拉取。

---

## 项目初始化

### 使用 joyadata-cli

```bash
# 1. 安装 CLI
npm i -g joyadata-cli

# 2. 创建项目
joyadata-cli create [项目名称]

# 3. 进入目录并下载依赖
cd [项目名称]
yarn

# 4. 启动项目
yarn dev
```

### 手动克隆模板

```bash
git clone http://39.107.213.160/zhangzhe/joyadata_vue_template.git
cd joyadata_vue_template
yarn
yarn dev
```

---

## 项目目录结构

```
src/
├── api/           # 请求地址
├── assets/        # 图片资源
├── components/    # 组件
├── env/           # 环境配置
├── icons/         # SVG 图标
├── layout/        # 公共页面
├── mixins/        # 公共方法
├── router/        # 路由配置
├── store/         # Vuex 数据
├── styles/        # 公共样式
├── utils/         # 工具方法
└── views/         # 页面视图

mock/              # 模拟数据
```

### Mock 数据配置

```javascript
// vue.config.js
devServer: {
  before: require('./mock/mock-server.js')  // 注释掉则不使用 mock
}

// .env 文件
VUE_APP_API_BASE_URL = "/dev-api"  // 走 mock 数据
```

---

## 数据请求

### 请求方法

```javascript
this.$request._get(url, params)    // GET
this.$request._post(url, params)   // POST
this.$request._put(url, params)    // PUT
this.$request._delete(url, params) // DELETE
this.$request._downFile(url, params, method) // 文件下载
```

### 请求示例

```javascript
// 列表查询
this.$request._get("/api/list", {
  page: 0,
  pager: 10,
  searchby: "name",
  name: "关键词"
})

// 新增
this.$request._post("/api/list", { name: "名称" })

// 修改
this.$request._put("/api/list/1", { name: "新名称" })

// 删除
this.$request._delete("/api/list/1")
```

---

## API 接口规范

### URL 格式

```
ip:端口/项目名/版本/模块/功能/表
```

### 示例

```
http://192.168.80.180:9200/jddsi/v1/cms/approval_categorys
```

### 请求后缀

| 后缀 | 说明 |
|------|------|
| /fulltree | 全树形结构 |
| /dict | 字典结构 |
| /eq/x1/x2 | 查询 x1=x2 的数据 |

### 列表参数

| 参数 | 说明 |
|------|------|
| page | 当前页，默认 0 |
| pager | 每页数量 |
| groupbys | 分组查询 |
| sortby | 排序字段 |
| searchby | 搜索字段 |
| paramkeys | 额外参数 |
| withs | 关联字段查询 |
| lazys | 级联查询 |
| cascades | 级联保存 |

### 树形接口

| 接口 | 说明 |
|------|------|
| /tree | 普通查询 |
| /tree/fulltree | 全树 |
| /tree/minitree | Mini 树 |
| /tree/parent/{id} | 父级树（异步加载） |
| /tree/parents/{id} | 所有父级树 |
| /tree/children/{id} | 子级树（异步加载） |
| /tree/children/{id} | 所有子级树 |

---

## Axios 高级用法

### 请求取消

```javascript
import axios from "axios";

export default {
  methods: {
    async fetchData() {
      // 创建 CancelToken
      const source = axios.CancelToken.source();
      
      try {
        const res = await this.$request._get(
          "/api/url",
          { paramkeys: "type", type: "value" },
          {
            cancelToken: source.token,
            onUploadProgress: (progressEvent) => {
              // 上传进度
              if (progressEvent.lengthComputable) {
                this.percentage = ((progressEvent.loaded / progressEvent.total) * 100).toFixed(2);
              }
            }
          }
        );
      } catch (error) {
        console.log(error);
      }
      
      // 取消请求
      source.cancel({ code: 2 });
    }
  }
};
```

### 文件下载

```javascript
import { downloadFile } from "joyadata-coms/src/utils";

async download() {
  try {
    const res = await this.$request._downFile(
      "/api/download",
      {},
      "get",
      {
        onDownloadProgress: (progressEvent) => {
          if (progressEvent.lengthComputable) {
            this.percentage = ((progressEvent.loaded / progressEvent.total) * 100).toFixed(2);
          }
        }
      }
    );
    downloadFile(res.data, "文件名", "xlsx");
  } catch (error) {
    console.log(error);
  }
}
```

---

## 注意事项

1. **依赖安装**: 使用 `yarn` 而非 `npm`
2. **Mock 切换**: 注释掉 `vue.config.js` 中的 mock 配置
3. **请求前缀**: 使用 `/dev-api` 走 mock 数据
4. **接口路径**: 遵循 `项目名/版本/模块/功能/表` 规范
