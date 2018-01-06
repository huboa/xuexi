博客地址：
    http://www.jianshu.com/p/1aa7ade32825

目录结构
├── css                 css样式文件目录
├── chouti.html         主页文件
├── images              图片存放目录
├── jquery-3.2.1.js     jQuery框架文件
└── README.txt          说明文件

“最新”、“发现”、“人类发布”三个按钮和底部分页用jQuery实现了动态效果


遇到的问题：
    当父级元素没有设定高度，想通过子元素将父元素的高度撑起，如果子元素是浮动的（float），\
    则子元素就无法撑起父元素的高度，这时就需要对父元素清除两侧浮动，假设父元素的class='item',\
    可以对父元素加如下css样式：
    .item:after{
        content:"";
        display:block;
        clear:both;
    }
    以上css的意思是，在父元素之后添加一个块级标签，内容为空，并清除两侧浮动；
