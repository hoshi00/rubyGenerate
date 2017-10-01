import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")

class txtWrapCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        start = "<ruby>"
        end = "<rp>(</rp><rt> </rt><rp>)</rp></ruby>"


        for region in self.view.sel():
                if not region.empty():
                    self.view.replace(edit, region, start + self.view.substr(region) + end)