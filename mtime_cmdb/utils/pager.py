
class Pagination(object):
    def __init__(self,item_total_count,per_page_item_count=10,request_current_page=1,per_group_page_count=10,request_url=''):
        """
        :param item_total_count: 查询数据库总条数
        :param per_page_item_count: 每页显示item数
        :param request_current_page: 请求当前页码
        :param per_group_page_count: 最大页码数－每个ｈｔｍｌ页面显示几页
        """
        ###初始化页码变量
        self.request_url=request_url

        # print("check url info ",self.request_url)
        self.item_total_count = item_total_count
        self.per_page_item_count = per_page_item_count


        page_total_count,item_remainder = divmod(item_total_count, per_page_item_count)
        # print("check item 总数",item_total_count,"每页码显示item 个数",per_page_item_count)
        # print("check page 总页数" ,page_total_count,"item 余数",item_remainder)
        if  item_remainder:
            page_total_count += 1
        self.page_total_count = page_total_count   ####总页数
        try:
            request_current_page = int(request_current_page)
        except Exception as e:
            request_current_page = 1
        if request_current_page > page_total_count:
            request_current_page = page_total_count
        if request_current_page < 1:
            request_current_page = 1

        self.request_current_page = request_current_page   ##请求页码


        ###初始化页码组
        all_page_group_count, page_remainder = divmod(page_total_count,per_group_page_count)
        # print("check group 总组数",all_page_group_count,"每组页数",per_group_page_count,"最后一组页数",page_remainder)
        if  page_remainder:
            all_page_group_count += 1

        self.all_page_group_count = all_page_group_count   #页码组数
        self.per_group_page_count = per_group_page_count   #每组页码数
        self.current_page_group_id = int((request_current_page - 1) // per_group_page_count + 1)  ##页码组id
        self.current_page_group_start = (self.current_page_group_id - 1) * per_group_page_count + 1  ##页码组开始页

        ##页码组开结束页
        if  self.current_page_group_id >= all_page_group_count:
            self.current_page_group_end = page_total_count
        else:
            self.current_page_group_end = self.current_page_group_start + per_group_page_count - 1

        print("页码总组数", self.all_page_group_count, "当前页码组id", self.current_page_group_id, "开始页", self.current_page_group_start, "组结束页",self.current_page_group_end, )

    ##当前页码项目分片1
    @property
    def current_page_start_item(self):
        return (self.request_current_page - 1) * self.per_page_item_count

    ##当前页码项目分片2
    @property
    def current_page_end_item(self):

        if self.request_current_page >= self.page_total_count:
            req = self.item_total_count
        else:
            req = (self.request_current_page) * self.per_page_item_count
        print("check current", req)
        return req


### 生成html 返回
    def page_html(self):

        page_html = ''
        for i in range(self.current_page_group_start,  self.current_page_group_end + 1):
            if i == self.request_current_page:
                temp = '<a class="active" href="%s?page=%s&items=%s">%s</a>' % (self.request_url,i,self.per_page_item_count, i)
            else:
                temp = '<a href=%s?page=%s&items=%s>%s</a>' % (self.request_url,i,self.per_page_item_count ,i,)
            page_html += temp


            ###单页
        if self.request_current_page > 1:
            pre_page = self.request_current_page - 1
            pre_page_html = '<a href=%s?page=%s&items=%s><</a>' % (self.request_url,pre_page,self.per_page_item_count)
        else:
            pre_page = self.request_current_page
            pre_page_html = '<a href=%s?page=%s&items=%s><</a>' % (self.request_url,pre_page,self.per_page_item_count,)
            # pre_page_html = ""
        if self.request_current_page <  self.page_total_count :
            next_page = self.request_current_page + 1
            next_page_html = '<a href=%s?page=%s&items=%s>></a>' % (self.request_url,next_page,self.per_page_item_count,)
        else:
            next_page = self.request_current_page
            next_page_html = '<a href=%s?page=%s&items=%s>></a>'  % (self.request_url,next_page,self.per_page_item_count,)
            # next_page_html = ""

            ####页码组

        if self.current_page_group_id > 1:
            pre_group_page_id = self.request_current_page - self.per_group_page_count
            pre_page_group_html = '<a href=%s?page=%s&items=%s><<</a>' % (self.request_url,pre_group_page_id,self.per_page_item_count,)

        else:
            # pre_page_group_html = ""
            pre_group_page_id = self.request_current_page
            pre_page_group_html = '<a href=%s?page=%s&items=%s><<</a>' % (self.request_url,pre_group_page_id,self.per_page_item_count,)

        if self.current_page_group_id >= self.all_page_group_count:
            next_group_page_id =  self.request_current_page
            next_page_group_html = '<a href=%s?page=%s&items=%s>>></a>' %  (self.request_url,next_group_page_id,self.per_page_item_count,)
            # next_page_group_html = ""
        else:
            next_group_page_id =  self.request_current_page  + self.per_group_page_count
            next_page_group_html = '<a href=%s?page=%s&items=%s>>></a>' % (self.request_url,next_group_page_id,self.per_page_item_count,)

            ##首页尾页
        one_page_html = '<a href=%s?page=%s&items=%s>首页</a>' % (self.request_url,1,self.per_page_item_count,)
        end_page_html = '<a href=%s?page=%s&items=%s>末页</a>' % (self.request_url,self.page_total_count,self.per_page_item_count,)
        ###共 多少页
        all_page_html = ' 页<select name="items"> <option value="20">默认</option><option value="5">5</option><option value="10">10</option> <option value="20">20</option> <option value="50">50</option> <option value="100">100</option></select>行  共%s页' % (self.page_total_count )
        # select_page_html='<form action="">page: <input type="text" name="page"><input type="submit" value="提交"></form>'
        select_page_html = '  到  <input type="text" name="page"  size="1" > 页  <input type="submit" value="确定"></form>'
        page_html = "<form >" + one_page_html + pre_page_group_html + pre_page_html + page_html + next_page_html + next_page_group_html + end_page_html + all_page_html + select_page_html
        return  page_html