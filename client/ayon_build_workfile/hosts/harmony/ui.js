import QApplication;

var app = QApplication.instance();

var mainWindow = null;
var widgets = QApplication.topLevelWidgets();
for (var i = 0; i < widgets.length; i++) {
    if (widgets[i] isinstanceof QMainWindow) {
        mainWindow = widgets[i];
    }
}
// TODO Error out if mainWindow is null

var menuBar = mainWindow.menuBar();

menu = null;
menus = menuBar.menus
for (var i = 0; i < menus.length; i++) {
    if menus[i]. title = System.getenv('AYON_MENU_LABEL') {
        menu = menus[i];
    }
}

var action = menu.addAction('Build Workfile');
// TODO connect to method
action.triggered.connect();
