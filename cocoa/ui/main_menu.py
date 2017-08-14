ownerclass = 'MGAppDelegate'
ownerimport = 'MGAppDelegate.h'

result = Menu("")
appMenu = result.addMenu("moneyGuru")
fileMenu = result.addMenu("File")
editMenu = result.addMenu("Edit")
docMenu = result.addMenu("Document")
viewMenu = result.addMenu("View")
windowMenu = result.addMenu("Window")
helpMenu = result.addMenu("Help")

appMenu.addItem("About moneyGuru", Action(owner, 'showAboutBox'))
appMenu.addSeparator()
appMenu.addItem("Preferences...", Action(owner, 'showPreferencesPanel'), 'cmd+,')
appMenu.addSeparator()
NSApp.servicesMenu = appMenu.addMenu("Services")
appMenu.addSeparator()
appMenu.addItem("Hide moneyGuru", Action(NSApp, 'hide:'), 'cmd+h')
appMenu.addItem("Hide Others", Action(NSApp, 'hideOtherApplications:'), 'cmd+alt+h')
appMenu.addItem("Show All", Action(NSApp, 'unhideAllApplications:'))
appMenu.addSeparator()
appMenu.addItem("Quit moneyGuru", Action(NSApp, 'terminate:'), 'cmd+q')

fileMenu.addItem("New Document", Action(None, 'newDocument:'))
fileMenu.addItem("New Tab", Action(None, 'newTab'), 'cmd+t')
fileMenu.addItem("Open...", Action(None, 'openDocument:'), 'cmd+o')
# The "Open Recent" item will be automatically added here, don't ask me why. Some kind of NSDocument magic.
fileMenu.addItem("Open Example Document", Action(None, 'openExampleDocument'))
fileMenu.addItem("Open Plugin Folder", Action(owner.model, 'openPluginFolder'))
fileMenu.addItem("Import...", Action(None, 'import'), 'cmd+alt+i')
fileMenu.addItem("Export...", Action(None, 'export'), 'cmd+alt+e')
fileMenu.addSeparator()
fileMenu.addItem("Close", Action(None, 'performClose:'), 'cmd+w')
fileMenu.addItem("Close Window", Action(None, 'performClose:'), 'cmd+shift+w', tag=const.MGCloseWindowMenuItem)
fileMenu.addItem("Save", Action(None, 'saveDocument:'), 'cmd+s')
fileMenu.addItem("Save As...", Action(None, 'saveDocumentAs:'), 'cmd+shift+s')
fileMenu.addSeparator()
fileMenu.addItem("Page Setup...", Action(None, 'runPageLayout:'), 'cmd+shift+p')
fileMenu.addItem("Print", Action(None, 'printDocument:'), 'cmd+p')

editMenu.addItem("Undo", Action(None, 'undo:'), 'cmd+z')
editMenu.addItem("Redo", Action(None, 'redo:'), 'cmd+shift+z')
editMenu.addSeparator()
editMenu.addItem("Cut", Action(None, 'cut:'), 'cmd+x')
editMenu.addItem("Copy", Action(None, 'copy:'), 'cmd+c')
editMenu.addItem("Paste", Action(None, 'paste:'), 'cmd+v')
editMenu.addItem("Delete", Action(None, 'delete:'), 'backspace')
editMenu.addItem("Duplicate", Action(None, 'duplicateItem'), 'cmd+d')
editMenu.addItem("Select All", Action(None, 'selectAll:'), 'cmd+a')
editMenu.addItem("Search...", Action(None, 'search'), 'cmd+shift+f')

