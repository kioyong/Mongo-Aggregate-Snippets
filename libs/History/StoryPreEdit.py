#coding=utf-8
#create by yong.a.liang
#create date 2017-04-28
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class UsEditCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "\(|\)|\{\}|\$|\^|\-"})
        # window.run_command("insert", {"characters": "\$\"\)|public void [\w_]+\(.."})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("left_delete")

