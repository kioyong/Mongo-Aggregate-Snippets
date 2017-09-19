#coding=utf-8
#create by yong.a.liang
#create date 2017-04-28
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class StoryPreEditCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        # window.run_command("permute_lines", {"operation": "unique"})
        # window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "\(|\)|\{\}|\$|\^|\-|\."})
        # window.run_command("insert", {"characters": "\$\"\)|public void [\w_]+\(.."})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("left_delete")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "'"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("insert", {"characters": "\""})
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "\|"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("move_to",{"to":"eol"})
        # window.run_command("move_to",{"to": "bol", "extend": True})
        # window.run_command("move_to",{"to": "bol", "extend": True})
        # window.run_command("left_delete")
        # window.run_command("left_delete")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "@US"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("move_to",{"to": "bol", "extend": False})
        # window.run_command("move_to",{"to": "bof", "extend": True})
        # window.run_command("left_delete")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "Feature:"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("move_to",{"to":"eol", "extend": True})
        # window.run_command("cut")
        # window.run_command("left_delete")
        # window.run_command("move_to",{"to": "bof"})
        # window.run_command("move_to",{"to":"eol"})
        # window.run_command("insert", {"characters": "\n"})
        # window.run_command("paste")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "Feature:"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("move_to",{"to": "eol", "extend": False})
        # window.run_command("right_delete")
        # window.run_command("move_to",{"to": "eol", "extend": True})
        # window.run_command("left_delete")
        # window.run_command("move_to",{"to": "bof"})
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": " $"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("left_delete")
        # window.run_command("move_to",{"to": "bof"})
        # window.run_command("move_to",{"to": "eol", "extend": True})
        # window.run_command("copy")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "^\w"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("move_to",{"to": "eol", "extend": False})
        # window.run_command("insert", {"characters": " for @"})
        # window.run_command("paste")
        # window.run_command("show_panel", {"panel": "find"})
        # window.run_command("insert", {"characters": "@@"})
        # window.run_command("hide_panel",{"cancel":"true"})
        # window.run_command("find_all", {"characters": "n"})
        # window.run_command("left_delete")



















