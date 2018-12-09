#!/usr/bin/env python3

import os, sys
import tkinter as tk
import tkinter.font as tkFont

class XMLView():
    def __init__(self, txtwig=None, string=None):
        if txtwig and string:
            self.loadTags(txtwig)
            self.parser(txtwig, string)

    def loadTags(self, txtwig):
        self.txtwig = txtwig
        font_name = txtwig['font']
        b = tkFont.nametofont(font_name).copy()
        b.config(weight="bold")

        txtwig.tag_config("tags", foreground="purple", font=b)
        txtwig.tag_config("attribs", font=b)
        txtwig.tag_config("values", foreground="blue")

    def de_code(self, code, b, e):
        if b == e: return
        beg = str(b[0])+'.'+str(b[1])
        end = str(e[0])+'.'+str(e[1])
        self.txtwig.tag_add(code, beg, end)
        # print(code, self.txtwig.get(beg, end), beg, end)
        return end

    def parser(self, txtwig, string, index=None):
        if not index:
            index = txtwig.index("current")

        # print("parser", index)
        self.j, self.i = [ int(i) for i in index.split('.') ]
        txtwig.mark_set("insert", index)
        beg = end = [ self.j, self.i ]
        in_tag_flag = False
        tag_name_flag = False
        in_quote = False
        quote = None
        for char in string:
            txtwig.insert('insert', char)
            self.i += 1
            if   char == '<':
                beg = [self.j, self.i]
                in_tag_flag = True
            elif char == '>':
                end = [self.j, self.i-1]
                if not tag_name_flag:
                    self.de_code("tags", beg, end)
                    tagf = False
                beg = [self.j, self.i]
                in_tag_flag = False
            elif char in '\'"':
                if not in_tag_flag: continue
                in_quote = not in_quote
                quote = char
                end = [self.j, self.i-1]
                self.de_code("values", beg, end)
                beg = [self.j, self.i]
            elif char == "?":
                if in_quote: continue
                beg = [self.j, self.i]
            elif char == ' ':
                if in_quote: continue
                if not in_tag_flag: continue
                end = [self.j, self.i-1]
                if tag_name_flag:
                    self.de_code("attribs", beg, end)
                else:
                    self.de_code("tags", beg, end)
                beg = [self.j, self.i]
            elif char == '=':
                if in_quote: continue
                end = [self.j, self.i-1]
                self.de_code("attribs", beg, end)
                beg = [self.j, self.i]
            elif char == '\n':
                if in_tag_flag:
                    end = [self.j, self.i-1]
                    # print()
                    if tag_name_flag:
                        self.de_code("attribs", beg, end)
                    else:
                        self.de_code("tags", beg, end)

                self.j += 1; self.i = 0
                beg = [self.j, self.i]

        return self.j, self.i

def handle(event):
    root.title(event.data)
    engine.txtwig.delete('1.0', "end")
    engine.parser(engine.txtwig, open(event.data).read())

if __name__ == "__main__" :
    if len(sys.argv)<2:
        print("Argument(s) Missing", file=sys.stderr); exit(1);

    root = tk.Tk()
    root.bind("<Key-Escape>", lambda event: root.quit())

    def_font = tkFont.Font(family="DejaVuSansMono", size=11)
    text = tk.Text(root, font=def_font)
    string = open(sys.argv[1]).read()
    engine = XMLView(text, string)
    text.pack(expand=True, fill="both")

    try:
        filepath=os.path.abspath(__file__)
        fullpath=os.path.dirname(filepath)
        sys.path.append(fullpath+"/..")

        from tk_fileDND.wrapper import tkDND
        dnd = tkDND(root)
        dnd.bindtarget(text, handle, 'text/uri-list')
    except:
        print("Drag and Drop module not found")

    tk.mainloop()