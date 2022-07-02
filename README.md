<div align="center">
<h1>时光相册签到(云函数版)</h1>

[![GitHub issues](https://img.shields.io/github/issues/ICE99125/TimeAlbum?color=red&style=for-the-badge)](https://github.com/ICE99125/TimeAlbum/issues) [![GitHub forks](https://img.shields.io/github/forks/ICE99125/TimeAlbum?style=for-the-badge)](https://github.com/ICE99125/TimeAlbum/network) [![GitHub stars](https://img.shields.io/github/stars/ICE99125/TimeAlbum?style=for-the-badge)](https://github.com/ICE99125/TimeAlbum/stargazers) [![Python](https://img.shields.io/badge/python-3.6%2B-orange?style=for-the-badge)](https://www.python.org/)

</div>

### 步骤

查看[这里](https://github.com/ICE99125/BiliBili_Checkin.git)

### 每日任务

需要抓包....可以使用 Nox + fidder 来抓

#### 获取某张图片的 MD5 值

点击备注, 然后找这个请求

[![j3E6tH.png](https://s1.ax1x.com/2022/07/02/j3E6tH.png)](https://imgtu.com/i/j3E6tH)


#### 获取 asset_ids


这里不要直接复制它的值


[![j3Echd.png](https://s1.ax1x.com/2022/07/02/j3Echd.png)](https://imgtu.com/i/j3Echd)


先保存一下


[![j3EyAe.png](https://s1.ax1x.com/2022/07/02/j3EyAe.png)](https://imgtu.com/i/j3EyAe)


[![j3Er7D.png](https://s1.ax1x.com/2022/07/02/j3Er7D.png)](https://imgtu.com/i/j3Er7D)


#### 获取 tag_id

先把一张相片移入相册, 然后还是找 /v4/PostSyncC.... 的请求

里面的 tag_id 就是相册的 id

