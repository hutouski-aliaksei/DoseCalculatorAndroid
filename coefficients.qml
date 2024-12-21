import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import QtQuick.Dialogs
import QtQuick.Window

Page {
    id: root

    property int margin: 10

    Material.theme: Material.Light
    Material.accent: custom_color
    width: Screen.width
    height: Screen.height
    header: Item {
        height: 50
    }


    footer: Item
    {
        height: button_height
    }
}
