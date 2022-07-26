# Pyinstaller GUI by Pop Mario Denis
# Pyinstaller by pyinstaller.org

logo1="""@@@@@@@@@@@@@@@@&#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(
           *###############*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,..... //.@@@@@@@@@
@@@@@@#########%%%%%%%%%%###@@@@@@@%......                          ////.@@@@@@@
@@@@@@*######%%%%%%%%%%%%%%#*                                       ////.@@@@@@@
@@,****######%%%%%%%%%%%%%%%*                                       /////@@@@@@@
@@.****#####%%%%%%%%%%%%%%%%*                                        ////@@@@@@@
@@.****#####%%%%%%%%%%%%%*************                               ////.@@@@@@
@@*****#####%%%%%%%*%%%%%%%%%%%%%%%%%%%####.                         ////.@@@@@@
@@@****#####%%%%%*%%%%%%%%%%%%%%%%%%%%%%%%###                        /////@@@@@@
@@@.***#####%%%%%*%%%%%%%%%%%%%%%%%%     %%##.                        ////@@@@@@
@@@.***#####%%%%%*%%%%%%%%%%%%%%%%%%     %%##.                        ////.@@@@@
@@@****#####%%%%%*%%%%%%%%%%%%%%%%%%%%%%%####.                        ////.@@@@@
@@@@***#####%%%%%*%%%%%%%%%%%%%%%%///////////.       @@@@@            /////@@@@@
@@@@,**#####%%%%%*%%%%%%%%%%%%%%%%*                     @@@@@          ////@@@@@
@@@@.**#####%%%%%%%%%%%%%%%%%%%%%%*                        @@@@@       ////.@@@@
@@@@,**######%%%%%%%%%%%%%%%%%%%%#*                       @@@@         ////.@@@@
@@@@@**(#####%%%%%%%%%%%%%%%%%%%##*                     @@@@           ////*@@@@
@@@@@,**#######%%%%%%%%%%%%%%%%##*                    @@@@              ////@@@@
@@@@@.***/########%%%%%%%%%%###*                                      //////.@@@
@@@@@.****  *##############/*                ,//////////////////////////////.@@@
@@@@@@*****         ***************************/////////////////////////////*@@@
@@@@@@,******************************,,,,,,#%%%%%%%%%%%%%%%//////////////////@@@
@@@@@@.***************#############%%%%%%%%%%%%%%%%%%%%%%%%%/////////////////.@@
@@@@@@.**************,###########%%%%%%%%%%%%%%%%%%%%%%%%%%%,////////////////.@@
@@@@@@@***************########%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&,////////////////*@@
@@@@@@@,**************######%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&//////////////////@@
@@@@@@@.**************,##%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&*////////////////.@
@@@@@@@.**************,%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&,**//////////////.@
@@@@@@@@***************%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&,*****///////////.@
@@@@@@@@***************%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&/********...../@@@@
@@@@@@@@@.*************,%%%%%%%%%%%%%%%%%%&&&&&&&&/,,,,,%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@%(*.******,...,%*,,,,,,,*******///////((((((#####%%%%%%&&&&&@@@@@@@@@@@ """
print("Anti-Bug info Terminal console if error ")
#import librery


import tkinter as  tk
from tkinter import ttk
import os,time
import platform as pf
from tkinter import filedialog as fl
from tkinter import *
try:
    import webbrowser
except:
    os.system('pip3 install webbrowser,')
try:
    import PyInstaller as pyIn # import pyinstaller (by timgates42)
except pyIn:
    
    print('not found pyinstaller ')

import sys
version_python=pf.python_version()
pyinstaller_version=pyIn.__version__
system_version=pf.system()
__versionGUI__="v0.1_Pre-Alpha"
__buildGUI__="0.1"
def message_windows():
    def __init__(self):
            root =tk.Tk()
            root.geometry('500x100+350+120')
            root.title('message ')
            root.resizable(False,False)
            root.configure(bg='white')
            def ok_c():
                sys.exit()
            self.lb_txt_done=tk.Label(root,text='Done ,you find src folder  of pyinstaller GUI',bg='white')
            self.lb_txt_done.pack()
            bt_ok=tk.Button(root,text='OK',command=ok_c)
            bt_ok.pack()
class error_webbrowser():
    def __init__(self):
            root =tk.Tk()
            root.geometry('500x100+350+120')
            root.title('Error WebBrowser')
            root.resizable(False,False)
            root.configure(bg='white')
            def ok_c():
                os.system('pip3 install webbrowser')
            self.lb_txt_done=tk.Label(root,text='Webbrowser not found ,click ok button for install ',bg='white')
            self.lb_txt_done.pack()
            bt_ok=tk.Button(root,text='OK',command=ok_c)
            bt_ok.pack()
class windows ():

    def __init__(self) -> None:
       
                    
            
