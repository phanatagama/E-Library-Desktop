# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"E-Library", pos = wx.DefaultPosition, size = wx.Size( 787,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About Us", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu2, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.header = wx.StaticText( self, wx.ID_ANY, u"Sistem Informasi Perpustakaan", wx.DefaultPosition, wx.Size( 1200,50 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.header.Wrap( -1 )

		self.header.SetFont( wx.Font( 30, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiCondensed" ) )
		self.header.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.header.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1.Add( self.header, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH|wx.NB_LEFT )
		self.m_notebook1.SetBackgroundColour( wx.Colour( 96, 184, 255 ) )

		self.bookPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 1, 1, 0, 0 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		fgSizer9 = wx.FlexGridSizer( 1, 3, 0, 5 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.btnTambahBuku = wx.Button( self.bookPanel, wx.ID_ANY, u"Tambah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.btnTambahBuku, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.searchBox = wx.SearchCtrl( self.bookPanel, wx.ID_ANY, u"Cari Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchBox.ShowSearchButton( True )
		self.searchBox.ShowCancelButton( False )
		fgSizer9.Add( self.searchBox, 0, wx.TOP, 5 )

		comboBoxChoices = [ u"2020", u"2019", u"2018", u"2017" ]
		self.comboBox = wx.ComboBox( self.bookPanel, wx.ID_ANY, u"Filter", wx.DefaultPosition, wx.DefaultSize, comboBoxChoices, wx.CB_READONLY )
		fgSizer9.Add( self.comboBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( fgSizer9, 0, 0, 5 )

		self.bookTable = wx.grid.Grid( self.bookPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		# Grid
		self.bookTable.CreateGrid( 20, 8 )
		self.bookTable.EnableEditing( False )
		self.bookTable.EnableGridLines( True )
		self.bookTable.SetGridLineColour( wx.Colour( 155, 205, 255 ) )
		self.bookTable.EnableDragGridSize( False )
		self.bookTable.SetMargins( 0, 0 )

		# Columns
		self.bookTable.SetColSize( 0, 100 )
		self.bookTable.EnableDragColMove( False )
		self.bookTable.EnableDragColSize( True )
		self.bookTable.SetColLabelSize( 25 )
		self.bookTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.bookTable.SetRowSize( 0, 25 )
		self.bookTable.EnableDragRowSize( True )
		self.bookTable.SetRowLabelSize( 50 )
		self.bookTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.bookTable.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.bookTable.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		# Cell Defaults
		self.bookTable.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer5.Add( self.bookTable, 1, wx.EXPAND|wx.LEFT, 5 )


		gSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.bookPanel.SetSizer( gSizer3 )
		self.bookPanel.Layout()
		gSizer3.Fit( self.bookPanel )
		self.m_notebook1.AddPage( self.bookPanel, u"Buku", True )
		self.borrowPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer43 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer43.SetFlexibleDirection( wx.BOTH )
		fgSizer43.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer10211 = wx.BoxSizer( wx.VERTICAL )

		self.borrowTable = wx.grid.Grid( self.borrowPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.borrowTable.CreateGrid( 20, 5 )
		self.borrowTable.EnableEditing( False )
		self.borrowTable.EnableGridLines( True )
		self.borrowTable.SetGridLineColour( wx.Colour( 155, 205, 255 ) )
		self.borrowTable.EnableDragGridSize( False )
		self.borrowTable.SetMargins( 0, 0 )

		# Columns
		self.borrowTable.SetColSize( 0, 100 )
		self.borrowTable.EnableDragColMove( False )
		self.borrowTable.EnableDragColSize( True )
		self.borrowTable.SetColLabelSize( 25 )
		self.borrowTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.borrowTable.SetRowSize( 0, 25 )
		self.borrowTable.EnableDragRowSize( True )
		self.borrowTable.SetRowLabelSize( 50 )
		self.borrowTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.borrowTable.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.borrowTable.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		# Cell Defaults
		self.borrowTable.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer10211.Add( self.borrowTable, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		fgSizer43.Add( bSizer10211, 1, wx.EXPAND, 5 )

		fgSizer13211 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer13211.SetFlexibleDirection( wx.BOTH )
		fgSizer13211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.borrowLogo = wx.StaticBitmap( self.borrowPanel, wx.ID_ANY, wx.Bitmap( u"../../Pertemuan 9/testqr.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13211.Add( self.borrowLogo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		fgSizer16211 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer16211.SetFlexibleDirection( wx.BOTH )
		fgSizer16211.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textIdBuku = wx.StaticText( self.borrowPanel, wx.ID_ANY, u"Masukkan ID Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textIdBuku.Wrap( -1 )

		self.textIdBuku.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI" ) )

		fgSizer16211.Add( self.textIdBuku, 0, wx.ALL, 5 )

		self.textIdMahasiswa = wx.StaticText( self.borrowPanel, wx.ID_ANY, u"Masukkan ID Mahasiswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textIdMahasiswa.Wrap( -1 )

		self.textIdMahasiswa.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI" ) )

		fgSizer16211.Add( self.textIdMahasiswa, 0, wx.ALL, 5 )

		self.inputIdBuku = wx.TextCtrl( self.borrowPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16211.Add( self.inputIdBuku, 0, wx.ALL|wx.EXPAND, 5 )

		self.inputIdMahasiswa = wx.TextCtrl( self.borrowPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer16211.Add( self.inputIdMahasiswa, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer13211.Add( fgSizer16211, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnTambahPeminjaman = wx.Button( self.borrowPanel, wx.ID_ANY, u"+ Tambah Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnTambahPeminjaman.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Segoe UI Light" ) )
		self.btnTambahPeminjaman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.btnTambahPeminjaman.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		fgSizer13211.Add( self.btnTambahPeminjaman, 0, wx.ALL|wx.EXPAND, 5 )


		fgSizer43.Add( fgSizer13211, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.borrowPanel.SetSizer( fgSizer43 )
		self.borrowPanel.Layout()
		fgSizer43.Fit( self.borrowPanel )
		self.m_notebook1.AddPage( self.borrowPanel, u"Peminjaman", False )
		self.historyPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer31 = wx.GridSizer( 1, 1, 0, 0 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		fgSizer21 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.textIdMahasiswa2 = wx.StaticText( self.historyPanel, wx.ID_ANY, u"ID Mahasiswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textIdMahasiswa2.Wrap( -1 )

		fgSizer21.Add( self.textIdMahasiswa2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.inputIdMahasiswa2 = wx.TextCtrl( self.historyPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.inputIdMahasiswa2, 0, wx.ALL, 5 )

		self.btnSubmit = wx.Button( self.historyPanel, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer21.Add( self.btnSubmit, 0, wx.ALL, 5 )


		gSizer6.Add( fgSizer21, 1, wx.EXPAND, 5 )

		fgSizer91 = wx.FlexGridSizer( 1, 2, 0, 5 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.searchBoxHistory = wx.SearchCtrl( self.historyPanel, wx.ID_ANY, u"Cari Pengembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchBoxHistory.ShowSearchButton( True )
		self.searchBoxHistory.ShowCancelButton( False )
		fgSizer91.Add( self.searchBoxHistory, 0, wx.TOP, 5 )

		comboBoxHistoryChoices = [ u"Hari Ini", u"Minggu Ini", u"Bulan Ini", u"Tahun Ini" ]
		self.comboBoxHistory = wx.ComboBox( self.historyPanel, wx.ID_ANY, u"Tahun Ini", wx.DefaultPosition, wx.DefaultSize, comboBoxHistoryChoices, wx.CB_READONLY )
		self.comboBoxHistory.SetSelection( 3 )
		fgSizer91.Add( self.comboBoxHistory, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer6.Add( fgSizer91, 0, wx.ALIGN_RIGHT, 5 )


		bSizer51.Add( gSizer6, 1, wx.EXPAND, 5 )

		self.historyTable = wx.grid.Grid( self.historyPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

		# Grid
		self.historyTable.CreateGrid( 20, 7 )
		self.historyTable.EnableEditing( False )
		self.historyTable.EnableGridLines( True )
		self.historyTable.SetGridLineColour( wx.Colour( 155, 205, 255 ) )
		self.historyTable.EnableDragGridSize( False )
		self.historyTable.SetMargins( 0, 0 )

		# Columns
		self.historyTable.SetColSize( 0, 100 )
		self.historyTable.EnableDragColMove( False )
		self.historyTable.EnableDragColSize( True )
		self.historyTable.SetColLabelSize( 25 )
		self.historyTable.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.historyTable.SetRowSize( 0, 25 )
		self.historyTable.EnableDragRowSize( True )
		self.historyTable.SetRowLabelSize( 50 )
		self.historyTable.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.historyTable.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.historyTable.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		# Cell Defaults
		self.historyTable.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer51.Add( self.historyTable, 1, wx.EXPAND|wx.LEFT, 5 )


		gSizer31.Add( bSizer51, 1, wx.EXPAND, 5 )


		self.historyPanel.SetSizer( gSizer31 )
		self.historyPanel.Layout()
		gSizer31.Fit( self.historyPanel )
		self.m_notebook1.AddPage( self.historyPanel, u"Pengembalian", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnTambahBuku.Bind( wx.EVT_BUTTON, self.onBtnTambahBuku )
		self.searchBox.Bind( wx.EVT_TEXT, self.onSearchBox )
		self.comboBox.Bind( wx.EVT_COMBOBOX, self.onComboBox )
		self.bookTable.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.sortData )
		self.bookTable.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectRow )
		self.btnTambahPeminjaman.Bind( wx.EVT_BUTTON, self.onBtnTambahPeminjaman )
		self.btnSubmit.Bind( wx.EVT_BUTTON, self.onBtnSubmit )
		self.searchBoxHistory.Bind( wx.EVT_TEXT, self.onSearchBox )
		self.historyTable.Bind( wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.sortData )
		self.historyTable.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectRow )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onBtnTambahBuku( self, event ):
		event.Skip()

	def onSearchBox( self, event ):
		event.Skip()

	def onComboBox( self, event ):
		event.Skip()

	def sortData( self, event ):
		event.Skip()

	def selectRow( self, event ):
		event.Skip()

	def onBtnTambahPeminjaman( self, event ):
		event.Skip()

	def onBtnSubmit( self, event ):
		event.Skip()





###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 144,161 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 144,161 ), wx.Size( 144,161 ) )
		self.SetBackgroundColour( wx.Colour( 155, 205, 255 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		gSizer5 = wx.GridSizer( 4, 1, 0, 0 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer5.Add( self.m_staticText16, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.inputUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.inputUsername, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer5.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.inputPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.inputPassword, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer7.Add( gSizer5, 1, wx.EXPAND, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.btnLogin, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnLogin.Bind( wx.EVT_BUTTON, self.onBtnLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onBtnLogin( self, event ):
		event.Skip()


###########################################################################
## Class Book
###########################################################################

class Book ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Buku", pos = wx.DefaultPosition, size = wx.Size( 295,403 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 155, 205, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Buku Baru", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiCondensed" ) )
		self.m_staticText14.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_staticText14.SetBackgroundColour( wx.Colour( 155, 205, 255 ) )

		bSizer4.Add( self.m_staticText14, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Judul", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer4.Add( self.m_textCtrl10, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText152 = wx.StaticText( self, wx.ID_ANY, u"Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		self.m_staticText152.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer4.Add( self.m_staticText152, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl11, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer4.Add( self.m_staticText151, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl12, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText1511 = wx.StaticText( self, wx.ID_ANY, u"Tahun Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1511.Wrap( -1 )

		self.m_staticText1511.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer4.Add( self.m_staticText1511, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl13, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15111 = wx.StaticText( self, wx.ID_ANY, u"Rak Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15111.Wrap( -1 )

		self.m_staticText15111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Montserrat Black" ) )

		bSizer4.Add( self.m_staticText15111, 0, wx.ALL, 5 )

		self.m_textCtrl131 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_textCtrl131, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnSimpanBuku )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanBuku( self, event ):
		event.Skip()


###########################################################################
## Class Nota
###########################################################################

class Nota ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Nota Peminjaman", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 155, 205, 255 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nota Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiCondensed" ) )

		bSizer6.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer7 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Nama Peminjam :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer7.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.m_textCtrl9.SetMinSize( wx.Size( 150,-1 ) )
		self.m_textCtrl9.SetMaxSize( wx.Size( 150,-1 ) )

		fgSizer7.Add( self.m_textCtrl9, 0, 0, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"Judul Buku :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText141.SetMaxSize( wx.Size( 269,300269 ) )

		fgSizer7.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_textCtrl91 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.m_textCtrl91.SetMinSize( wx.Size( 150,-1 ) )
		self.m_textCtrl91.SetMaxSize( wx.Size( 150,-1 ) )

		fgSizer7.Add( self.m_textCtrl91, 0, 0, 5 )

		self.m_staticText142 = wx.StaticText( self, wx.ID_ANY, u"Petugas :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		self.m_staticText142.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer7.Add( self.m_staticText142, 0, wx.ALL, 5 )

		self.m_textCtrl92 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.m_textCtrl92.SetMinSize( wx.Size( 150,-1 ) )
		self.m_textCtrl92.SetMaxSize( wx.Size( 150,-1 ) )

		fgSizer7.Add( self.m_textCtrl92, 0, 0, 5 )

		self.m_staticText143 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pinjam :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText143.Wrap( -1 )

		self.m_staticText143.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		fgSizer7.Add( self.m_staticText143, 0, wx.ALL, 5 )

		self.m_textCtrl93 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_READONLY )
		self.m_textCtrl93.SetMinSize( wx.Size( 150,-1 ) )
		self.m_textCtrl93.SetMaxSize( wx.Size( 150,-1 ) )

		fgSizer7.Add( self.m_textCtrl93, 0, 0, 5 )


		bSizer6.Add( fgSizer7, 0, wx.EXPAND, 5 )

		self.btnSelesai = wx.Button( self, wx.ID_ANY, u"Selesai", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnSelesai, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSelesai.Bind( wx.EVT_BUTTON, self.onBtnSelesai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onBtnSelesai( self, event ):
		event.Skip()


