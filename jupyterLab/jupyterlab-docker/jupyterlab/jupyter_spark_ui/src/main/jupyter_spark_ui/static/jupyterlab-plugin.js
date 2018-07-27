import "./spark.css";

import "bootstrap/dist/css/bootstrap.min.css";

import {
    Widget
} from '@phosphor/widgets';

import { each } from '@phosphor/algorithm';

import {
    ILayoutRestorer,
    JupyterLab,
    JupyterLabPlugin
} from '@jupyterlab/application';

var common = require('./extension.js');

const plugin = {
    id: 'jupyter_spark_ui',
    autoStart: true,
    requires: [ILayoutRestorer],
    activate: (app, restorer) => {
        let api_url = app.serviceManager.serverSettings.baseUrl + "/../spark/api/v1";
        let widget = new Widget();
        widget.id = 'jupyter-spark';
        widget.class = 'jupter-spark-panel';
        widget.title.label = 'Spark';
        widget.title.closable = true;
        restorer.add(widget, 'jupyter-spark');

        widget.onBeforeShow = (msg) => {
            widget.intervalId = window.setInterval(common().update, 500, api_url);
        };

        widget.onBeforeHide = (msg) => {
            window.clearInterval(widget.intervalId);
        };

        let div = document.createElement('div');
        div.id = "spark_dialog_contents";
        widget.node.appendChild(div);

        app.shell.addToLeftArea(widget);


        // test to catch all open tabs
        app.restored.then(function () {
            var populate = function () {
                //tabs.clearTabs();
                each(app.shell.widgets('main'), function (widget) {
                    console.log(widget.title);
                    console.log(api_url);
                });
            };
            // Connect signal handlers.
            app.shell.layoutModified.connect(function () {
                populate();
            });

         /*   tabs.tabActivateRequested.connect(function (sender, tab) {
                shell.activateById(tab.title.owner.id);
            });
            tabs.tabCloseRequested.connect(function (sender, tab) {
                tab.title.owner.close();
            });
         */
            // Populate the tab manager.
            populate();
        });
    }
};

export default plugin;