# info windows
        def info():
            
            text_info="""
------------------------------Credits--------------------------------
Pyinstaller GUI Interface by Pop Mario Denis
Pyinstaller by pyinstaller.org
-----------------Info Version and system----------------------------
pyinstaller GUI version is :%s
pyinstaller GUI build is :%s
pyinstaller version is :%s
python version is :%s
system use is:%s
------------------------LICENSE-----------------------------------------
pyinstaller GUI license : MIT


 """ %(__versionGUI__,__buildGUI__,pyinstaller_version,version_python,system_version)       #def info interface
            root =tk.Tk()
            root.geometry('850x450')
            root.title('pyinstaller GUI(Info page)')
            root.resizable(False,False)
            root.configure(bg='white')
            self.info_label=tk.Label(root,text=text_info,font=('italy',20),bg='white')
            self.info_label.place(x=10,y=10)

        # windows home page
        root =tk.Tk()
        root.geometry('500x280+350+120')
        root.title('pyinstaller GUI(Home Page)')
        root.resizable(False,False)
        root.configure(bg='white')
        self.frame_info=tk.Frame(root,bg='white')
        self.frame_info.place(x=30,y=40,width=440,height=370)
   
          
        def error_sel():
            self.error_label2=tk.Label(self.frame_info,text='close page',font=('c059',20),bg='white')
            self.error_label2.place(x=199,y=10)
            self.linux_bt.configure(state=DISABLED)
            self.bt_res_info.configure(state=ACTIVE)
            self.bt_start.configure(state=DISABLED)

           

          
            

     
        
        def reset_info():
            self.error_label2.destroy()
            self.linux_bt.configure(state=ACTIVE)
            self.bt_start.configure(state=ACTIVE)
            self.bt_res_info.configure(state=DISABLED)

       
        self.bt_res_info=tk.Button(self.frame_info,text='reset info ',state=DISABLED,borderwidth=0,bg='white',fg='black',activebackground='white',activeforeground='black',command=reset_info)
        self.bt_res_info.place(x=190,y=200)
        self.error_label=tk.Label(self.frame_info,text='error and info :',font=('c059',20),bg='white')
        self.error_label.place(x=10,y=10)

        info_label=tk.Label(self.frame_info,text='progress state :',font=('c059',20),bg='white')
        info_label.place(x=10,y=48)

    # new windows for file
        def new_windows():
    
            root =tk.Tk()
            root.geometry('360x400')
            root.title('pyinstaller GUI')
            root.resizable(False,False)
            root.configure(bg='white')

          
            # sel button and other button comfigure\
            
        
                   
            def st_sel():
                try:
                       
                 
           
                    lb_wait_for=tk.Label(self.frame_info,text='Wait for ..',font=('c059',20),bg='white')
                    lb_wait_for.place(x=250,y=48)
                    file_sel=fl.askopenfilename(initialdir = '/home',title = 'file python',filetypes=(("python files","*.py"),("all files","*.*")))
                
                    
                    os.system('pyinstaller --onefile %s'%(file_sel))
                    lb_wait_for.destroy()
                    message_windows()
                    
                   
                    
                except:
                    lb_wait_for.destroy() 
                    error_sel()

               
                
                  

            

            self.label_i=tk.Label(root,text='Pyinstaller Mode',bg='white',font=('ani',20),fg='black')
            self.label_i.place(x=100,y=10)

            self.bt_start=tk.Button(root,text='Start',command=st_sel,borderwidth=0,bg='white',fg='black',activebackground='white',activeforeground='black')
            self.bt_start.place(x=130,y=70)

            self.lb_txt_easy=tk.Label(root,text='Easy mode:',font=('ani',17),bg='white',fg='black')
            self.lb_txt_easy.place(x=10,y=58)
            

            #advance mode for setup conver
            self.lb_txt_AD=tk.Label(root,text='Advance mode(Aplha version):',
            font=('ani',17),
            bg='white',
            fg='black')
            self.lb_txt_AD.place(x=10,y=100)

            # command andvace mode  
            def exe_c():
               
                    ad_con=ad.get()
                    if ad_con == '--onefile -w --noconsole':
                        fwn()
                    if ad_con =='-- onedir -w --noconsole':
                        dwn()
                    if ad_con == '--onefile -w':
                        fw()
                    if ad_con == '--onedir -w':
                        dw()
                    print(ad_con)
               
                    
            def fwn():
                try:
                    lb_wait_for=tk.Label(self.frame_info,text='Wait for ..',font=('c059',20),bg='white')
                    lb_wait_for.place(x=250,y=48)
                    file_sel=fl.askopenfilename(initialdir = '/home',title = 'file python',filetypes=(("python files","*.py"),("all files","*.*")))
                
                    os.system('pyinstaller --onefile -w --noconsole %s'%(file_sel))
                    lb_wait_for.destroy()
                    message_windows()
                except:
                    lb_wait_for.destroy()
            def dwn():
                try:
                    lb_wait_for=tk.Label(self.frame_info,text='Wait for ..',font=('c059',20),bg='white')
                    lb_wait_for.place(x=250,y=48)
                    file_sel=fl.askopenfilename(initialdir = '/home',title = 'file python',filetypes=(("python files","*.py"),("all files","*.*")))
                    
                    os.system('pyinstaller --onedire -w --noconsole  %s'%(file_sel))
                    lb_wait_for.destroy()
                    message_windows()
                except:
                    lb_wait_for.destroy()
            def fw():
                try:
                    lb_wait_for=tk.Label(self.frame_info,text='Wait for ..',font=('c059',20),bg='white')
                    lb_wait_for.place(x=250,y=48)
                    file_sel=fl.askopenfilename(initialdir = '/home',title = 'file python',filetypes=(("python files","*.py"),("all files","*.*")))
                    
                    os.system('pyinstaller --onefile -w %s'%(file_sel))
                    lb_wait_for.destroy()
                    message_windows()
                except:
                    lb_wait_for.destroy()
               
            def dw():
                try:
                    lb_wait_for=tk.Label(self.frame_info,text='Wait for ..',font=('c059',20),bg='white')
                    lb_wait_for.place(x=250,y=48)
                    file_sel=fl.askopenfilename(initialdir = '/home',title = 'file python',filetypes=(("python files","*.py"),("all files","*.*")))
                    
                    os.system('pyinstaller --onedir -windowed  %s'%(file_sel))
                    lb_wait_for.destroy()

                    message_windows()
                except:
                    lb_wait_for.destroy()

               
                # advance mode GUI setting
          
            self.lb_txt_com=tk.Label(root,text='select command :',font=('ani',17),bg='white',fg='black')
            self.lb_txt_com.place(x=100,y=140,height=33)
            bt_st_ad=tk.Button(root,text='start',command=exe_c,borderwidth=0,bg='white')
            bt_st_ad.place(x=100,y=222,width=200)
            #ad ()
            ad=ttk.Combobox(root,
            values=('--onefile -w --noconsole',
                    '-- onedir -w --noconsole',
                    '--onefile -w',
                    '--onedir -w'))
            ad.place(x=100,y=170,width=200)
        
          
            
        def Quit():
            sys.exit()
        # button  and place 
        self.linux_bt=tk.Button(root,text='Start pyinstaller ',command=new_windows,bg='white',fg='black',activebackground='white',activeforeground='black',borderwidth=0)
        self.linux_bt.place(x=190,y=200)
        def other_com():
            root =tk.Tk()
            root.geometry('360x400')
            root.title('pyinstaller GUI(Setting)')
            root.resizable(False,False)
            root.configure(bg='white')

            def upgrade():
                os.system('pip3 install --upgrade pyinstaller')
            def install_pyinstaller():
                os.system('pip install  pyinstaller')
            lb_txt_upgrade=tk.Label(root,text='upgrade pyinstaller',font=('c059',13),bg='white')
            lb_txt_upgrade.pack()
            bt_upgrade=tk.Button(root,text='upgrade',bg='white',fg='black',activebackground='white',activeforeground='black',borderwidth=0,command=upgrade)
            bt_upgrade.pack(pady=10)
            txt_l=tk.Label(root,text='install pyinstaller librery for python3(pip3)',font=('c059',13),bg='white')
            txt_l.pack()
            bt_install=tk.Button(root,text='Install pyinstaller',bg='white',fg='black',activebackground='white',activeforeground='black',borderwidth=0,command=install_pyinstaller)
            bt_install.pack(pady=10)
            

        def rda_github():
            try:
                url='https://github.com/RedAnonymusITA'
                webbrowser.open(url)
            except:
                error_webbrowser()

        def pyinstaller_github():
            try:
                url='https://github.com/pyinstaller/pyinstaller'
                webbrowser.open(url)
            except:
                error_webbrowser()

        menu1=tk.Menu(root,bg="white",fg='black',borderwidth=0)
        root.configure(menu=menu1)
        file_menu=Menu(menu1,bg="white")
        menu1.add_cascade(label="Menu",menu=file_menu)
       
        file_menu.add_command(label="RDA Github",activebackground='white',command=rda_github)
        file_menu.add_command(label="pyinstaller Github",activebackground='white',command=pyinstaller_github)
        file_menu.add_command(label="setting",activebackground='white',command=other_com)
      
        file_menu.add_separator()
        file_menu.add_command(label="INFO",activebackground='white',command=info)
        file_menu.add_command(label="EXIT",activebackground='white',command=Quit)
        root.mainloop()

windows()
    
