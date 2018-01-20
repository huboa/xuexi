from types import FunctionType
# def header_list(config):
#     result = []
#     # ['id', 'name', 'email',display_edit,display_del]
#     # ['ID', '用户名', '邮箱','临时表头',临时表头]
#
#     for n in config.get_list_display():
#         if isinstance(n, FunctionType):
#             # 执行list_display中的函数
#             val = n(config, is_header=True)
#         else:
#             val = config.mcls._meta.get_field(n).verbose_name
#             result.append(val)
#
#     return result
#
#
# def body_list(config,xxx):
#     # 处理表内容
#     body_list = []
#     """
#     [
#         obj,
#         obj,
#         obj,
#     ]
#     # ['id', 'name', 'email',display_edit,display_del]
#     [
#         [1, '天了','123@liv.com'],
#         [2, '天1了','123@liv.com'],
#         [3, '天了123','123@liv.com'],
#     ]
#     """
#     for row in result_list:
#         temp = []
#         for n in self.get_list_display():
#             if isinstance(n, FunctionType):
#                 val = n(self, row=row)
#             else:
#                 val = getattr(row, n)
#             temp.append(val)
#         body_list.append(temp)
#
# def add_url(config):
#     app_model_name = (self.mcls._meta.app_label, self.mcls._meta.model_name,)
#     name = "stark:%s_%s_add" % app_model_name
#     add_url = reverse(name)