#
#   diamock.py ..  bunnyfied by SoSie on 02 jan 2022
#
#  see https://sosie-js.github.io/python-dia/mock/
#  version 2.0
#  This version adds about_diamock() popup


import sys
python_ver=sys.version_info
python2 = (python_ver[0] == 2)

from dumpObj import dumpObj #here is the golden carot


import warnings

#NOTE, As Namespace Gtk is already loaded with version 2.0, 
#for dia 0.97.2, we cannot choose 3.0
gtk_ver= "2.0" #PyGTK is only for gtk2.0 and python2 due to error on import gi: When using gi.repository you must not import static modules like "gobject"
gtk_ver ="2.0gi" #outdated in python3, that recommends 3.0gi

#Autodetect which python GTK+ gas factory to use, works for python2/3
try:
    if(python2 and "gi" in gtk_ver):
        gtk_ver="2.0" 
        raise(Exception("pyGtk is the standard for gtk2.0, gi is for now in fact not supported on python2"))    
    gtk_support="pyGObject"
    import gi
    gtk_ver=gtk_ver.replace("gi","")
    gi.require_version('Pango', '1.0')
    gi.require_version('Gtk', gtk_ver)
    try:
        gtks=True
        gi.require_version('GtkSource', gtk_ver)  #http://lazka.github.io/pgi-docs/#GtkSource-4
    except:
        gtks=False
   
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        from gi.repository import Pango, Gtk, Gdk
        from gi.repository import GLib as GObject #PyGIDeprecationWarning: GObject.timeout_add is deprecated; use GLib.timeout_add instead
        if gtks:
            from gi.repository import GtkSource as gtksourceview
            buf = gtksourceview.Buffer()
    gtk_version = str(gi.version_info)[1:-1].replace(', ','.')
except Exception as e:
    import pygtk
    gtk_support="pyGTK"
    pygtk.require(gtk_ver)

    #Because Gtk 2.0 was not designed for use with introspection some of the interfaces 
    #and API will fail.  As such this is not supported by the pygobject development team 
    #and we encourage you to port your app to Gtk 3 or greater. 
    import gtk as Gtk
    try:
        import gtk.keysyms
    except:
        # FIXME : Weird error: sys.path must be a list of directory names
        pass
    import gobject as GObject
    gtk_version = str(getattr(GObject, 'pygobject_version', []))[1:-1].replace(',','.')
   
