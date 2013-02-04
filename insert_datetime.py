# coding=utf-8
# 比较版本号
# import sys;print(sys.version_info[:2] < (3,0))
# import platform;print(platform.python_version() < '3.0')
# print(int(sublime.version()) < 3000)

import sys, sublime_plugin, datetime

class insertDatetimeCommand(sublime_plugin.TextCommand):
  def run(self, edit, format):
    timestamp = datetime.datetime.now()
    if format == 'ymd':
        # yyyy-mm-dd
        timestamp = timestamp.strftime('%Y-%m-%d')
    elif format == 'ymdhms':
        # %X = %H:%M:%S
        timestamp = timestamp.strftime('%Y-%m-%d %X')
    else: # format == "xxx"
        # 2012-02-18 13:17:28.047000
        #timestamp = datetime.datetime.now().isoformat(' ')
        # Sat Feb 18 13:20:41 2012
        #timestamp = datetime.datetime.now().ctime()

        # 数字变为字符串 str(xx),字符串变为数字 int(string)
        timestamp = int(timestamp.strftime("%w"))
        week = {
            1 : '一', 2 : '二', 3 : '三', 4 : '四', 5 : '五', 6 : '六', 7 : '日'
        }

        timestamp = '星期' + week[timestamp]
        
        # print(sys.version_info[:2] < (3,0))
        if sys.version_info[:2] < (3,0):
            ## 中文要指定: coding=utf-8 | gbk ，再decode
            timestamp = timestamp.decode('utf-8')
        # else:
            # timestamp = timestamp.encode('utf-8').decode('utf-8')

    #for region in the selection
    for r in self.view.sel():
      #put in the timestamp
      #(if text is selected, it'll be replaced in an intuitive fashion)
      self.view.erase(edit, r)
      self.view.insert(edit, r.begin(), timestamp)