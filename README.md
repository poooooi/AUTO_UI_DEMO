## 项目目的

UI 自动化的 DEMO

## 项目维护人

poooooi

## 框架结构

```AUTO_UI_DEMO
    ├─ config         # 配置层，把所有的项目相关的配置均放到这里，用Python支持较好的配置文件格式如ini或yaml等进行配置。实现配置与代码分离。
    ├─ data           # 数据层，把所有的testcase的参数化相关的文件放到这里，一般可采用xlsx、csv、xml等格式。实现数据与代码分离。
    ├─ drivers        # 驱动层，放所需的驱动，如Chromedriver、IEDriverServer等。
    ├─ log            # 日志层，所有生成的日志均存放在这里，可将日志分类，如运行时日志test log，错误日志error log等。
    ├─ report         # 报告层，放程序运行生成的报告，一般可有html报告、excel报告等。
    ├─ src            # src层，放所有测试相关的文件
    │  ├─ case        # 测试用例
    │  ├─ common      # 项目相关的抽象通用代码
    │  ├─ page        # 页面类，(Page-Object思想)
    │  ├─ suite       # 组织的测试套件
    ├─ utils          # 公共方法层，所有的支撑代码都在这里(包括读取config的类、写log的类、读取excel、xml的类、生成报告的类（如HTMLTestRunner）、数据库连接、发送邮件等类和方法)
    ├─ ReadMe.md
```

## 使用方式

## 维护方式
