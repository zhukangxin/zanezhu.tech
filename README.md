# zanezhu.tech 个人网站 · 部署与维护手册

中英双语个人网站：英文版在 `zanezhu.tech/`，中文版在 `zanezhu.tech/zh/`。
内容放在 GitHub 上，由 Netlify 免费托管。在 `zanezhu.tech/admin` 后台写文章、发动态、改简历，保存后约 1 分钟网站自动更新。

整个上线过程约 1–2 小时，只需要第一次做一遍。

---

## 一、上线（第一次做一遍）

### 第 1 步：把网站放到 GitHub

1. 登录 [github.com](https://github.com)（没有账号先注册）。
2. 右上角 **+** → **New repository**。
   - Repository name 填：`zanezhu.tech`
   - 选 **Private**（私有，别人看不到源文件）或 Public 均可
   - 不要勾选 "Add a README"
   - 点 **Create repository**
3. 在新仓库页面点 **uploading an existing file**。
4. 把解压后 `zanezhu-site` 文件夹**里面的所有文件和文件夹**拖进去（不是拖文件夹本身）。
5. 页面底部点 **Commit changes**。

### 第 2 步：改一处设置

在 GitHub 仓库里打开 `static/admin/config.yml`，点右上角铅笔图标编辑：

```yaml
repo: YOUR_GITHUB_USERNAME/zanezhu.tech
```

把 `YOUR_GITHUB_USERNAME` 换成你的 GitHub 用户名，然后点 **Commit changes**。

### 第 3 步：用 Netlify 发布

1. 打开 [netlify.com](https://www.netlify.com)，选择 **Sign up with GitHub**。
2. **Add new project → Import an existing project → GitHub**，授权后选择 `zanezhu.tech` 仓库。
3. 构建设置会自动读取，无需修改（命令 `python build.py`，发布目录 `dist`）。
4. 点 **Deploy**。1–2 分钟后会得到一个临时网址，如 `xxx.netlify.app`，打开就能看到网站。

### 第 4 步：绑定域名 zanezhu.tech

1. 如果还没买域名，可以在 Cloudflare、Namecheap 或 Porkbun 购买 `zanezhu.tech`。
   注意：`.tech` 域名首年常有优惠，但**续费价格可能明显更高**，购买前请看清续费价。
2. Netlify 项目里进入 **Domain management → Add a domain**，输入 `zanezhu.tech`。
3. 按 Netlify 的提示设置 DNS，二选一：
   - 把域名的 Nameservers 改成 Netlify 提供的 4 个地址（最简单）；或
   - 在域名商处添加 Netlify 给出的 A 记录和 CNAME 记录。
4. DNS 生效后（几分钟到几小时），Netlify 会自动申请 HTTPS 证书。

### 第 5 步：开通在线编辑后台

后台需要用 GitHub 账号登录，因此要做一次授权设置：

1. GitHub 右上角头像 → **Settings → Developer settings → OAuth Apps → New OAuth App**：
   - Application name：`zanezhu.tech CMS`
   - Homepage URL：`https://zanezhu.tech`
   - Authorization callback URL：`https://api.netlify.com/auth/done`
   - 点 **Register application**，再点 **Generate a new client secret**
   - 记下 **Client ID** 和 **Client secret**
2. 回到 Netlify 项目，找到 **OAuth** 设置（通常在 Project configuration → Access & security 下），**Install provider → GitHub**，填入上面的 Client ID 和 Client secret。
3. 打开 `https://zanezhu.tech/admin`，点 **使用 GitHub 登录**，就能看到后台。

> Netlify 菜单名称偶尔会调整。如果找不到某个选项，在 Netlify 帮助文档中搜索 "OAuth provider GitHub"。

### 第 6 步：让搜索引擎收录

1. **Google Search Console**：[search.google.com/search-console](https://search.google.com/search-console)
   - 添加资源，选 **网域（Domain）**，输入 `zanezhu.tech`，按提示在域名 DNS 里加一条 TXT 记录完成验证
   - 左侧 **Sitemaps** → 提交 `https://zanezhu.tech/sitemap.xml`
   - 在「网址检查」里输入首页网址，点「请求编入索引」，可以加快收录
2. **Bing Webmaster Tools**：[bing.com/webmasters](https://www.bing.com/webmasters)，可以直接从 Google Search Console 导入。Bing 同时覆盖 DuckDuckGo 和 Yahoo 的结果。
3. **百度站长平台**（可选）：[ziyuan.baidu.com](https://ziyuan.baidu.com)。验证码可以填到 `data/site.yaml` 的 `baidu_site_verification`。百度对境外服务器上的网站收录较慢，属正常现象。
4. **LinkedIn**：在个人资料的 Contact info 里添加网站 `https://zanezhu.tech`，并在 Featured 中放上网站链接。外部链接是搜索排名的重要信号。

一般 3–14 天后，搜索 "Kangxin Zhu"、"Zane Zhu" 或 "朱康辛" 就能看到网站。

---

## 二、日常维护（都在 zanezhu.tech/admin 完成）

| 想做的事 | 在后台点哪里 |
|---|---|
| 发一条动态 | 「动态（中文）」或「Updates (English)」→ 新建 → 填标题和内容 → 发布 |
| 发一篇文章 | 「文章（中文）」或「Articles (English)」→ 新建 → 填写 → 发布 |
| 收录一篇已在别处发表的文章 | 新建文章，填写「最初发表于」和「原文链接」，正文可以只写摘要或留空 |
| 修改简历 | 「个人简历 Résumé」→ 修改对应字段 → 发布 |
| 上传头像 | 「个人简历」→「头像」上传图片 → 发布 |

每次点「发布」后，后台会把改动保存到 GitHub，Netlify 自动重新生成网站，约 1 分钟后生效。

**文章的几个小规则：**

- **网址名**用英文小写和短横线，例如 `digital-payment-strategy`，会成为网址 `zanezhu.tech/zh/articles/digital-payment-strategy/`。
- 同一篇文章的中英文版本用**同一个网址名**，网站会自动关联两个语言版本，点右上角 EN/中文 可以互相切换。
- 只写了中文、没有英文版本也没关系。
- 勾选「草稿」后文章会保存，但不在网站上显示。

**整理那 10 篇文章：** 每篇准备好标题、日期、发表平台、原文链接和一两句摘要即可。愿意的话也可以贴上全文。全文发在自己网站上对搜索排名最有帮助，但请先确认原发表平台允许转载。

---

## 三、文件说明（给 AI 编程工具或工程师看）

```
data/profile.yaml      简历内容（中英双语，所有简历文字都在这里）
data/site.yaml         网站设置、导航和界面文字、搜索引擎验证码
content/articles/zh|en 文章（Markdown 文件）
content/updates/zh|en  动态（Markdown 文件）
templates/             页面模板（Jinja2）
static/                CSS、图标、后台（admin/）、上传的图片
build.py               网站生成器：读取以上内容，生成 dist/
netlify.toml           Netlify 构建设置
```

本地预览（可选，需要安装 Python 3）：

```bash
pip install -r requirements.txt
python build.py
python -m http.server 8000 --directory dist   # 浏览器打开 http://localhost:8000
```

SEO 已内置：每页独立的标题和描述、canonical、中英 hreflang 互指、Open Graph 分享卡片、Schema.org Person/BlogPosting 结构化数据、sitemap.xml、robots.txt、中英文 RSS。网站不依赖任何外部字体或脚本（后台除外），因此在中国大陆访问也较快。

---

## 四、自有服务器（阿里云）上的更新方式

网站源文件在 GitHub，服务器上的副本在 `/opt/zanezhu.tech`，网页目录是 `/var/www/zanezhu.tech`。

**手动更新**（在 GitHub 改完内容后，SSH 登录服务器运行）：

```bash
bash /opt/zanezhu.tech/update.sh --force
```

**自动更新**（推荐，每 5 分钟检查一次 GitHub，有新内容就自动重新生成）：

```bash
crontab -e
# 在打开的文件最后加一行，保存退出：
*/5 * * * * bash /opt/zanezhu.tech/update.sh >> /var/log/zanezhu-update.log 2>&1
```

**在 GitHub 网页上直接修改内容**（不需要后台）：

| 要改什么 | 文件位置 | 怎么做 |
|---|---|---|
| 个人简介、简历 | `data/profile.yaml` | 打开文件 → 点铅笔图标编辑 → Commit changes |
| 新增文章 | `content/articles/zh/` 或 `en/` | 进入文件夹 → Add file → Create new file，文件名如 `my-article.md` |
| 新增作品 | `content/projects/zh/` 或 `en/` | 同上，文件名如 `my-project.md` |
| 新增动态 | `content/updates/zh/` 或 `en/` | 同上，文件名如 `2026-11-01-note.md` |

新文件的格式可以照抄同一文件夹里的 `example-*.md`，把 `draft: true` 改成 `false`。
