# -*- coding: utf-8 -*-
""" 
@Time    : 2024/9/3 10:06
@Author  : zhangsan
@FileName: wechat_PCA.py
@SoftWare: PyCharm
"""
import time
import random
import uiautomation as auto
import pyautogui
import re
import tkinter as tk
import pyperclip as cp

# --hidden-import 有一些模块或包不希望在打包结果中出现    --add-data 添加数据文件     -F 是指打包exe  -w 是指运行时不需要命令行窗口   --icon 导入图标
# pyinstaller --hidden-import=comtypes.stream -F -w --icon=logo.ico wechat_PCA.py
# # 关键字
# keyword = '测试'
# # 排除的参数
# excluded_parameters = "测试6"    # 空格、逗号、分号等分隔符
# # 消息
# information = "你好，我是机器人，很高兴为你服务。"

class wechat_ui():
    def __init__(self, win):
        self.win = win

    def input_group(self, keyword):
        # 搜索框
        search = wechatWindow.EditControl(Name="搜索")
        # 点击搜索框
        search.Click()
        # 清空按钮
        clear = wechatWindow.ButtonControl(Name="清空")
        # 点击清空
        clear.Click()
        # 点击搜索框
        search.Click()
        # 输入群组名称
        search.SendKeys(keyword)
        # 获取搜索结果
        all_data = wechatWindow.ListControl(Name=Name).GetChildren()
        return all_data

    def get_list_from_second_empty_string(self, input_list):
        # 找到第二个空字符串的索引
        first_empty_index = input_list.index('')
        second_empty_index = input_list.index('', first_empty_index + 1)
        # 从第二个空字符串开始返回列表
        return input_list[second_empty_index:]

    def get_group(self, all_data):
        # 面板字符列表
        pane_control_list = []
        # 面板字符索引位置
        pane_control_index_list = []
        # 全部展开按钮
        button_name_list = []
        # 全部展开按钮索引
        button_name_index_list = []
        # 全部信息列表
        all_information_list = []
        # 存入展开后的群组名称
        group_list = []
        # 检索三个展开按钮名称
        for i in range(len(all_data)):
            all_information_list.append(all_data[i].Name)
            if '显示全部' in all_data[i].Name:
                button_name_index_list.append(i)
                button_name_list.append(all_data[i].Name)
        # 遍历所有子控件
        for i in range(len(all_data)):
            if all_data[i].ControlType == 50033:
                pane_control_index_list.append(i)
                if all_data[i].GetChildren()[0].Name != '公众号':
                    pane_control_list.append(all_data[i].GetChildren()[0].Name)
        # print(all_information_list)
        # print(button_name_index_list)
        # print(button_name_list)
        # print(pane_control_index_list)
        # print(pane_control_list)
        if len(button_name_list) == 3:
            for i in range(button_name_index_list[1] + 2):
                auto.SendKeys('{DOWN}')
            wechatWindow.ButtonControl(Name=button_name_list[1]).Click()
            for j in range(int(''.join(filter(str.isdigit, button_name_list[1])))):
                pyautogui.scroll(-100)
            all_data = wechatWindow.ListControl(Name=Name).GetChildren()
            for group in all_data:
                group_list.append(group.Name)
            if '收起' in group_list:
                group_last_index = group_list.index('收起')
            return group_list[pane_control_index_list[1]: group_last_index]
        if len(pane_control_list) >= 3 and len(button_name_list) == 2:
            if (pane_control_index_list[1] - pane_control_index_list[0]) != 7:
                for i in range(button_name_index_list[0] + 2):
                    auto.SendKeys('{DOWN}')
                wechatWindow.ButtonControl(Name=button_name_list[0]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[0])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[1]: group_last_index]
            if (pane_control_index_list[2] - pane_control_index_list[1]) != 7:
                for j in range(button_name_index_list[2] + 2):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                return group_list[pane_control_index_list[1]: pane_control_index_list[2]]
        if set(pane_control_list) == {'群聊', '聊天记录'}:
            if len(button_name_list) == 2:
                wechatWindow.ButtonControl(Name=button_name_list[0]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[0])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[0]: group_last_index]
            if len(button_name_list) == 0:
                return group_list[pane_control_index_list[0]: pane_control_index_list[1]]
            if len(button_name_list) == 1 and button_name_index_list[0] == 6:
                wechatWindow.ButtonControl(Name=button_name_list[0]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[0])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[0]: group_last_index]
            else:
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                return group_list[pane_control_index_list[0]: pane_control_index_list[1]]
        if set(pane_control_list) == {'联系人', '群聊'}:
            if len(button_name_list) == 2:
                for i in range(button_name_index_list[1] + 2):
                    auto.SendKeys('{DOWN}')
                wechatWindow.ButtonControl(Name=button_name_list[1]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[1])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[1]: group_last_index]
            if len(button_name_list) == 1 and (pane_control_index_list[1] - pane_control_index_list[0]) != 7:
                for i in range(button_name_index_list[0] + 2):
                    auto.SendKeys('{DOWN}')
                wechatWindow.ButtonControl(Name=button_name_list[0]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[0])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[1]: group_last_index]
            if len(button_name_list) == 1 and (pane_control_index_list[1] - pane_control_index_list[0]) == 7:
                if len(all_information_list) > (pane_control_index_list[1] + 6):
                    return all_information_list[pane_control_index_list[1]:pane_control_index_list[1] + 6]
                else:
                    return all_information_list[pane_control_index_list[1]::]
        if set(pane_control_list) == {'群聊'}:
            if len(button_name_list) == 1:
                for i in range(button_name_index_list[0] + 2):
                    auto.SendKeys('{DOWN}')
                wechatWindow.ButtonControl(Name=button_name_list[0]).Click()
                for j in range(int(''.join(filter(str.isdigit, button_name_list[0])))):
                    pyautogui.scroll(-100)
                all_data = wechatWindow.ListControl(Name=Name).GetChildren()
                for group in all_data:
                    group_list.append(group.Name)
                if '收起' in group_list:
                    group_last_index = group_list.index('收起')
                return group_list[pane_control_index_list[0]: group_last_index]
            if len(button_name_list) == 0:
                if len(all_information_list) >= 7:
                    return all_information_list[0:7]
                else:
                    return all_information_list[0::]

    def filter_elements_by_keyword(self, group, keyword):
        keyword_replace = keyword.replace('\n', '')
        first_arr = []
        for item in group:
            if keyword_replace in item:
                first_arr.append(item)
        return first_arr

    def input_excluded_parameters(self, keyword, excluded_parameters, group):
        if excluded_parameters == '\n':
            return group
        else:
            first_arr = self.filter_elements_by_keyword(group, keyword)
            excluded_parameters_replace = excluded_parameters.replace("\n", '')
            part_list = re.split(r',|;', excluded_parameters_replace)
            # 排除干扰
            return [item for item in first_arr if not any(keyword in item for keyword in part_list)]

    def send_information(self, information, excluded_group):
        k = 0
        for i in range(len(excluded_group)):
            # 搜索框
            search = wechatWindow.EditControl(Name="搜索")
            # 点击搜索框
            search.Click()
            # 清空按钮
            clear = wechatWindow.ButtonControl(Name="清空")
            # 点击清空
            clear.Click()
            # 点击搜索框
            search.Click()
            # 输入群组名称
            search.SendKeys(excluded_group[i])
            # 点击群组
            group = wechatWindow.ListControl(Name=Name).GetChildren()
            for j in range(len(group)):
                if excluded_group[i] == group[j].Name and group[j].Name != '搜索 ' + excluded_group[i]:
                    try:
                        k += 1
                        parent_control = group[j].GetParentControl().GetChildren()[0].GetChildren()
                        if parent_control[0].Name == '群聊':
                            group[j].Click()
                            wechatWindow.EditControl(Name=excluded_group[i]).Click()
                            cp.copy(information)
                            pyautogui.hotkey('ctrl', 'v')
                            wechatWindow.ButtonControl(Name="发送(S)").Click()
                            with open("已发送的群记录.txt", encoding="utf-8-sig", mode="a") as f:
                                f.write(excluded_group[i] + ";")
                            # 超过7个休息2-4秒
                            if k % 7 == 0:
                                time.sleep(random.uniform(2, 4))
                    except Exception as e:
                        # 如果发生异常（例如找不到控件），打印错误信息并跳出循环
                        print(f"无法找到群：{excluded_group[i]}，错误信息：{e}")
                        continue

    def ui(self):
        self.win.title("wechat_PCA_v1.0.0")  # #窗口标题
        # 设置 窗口宽 高
        self.x, self.y = 800, 520
        # 获取屏幕宽、高
        self.windowX = self.win.winfo_screenwidth()
        self.windowY = self.win.winfo_screenheight()
        # 计算中心坐标
        self.cen_x = (self.windowX - self.x) / 2
        self.cen_y = (self.windowY - self.y) / 2
        # 设置窗体大小,并置于中心位置
        # 设置窗体大小,并置于中心位置
        self.win.geometry("%dx%d+%d+%d" % (self.x, self.y, self.cen_x, self.cen_y))
        self.win.resizable(False, False)  # 禁止调整大小
        # 窗口图标
        # icon = PhotoImage(file="./logo.png")
        # self.win.iconphoto(True, icon)
        self.label1 = tk.Label(self.win, text="输入搜索的关键字", fg="red")
        self.label2 = tk.Label(self.win, text="输入排除的参数（逗号或者分号）", fg="red")
        self.label3 = tk.Label(self.win, text="输入要发送的消息", fg="red")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.text1 = tk.Text(width=40, height=2)
        self.text1.grid(row=0, column=1, padx=10, pady=10)
        self.text2 = tk.Text(width=40, height=12)
        self.text2.grid(row=1, column=1, padx=10, pady=10)
        self.text3 = tk.Text(width=40, height=12)
        self.text3.grid(row=2, column=1, padx=10, pady=10)
        self.button1 = tk.Button(text="启动脚本", width=10, height=2, command=self.operation)
        self.button1.grid(row=1, column=4, padx=10, pady=10)

    def operation(self):
        all_data = self.input_group(self.text1.get('1.0', 'end'))
        group = self.get_group(all_data)
        excluded_group = self.input_excluded_parameters(
            self.text1.get('1.0', 'end'), self.text2.get('1.0', 'end'), group
        )
        self.send_information(self.text3.get('1.0', 'end'), excluded_group)




if __name__ == '__main__':
    # # 全局参数
    # wechatWindow = auto.WindowControl(searchDepth=1, Name="微信", ClassName='WeChatMainWndForPC')
    # Name = "@str:IDS_FAV_SEARCH_RESULT:3780"
    # win = tk.Tk()
    # web = wechat_ui(win)
    # web.ui()
    # # 窗口持久化
    # win.mainloop()
    # 全局参数
    wechatWindow = auto.WindowControl(searchDepth=1, Name="微信", ClassName='WeChatMainWndForPC')
    Name = "@str:IDS_FAV_SEARCH_RESULT:3780"
    win = tk.Tk()
    web = wechat_ui(win)
    web.ui()
    # 窗口持久化
    win.mainloop()
