#coding=utf-8
#create by yong.a.liang
#create date 2016-07-07
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class UsEditCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>filter log info
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "info "})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("expand_selection",{"to": "line"})
        # window.run_command("left_delete")
        # window.run_command("move_to", {"to": "bof"})
        # <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>filter org.* package
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "\(|\)|\{\}|\$|\^|\-|'"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        # window.run_command("expand_selection",{"to": "line"})
        window.run_command("left_delete")
        # window.run_command("move_to", {"to": "bof"})
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

'''
^[0-9\-\sa-z\,\:]+\[[a-z\-0-9]+\]\s\[org\.[a-z\.0-9]+.*
^[0-9\-\sa-z\,\:]+\[[a-z\-0-9]+\]\s\[org\..*
'''
