#coding=utf-8
#created by yong.a.liang
#created date 2017-04-29
#modified by xxx
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class AggToRunCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "aggregate"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("move",{"forward": False, "by": "words"})
        window.run_command("move",{"forward": False, "by": "characters"})
        window.run_command("move",{"extend": True,"forward": False, "by": "words"})
        window.run_command("copy")
        window.run_command("move_to",{"extend": False, "to": "eol"})
        window.run_command("move_to",{"extend": True, "to": "bol"})
        window.run_command("right_delete")
        window.run_command("insert", {"characters": "{\nrunCommand:{\naggregate:'"})
        window.run_command("paste")
        window.run_command("insert", {"characters": "',\n pipeline:["})
        window.run_command("move_to",{"extend": False, "to": "eof"})

        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "])"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("right_delete")

        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "\]\)"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("right_delete")
        window.run_command("move_to",{"extend": True, "to": "eof"})
        window.run_command("right_delete")
        window.run_command("insert", {"characters": "]}}"})
