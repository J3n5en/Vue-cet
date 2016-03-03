# 4/6级成绩查询api接口说明文档



## 使用说明：

---

## 1. 有准考证4/6级成绩查询

URL: `http://[domain]/GetCetScore/<ticket>/<username>`

访问方式：GET、POST

参数：

| 参数名        | 类型      | 是否必须 | 描述      | 示例              |
| ---------- | ------- | ---- | ------- | --------------- |
| <ticket>   | Integer | 是    | 考生准考证号码 | 440530151110612 |
| <username> | String  | 是    | 考生姓名    | 罗增榕             |

调用成功返回事例：

``` json
{
    "Contact_us": "wangyuan.info",
    "Listening": "130",
    "Reading": "169",
    "Status": "1",
    "Total": "446",
    "Writing": "147",
    "name": "罗撒旦",
    "result": "44053015132210612",
    "school": "韶关学院"
}
```

## 2. 无准考证查询

 URL: `http://[domain]/GetCetScoreWithoutTickets/<province>/<school>/<cet_type>/<username>` 

访问方式：GET、POST

参数：

| 参数名        | 类型      | 是否必须 | 描述               | 示例   |
| ---------- | ------- | ---- | ---------------- | ---- |
| <province> | String  | 是    | 考生所在省份           | 广东   |
| <school>   | String  | 是    | 考生所在学校           | 韶关学院 |
| <cet_type> | Integer | 是    | 考试类型，其中1为四级，2为6级 | 1    |
| <username> | String  | 是    | 考生姓名             | 罗增榕  |

调用成功返回事例：

``` json
{
    "Contact_us": "wangyuan.info",
    "Listening": "130",
    "Reading": "169",
    "Status": "1",
    "Total": "446",
    "Writing": "147",
    "name": "罗撒旦",
    "result": "44053015132210612",
    "school": "韶关学院"
}
```

## 3. 针对韶关学院的无准考证成绩查询

URL: `http://[domain]/GetCetScoreWithoutTickets/<province>/<school>/<cet_type>/<username>` 

访问方式：GET、POST

参数：

| 参数名        | 类型       | 是否必须 | 描述               | 示例       |
| ---------- | -------- | ---- | ---------------- | -------- |
| <cet_type> | cet_type | 是    | 考试类型，其中1为四级，2为6级 | 1        |
| <cet_type> | String   | 是    | 考试姓名             | cet_type |

调用成功返回事例：

``` json
{
    "Contact_us": "wangyuan.info",
    "Listening": "130",
    "Reading": "169",
    "Status": "1",
    "Total": "446",
    "Writing": "147",
    "name": "罗撒旦",
    "result": "44053015132210612",
    "school": "韶关学院"
}
```



## 部署说明：

---

脚本依赖：

``` python
Flask==0.10.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
requests==2.9.1
Werkzeug==0.11.4
wheel==0.24.0

```

推荐部署方式：`flask + gevent + gunicorn + nginx`





## 注意：

---

其中[domain] 为部署后的域名。

调用失败返回事例:

``` json
{
    "Contact_us": "wangyuan.info",
    "Status": "0"
}
```



## Contact：

---

Blog:blog.j3n5en.com

email:admin@j3n5en.com



## License

---

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE Version 2, December 2004

Copyright (C) 2004 Sam Hocevar [sam@hocevar.net](mailto:sam@hocevar.net)

Everyone is permitted to copy and distribute verbatim or modified copies of this license document, and changing it is allowed as long as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

1.  You just DO WHAT THE FUCK YOU WANT TO.