docMenu.addItem(NLSTR("New <item>"), Action(None, 'newItem'), 'cmd+n', tag=const.MGNewItemMenuItem)
docMenu.addItem("New Account Group", Action(None, 'newGroup'), 'cmd+shift+n')
docMenu.addSeparator()
docMenu.addItem("Show Info", Action(None, 'editItemInfo'), 'cmd+i')
docMenu.addItem("Move Up", Action(None, 'moveSelectionUp'), 'cmd++')
docMenu.addItem("Move Down", Action(None, 'moveSelectionDown'), 'cmd+-')
docMenu.addItem("Make Schedule from Selected", Action(None, 'makeScheduleFromSelected'), 'cmd+m')
docMenu.addItem("Reconcile Selection", Action(None, 'toggleEntriesReconciled'), 'cmd+r')
docMenu.addItem("Toggle Reconciliation Mode", Action(None, 'toggleReconciliationMode'), 'cmd+shift+r')
docMenu.addItem("Toggle Exclusion Status of Account", Action(None, 'toggleExcluded'), 'cmd+shift+x')
docMenu.addSeparator()
docMenu.addItem("Show Account", Action(None, 'showSelectedAccount'), 'cmd+]')
docMenu.addItem("Go Back", Action(None, 'navigateBack'), 'cmd+[')
docMenu.addItem("Jump to Account...", Action(None, 'jumpToAccount'), 'cmd+shift+a')
docMenu.addItem("Lookup Completion...", Action(None, 'lookupCompletion'), 'cmd+l')

viewMenu.addItem("Net Worth", Action(None, 'showBalanceSheet'), 'cmd+1')
viewMenu.addItem("Profit & Loss", Action(None, 'showIncomeStatement'), 'cmd+2')
viewMenu.addItem("Transactions", Action(None, 'showTransactionTable'), 'cmd+3')
viewMenu.addItem("Previous Tab", Action(None, 'showPreviousView'), 'cmd+shift+[')
viewMenu.addItem("Next Tab", Action(None, 'showNextView'), 'cmd+shift+]')
viewMenu.addSeparator()
viewMenu.addItem("Month", Action(None, 'selectMonthRange'), 'cmd+alt+1')
viewMenu.addItem("Quarter", Action(None, 'selectQuarterRange'), 'cmd+alt+2')
viewMenu.addItem("Year", Action(None, 'selectYearRange'), 'cmd+alt+3')
viewMenu.addItem("Year to date", Action(None, 'selectYearToDateRange'), 'cmd+alt+4')
viewMenu.addItem("Running year", Action(None, 'selectRunningYearRange'), 'cmd+alt+5')
viewMenu.addItem("All transactions", Action(None, 'selectAllTransactionsRange'), 'cmd+alt+6')
viewMenu.addItem("Custom date range...", Action(None, 'selectCustomDateRange'), 'cmd+alt+7')
for i in range(3):
    if i == 2:
        shortcutKey = '0'
    else:
        shortcutKey = str(8+i)
    item = viewMenu.addItem("", Action(None, 'selectSavedCustomRange:'),
        'cmd+alt+{}'.format(shortcutKey), tag=2000+i)
    item.hidden = True
    setattr(owner, 'customDateRangeItem{}'.format(i+1), item)
viewMenu.addItem("Previous Date Range", Action(None, 'selectPrevDateRange'), 'cmd+alt+[')
viewMenu.addItem("Next Date Range", Action(None, 'selectNextDateRange'), 'cmd+alt+]')
viewMenu.addItem("Today's Date Range", Action(None, 'selectTodayDateRange'), 'cmd+alt+t')
viewMenu.addSeparator()
viewMenu.addItem("Toggle Graph", Action(None, 'toggleGraph'), 'cmd+alt+g')
viewMenu.addItem("Toggle Pie Charts", Action(None, 'togglePieChart'), 'cmd+alt+p')

windowMenu.addItem("Minimize", Action(None, 'performMinimize:'))
windowMenu.addItem("Zoom", Action(None, 'performZoom:'))
windowMenu.addSeparator()
windowMenu.addItem("Bring All to Front", Action(None, 'arrangeInFront:'))

helpMenu.addItem("moneyGuru Help", Action(owner, 'openHelp'), 'cmd+?')
helpMenu.addItem("moneyGuru Website", Action(owner, 'openWebsite'))
