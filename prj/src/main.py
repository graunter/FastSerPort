import TermTk as ttk        # pip3 install --upgrade pyTermTk
from TermTk import TTkLog, TTkTerm
import sys, os, argparse
import sys
import glob
import serial               #pip install pyserial

port_lst_names = None

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass

    return result

def on_scan_btn():
    global port_lst_names

    # TODO: reselect the curent port name if present in rescan
    result = serial_ports()

    while port_lst_names.items():
        port_lst_names.removeAt(0)

    port_lst_names.addItems(result)


def BuildMainScreen(root=None):

    global port_lst_names

    root_layout = ttk.TTkVBoxLayout()
    root.setLayout(root_layout)

    select_frame = ttk.TTkFrame(parent=root)
    select_layout = ttk.TTkHBoxLayout()
    select_frame.setLayout(select_layout)

    port_lst_frame = ttk.TTkFrame(border=True, title="Port list")
    select_layout.addWidget(port_lst_frame)
    port_lst_layout = ttk.TTkVBoxLayout()
    port_lst_frame.setLayout(port_lst_layout)

    port_lst_names = ttk.TTkList(name="Port list", border=True, items=serial_ports())
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

    scan_btn = ttk.TTkButton(text = "Scan", border=True)
    scan_btn.clicked.connect(on_scan_btn)
    btns_line_layout.addWidget(scan_btn)

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

    exit_btn = ttk.TTkButton(text = "Exit", border=True)
    exit_btn.clicked.connect(ttk.TTkHelper.quit)
    btns_line_layout.addWidget(exit_btn)     

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