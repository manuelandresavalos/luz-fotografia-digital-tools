#!/bin/python
"""
Hello World, but with more meat.
"""

import wx

class mainFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(mainFrame, self).__init__(*args, **kw)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("...")

        # ---------------------------------------------------------------------------------------------------------------------------
        # create panel 1 ------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        self.panelClientes = wx.Panel(self, size=(1024,768))
        # armo el panel 1
        # agrego una caja y y alineo los elementos verticalmente
        clientBox = wx.BoxSizer(wx.VERTICAL)

        # Creo un objeto texto en modo estatico y se lo agrego al panel 1
        clientText = wx.StaticText(self.panelClientes, -1, "En panel de Clientes")
        # seteo la fuente
        clientText.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        # seteo el tamanio
        clientText.SetSize(clientText.GetBestSize())

        # Creo un boton
        clientClose = wx.Button(self.panelClientes, wx.ID_CLOSE, "Close")
        # Hago que el boton escuche el evento EVT_BUTTON y ejecute OnClose
        clientClose.Bind(wx.EVT_BUTTON, self.OnClose)

        # agrego el texto a la caja.
        clientBox.Add(clientText, 0, wx.ALL, 10)
        # agrego el boton a la caja.
        clientBox.Add(clientClose, 0, wx.ALL, 10)

        self.panelClientes.SetSizer(clientBox)
        self.panelClientes.Layout()

        # ---------------------------------------------------------------------------------------------------------------------------
        # create panel 2 ------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        self.panelCombos = wx.Panel(self, size=(1024,768))
        
        # armo el panel 2
        # agrego una caja y y alineo los elementos verticalmente
        cobmosBox = wx.BoxSizer(wx.VERTICAL)

        # Creo un objeto texto en modo estatico y se lo agrego al panel 1
        combosText = wx.StaticText(self.panelCombos, -1, "En panel de Combos")
        # seteo la fuente
        combosText.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        # seteo el tamanio
        combosText.SetSize(combosText.GetBestSize())

        # Creo un boton
        combosClose = wx.Button(self.panelCombos, wx.ID_CLOSE, "Close")
        # Hago que el boton escuche el evento EVT_BUTTON y ejecute OnClose
        combosClose.Bind(wx.EVT_BUTTON, self.OnClose)

        # agrego el texto a la caja.
        cobmosBox.Add(combosText, 0, wx.ALL, 10)
        # agrego el boton a la caja.
        cobmosBox.Add(combosClose, 0, wx.ALL, 10)

        self.panelCombos.SetSizer(cobmosBox)
        self.panelCombos.Layout()

        self.panelClientes.Hide()
        self.panelCombos.Hide()

    def OnButton(self, Event, button_label):
        print "In OnButton:", button_label

    def makeMenuBar(self):
        # Creo los menues y sus opciones hijas.
        fileMenu = wx.Menu()
        fileMenu_exitItem = fileMenu.Append(wx.ID_EXIT)

        # CLIENTES
        clientes = wx.Menu()
        clientes_alta = clientes.Append(-1, "&Alta de Clientes", "Dar de alta a un nuevo cliente")
        clientes_modificacion = clientes.Append(-1, "&Modificacion de Clientes", "Modificar un cliente existente")
        clientes_baja = clientes.Append(-1, "&Eliminar Clientes", "Eliminar un cliente")
        clientes_buscar = clientes.Append(-1, "&Buscar Clientes", "Buscar un cliente entre la base de datos")

        # COMBOS
        combos = wx.Menu()
        combos_alta = combos.Append(-1, "&Alta de combos", "Dar de alta a un nuevo combo")
        combos_modificacion = combos.Append(-1, "&Modificacion de combos", "Modificar un combo existente")
        combos_baja = combos.Append(-1, "&Eliminar combos", "Eliminar un combo")
        combos_buscar = combos.Append(-1, "&Buscar combos", "Buscar un combo entre la base de datos")

        # PRODUCTOS
        productos = wx.Menu()
        productos_alta = productos.Append(-1, "&Alta de productos", "Dar de alta a un nuevo producto")
        productos_modificacion = productos.Append(-1, "&Modificacion de productos", "Modificar un producto existente")
        productos_baja = productos.Append(-1, "&Eliminar productos", "Eliminar un producto")
        productos_buscar = productos.Append(-1, "&Buscar productos", "Buscar un producto entre la base de datos")

        # PRECIOS Y COSTOS
        precios_y_costos = wx.Menu();
        precios_y_costos_alta = precios_y_costos.Append(-1, "&Alta de precios y costos", "Dar de alta a un nuevo precio y costo")
        precios_y_costos_modificacion = precios_y_costos.Append(-1, "&Modificacion de precios y costoss", "Modificar un precio y costo existente")
        precios_y_costos_baja = precios_y_costos.Append(-1, "&Eliminar precios y costos", "Eliminar un precio y costo")
        precios_y_costos_buscar = precios_y_costos.Append(-1, "&Buscar precios y costos", "Buscar un precio y costo entre la base de datos")

        # SOCIAL
        socialMenu = wx.Menu()
        socialMenu_facebook = socialMenu.Append(-1, "&Facebook", "Revisar la Facebook Fan Page")
        socialMenu_twitter = socialMenu.Append(-1, "&Twitter", "Revisar Twitter")
        socialMenu_500px = socialMenu.Append(-1, "&500px", "Revisar 500px")

        # EMAIL
        emailMenu = wx.Menu()
        emailMenu_email = emailMenu.Append(-1, "&Email", "Revisar Email")

        # AYUDA
        helpMenu = wx.Menu()
        helpMenu_aboutItem = helpMenu.Append(wx.ID_ABOUT)

        #Agrego los menues a la barra de menu.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(clientes, "&Clientes")
        menuBar.Append(combos, "&Combos")
        menuBar.Append(productos, "&Productos")
        menuBar.Append(precios_y_costos, "&Precios y costos")
        menuBar.Append(socialMenu, "&SocialMedia")
        menuBar.Append(emailMenu, "&Email")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        self.Bind(wx.EVT_MENU, self.OnClientes,  clientes_alta)
        self.Bind(wx.EVT_MENU, self.OnCombos,  combos_alta)
        self.Bind(wx.EVT_MENU, self.OnExit,  fileMenu_exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, helpMenu_aboutItem)

    def OnClientes(self, event):
        self.panelClientes.Show()
        self.panelCombos.Hide()

    def OnCombos(self, event):
        self.panelClientes.Hide()
        self.panelCombos.Show()

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App(redirect=True)
    mainFrame = mainFrame(None, title='Luz Fotografia Digital - UnityTool', size=(1024,768))
    mainFrame.Centre()
    mainFrame.Show()
    app.MainLoop()