def about_diamock(*args):
    
    """ Popup the About Dialog diamock """
    
    
    #Now set your dia playground
    active_display = dia.active_display()

    if not active_display is None: #occurs when no object in the page
        
        d = active_display.diagram
        data = d.data
        layer = data.active_layer
        objects = layer.objects

    else:
        layer=None
        objects=[]
        
    dumpObj(layer)
    print("Number of objects on the diagram :"+ str(len(objects))) #is zero here which is normal for an empty diagram

    #otypes=dia.registered_types()  is not supported yet.
    #As this is the core of creating objects to be added to layer
    #we can play only here

    
    

    VERSION="2.0"
    PROGRAM_NAME="Mock Plugin for Python-Dia"
    
    LICENSE="LGPL3"
    COPYRIGHT=LICENSE+" - using "+gtk_support+ " for gtk+"+gtk_version
    AUTHORS=["Chris Daley(chebizarro)","Olivier Lutzwiller(SoSie)"] 
    
    COMMENTS="Improved Dia Mock for Python"+".".join(map(str,python_ver))
    WEBSITE="https://sosie-js.github.io/python-dia/mock/"
            
    if gtk_support == "pyGTK":
        
        ## Using pyGTK way 
        ##############################
        
        #https://wiki.gnome.org/Projects/PyGTK
        about = Gtk.AboutDialog()
        about.set_program_name(PROGRAM_NAME)
        about.set_version(VERSION)
        about.set_authors(AUTHORS)
        about.set_copyright(COPYRIGHT)
        about.set_comments(COMMENTS)
        about.set_website(WEBSITE)
        about.run()
        about.destroy()
    else:
    
        
        ## Using pyObject way : crashes !
        ##############################
        
        #https://pygobject.readthedocs.io/en/latest/getting_started.html
        """
        try:
            if gtk_support=="pyGObject":
                if gtk_ver == "3.0":
                    dialog = Gtk.AboutDialog()
                    dialog.set_title("AboutDialog")
                    dialog.set_name("Python Gtk+3")
                    dialog.set_version(VERSION)
                    dialog.set_comments(COMMENTS)
                    dialog.set_website(WEBSITE)
                    dialog.set_website_label("PyGtk3 API")
                    dialog.set_authors(AUTHORS)
                    #dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/gtk.png", 64, 64))
                    dialog.connect('response', lambda dialog, data: dialog.destroy())
                    dialog.show_all()
                else:
                    dialog = Gtk.AboutDialog()
                    #dialog.set_logo_icon_name('io.github.ImEditor')
                    #dialog.set_program_name(PROGRAM_NAME)
                    dialog.set_version(VERSION)
                    dialog.set_website(WEBSITE)
                    dialog.set_authors(",".join(AUTHORS))
                    dialog.set_comments(COMMENTS)
                    dialog.set_license(LICENSE)
                    dialog.run()
                    dialog.destroy() 
        except:
        """
        
        ## Using tkinter to mock AboutDialog ui as replacement
        ##############################
        
        if  python2 :
            import Tkinter as tk
            import tkFont
        else :
            import tkinter as tk
            import tkinter.font as tkFont

        root = tk.Tk()
        root.title("About "+PROGRAM_NAME)
        root.geometry('600x220+50+50')
        root.resizable(False, False)
        #root.iconbitmap('./assets/pythontutorial.ico')
        
        def credits():
            
            fenetre0 =tk.Toplevel()
            fenetre0.title("Credits")
            fenetre0.geometry('350x250+50+50')
            fenetre0.resizable(False, False)
           
            cadre0 =tk.Frame(fenetre0)
           
            tab0 =tk.Text(cadre0)
            tab0.config(font ="sans 12", width =10, height =1)
            tab0.insert("end", "Written by")
            tab0.config(state =tk.DISABLED)
            tab0.pack()
            
            texte0 =tk.Text(cadre0)
            texte0.config(font ="sans 12", width =25, height =6)
            
            ret=""
            for author in AUTHORS:
                texte0.insert("end", ret+author)
                ret="\n"
                
            texte0.config(state =tk.DISABLED)
            texte0.pack()
         
            bouton1 =tk.Button(cadre0, text ="Close", command =fenetre0.destroy)
            bouton1.pack(side =tk.RIGHT)
            
            cadre0.pack(padx=3)
        
        root.aspect(3, 2, 5, 3)
        
        cadre0 =tk.Frame(root)

        sep0 = tk.Label(cadre0, text="")
        sep0.pack()
        
        title = tk.Label(cadre0, text=PROGRAM_NAME+" " +VERSION, font ="sans 16 bold")
        title.pack()

        comments = tk.Label(cadre0, text=COMMENTS)
        comments.pack()
        
        copyright= tk.Label(cadre0, text=COPYRIGHT)
        copyright.pack()
        
        #Creates the website link
        
        def callback(url):
            import webbrowser
            webbrowser.open_new(url)

        website = tk.Label(cadre0, text=WEBSITE,  fg="blue", cursor="hand2")
        website.pack()
        website.bind("<Button-1>", lambda e: callback(WEBSITE))

        # clone the font, set the underline attribute,
        # and assign it to our widget
        f = tkFont.Font(website, website.cget("font"))
        f.configure(underline = True)
        website.configure(font=f)

        #separator
        sep1 = tk.Label(cadre0, text="")
        sep1.pack()
        
        bouton0 =tk.Button(cadre0,text ="Credits", command =credits)
        bouton0.pack(side =tk.LEFT)
        
        bouton1 =tk.Button(cadre0, text ="Close", command =root.destroy)
        bouton1.pack(side =tk.RIGHT)
        
        cadre0.pack(padx=3)
        
        root.mainloop()
        
        ## Using text console way 
        ##############################
        
        print("==="+PROGRAM_NAME+VERSION+"===")
        print("Authors:"+",".join(AUTHORS))
        print(COMMENTS)
        print("Copyright:"+COPYRIGHT)
        print("Website:"+WEBSITE)
        print("=================================")


import inspect
def onDiaLaunched():
    stack=inspect.stack()
    return ("python-startup.py" in stack[-1][1])


if __name__ == '__main__' or not onDiaLaunched():
    
    
    #dia is the mocked version of lib pydia library.
    # it is now python2-3 compatible
    #available here: https://github.com/sosie-js/python-dia-mock-plugin
    #see the installation steps on  https://sosie-js.github.io/python-dia/mock/
    
    import dia 
    
    about_diamock()

else:

    import dia
    
    """
    import dill
    d=dill.dumps(dia)
    file_path="dill"+__name__+"-dia.dump"
      
    with open(file_path, "wb") as w:
        w.write(d)
        
    """
    
#========== PUT YOUR PYDIA SCRIPT HERE ===========

#NOTE: active_display = dia.active_display() is Not accessible here
# it will be only in about_diamock()

#enjoy the doc
dumpObj(dia)

#and the About
dia.register_action ("About DiaMock", "About DiaMock", 
                     "/DisplayMenu/Help/HelpAboutDiaMock", 
                     about_diamock)
