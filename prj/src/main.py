import TermTk as ttk
import sys, os, argparse

def BuildMainScreen(root=None):

    root_layout = ttk.TTkVBoxLayout()
    root.setLayout(root_layout)

    select_frame = ttk.TTkFrame(parent=root)
    select_layout = ttk.TTkHBoxLayout()
    select_frame.setLayout(select_layout)

    port_lst_frame = ttk.TTkFrame(border=True, title="Port list")
    select_layout.addWidget(port_lst_frame)
    port_lst_layout = ttk.TTkVBoxLayout()
    port_lst_frame.setLayout(port_lst_layout)

    port_lst_names = ttk.TTkList(name="Port list", border=True, items=["Item 1","Item 2","Item 3"])
    port_lst_layout.addWidget(port_lst_names)

    port_arg_frame = ttk.TTkFrame(border=True, title="Call arguments")
    select_layout.addWidget(port_arg_frame)
    port_arg_layout = ttk.TTkVBoxLayout()
    port_arg_frame.setLayout(port_arg_layout)

    port_arg_names = ttk.TTkList(name="Call arguments", border=True, items=["Arg 1","Arg 2","Arg 3"])
    port_arg_layout.addWidget(port_arg_names)


    btns_line_frame = ttk.TTkFrame(border=0, maxHeight = 5)
    root_layout.addWidget(btns_line_frame)
    btns_line_layout = ttk.TTkHBoxLayout()
    btns_line_frame.setLayout(btns_line_layout)


    btns_line_layout.addWidget(ttk.TTkButton(text = "Open", border=True))
    btns_line_layout.addWidget(ttk.TTkButton(text = "Scan", border=True))

    small_btns_frame = ttk.TTkFrame(border=0)
    small_btns_layout = ttk.TTkHBoxLayout()
    small_btns_frame.setLayout(small_btns_layout)

    small_btns_layout.addWidget(ttk.TTkButton(text = "\u2191", border=True))
    small_btns_layout.addWidget(ttk.TTkButton(text = "\u2193", border=True))
    small_btns_layout.addWidget(ttk.TTkButton(text = "+", border=True))
    small_btns_layout.addWidget(ttk.TTkButton(text = "x", border=True))
    small_btns_layout.addWidget(ttk.TTkButton(text = "...", border=True))

    btns_line_layout.addWidget(small_btns_frame)

    btns_line_layout.addWidget(ttk.TTkButton(text = "Close", border=True))     
    btns_line_layout.addWidget(ttk.TTkButton(text = "Exit", border=True))     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Full Screen (default)', action='store_true')
    parser.add_argument('-w', help='Windowed',    action='store_true')
    args = parser.parse_args()
    windowed = args.w
    windowed = False

    root = ttk.TTk(title="Ser-porter")

    if windowed:
        MainWnd = ttk.TTkWindow(parent=root,pos=(1,1), size=(120,40), title="Ser-porter", border=True, layout=ttk.TTkGridLayout())
        border = True
    else:
        root.setLayout(ttk.TTkGridLayout())
        MainWnd = root
        border = False

    BuildMainScreen(MainWnd)
    
    root.mainloop()

if __name__ == "__main__":
    main()    