from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction


class SimpleCalcExtension(Extension):

    def __init__(self):
        super(SimpleCalcExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        argumentToEval = event.get_argument()
        argumentToEval = argumentToEval.replace('\'', '')
        argumentToEval = argumentToEval.replace('"', '')
        resultEval = eval(argumentToEval)
        resultParsed = ""
        if isinstance(resultEval, int):
            resultParsed = str(resultEval)
        elif isinstance(resultEval, float):
            resultParsed = "{:.8}".format(resultEval)
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name=resultParsed,
                                         description='Enter to copy to clipboard',
                                         on_enter=CopyToClipboardAction(resultParsed)))
        return RenderResultListAction(items)


if __name__ == '__main__':
    SimpleCalcExtension().run()


