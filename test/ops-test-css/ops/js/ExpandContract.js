/***************************  2014星光不落 ***************************/
!function () {
    ExpandContract = Class.create();
    var serverUrl = "http://api.mtime.com";
    Object.extend(ExpandContract.prototype, {
        name: "ExpandContract",
        //初始化
        initialize: function (options) {
            this.setOptions(options);
            this.initializeDOM();
            this.initializeEvent();
            this.initializeAnimate();
            this.load();
        },

        setOptions: function (options) {
            Object.extend(Object.extend(this, this.options), options);
        },


        //初始化DOM元素
        initializeDOM: function () {
            this.$mh_siderhdla = $$(".mh_sider dl a");
            // this.returnTop = $$(".mh_title");
        },

        destroyDOM: function () {

        },

        //初始化DOM事件
        initializeEvent: function () {
            var that = this,
                pageNum = location.href.match(/[page]{4}[-]{1}\d{1,}/);

            for (var i = 0; i < this.$mh_siderhdla.length; i++) {
                pageIndex = this.$mh_siderhdla[i].readAttribute('href').replace(".html", "");

                if (pageNum && pageIndex == pageNum) {
                    this.$mh_siderhdla[i].parentNode.addClassName("cur");
                }
            }
            // this.returnTop.onclick = function () {
            //     document.documentElement.scrollTop = document.body.scrollTop = 0;
            // }
            // this.returnTop.each(function (el) {
            //     el.observe("click", this.expendHandler);
            // });

            // // this.returnTop.observe("click", this.expendHandler);
            // this.expendHandler = this.expend.bind(this);




            // this.expendHandler = this.expend.bind(this);
            // if (this.$mh_siderh4s) {
            //     this.$mh_siderh4s.each(function (el) {
            //         el.addClassName("curr");
            //         el.nextSiblings()[0].show();
            //         el.observe("click", that.expendHandler);
            //     });

            // }

            //if(this.$mh_siderhdla){
            //                this.$mh_siderhdla.each(function(el){
            //                    if(pageNum && "page-"+(index+1) == pageNum[0]){
            //                        $(el.parentElement).addClassName("on");
            //                    }
            //                });
            //
            //            }

            Event.observe(window, "unload", this.close.bind(this));
        },

        //销毁DOM事件
        destroyEvent: function () {
        },

        initializeAnimate: function () {
        },

        destroyControl: function () {

        },

        load: function () {
        },
        // expend: function (evt) {
        //     alert("111")
        //     document.documentElement.scrollTop = document.body.scrollTop = 0;
        // },
        getUrlParam: function (name) {
            var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);
            if (r != null) return unescape(r[2]); return null;

        },
        //资源清理
        close: function () {
            this.destroyControl();
            this.destroyEvent();
            this.destroyDOM();
        }
    });
    window.ExpandContract = ExpandContract;
}();