/***************************  新闻评论 ***************************/

var NewsCommentsClient = Mtime.Page.NewsCommentsClient;
NewsCommentsClient = Class.create();

Object.extend(NewsCommentsClient.prototype, {
    name: "NewsCommentsClient",

    relatedID: -1,

    relatedType: 0,

    commentGroupID: -1,

    pageIndex: 1,

    isLogin: true,

    isRobotActive: false,
    //服务器端方法
    server: {
        //查询往期新闻
        getNewsCommentList: function (id, type, orderType, pageIndex, clientCallBack) {
            return Mtime.Component.Ajax.request(channelService, 'Mtime.Channel.Pages.NewsService', 'GetNewsComments', [id, type, orderType, pageIndex], clientCallBack, '/service/news.mcs', 'get', '20000');
        },

        UpdateCMSCommentByVCode: function (relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status, vcode, vcodeId, callBack) {
            return Mtime.Component.Ajax.request(channelService, 'Mtime.Channel.Pages.NewsService', 'UpdateCMSCommentByVCode', [relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status, vcode, vcodeId], callBack, '/service/news.mcs', 'get', '20000');
        },

        RefreshVcode: function (callBack) {
            return Mtime.Component.Ajax.request(channelService, 'Mtime.Channel.Pages.NewsService', 'RefreshVcode', [Math.floor(Math.random() * 999999999)], callBack, '/service/news.mcs', 'get', '20000');
        },

        CommentForwardNews: function (newsId, text, callBack) {
            return Mtime.Component.Ajax.get('Mtime.Service.Pages.TwitterService', 'CommentForwardNews', [newsId, text], callBack, '/Service/Twitter.msi', 'get', '20000');
        },

        getNewsCommentPageNewComment: function (isAllowAnonymousComment, commentId, commentContent, clientCallBack) {
            return Mtime.Component.Ajax.request(channelService, 'Mtime.Channel.Pages.NewsService', 'GetNewsCommentPageNewComment', [isAllowAnonymousComment, commentId, commentContent], clientCallBack, '/service/news.mcs', 'get', '20000');
        }

    },

    options : {
        newsId: '',
        callback: null
    },

    //初始化
    initialize: function (options) {
        this.setOptions(options);
        this.initializeServerData();
        this.intitField();
        this.initializeDOM();
        this.initializeEvent();
        this.initializeControl();
        this.load();
    },

    setOptions : function(options) {
        Object.extend(Object.extend(this, this.options), options);
    },

    //初始化服务器端数据
    initializeServerData: function () {

    },

    intitField: function () {
        //回复
        this.linkReplyCommentPrefix = "m_linkReplyComment_";

        //回复区域
        this.divReplyBodyPrefix = "m_divReplyBody_";

        //回复编辑器区域
        this.divReplyEditorPrefix = "m_divReplyEditor_";

        //回复编辑器
        this.txtReplyEditorPrefix = "m_txtReplyEditor_";

        //回复:保存
        this.btnSaveReplyPrefix = "m_btnSaveReply_";

        //回复:取消
        this.btnCancelReplyPrefix = "m_btnCancelReply_";

        //回复:编辑
        this.linkEditCommentPrefix = "m_linkEditComment_";

        //回复:删除
        this.linkDelCommentPrefix = "m_linkDelComment_";

        //回复内容区域
        this.divReplyPrefix = "m_divReply_";

        //回复编辑内容区域
        this.divEditReplyPrefix = "m_divEditReply_";

        //编辑回复 编辑器
        this.txtEditReplyEditorPrefix = "m_txtEditReplyEditor_";

        //编辑回复 保存
        this.btnSaveEditReplyPrefix = "m_btnSaveEditReply_";

        //编辑回复 取消
        this.btnCancelEditReplyPrefix = "m_btnCancelEditReply_";

        this.txtVerifyCodePrefix = "m_txtVerifyCode_";
        this.hdVerifyCodeIDPrefix = "m_hdVerifyCodeID_";
        this.imgVerifyCodePrefix = "m_imgVerifyCode_";
        this.linkRefreshVerifyCodePrefix = "m_linkRefreshVerifyCode_";

        this.newsType = 3;
        this.orderType = 1;
    },

    //初始化DOM元素
    initializeDOM: function () {
        this.divCommentListRegion = $("m_divCommentListRegion");
    },

    destroyDOM: function () {
        this.divCommentListRegion = null;
        this.txtCommentEditor = null;
        this.btnSaveComment = null;
        this.newsId = null;
        this.newsType = null;
        this.orderType = null;
        this.pageIndex = null;
    },

    //初始化DOM事件
    initializeEvent: function () {
        this.divCommentListRegionHandler = this.commentListRegion_onClick.bind(this);
        if(this.divCommentListRegion){
            this.divCommentListRegion.observe("click", this.divCommentListRegionHandler);
        }
        
        Event.observe(window, "unload", this.close.bind(this));
    },

    //销毁DOM事件
    destroyEvent: function () {
        this.divCommentListRegion.stopObserving("click", this.divCommentListRegionHandler);
    },

    initializeControl: function () {

    },

    destroyControl: function () {

    },

    load: function () {
        this.getCommentList();
    },

    commentListRegion_onClick: function (evt) {

        var element = Event.findElement(evt, "a");
        if (element && element.readAttribute) {
            if (element.readAttribute("ordertype") === "new") { Event.stop(evt); this.orderType = 1; this.getCommentList(); }
            if (element.readAttribute("ordertype") === "hot") { Event.stop(evt); this.orderType = 0; this.getCommentList(); }
            if (element.readAttribute("pageindex")) { Event.stop(evt); this.pageIndex = parseInt(element.readAttribute("pageindex"), 0); this.getCommentList(); }
        }

        var clickElement = Event.element(evt);
        var method = clickElement.readAttribute("method");
        var eleId = clickElement.id;
        var commentId = eleId.split("_")[2];
        if (method == 'RefreshVerifyCode') {
            this.server.RefreshVcode(
            function () {
                var res = refreshVcodeResult;
                var codeSrc = res.value.src;
                var codeId = res.value.id;
                var txtVerifyCode = this.txtVerifyCodePrefix;
                var hdVerifyCodeID = this.hdVerifyCodeIDPrefix;
                var imgVerifyCode = this.imgVerifyCodePrefix;
                if (commentId) {
                    hdVerifyCodeID += commentId;
                    imgVerifyCode += commentId;
                    txtVerifyCode += commentId;
                }
                if (clickElement.up().down('span')) {
                    var sb = new StringBuilder(); // html片段
                    sb.append(String.format('<input id="{1}" value="{0}" type="hidden">', codeId, txtVerifyCode));
                    sb.append(String.format('<img id="{1}" src="{0}" alt="" class="v_m" style="margin:0 10px;">', codeSrc, hdVerifyCodeID));
                    sb.append(String.format('<a id="{0}" method="RefreshVerifyCode" href="javascript:void(0)" title="刷新换一张" class="ml10">刷新</a></span>', imgVerifyCode));
                    clickElement.up().down('span').innerHTML = sb.toString();
                    clickElement.removeAttribute("method");
                }
                else {
                    clickElement.up().down('input[type="hidden"]').value = codeId;
                    clickElement.up().down('img').src = codeSrc;
                }
            } .bind(this));
            return;
        }
        var vcodeId = "";
        var vcode = "";

        //点击"回复"
        if (this.find(eleId, this.linkReplyCommentPrefix)) {
            $(this.divReplyBodyPrefix + commentId).show();
            $(this.divReplyEditorPrefix + commentId).show();
            $(this.divReplyEditorPrefix + commentId).scrollTo();

            $(this.txtReplyEditorPrefix + commentId).value = "";
        }
        //回复:确定
        else if (this.find(eleId, this.btnSaveReplyPrefix)) {
            var replyContent = $(this.txtReplyEditorPrefix + commentId).value;

            if (replyContent.blank()) {
                $alert("请输入回复内容。");
                return;
            }

            if (!this.isLogin) {
                if (clickElement.previous()) {
                    vcode = clickElement.previous().down('input[type="text"]').value;
                    if (vcode.blank()) {
                        $alert('请输入验证码。');
                        return;
                    }
                    vcodeId = clickElement.previous().down('input[type="hidden"]').value;
                }
            }

            this.onUpdateCMSComment(parseInt(this.newsId, 10), parseInt(this.newsType, 10), commentId, -1, this.commentGroupID, replyContent, this.orderType, 0, 1, vcode, vcodeId);

        }
        //回复:取消
        else if (this.find(eleId, this.btnCancelReplyPrefix)) {
            $(this.divReplyEditorPrefix + commentId).hide();

            if ($(this.divReplyEditorPrefix + commentId).previousSiblings().length === 0) {
                $(this.divReplyBodyPrefix + commentId).hide();
            }
        }
        //编辑回复:确定
        else if (this.find(eleId, this.btnSaveEditReplyPrefix)) {
            var newContent = $(this.txtEditReplyEditorPrefix + commentId).value;

            if (newContent.blank()) {
                $alert("请输入回复内容。");
                return;
            }

            this.onUpdateCMSComment(parseInt(this.newsId, 10), parseInt(this.newsType, 10), -1, commentId, this.commentGroupID, newContent, this.orderType, 0, 1, "", "");
        }
        //编辑回复:取消
        else if (this.find(eleId, this.btnCancelEditReplyPrefix)) {
            $(this.divReplyPrefix + commentId).show();
            $(this.divEditReplyPrefix + commentId).update("");
        }
        //编辑
        else if (this.find(eleId, this.linkEditCommentPrefix)) {

            var template = "<textarea id=\"m_txtEditReplyEditor_{0}\" rows=\"6\" class=\"bor_a5\" style=\"width: 98%;\">{1}</textarea><p class=\"mt10\"><input id=\"m_btnSaveEditReply_{0}\" value=\"写好了\" class=\"btn_square_hover mr15\" type=\"submit\"><input id=\"m_btnCancelEditReply_{0}\" value=\"取消\"  class=\"btn_square\" type=\"submit\"></p>";

            var oldContent = $(this.divReplyPrefix + commentId).innerHTML;
            var editorHtml = clickElement.getAttribute("isdelete") ? String.format(template, commentId, '') : String.format(template, commentId, oldContent);

            $(this.divReplyPrefix + commentId).hide();
            $(this.divEditReplyPrefix + commentId).update(editorHtml);

        }
        //删除
        else if (this.find(eleId, this.linkDelCommentPrefix)) {
            $alert(
                "<p class='tc'><b>是否要 删除 该评论?</b></p>",
                function () {
                    this.server.UpdateCMSCommentByVCode(parseInt(this.newsId, 10), parseInt(this.newsType, 10), -1, commentId, this.commentGroupID, "", this.orderType, 0, 3, "", "",
                        function () {
                            var res = updateCMSCommentByVCodeResult;
                            if (res.value && res.value[0] !== "") {
                                if (res.value[0] === "-1") {
                                    $alert("删除失败");
                                }
                                else {
                                    location.reload();
                                }
                            }
                            else {
                                location.reload();
                            }
                        } .bind(this));
                } .bind(this));
        }
        //保存评论
        if (!this.btnSaveComment) return;
        else if (eleId == this.btnSaveComment.id) {
            var commentContent = this.txtCommentEditor.value;

            if (commentContent.blank()) {
                $alert("请输入回复内容。");
                return;
            }

            if (!this.isLogin) {
                if (clickElement.previous()) {
                    vcode = clickElement.previous().down('input[type="text"]').value;
                    if (vcode.blank()) {
                        $alert('请输入验证码。');
                        return;
                    }
                    vcodeId = clickElement.previous().down('input[type="hidden"]').value;
                }
            }

            this.onUpdateCMSComment(parseInt(this.newsId, 10), parseInt(this.newsType, 10), 0, -1, this.commentGroupID, commentContent, this.orderType, 0, 1, vcode, vcodeId);
        }
    },

    refreshVerifyCode: function (evt) {
        var clickElement = Event.element(evt);

        var eleId = clickElement.id;
        var commentId = -1;

        if (eleId.split("_").length > 2) {
            commentId = eleId.split("_")[2];
        }

        this.server.RefreshVcode(
            function (res) {
                var codeSrc = res.value.src;
                var codeId = res.value.id;

                if (commentId == -1) {
                    this.hdVerifyCodeID.value = codeId;
                    this.imgVerifyCode.src = codeSrc;
                }
                else {
                    $(this.hdVerifyCodeIDPrefix + commentId).value = codeId;
                    $(this.imgVerifyCodePrefix + commentId).src = codeSrc;
                }
            } .bind(this));
    },

    find: function (eleID, prefix) {
        return eleID.indexOf(prefix) != -1;
    },

    //请求评论列表
    getCommentList: function () {
        this.server.getNewsCommentList(parseInt(this.newsId, 10), parseInt(this.newsType, 10), parseInt(this.orderType, 10), this.pageIndex, function () {
            if (newCommentsResult && newCommentsResult.value) {
                $("m_divCommentListRegion").innerHTML = newCommentsResult.value.newsCommentsHtml;
                this.commentInsertPlace = $("m_commentInsertPlace");
                this.relatedID = newCommentsResult.value.RelatedID;
                this.relatedType = newCommentsResult.value.RelatedType;
                this.pageIndex = newCommentsResult.value.PageIndex;
                this.commentGroupID = newCommentsResult.value.CommentGroupID;
                this.isLogin = newCommentsResult.value.IsLogin;
                this.isAllowAnonymousComment = newCommentsResult.value.isAllowAnonymousComment;

                this.txtCommentEditor = $("m_txtCommentEditor"); //评论编辑器
                this.btnSaveComment = $("m_btnSaveComment"); //保存评论
                $loadJs("/js/08/userAvatar.js", function () {
                    UsersAvatars.register("m_divCommentListRegion");
                });
                this.callback && this.callback(); 
            }
        } .bind(this));
    },

    //显示验证码对话框
    showValidDialog: function (relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status) {
        this.changeVcode();
        this.vcodeDialog = new Dialog({
            windowClassName: "w445",
            content: Builder.node("div", { className: "ml20 mr20" }, [
                    Builder.node("h3", { id: "tip" }, [
                        "抱歉，连续访问次数过多，为了证明你不是机器人，请输入验证码后继续查询"
                    ]),
                    Builder.node("p", { className: "mt10" }, [
                        Builder.node("input", { id: "vcodeText", type: "text", className: "w120" }),
                        Builder.node("img", { id: "vcodeImage", src: "" + this.vcodeSrc + "", alt: "验证码", className: "v_m mlr10" }),
                        Builder.node("a", { href: "#", id: "changeVcodeLink", onclick: "return false;" }, [
        "看不清楚？换一张"
    ])
                    ])
                ]),
            buttonRegionClass: "mt10 pb15 ml20",
            buttons: [{
                title: "确定",
                buttonStyle: "btn_square_hover mr15",
                callback: function (dialog) {
                    var vcode = dialog.getEl("vcodeText").value;
                    vcode = vcode.trim();
                    if (vcode.length > 0) {
                        this.onUpdateCMSComment(relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, this.orderType, 0, status, vcode, this.vcodeId);
                    }
                    else {
                        $alert("请输入验证码！");
                    }
                } .bind(this)
            }],
            readyCallback: this.onShowValidDialogReady.bind(this),
            closeCallback: this.onShowValidDialogClose.bind(this)
        });
    },

    onShowValidDialogReady: function (dialog) {
        //刷新验证码
        this.changeVcodeLink = dialog.getEl("changeVcodeLink");
        this.vcodeImage = dialog.getEl("vcodeImage");
        this.onClickChangeVcodeLinkHandler = this.changeVcode.bind(this);
        this.changeVcodeLink.observe("click", this.onClickChangeVcodeLinkHandler);
    },

    //更换验证码
    changeVcode: function () {
        this.server.RefreshVcode(
            function (res) {
                this.vcodeSrc = res.value.src;
                this.vcodeId = res.value.id;
                this.vcodeImage.src = this.vcodeSrc;
            } .bind(this));
    },

    onShowValidDialogClose: function () {
        this.changeVcodeLink.stopObserving("click", this.onClickChangeVcodeLinkHandler);
        this.changeVcodeLink = null;
        this.vcodeImage = null;
        this.isRobotActive = false;
        this.vcodeDialog = null;
    },

    onUpdateCMSComment: function (relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status, vcode, vcodeId) {
        this.server.UpdateCMSCommentByVCode(relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status, vcode, vcodeId,
                function () {
                    var res = updateCMSCommentByVCodeResult;
                    if (res.value && res.value[0] !== "") {
                        if (res.value[0] == "-4") {
                            $alert("请登录后进行评论。");
                        }
                        else if (res.value[0] == "-3") {
                            res.value.splice(0, 1);
                            $alert("你的文字中有被禁止的内容，请修改后发布。");
                        }
                        else if (res.value[0] == "-2") {
                            res.value.splice(0, 1);
                            $alert("你提交的内容可能不符合时光网的社区准则，需审核后才能发布。");
                        }
                        else if (res.value[0] == "-1") {
                            $alert("保存失败");
                        }
                        else if (res.value[0] === "-100") {
                            $alert("您在时光网发布的内容违反互联网管理规定，对此帐户予禁言处理。");
                        }
                        else if (res.value[0] && res.value[0] === "isRobot" && res.value[1] === "1") {
                            if (!this.isRobotActive) {
                                this.isRobotActive = true;
                                this.showValidDialog(relatedId, relatedType, parentId, commentId, commentGroupId, commentContent, orderType, topN, status);
                            }
                            else {
                                this.isRobotActive = true;
                                $alert(res.value[2]);
                            }
                        }
                        else {
                            this.isRobotActive = false;
                            if (this.vcodeDialog) {
                                this.vcodeDialog.close();
                            }
                            if (parentId > 0) {
                                //评论的回复，跳转去评论列表页首页
                                location.href = res.value[1];
                                location.reload();
                            } else {
                                //评论
                                var newCommentId = parseInt(res.value[2], 10);
                                this.server.getNewsCommentPageNewComment(this.isAllowAnonymousComment, newCommentId, commentContent, this.commentCallBack.bind(this));
                                if (this.isLogin) {
                                    $confirm('是否将该评论转发为我的微评', function () {
                                        this.server.CommentForwardNews(relatedId, commentContent, null);
                                    } .bind(this));
                                }
                            }
                        }
                    }
                    else {
                        location.reload();
                    }
                } .bind(this));
    },



    //评论回调方法
    commentCallBack: function (result) {
        if (result && result.value && this.commentInsertPlace) {
            var newEl = document.createElement("div");
            newEl.innerHTML = result.value.commentHtml;
            this.insertAfter(newEl, this.commentInsertPlace);
            this.registerAvatar();
            this.txtCommentEditor.value = "";
            this.initVCodeDom(this.btnSaveComment);
        }
    },

    insertAfter: function (newEl, targetEl) {
        var parentEl = targetEl.parentNode;
        if (parentEl.lastChild === targetEl) {
            parentEl.appendChild(newEl);
        } else {
            parentEl.insertBefore(newEl, targetEl.nextSibling);
        }
    },

    registerAvatar: function () {
        $loadJs("/js/08/userAvatar.js", function () {
            UsersAvatars.register("m_divCommentListRegion");
        });
    },

    initVCodeDom: function (dom) {
        var m_txtVerifyCode = $("m_txtVerifyCode");
        if (!this.isLogin && m_txtVerifyCode) {
            m_txtVerifyCode.value = "";
            m_txtVerifyCode.setAttribute("method", "RefreshVerifyCode");
            var parent = m_txtVerifyCode.parentNode;
            var spanNode = parent.down("span");
            spanNode.innerHTML = "";
        }
    },

    //资源清理
    close: function () {
        this.destroyControl();
        this.destroyEvent();
        this.destroyDOM();
    }
});