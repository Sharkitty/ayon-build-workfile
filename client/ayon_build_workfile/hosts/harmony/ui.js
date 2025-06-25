import QApplication;

function addButton() {
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

    onBuild = function() {
        app.ayonClient.send({
            'module': 'ayon_build_workfile.ui',
            'method': 'show'
        }, false);
    };

    var action = menu.addAction('Build Workfile');
    action.triggered.connect(onBuild);
}
