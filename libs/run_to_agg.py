#coding=utf-8
#created by yong.a.liang
#created date 2017-04-29
#modified by xxx
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class RunToAggCommand(sublime_plugin.WindowCommand):
    def run(self,reverse=False):
        window = self.window
        #pre edit, remove single space

        window.run_command("move_to",{"extend": False, "to": "eof"})
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": ": "})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("left_delete")
        window.run_command("insert", {"characters": ":"})
        #
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": ": "})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("left_delete")
        window.run_command("insert", {"characters": ":"})
        #
        window.run_command("insert", {"characters": ":  "})
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("left_delete")
        window.run_command("insert", {"characters": ":"})
        #
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "aggregate"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("move",{"forward": True, "by": "characters"})
        window.run_command("move",{"forward": True, "by": "characters"})
        window.run_command("move",{"forward": True, "by": "characters"})
        window.run_command("move",{"forward": True, "by": "words","extend": True})
        window.run_command("move",{"forward": False, "by": "characters","extend": True})
        window.run_command("move",{"forward": False, "by": "characters","extend": True})
        window.run_command("copy")

        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "pipeline"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("move_to",{"extend": False, "to": "eol"})
        window.run_command("move_to",{"extend": True, "to": "bof"})
        window.run_command("right_delete")
        window.run_command("insert", {"characters": "db."})
        window.run_command("paste")
        window.run_command("insert", {"characters": ".aggregate(["})

        window.run_command("move_to",{"extend": False, "to": "eof"})
        # # re
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "]}}"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("move_to",{"extend": False, "to": "eol"})
        window.run_command("move_to",{"extend": True, "to": "bol"})
        window.run_command("right_delete")

        window.run_command("move_to",{"extend": True, "to": "eof"})
        window.run_command("right_delete")

        window.run_command("insert", {"characters": "])"})